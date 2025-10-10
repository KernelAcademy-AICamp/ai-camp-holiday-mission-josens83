"""
호텔 리뷰 요약 모듈
sample_reviews.json 파일을 읽어서 리뷰를 청결, 위치, 서비스, 불편사항 중심으로 요약합니다.
"""

import json
import os
from datetime import datetime
from openai_client import initialize_openai_client


def load_reviews(file_path: str) -> list:
    """
    JSON 파일에서 리뷰 데이터를 로드합니다.
    
    Args:
        file_path: 리뷰 JSON 파일 경로
        
    Returns:
        list: 리뷰 데이터 리스트
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            reviews = json.load(f)
        print(f"✅ {len(reviews)}개의 리뷰를 성공적으로 로드했습니다.")
        return reviews
    except FileNotFoundError:
        print(f"❌ 파일을 찾을 수 없습니다: {file_path}")
        return []
    except json.JSONDecodeError:
        print(f"❌ JSON 파일 형식이 올바르지 않습니다: {file_path}")
        return []
    except Exception as e:
        print(f"❌ 파일 로드 중 오류 발생: {e}")
        return []


def summarize_single_review(client, review_text: str) -> str:
    """
    단일 리뷰를 청결, 위치, 서비스, 불편사항 중심으로 요약합니다.
    
    Args:
        client: OpenAI 클라이언트 객체
        review_text: 리뷰 텍스트
        
    Returns:
        str: 요약된 리뷰 (3문장 이내)
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": """당신은 호텔 리뷰 분석 전문가입니다. 
                    주어진 리뷰를 다음 4가지 핵심 키워드를 중심으로 3문장 이내로 요약해주세요:
                    1. 청결 (깨끗함, 위생, 정리 상태)
                    2. 위치 (교통편, 접근성, 주변 환경)
                    3. 서비스 (직원 친절도, 룸서비스, 체크인/아웃)
                    4. 불편사항 (문제점, 개선사항, 아쉬운 점)
                    
                    각 문장은 간결하고 명확하게 작성해주세요."""
                },
                {
                    "role": "user",
                    "content": f"다음 호텔 리뷰를 요약해주세요: {review_text}"
                }
            ],
            max_tokens=150,
            temperature=0.3
        )
        
        summary = response.choices[0].message.content.strip()
        return summary
        
    except Exception as e:
        print(f"❌ 리뷰 요약 중 오류 발생: {e}")
        return f"요약 실패: {str(e)}"


def summarize_all_reviews(reviews: list) -> str:
    """
    모든 리뷰를 종합적으로 요약합니다.
    
    Args:
        reviews: 리뷰 데이터 리스트
        
    Returns:
        str: 전체 리뷰 요약
    """
    client = initialize_openai_client()
    
    if not client:
        return "OpenAI 클라이언트 초기화에 실패했습니다."
    
    # 개별 리뷰 요약
    individual_summaries = []
    for i, review in enumerate(reviews, 1):
        print(f"📝 리뷰 {i}/{len(reviews)} 요약 중...")
        summary = summarize_single_review(client, review['review'])
        individual_summaries.append(f"리뷰 {i} (⭐{review['stars']}): {summary}")
    
    # 전체 종합 요약
    print("🔄 전체 리뷰 종합 요약 중...")
    all_reviews_text = "\n".join([f"리뷰 {i+1}: {review['review']}" for i, review in enumerate(reviews)])
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": """당신은 호텔 리뷰 종합 분석 전문가입니다.
                    주어진 모든 리뷰를 분석하여 다음 4가지 핵심 키워드를 중심으로 종합 요약해주세요:
                    1. 청결 (전체적인 청결도 평가)
                    2. 위치 (위치의 장단점)
                    3. 서비스 (서비스 품질 종합 평가)
                    4. 불편사항 (주요 문제점과 개선사항)
                    
                    3문장 이내로 간결하게 작성해주세요."""
                },
                {
                    "role": "user",
                    "content": f"다음 모든 리뷰를 종합 요약해주세요:\n{all_reviews_text}"
                }
            ],
            max_tokens=200,
            temperature=0.3
        )
        
        overall_summary = response.choices[0].message.content.strip()
        
        # 결과 구성
        result = f"""=== AI Camp Holiday Mission - 호텔 리뷰 요약 결과 ===

총 리뷰 개수: {len(reviews)}
요약 일시: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
사용 모델: gpt-3.5-turbo

=== 개별 리뷰 요약 ===
{chr(10).join(individual_summaries)}

=== 전체 종합 요약 ===
{overall_summary}

=== 요약 완료 ===
"""
        return result
        
    except Exception as e:
        print(f"❌ 종합 요약 중 오류 발생: {e}")
        return f"종합 요약 실패: {str(e)}"


def save_summary_to_file(summary: str, file_path: str) -> bool:
    """
    요약 결과를 파일로 저장합니다.
    
    Args:
        summary: 요약 텍스트
        file_path: 저장할 파일 경로
        
    Returns:
        bool: 저장 성공 여부
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(summary)
        print(f"✅ 요약 결과가 {file_path}에 저장되었습니다.")
        return True
    except Exception as e:
        print(f"❌ 파일 저장 중 오류 발생: {e}")
        return False


def main():
    """
    메인 실행 함수
    """
    print("🏨 호텔 리뷰 요약 프로그램 시작")
    print("=" * 50)
    
    # 리뷰 데이터 로드
    reviews = load_reviews('sample_reviews.json')
    
    if not reviews:
        print("❌ 리뷰 데이터를 로드할 수 없습니다. 프로그램을 종료합니다.")
        return
    
    # 리뷰 요약
    summary = summarize_all_reviews(reviews)
    
    # 결과 저장
    if save_summary_to_file(summary, 'hotel_review_summary.txt'):
        print("\n🎉 호텔 리뷰 요약이 완료되었습니다!")
        print("📄 결과 파일: hotel_review_summary.txt")
    else:
        print("\n❌ 파일 저장에 실패했습니다.")


if __name__ == "__main__":
    main()

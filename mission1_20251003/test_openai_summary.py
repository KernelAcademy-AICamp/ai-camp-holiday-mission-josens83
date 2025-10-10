"""
OpenAI API 테스트용 간단한 요약 예시
"이 프로젝트는 AI Camp Holiday Mission입니다" 문장을 한 줄로 요약하는 테스트 코드
"""

from openai_client import initialize_openai_client, test_openai_connection


def test_summarization():
    """
    OpenAI API를 사용하여 간단한 텍스트 요약 테스트를 수행합니다.
    """
    print("🚀 OpenAI API 요약 테스트를 시작합니다...")
    print("-" * 50)
    
    # OpenAI 클라이언트 초기화
    client = initialize_openai_client()
    
    if not client:
        print("❌ 클라이언트 초기화에 실패했습니다. 테스트를 중단합니다.")
        return False
    
    # 연결 테스트
    if not test_openai_connection(client):
        print("❌ API 연결 테스트에 실패했습니다. 테스트를 중단합니다.")
        return False
    
    try:
        # 테스트할 원본 텍스트
        original_text = "이 프로젝트는 AI Camp Holiday Mission입니다"
        
        print(f"📝 원본 텍스트: {original_text}")
        print("🤖 AI가 요약을 생성 중...")
        
        # OpenAI API를 사용한 요약 요청
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system", 
                    "content": "당신은 텍스트를 한 줄로 간결하게 요약하는 전문가입니다."
                },
                {
                    "role": "user", 
                    "content": f"다음 텍스트를 한 줄로 요약해주세요: {original_text}"
                }
            ],
            max_tokens=50,
            temperature=0.3
        )
        
        # 응답에서 요약 결과 추출
        summary = response.choices[0].message.content.strip()
        
        print(f"✨ AI 요약 결과: {summary}")
        print("-" * 50)
        print("✅ OpenAI API 요약 테스트가 성공적으로 완료되었습니다!")
        
        return True
        
    except Exception as e:
        print(f"❌ 요약 테스트 중 오류 발생: {e}")
        return False


def test_multiple_summaries():
    """
    여러 가지 텍스트에 대해 요약 테스트를 수행합니다.
    """
    print("\n🔄 다양한 텍스트 요약 테스트를 시작합니다...")
    print("-" * 50)
    
    client = initialize_openai_client()
    
    if not client:
        return False
    
    # 테스트할 텍스트들
    test_texts = [
        "이 프로젝트는 AI Camp Holiday Mission입니다",
        "인공지능과 머신러닝을 활용한 혁신적인 솔루션을 개발합니다",
        "데이터 분석과 자연어 처리를 통해 사용자에게 가치를 제공합니다"
    ]
    
    try:
        for i, text in enumerate(test_texts, 1):
            print(f"\n📝 테스트 {i}: {text}")
            
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system", 
                        "content": "텍스트를 한 줄로 간결하게 요약해주세요."
                    },
                    {
                        "role": "user", 
                        "content": f"다음 텍스트를 요약해주세요: {text}"
                    }
                ],
                max_tokens=30,
                temperature=0.2
            )
            
            summary = response.choices[0].message.content.strip()
            print(f"✨ 요약: {summary}")
        
        print("\n✅ 모든 요약 테스트가 완료되었습니다!")
        return True
        
    except Exception as e:
        print(f"❌ 다중 요약 테스트 중 오류 발생: {e}")
        return False


if __name__ == "__main__":
    print("🎯 OpenAI API 요약 기능 테스트")
    print("=" * 50)
    
    # 기본 요약 테스트
    success = test_summarization()
    
    if success:
        # 추가 다중 요약 테스트
        test_multiple_summaries()
    
    print("\n🏁 테스트 완료!")

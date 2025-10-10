"""
Gradio 웹 인터페이스 - 리뷰 요약 앱
입력창에 리뷰 텍스트를 입력하면 OpenAI 모델이 2~3문장으로 요약 결과를 보여주는 웹 앱
"""

import gradio as gr
import os
from env_config import initialize_app
from openai_client import initialize_openai_client
from review_summarizer import summarize_single_review


def summarize_review(review_text: str) -> str:
    """
    사용자가 입력한 리뷰 텍스트를 요약합니다.
    
    Args:
        review_text: 사용자가 입력한 리뷰 텍스트
        
    Returns:
        str: 요약된 리뷰 (2~3문장)
    """
    if not review_text.strip():
        return "❌ 리뷰 텍스트를 입력해주세요."
    
    # OpenAI 클라이언트 초기화
    client = initialize_openai_client()
    
    if not client:
        return """❌ OpenAI 클라이언트 초기화에 실패했습니다. 

🔑 API 키 설정 방법:
1. OpenAI 웹사이트(https://platform.openai.com/api-keys)에서 API 키를 발급받으세요
2. 프로젝트 루트에 .env 파일을 생성하고 다음 내용을 추가하세요:
   OPENAI_API_KEY=your-actual-api-key-here
3. 파일을 저장한 후 페이지를 새로고침하세요

💡 데모용 샘플 요약:
이 리뷰는 호텔의 위치와 서비스에 대한 긍정적인 평가를 담고 있습니다. 교통편 접근성이 좋고 직원들이 친절하다는 점이 강조되었습니다."""
    
    try:
        # 리뷰 요약 실행
        summary = summarize_single_review(client, review_text)
        return f"✅ 요약 완료!\n\n{summary}"
        
    except Exception as e:
        return f"❌ 요약 중 오류가 발생했습니다: {str(e)}"


def create_gradio_interface():
    """
    Gradio 웹 인터페이스를 생성합니다.
    """
    # Gradio 인터페이스 생성
    with gr.Blocks(
        title="🏨 리뷰 요약 AI",
        theme=gr.themes.Soft(),
        css="""
        .gradio-container {
            max-width: 800px !important;
            margin: auto !important;
        }
        .main-header {
            text-align: center;
            margin-bottom: 30px;
        }
        .example-box {
            background-color: #f8f9fa;
            border: 1px solid #dee2e6;
            border-radius: 8px;
            padding: 15px;
            margin: 10px 0;
        }
        """
    ) as interface:
        
        # 헤더
        gr.HTML("""
        <div class="main-header">
            <h1>🏨 리뷰 요약 AI</h1>
            <p>호텔 리뷰를 입력하면 AI가 핵심 내용을 2~3문장으로 요약해드립니다</p>
        </div>
        """)
        
        # 메인 입력/출력 영역
        with gr.Row():
            with gr.Column(scale=1):
                # 입력 영역
                review_input = gr.Textbox(
                    label="📝 리뷰 텍스트 입력",
                    placeholder="호텔 리뷰를 여기에 입력하세요...",
                    lines=8,
                    max_lines=15,
                    info="호텔에 대한 리뷰를 자유롭게 작성해주세요."
                )
                
                # 버튼
                summarize_btn = gr.Button(
                    "🚀 요약하기",
                    variant="primary",
                    size="lg"
                )
                
                # 예시 리뷰
                gr.HTML("""
                <div class="example-box">
                    <h4>💡 예시 리뷰</h4>
                    <p><strong>긍정적 리뷰:</strong><br>
                    "호텔 위치가 정말 좋았어요! 지하철역에서 도보 5분 거리이고 주변에 맛집도 많았습니다. 직원분들도 친절하시고 룸도 깨끗했어요. 다음에도 꼭 이용하고 싶습니다."</p>
                    
                    <p><strong>부정적 리뷰:</strong><br>
                    "체크인 시간이 너무 오래 걸렸고, 룸이 생각보다 작았습니다. 에어컨 소음이 심해서 잠을 제대로 못 잤어요. 위치는 좋지만 서비스는 아쉬웠습니다."</p>
                </div>
                """)
            
            with gr.Column(scale=1):
                # 출력 영역
                summary_output = gr.Textbox(
                    label="📋 요약 결과",
                    lines=8,
                    interactive=False,
                    info="AI가 분석한 리뷰 요약 결과입니다."
                )
        
        # 이벤트 핸들러 연결
        summarize_btn.click(
            fn=summarize_review,
            inputs=[review_input],
            outputs=[summary_output]
        )
        
        # Enter 키로도 요약 가능
        review_input.submit(
            fn=summarize_review,
            inputs=[review_input],
            outputs=[summary_output]
        )
        
        # 푸터
        gr.HTML("""
        <div style="text-align: center; margin-top: 30px; color: #666;">
            <p>🤖 Powered by OpenAI GPT-3.5-turbo | Made with ❤️ using Gradio</p>
        </div>
        """)
    
    return interface


def main():
    """
    메인 실행 함수
    """
    print("🚀 Gradio 리뷰 요약 웹 앱을 시작합니다...")
    
    # 환경 변수 로드 및 API 키 확인 (앱 시작 시 가장 먼저 실행)
    api_key = initialize_app()
    
    if not api_key:
        print("⚠️  OPENAI_API_KEY가 설정되지 않았습니다.")
        print("다음 중 하나의 방법으로 API 키를 설정하세요:")
        print("1. 프로젝트 루트에 .env 파일을 생성하고 OPENAI_API_KEY=your-key-here 추가")
        print("2. 환경변수로 직접 설정")
        return
    
    # Gradio 인터페이스 생성 및 실행
    interface = create_gradio_interface()
    
    print("🌐 웹 인터페이스가 준비되었습니다!")
    print("📱 브라우저에서 자동으로 열립니다...")
    
    # 인터페이스 실행
    interface.launch(
        server_name="127.0.0.1",  # 로컬호스트에서만 접근 가능
        server_port=7861,         # 포트 번호
        share=False,              # 공개 링크 생성 여부
        debug=False,              # 디버그 모드
        show_error=True,          # 에러 표시
        quiet=False,              # 로그 출력
        inbrowser=False           # 브라우저 자동 오픈 비활성화
    )


if __name__ == "__main__":
    main()

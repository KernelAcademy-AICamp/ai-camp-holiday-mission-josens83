"""
환경변수 설정 파일
OpenAI API 키를 관리합니다.
"""
import os
from dotenv import load_dotenv

# .env 파일 로드 (있는 경우)
load_dotenv()

# OpenAI API 키 설정
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')

# API 키가 설정되지 않은 경우 안내 메시지
if not OPENAI_API_KEY:
    print("⚠️  OPENAI_API_KEY가 설정되지 않았습니다.")
    print("다음 중 하나의 방법으로 API 키를 설정하세요:")
    print("1. .env 파일에 OPENAI_API_KEY=your-key-here 추가")
    print("2. 환경변수로 직접 설정")
    print("3. config.py 파일에서 직접 설정")


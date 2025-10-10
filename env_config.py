"""
환경 변수 로딩 및 API 키 관리 모듈
앱 시작 시 가장 먼저 .env 파일을 로드하고 API 키 상태를 확인합니다.
"""

import os
import logging
from dotenv import load_dotenv

# 로깅 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def load_environment():
    """
    .env 파일을 로드하고 환경 변수를 설정합니다.
    앱 시작 시 가장 먼저 호출되어야 합니다.
    """
    # .env 파일 로드
    env_path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(env_path)
    
    logger.info("🔧 Environment variables loaded from .env file")


def check_api_key():
    """
    OPENAI_API_KEY가 설정되어 있는지 확인하고 로그를 출력합니다.
    
    Returns:
        str: API 키가 있으면 키의 앞 6자리를 포함한 문자열, 없으면 None
    """
    api_key = os.getenv('OPENAI_API_KEY')
    
    if api_key:
        # API 키의 앞 6자리만 표시 (보안을 위해)
        masked_key = api_key[:6] + "..." if len(api_key) > 6 else api_key
        logger.info(f"✅ API KEY OK: {masked_key}")
        return api_key
    else:
        logger.warning("❌ API KEY MISSING")
        return None


def initialize_app():
    """
    앱 초기화 함수 - 환경 변수 로드 및 API 키 확인
    모든 앱의 시작점에서 호출해야 합니다.
    
    Returns:
        str: API 키 (있으면), None (없으면)
    """
    # 1. 환경 변수 로드
    load_environment()
    
    # 2. API 키 확인
    api_key = check_api_key()
    
    return api_key


if __name__ == "__main__":
    # 테스트 실행
    print("🧪 Testing environment loading...")
    api_key = initialize_app()
    
    if api_key:
        print(f"✅ App initialization successful. API key available.")
    else:
        print("⚠️ App initialization completed, but API key is missing.")

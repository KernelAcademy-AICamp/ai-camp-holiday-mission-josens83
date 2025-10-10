"""
OpenAI 클라이언트 초기화 모듈
.env 파일에서 OPENAI_API_KEY를 불러와서 OpenAI 클라이언트를 초기화합니다.
"""

import os
from openai import OpenAI
from typing import Optional
from env_config import initialize_app


def initialize_openai_client() -> Optional[OpenAI]:
    """
    .env 파일에서 OPENAI_API_KEY를 불러와서 OpenAI 클라이언트를 초기화합니다.
    
    Returns:
        OpenAI: 초기화된 OpenAI 클라이언트 객체
        None: API 키가 없거나 초기화에 실패한 경우
        
    Raises:
        ValueError: API 키가 없을 경우
        Exception: 기타 초기화 오류
    """
    try:
        # 환경 변수 로드 및 API 키 확인
        api_key = initialize_app()
        
        if not api_key:
            raise ValueError(
                "OPENAI_API_KEY가 설정되지 않았습니다. "
                ".env 파일에 'OPENAI_API_KEY=your_api_key_here'를 추가해주세요."
            )
        
        # API 키가 비어있는 경우 체크
        if api_key.strip() == "":
            raise ValueError(
                "OPENAI_API_KEY가 비어있습니다. "
                "유효한 API 키를 .env 파일에 설정해주세요."
            )
        
        # OpenAI 클라이언트 초기화
        client = OpenAI(api_key=api_key)
        
        print("✅ OpenAI 클라이언트가 성공적으로 초기화되었습니다.")
        return client
        
    except ValueError as e:
        print(f"❌ API 키 오류: {e}")
        return None
        
    except Exception as e:
        print(f"❌ OpenAI 클라이언트 초기화 실패: {e}")
        return None


def test_openai_connection(client: OpenAI) -> bool:
    """
    OpenAI 클라이언트 연결을 테스트합니다.
    
    Args:
        client: OpenAI 클라이언트 객체
        
    Returns:
        bool: 연결 성공 여부
    """
    try:
        # 간단한 API 호출로 연결 테스트
        models = client.models.list()
        print("✅ OpenAI API 연결 테스트 성공")
        return True
        
    except Exception as e:
        print(f"❌ OpenAI API 연결 테스트 실패: {e}")
        return False


if __name__ == "__main__":
    # 클라이언트 초기화 테스트
    client = initialize_openai_client()
    
    if client:
        # 연결 테스트
        test_openai_connection(client)
    else:
        print("클라이언트 초기화에 실패했습니다.")

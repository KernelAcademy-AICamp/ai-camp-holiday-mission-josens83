@echo off
echo AI Camp Holiday Mission - 가상환경 설정 스크립트
echo ================================================

echo.
echo 1. Python 가상환경 생성 중...
python -m venv venv

echo.
echo 2. 가상환경 활성화 중...
call venv\Scripts\activate.bat

echo.
echo 3. pip 업그레이드 중...
python -m pip install --upgrade pip

echo.
echo 4. 필요한 패키지 설치 중...
pip install -r requirements.txt

echo.
echo 5. Jupyter 커널 등록 중...
python -m ipykernel install --user --name=ai-camp-holiday --display-name="AI Camp Holiday Mission"

echo.
echo ================================================
echo 가상환경 설정이 완료되었습니다!
echo.
echo 가상환경 활성화: venv\Scripts\activate.bat
echo Jupyter 실행: jupyter lab
echo Gradio 데모 실행: python demo.py
echo ================================================
pause

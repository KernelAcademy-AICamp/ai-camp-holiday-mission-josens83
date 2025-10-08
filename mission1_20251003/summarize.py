import os
import json
from dotenv import load_dotenv
from openai import OpenAI

# ------------------------------------------------------------
# 1️⃣ 환경 변수 불러오기 (.env에서 OPENAI_API_KEY 로드)
# ------------------------------------------------------------
# ⚠️ .env 파일 예시:
# OPENAI_API_KEY=sk-xxxxx...
# ------------------------------------------------------------

load_dotenv()  # 현재 폴더 또는 상위 폴더의 .env 파일 자동 로드

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("❌ 환경 변수 OPENAI_API_KEY가 없습니다. .env 파일을 확인하세요!")

# OpenAI 클라이언트 생성
client = OpenAI(api_key=api_key)

# ------------------------------------------------------------
# 2️⃣ 입력/출력 파일 경로 설정
# ------------------------------------------------------------
INPUT_FILE = "filtered_reviews.json"
OUTPUT_FILE = "summary.txt"

# ------------------------------------------------------------
# 3️⃣ 리뷰 데이터 로드
# ------------------------------------------------------------
try:
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        reviews = json.load(f)
except FileNotFoundError:
    raise FileNotFoundError(f"❌ '{INPUT_FILE}' 파일이 존재하지 않습니다.")
except json.JSONDecodeError:
    raise ValueError(f"❌ '{INPUT_FILE}' 파일의 JSON 형식이 잘못되었습니다.")

# ------------------------------------------------------------
# 4️⃣ 리뷰 텍스트 합치기
# ------------------------------------------------------------
texts = []
for r in reviews:
    if isinstance(r, dict):
        text = r.get("text") or r.get("review")
        if text:
            texts.append(text.strip())

if not texts:
    raise ValueError("❌ 리뷰 텍스트가 비어 있습니다. JSON 데이터 구조를 확인하세요.")

all_text = "\n".join(texts[:100])  # 너무 많으면 모델 입력 초과 방지 (100개까지만 사용)

# ------------------------------------------------------------
# 5️⃣ 프롬프트 구성
# ------------------------------------------------------------
prompt = f"""
다음은 한 호텔에 대한 실제 고객 리뷰 모음이야.
이 리뷰들을 3문장 이내로 핵심만 요약해줘.
특히 청결, 위치, 서비스, 불편사항에 초점을 맞춰줘.

리뷰들:
{all_text}
"""

# ------------------------------------------------------------
# 6️⃣ OpenAI 모델 호출
# ------------------------------------------------------------
try:
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # 빠르고 저렴한 모델
        messages=[
            {"role": "system", "content": "너는 호텔 리뷰를 요약하는 전문가야."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.4  # 안정적인 요약을 위해 낮은 값
    )
    summary = response.choices[0].message.content.strip()

except Exception as e:
    raise RuntimeError(f"❌ OpenAI API 호출 중 오류 발생: {e}")

# ------------------------------------------------------------
# 7️⃣ 요약 결과 저장
# ------------------------------------------------------------
try:
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(summary)
    print("✅ 요약문 생성 완료! summary.txt 파일을 확인하세요.")
except Exception as e:
    raise RuntimeError(f"❌ 요약 파일 저장 중 오류 발생: {e}")

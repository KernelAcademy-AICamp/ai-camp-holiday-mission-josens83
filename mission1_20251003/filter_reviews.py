import json
import re

# 파일 불러오기
with open("reviews.json", "r", encoding="utf-8") as f:
    reviews = json.load(f)

filtered = []
for r in reviews:
    text = r["text"]

    # ✅ 기본 정제: 특수문자, 줄바꿈, 공백 정리
    text = text.replace("\n", " ").replace("\r", " ")
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"[^ㄱ-ㅎ가-힣0-9a-zA-Z\s.,!?]", "", text)

    # ✅ 너무 짧은 문장은 제거 (10자 미만)
    if len(text) >= 10:
        filtered.append({"date": r["date"], "text": text})

# ✅ 파일 저장
with open("filtered_reviews.json", "w", encoding="utf-8") as f:
    json.dump(filtered, f, ensure_ascii=False, indent=2)

print(f"✅ 정제 완료! {len(filtered)}개의 리뷰를 filtered_reviews.json에 저장했습니다.")

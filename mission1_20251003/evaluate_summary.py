from pathlib import Path

def evaluate_summary(path="summary.txt"):
    text = Path(path).read_text(encoding="utf-8")

    # 1️⃣ 길이 검사
    length = len(text)
    if length < 100:
        print("⚠️ 요약이 너무 짧아요 (100자 미만)")
    elif length > 3000:
        print("⚠️ 요약이 너무 길어요 (3000자 초과)")
    else:
        print("✅ 길이 적당함")

    # 2️⃣ 중복 문장 검사
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    duplicates = [l for l in lines if lines.count(l) > 1]
    if duplicates:
        print(f"⚠️ 중복된 문장 발견: {set(duplicates)}")
    else:
        print("✅ 중복 없음")

    # 3️⃣ 기본 단어 점검
    positive_keywords = ["좋다", "깨끗", "친절", "만족", "추천"]
    negative_keywords = ["불친절", "더럽", "시끄럽", "비싸", "아쉽"]

    pos_hits = sum(k in text for k in positive_keywords)
    neg_hits = sum(k in text for k in negative_keywords)
    print(f"✅ 긍정 단어 수: {pos_hits}, 부정 단어 수: {neg_hits}")

    if pos_hits + neg_hits == 0:
        print("⚠️ 긍정/부정 표현이 너무 적어요 — 요약이 일반적일 수 있음")

if __name__ == "__main__":
    evaluate_summary()

import json, datetime

# 강의 조건 --------------------------------------------------
# 1) 모텔은 3개월, 호텔/펜션/게하 등은 6개월 (여기선 6개월 기준 적용)
MONTH_WINDOW = 6
# 2) 후기 3개 이상 + 총 글자수 90자 이상
MIN_COUNT = 3
MIN_CHARS = 90
# 3) 최대 50개까지만 사용
MAX_REVIEWS = 50
# -----------------------------------------------------------

def load_seed(path="seed_reviews.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def filter_by_date(reviews, month_window=MONTH_WINDOW):
    cutoff = datetime.datetime.now() - datetime.timedelta(days=30*month_window)
    kept = []
    for r in reviews:
        try:
            d = datetime.datetime.strptime(r["date"], "%Y.%m.%d")
            if d >= cutoff:
                kept.append({**r, "date_obj": d})
        except:
            # 날짜 파싱 실패는 제외
            pass
    # 최신순 정렬
    kept.sort(key=lambda x: x["date_obj"], reverse=True)
    return kept

def enforce_rules(reviews):
    # 최대 50개 제한
    reviews = reviews[:MAX_REVIEWS]
    total_text = "".join([r["text"] for r in reviews])
    if len(reviews) < MIN_COUNT or len(total_text) < MIN_CHARS:
        return None
    # 저장 형식 단순화
    return [{"date": r["date"], "text": r["text"]} for r in reviews]

def main():
    seed = load_seed()
    recent = filter_by_date(seed)
    final = enforce_rules(recent)
    if final is None:
        print("⚠️ 조건 미달(개수<3 또는 총 90자 미만). 파일 생성 안 함.")
        return
    with open("reviews.json", "w", encoding="utf-8") as f:
        json.dump(final, f, ensure_ascii=False, indent=2)
    print(f"✅ reviews.json 생성 완료! (리뷰 {len(final)}개)")

if __name__ == "__main__":
    main()

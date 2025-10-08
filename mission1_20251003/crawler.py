import requests
from bs4 import BeautifulSoup
import json
import datetime
import time

def fetch_reviews(hotel_url, pages=3, max_reviews=50):
    """야놀자 숙소 후기 페이지에서 최근 3~6개월 내 리뷰 수집"""
    all_reviews = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/115.0 Safari/537.36"
    }

    for page in range(1, pages + 1):
        url = f"{hotel_url}?page={page}"
        print(f"[{page}페이지 요청 중] {url}")
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"⚠️ 요청 실패: {response.status_code}")
            continue

        soup = BeautifulSoup(response.text, "html.parser")

        # HTML 구조 예시 (실제 class명은 사이트 구조에 따라 조정)
        review_blocks = soup.find_all("div", class_="review-block")

        for block in review_blocks:
            text_tag = block.find("div", class_="review-text")
            date_tag = block.find("span", class_="date")
            if not text_tag or not date_tag:
                continue

            review_text = text_tag.get_text(strip=True)
            review_date = date_tag.get_text(strip=True)
            all_reviews.append({"date": review_date, "text": review_text})

        time.sleep(1)  # 과도한 요청 방지

    # 날짜 필터링 (최근 6개월 이내)
    cutoff_date = datetime.datetime.now() - datetime.timedelta(days=180)
    filtered = []
    for r in all_reviews:
        try:
            date_obj = datetime.datetime.strptime(r["date"], "%Y.%m.%d")
            if date_obj > cutoff_date:
                filtered.append(r)
        except:
            continue

    # 조건 필터링 (리뷰 수 / 글자 수)
    total_text = "".join([r["text"] for r in filtered])
    if len(filtered) < 3 or len(total_text) < 90:
        print("⚠️ 후기 수 부족 혹은 글자 수 부족 → 요약 불가")
        return None

    # 최신순 정렬 후 50개까지만 사용
    filtered = sorted(filtered, key=lambda x: x["date"], reverse=True)[:max_reviews]
    print(f"✅ 수집 완료: {len(filtered)}개 리뷰")

    return filtered


if __name__ == "__main__":
    # ⚙️ 예시 URL (실제 숙소별 ID로 변경)
    hotel_url = "https://www.yanolja.com/hotel/100123/reviews"

    reviews = fetch_reviews(hotel_url, pages=3)

    if reviews:
        with open("reviews.json", "w", encoding="utf-8") as f:
            json.dump(reviews, f, ensure_ascii=False, indent=2)
        print("💾 reviews.json 파일 생성 완료!")
    else:
        print("❌ 조건에 맞는 리뷰가 없어 파일을 생성하지 않았습니다.")


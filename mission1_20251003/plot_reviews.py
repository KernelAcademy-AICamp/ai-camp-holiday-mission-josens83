import json
from collections import Counter
import matplotlib.pyplot as plt

with open("reviews.json", "r", encoding="utf-8") as f:
    reviews = json.load(f)

# 별점 카운트
stars = [r["stars"] for r in reviews if isinstance(r["stars"], int)]
cnt = Counter(stars)

# 그래프
plt.bar(cnt.keys(), cnt.values())
plt.title("별점 분포")
plt.xlabel("별점")
plt.ylabel("리뷰 개수")
plt.xticks([1,2,3,4,5])
plt.show()

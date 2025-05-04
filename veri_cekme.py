import requests
import json
import time
import csv

app_id = 730  # CS2 App ID
url = f"https://store.steampowered.com/appreviews/{app_id}?json=1"

params = {
    "filter": "recent",
    "language": "english",  # Yalnızca İngilizce yorumlar
    "day_range": 30,
    "review_type": "all",
    "purchase_type": "all",
    "num_per_page": 100,
    "cursor": "*"
}

all_reviews = []
total_reviews_needed = 5000

while len(all_reviews) < total_reviews_needed:
    response = requests.get(url, params=params)
    data = response.json()

    if "reviews" not in data:
        print("Veri çekilemedi, duruyoruz.")
        break

    reviews = data["reviews"]
    all_reviews.extend(reviews)

    print(f"Şu an çekilen toplam yorum sayısı: {len(all_reviews)}")

    # Cursor'u güncelle
    params["cursor"] = data.get("cursor", "*")

    # API'yi rahat bırakmak için 1 saniye bekleme
    time.sleep(1)

# Fazla çekildiyse keselim
all_reviews = all_reviews[:3000]

# CSV dosyasına kaydet
with open("cs2_yorumlar_ingilizce_5000.csv", "w", newline='', encoding="utf-8") as csvfile:

    fieldnames = ["steamid", "yorum", "begeni", "oynanan_saat"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for review in all_reviews:
        writer.writerow({
            "steamid": review['author']['steamid'],
            "yorum": review['review'],
            "begeni": "Evet" if review['voted_up'] else "Hayır",
            "oynanan_saat": review['author'].get('playtime_forever', 0) / 60  # dakika -> saat
        })

print("Toplam", len(all_reviews), "yorum çekildi ve cs2_yorumlar_ingilizce_5000.csv dosyasına kaydedildi.")

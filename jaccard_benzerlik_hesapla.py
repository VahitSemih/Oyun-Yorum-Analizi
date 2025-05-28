import pandas as pd
from itertools import combinations

# CSV dosyasını yükle (ilk 5 öneri yorum ID'leri içerir)
df = pd.read_csv("anlamsal_degerlendirme_template.csv")

# Her modelin 5 benzer metin setini hazırla
model_docs = {
    row['Model Adı']: set(row['5 Benzer Metin'].split(", "))
    for _, row in df.iterrows()
}

# Jaccard benzerliğini hesapla
def jaccard_benzerlik(set1, set2):
    return len(set1 & set2) / len(set1 | set2) if set1 | set2 else 0

# Sonuçları sakla
sonuclar = []

for model1, model2 in combinations(model_docs.keys(), 2):
    skor = jaccard_benzerlik(model_docs[model1], model_docs[model2])
    sonuclar.append({
        "Model A": model1,
        "Model B": model2,
        "Jaccard Benzerliği": round(skor, 3)
    })

# Sonuçları CSV'ye yaz
pd.DataFrame(sonuclar).to_csv("jaccard_benzerlikleri.csv", index=False, encoding="utf-8-sig")

print("✅ Jaccard benzerlikleri hesaplandı ve 'jaccard_benzerlikleri.csv' dosyasına kaydedildi.")

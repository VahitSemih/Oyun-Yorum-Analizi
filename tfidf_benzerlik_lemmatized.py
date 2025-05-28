import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def yukle_ve_hazirla(tfidf_path, text_path):
    # TF-IDF vektörlerini yükle
    tfidf_df = pd.read_csv(tfidf_path, index_col=0)

    # Metinleri yükle
    text_df = pd.read_csv(text_path)

    # "yorum" dışında kalan sütunu bul ve kullan
    metin_sutunlari = [col for col in text_df.columns if col != "yorum"]
    if not metin_sutunlari:
        raise ValueError("⚠️ 'yorum' dışındaki lemmatized metin sütunu bulunamadı.")

    secilen_sutun = metin_sutunlari[0]
    metinler = text_df[secilen_sutun].astype(str).tolist()
    return tfidf_df, metinler


def en_benzer_yorumlar(tfidf_df, metinler, index=0, top_n=5):
    print(f"\n🎯 Giriş Yorumu [{index}]:\n{metinler[index]}")
    benzerlik_matrisi = cosine_similarity(tfidf_df)
    benzerlikler = benzerlik_matrisi[index]
    benzer_indexler = np.argsort(benzerlikler)[::-1][1:top_n + 1]
    print("\n🔗 En Benzer Yorumlar:")
    for i in benzer_indexler:
        print(f"\n🔸 Yorum [{i}] (Skor: {benzerlikler[i]:.4f}):\n{metinler[i]}")


if __name__ == "__main__":
    tfidf_path = "tfidf_lemmatized.csv"
    text_path = "lemmatized_output.csv"

    tfidf_df, metinler = yukle_ve_hazirla(tfidf_path, text_path)
    en_benzer_yorumlar(tfidf_df, metinler, index=0, top_n=5)

import pandas as pd
import numpy as np
from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity
import os

def ortalama_vektor(cumle, model):
    kelimeler = cumle.split()
    vectors = [model.wv[word] for word in kelimeler if word in model.wv]
    return np.mean(vectors, axis=0) if vectors else np.zeros(model.vector_size)

def en_benzer_yorumlar(vektorler, metinler, index=0, top_n=5):
    benzerlik_matrisi = cosine_similarity([vektorler[index]], vektorler)[0]
    benzer_indexler = np.argsort(benzerlik_matrisi)[::-1][1:top_n+1]
    return [(i, benzerlik_matrisi[i], metinler[i]) for i in benzer_indexler]

def calistir_model(model_path, metinler, model_bilgi):
    print(f"\n📦 Model yükleniyor: {model_path}")
    model = Word2Vec.load(model_path)
    vektorler = np.array([ortalama_vektor(cumle, model) for cumle in metinler])
    sonuçlar = en_benzer_yorumlar(vektorler, metinler, index=0, top_n=5)

    liste = []
    for idx, skor, cumle in sonuçlar:
        liste.append({
            "Model_Tipi": model_bilgi["model_type"],
            "Window": model_bilgi["window"],
            "Vektör_Boyu": model_bilgi["vector_size"],
            "Yorum_Index": idx,
            "Benzerlik_Skoru": skor,
            "Yorum_Metni": cumle
        })

    return liste

if __name__ == "__main__":
    veri_tipi = "lemmatized"  # Bu script lemmatized veriler içindir
    metin_dosya_yolu = f"{veri_tipi}_output.csv"
    text_df = pd.read_csv(metin_dosya_yolu)
    metin_kolonu = [col for col in text_df.columns if col != "yorum"][0]
    metinler = text_df[metin_kolonu].astype(str).tolist()

    parametreler = [
        {'model_type': 'cbow', 'window': 2, 'vector_size': 100},
        {'model_type': 'skipgram', 'window': 2, 'vector_size': 100},
        {'model_type': 'cbow', 'window': 4, 'vector_size': 100},
        {'model_type': 'skipgram', 'window': 4, 'vector_size': 100},
        {'model_type': 'cbow', 'window': 2, 'vector_size': 300},
        {'model_type': 'skipgram', 'window': 2, 'vector_size': 300},
        {'model_type': 'cbow', 'window': 4, 'vector_size': 300},
        {'model_type': 'skipgram', 'window': 4, 'vector_size': 300}
    ]

    tüm_sonuçlar = []

    for p in parametreler:
        model_adi = f"word2vec_{veri_tipi}_{p['model_type']}_win{p['window']}_dim{p['vector_size']}.model"
        if os.path.exists(model_adi):
            liste = calistir_model(model_adi, metinler, p)
            tüm_sonuçlar.extend(liste)
        else:
            print(f"⚠️ Model bulunamadı: {model_adi}")

    # Sonuçları tek bir CSV dosyasına kaydet
    sonuc_df = pd.DataFrame(tüm_sonuçlar)
    sonuc_df.to_csv("word2vec_lemmatized_tum_sonuclar.csv", index=False, encoding="utf-8-sig")
    print("\n✅ Tüm sonuçlar kaydedildi: word2vec_lemmatized_tum_sonuclar.csv")

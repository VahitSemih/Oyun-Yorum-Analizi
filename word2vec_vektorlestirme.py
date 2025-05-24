import pandas as pd
from gensim.models import Word2Vec

# Parametreler
parameters = [
    {'model_type': 'cbow', 'window': 2, 'vector_size': 100},
    {'model_type': 'skipgram', 'window': 2, 'vector_size': 100},
    {'model_type': 'cbow', 'window': 4, 'vector_size': 100},
    {'model_type': 'skipgram', 'window': 4, 'vector_size': 100},
    {'model_type': 'cbow', 'window': 2, 'vector_size': 300},
    {'model_type': 'skipgram', 'window': 2, 'vector_size': 300},
    {'model_type': 'cbow', 'window': 4, 'vector_size': 300},
    {'model_type': 'skipgram', 'window': 4, 'vector_size': 300}
]

# Dosya yolları
stemmed_file = "stemmed_output.csv"
lemmatized_file = "lemmatized_output.csv"

# CSV'leri oku
stemmed_df = pd.read_csv(stemmed_file)
print("Stemmed CSV sütunları:", stemmed_df.columns.tolist())
stem_col = [c for c in stemmed_df.columns if c != "yorum"][0]
stemmed_corpus = stemmed_df[stem_col].astype(str)

lemmatized_df = pd.read_csv(lemmatized_file)
print("Lemmatized CSV sütunları:", lemmatized_df.columns.tolist())
lemma_col = [c for c in lemmatized_df.columns if c != "yorum"][0]
lemmatized_corpus = lemmatized_df[lemma_col].astype(str)

# Model eğitimi
def train_word2vec(corpus, model_type, window, vector_size, data_label):
    tokenized_corpus = [sentence.split() for sentence in corpus]

    model = Word2Vec(
        sentences=tokenized_corpus,
        vector_size=vector_size,
        window=window,
        sg=1 if model_type == 'skipgram' else 0,
        min_count=1,  # ✅ min_count=1 olarak ayarlandı
        workers=4
    )

    model_filename = f"word2vec_{data_label}_{model_type}_win{window}_dim{vector_size}.model"
    model.save(model_filename)
    print(f"✅ Model kaydedildi: {model_filename}")

    # "oyun" kelimesi varsa en yakın 5 kelimeyi göster
    if "oyun" in model.wv:
        print(f"\n🔍 {data_label} - {model_type} - window:{window} - dim:{vector_size}")
        print("En yakın 5 kelime (oyun):", model.wv.most_similar("oyun", topn=5))
    else:
        print(f"⚠️ 'oyun' kelimesi {data_label} ({model_type}, win:{window}) modelinde bulunamadı.")

    return model

# Tüm kombinasyonları çalıştır
for data_label, corpus in [("lemmatized", lemmatized_corpus), ("stemmed", stemmed_corpus)]:
    for params in parameters:
        train_word2vec(
            corpus=corpus,
            model_type=params['model_type'],
            window=params['window'],
            vector_size=params['vector_size'],
            data_label=data_label
        )

import pandas as pd
from gensim.models import Word2Vec
import gensim.downloader as api

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

# Stemmed Veri Seti
stemmed_file = "yorumlar_stemmed.csv"  # Stemmed veri setinizin dosya yolu
stemmed_df = pd.read_csv(stemmed_file)
print("Stemmed CSV sütunları:", stemmed_df.columns.tolist())
# "yorum" hariç diğer sütun stemmed verisini içeriyor
stem_col = [c for c in stemmed_df.columns if c != "yorum"][0]
stemmed_corpus = stemmed_df[stem_col].astype(str)

# Lemmatized Veri Seti
lemmatized_file = "yorumlar_lemmatized.csv"  # Lemmatized veri setinizin dosya yolu
lemmatized_df = pd.read_csv(lemmatized_file)
print("Lemmatized CSV sütunları:", lemmatized_df.columns.tolist())
# "yorum" hariç diğer sütun lemmatized verisini içeriyor
lemma_col = [c for c in lemmatized_df.columns if c != "yorum"][0]
lemmatized_corpus = lemmatized_df[lemma_col].astype(str)


# Word2Vec Modelini Eğitme ve Kaydetme
def train_word2vec(corpus, model_type, window, vector_size, data_label):
    # Tokenize metni
    tokenized_corpus = [sentence.split() for sentence in corpus]

    # Modeli oluştur
    model = Word2Vec(
        sentences=tokenized_corpus,
        vector_size=vector_size,
        window=window,
        sg=1 if model_type == 'skipgram' else 0,
        min_count=5,  # Kelime sayısı 5'ten azsa dikkate alınmaz
        workers=4
    )

    # Modeli kaydet
    model_filename = f"word2vec_{data_label}_{model_type}_win{window}_dim{vector_size}.model"
    model.save(model_filename)
    print(f"✅ {model_filename} oluşturuldu.")

    return model


# Verileri işleyip model eğitme
for data_label, corpus in [("lemmatized", lemmatized_corpus), ("stemmed", stemmed_corpus)]:
    for params in parameters:
        model = train_word2vec(corpus, params['model_type'], params['window'], params['vector_size'], data_label)

        # Örnek kelime vektörleri - Örneğin, "oyun" kelimesine en yakın 5 kelimeyi yazdır
        if "oyun" in model.wv:
            print(f"\n{data_label} - {params['model_type']} - {params['window']} - {params['vector_size']}:")
            print(f"En yakın 5 kelime (oyun için): {model.wv.most_similar('oyun', topn=5)}")
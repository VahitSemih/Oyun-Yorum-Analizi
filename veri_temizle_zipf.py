import pandas as pd
import nltk
import string
import re
import matplotlib.pyplot as plt
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Gerekli NLTK verileri
nltk.download('stopwords')
nltk.download('wordnet')

# CSV dosyasını oku
df = pd.read_csv("cs2_yorumlar_ingilizce_5000.csv")

# NLP araçları
tokenizer = RegexpTokenizer(r'\b[a-zA-Z]{2,}\b')
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# Temizleme ve NLP işlemi
def process_text(text):
    text = text.lower()
    tokens = tokenizer.tokenize(text)
    tokens_cleaned = [word for word in tokens if word not in stop_words]
    tokens_stemmed = [stemmer.stem(word) for word in tokens_cleaned]
    tokens_lemmatized = [lemmatizer.lemmatize(word) for word in tokens_cleaned]
    return " ".join(tokens_stemmed), " ".join(tokens_lemmatized)

# Listeler oluştur
stemmed_list = []
lemmatized_list = []

for comment in df['yorum'].astype(str):
    stemmed, lemmatized = process_text(comment)
    stemmed_list.append(stemmed)
    lemmatized_list.append(lemmatized)

# Yeni sütunlar ekle
df['stemmed'] = stemmed_list
df['lemmatized'] = lemmatized_list

# Sonuçları kaydet
df[['stemmed']].to_csv("stemmed_output.csv", index=False)
df[['lemmatized']].to_csv("lemmatized_output.csv", index=False)

# Zipf grafiği çizme
def plot_zipf(file_path, column_name, title):
    df = pd.read_csv(file_path)
    df = df.dropna(subset=[column_name])
    all_words = " ".join(df[column_name].astype(str)).split()
    word_freq = Counter(all_words)
    sorted_freq = sorted(word_freq.values(), reverse=True)[:1000]

    plt.figure(figsize=(10, 6))
    plt.plot(range(1, len(sorted_freq)+1), sorted_freq)
    plt.xscale('log')
    plt.yscale('log')
    plt.title(f"Zipf Plot - {title}")
    plt.xlabel("Kelime Sırası (log)")
    plt.ylabel("Frekans (log)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{title.replace(' ', '_').lower()}_zipf.png")
    plt.show()

# Grafik üret
plot_zipf("stemmed_output.csv", "stemmed", "Stemming Sonrası")
plot_zipf("lemmatized_output.csv", "lemmatized", "Lemmatization Sonrası")

# Kelime istatistik fonksiyonu
def get_word_stats_from_texts(texts, title=""):
    all_tokens = []
    for text in texts.astype(str):
        tokens = tokenizer.tokenize(text.lower())
        all_tokens.extend(tokens)
    total_words = len(all_tokens)
    unique_words = len(set(all_tokens))
    print(f"{title} | Toplam kelime: {total_words}, Benzersiz kelime: {unique_words}")
    return total_words, unique_words

# Orijinal veri
original_total, original_unique = get_word_stats_from_texts(df['yorum'], "Orijinal Veri")

# Stemmed
stemmed_total = len(" ".join(df['stemmed'].dropna()).split())
stemmed_unique = len(set(" ".join(df['stemmed'].dropna()).split()))

# Lemmatized
lemmatized_total = len(" ".join(df['lemmatized'].dropna()).split())
lemmatized_unique = len(set(" ".join(df['lemmatized'].dropna()).split()))

# Rapor
print("\nStemming Sonrası:")
print(f"Toplam kelime: {stemmed_total}, Benzersiz kelime: {stemmed_unique}")
print(f"Veri azaltımı: %{100 - (stemmed_total / original_total) * 100:.2f}")

print("\nLemmatization Sonrası:")
print(f"Toplam kelime: {lemmatized_total}, Benzersiz kelime: {lemmatized_unique}")
print(f"Veri azaltımı: %{100 - (lemmatized_total / original_total) * 100:.2f}")

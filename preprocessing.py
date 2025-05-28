import pandas as pd
import nltk
import csv
import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer

# Bu satırlar eksik veya bozuk indirilmiş dosyaları temizler
nltk.download('punkt', force=True)
nltk.download('punkt_tab', force=True)
nltk.download('stopwords', force=True)
nltk.download('wordnet', force=True)

# Dosya adını belirt
csv_file = "cs2_yorumlar_ingilizce_5000.csv"

# Dosya mevcut mu kontrol et
if not os.path.exists(csv_file):
    raise FileNotFoundError(f"Dosya bulunamadı: {csv_file}")

# CSV'yi oku
df = pd.read_csv(csv_file)

# İngilizce stop word listesi
stop_words = set(stopwords.words('english'))

# Lemmatizer ve Stemmer'ları başlat
lemmatizer = WordNetLemmatizer()
english_stemmer = PorterStemmer()

# Cümle işleme fonksiyonu
def preprocess_sentence(sentence):
    if not isinstance(sentence, str) or sentence.strip() == "":
        return [], []
    tokens = word_tokenize(sentence)
    filtered_tokens = [token.lower() for token in tokens if token.isalpha() and token.lower() not in stop_words]
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    stemmed_tokens = [english_stemmer.stem(token) for token in filtered_tokens]
    return lemmatized_tokens, stemmed_tokens

# Tüm yorumları işle
tokenized_corpus_lemmatized = []
tokenized_corpus_stemmed = []

for comment in df["yorum"]:
    lemmatized, stemmed = preprocess_sentence(comment)
    tokenized_corpus_lemmatized.append(lemmatized)
    tokenized_corpus_stemmed.append(stemmed)

# Lemmatize edilmiş cümleleri CSV'ye yaz
with open("lemmatized_sentences.csv", mode="w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    for tokens in tokenized_corpus_lemmatized:
        writer.writerow([' '.join(tokens)])  # Her cümle tek hücrede

# Stem'lenmiş cümleleri CSV'ye yaz
with open("stemmed_sentences.csv", mode="w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    for tokens in tokenized_corpus_stemmed:
        writer.writerow([' '.join(tokens)])

# İlk 5 cümleyi karşılaştırmalı olarak yazdır
for i in range(min(5, len(df))):
    print(f"Cümle {i+1} - Base: {df['yorum'].iloc[i]}")
    print(f"Cümle {i+1} - Lemmatized: {tokenized_corpus_lemmatized[i]}")
    print(f"Cümle {i+1} - Stemmed: {tokenized_corpus_stemmed[i]}")
    print("\n")

# İlk yorumu detaylı analiz et
if len(df) > 0:
    text = df["yorum"].iloc[0]
    print("İlk yorum:", text)
    print("Tokenize edilmiş:", word_tokenize(text.lower()))
    lemmatized, stemmed = preprocess_sentence(text)
    print("Stopword ve temizlik sonrası:", lemmatized)
    print("Stem uygulanmış tokenlar:", stemmed)

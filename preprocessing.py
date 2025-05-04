import pandas as pd
import nltk
import csv
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer

# nltk verilerini bir kez indir
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords")

try:
    nltk.data.find("corpora/wordnet")
except LookupError:
    nltk.download("wordnet")

# CSV'yi oku
df = pd.read_csv("cs2_yorumlar_ingilizce_5000.csv")

# İngilizce stop word listesi
stop_words = set(stopwords.words('english'))

# Lemmatizer ve Stemmer'ları başlat
lemmatizer = WordNetLemmatizer()
english_stemmer = PorterStemmer()

# İşleme fonksiyonu
def preprocess_sentence(sentence):
    tokens = word_tokenize(sentence)
    filtered_tokens = [token.lower() for token in tokens if token.isalpha() and token.lower() not in stop_words]
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    stemmed_tokens = [english_stemmer.stem(token) for token in filtered_tokens]
    return lemmatized_tokens, stemmed_tokens

# Tüm yorumları işle
tokenized_corpus_lemmatized = []
tokenized_corpus_stemmed = []

for comment in df["yorum"]:
    if isinstance(comment, str):  # Sadece string olanları işle
        lemmatized, stemmed = preprocess_sentence(comment)
        tokenized_corpus_lemmatized.append(lemmatized)
        tokenized_corpus_stemmed.append(stemmed)

# CSV'lere yaz
with open("lemmatized_sentences.csv", mode="w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    for tokens in tokenized_corpus_lemmatized:
        writer.writerow([' '.join(tokens)])

with open("stemmed_sentences.csv", mode="w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    for tokens in tokenized_corpus_stemmed:
        writer.writerow([' '.join(tokens)])

# İlk 5 cümleyi yazdıralım
for i in range(5):
    print(f"Cümle {i+1} - Base: {df['yorum'].iloc[i]}")
    print(f"Cümle {i+1} - Lemmatized: {tokenized_corpus_lemmatized[i]}")
    print(f"Cümle {i+1} - Stemmed: {tokenized_corpus_stemmed[i]}")
    print("\n")

# İlk yorumu yaz
text = df["yorum"].iloc[0]
print("İlk yorum:", text)
print("Temizlenmiş tokenlar:", word_tokenize(text.lower()))
print("Stem uygulanmış tokenlar:", tokenized_corpus_stemmed[0])

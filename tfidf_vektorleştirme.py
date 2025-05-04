import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# TF-IDF hesaplama fonksiyonu
def compute_tfidf(csv_path, text_column, output_filename):
    df = pd.read_csv(csv_path)
    df = df.dropna(subset=[text_column])
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(df[text_column])
    tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())
    tfidf_df.to_csv(output_filename, index=False)
    print(f"{output_filename} başarıyla kaydedildi. Boyut: {tfidf_df.shape}")

# Stemmed için TF-IDF
compute_tfidf("stemmed_output.csv", "stemmed", "tfidf_stemmed.csv")

# Lemmatized için TF-IDF
compute_tfidf("lemmatized_output.csv", "lemmatized", "tfidf_lemmatized.csv")

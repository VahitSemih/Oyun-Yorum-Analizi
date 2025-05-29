# 🎮 Oyun Yorum Analizi — Word2Vec ile Vektörleştirme

Bu proje, Steam üzerindeki CS2 (Counter-Strike 2) oyununa ait İngilizce kullanıcı yorumlarının metin işleme (NLP) teknikleriyle analiz edilmesini ve Word2Vec modelleriyle vektörleştirilmesini, yorumlar arasındaki anlamsal benzerliği ölçmek ve farklı vektörleme modellerini karşılaştırmaktır.

## 🗂️ Veri Seti

Veri seti iki farklı ön işlenmiş dosyadan oluşmaktadır:
- `yorumlar_stemmed.csv`: Köklerine indirgenmiş (stemmed) yorumlar.
- `yorumlar_lemmatized.csv`: Lemmatize edilmiş yorumlar.

Her iki dosyada da:
- `yorum`: Orijinal yorum metni
- `stemmed` veya `lemmatized`: Ön işlenmiş yorumlar

Veri seti, metin sınıflandırma, duygu analizi veya öneri sistemlerinde ön işleme/vektörleştirme adımı olarak kullanılabilir.

---

## ⚙️ Modelin Oluşturulması (Adım Adım)

### 1. Reponun Klonlanması

```bash
git clone https://github.com/VahitSemih/Oyun-Yorum-Analizi.git
cd Oyun-Yorum-Analizi
```

### 2. Sanal Ortam Oluştur (Opsiyonel fakat önerilir)

```bash
python -m venv venv
.\venv\Scripts\activate       # Windows
source venv/bin/activate       # macOS/Linux
```

### 3. Gerekli Kütüphanelerin Kurulumu
```bash
pip install -r requirements.txt
```

### 4. Zipf Grafiğinin Oluşturulması
```bash
python zipf.py 
```

### 5. Ön İşleme Adımları
```bash
python preprocessing.py 
```

### 6. Veri Temizlememe ve Temizlenmiş Zipf Grafiğinin Oluşturulması
```bash
python veri_temizle_zipf.py 
```

### 7.TFIDF ile vektörleştirme
```bash
python tfidf_vektorleştirme.py 
```

### 8. Modeli Eğitme Script’ini Çalıştır
```bash
python word2vec_vektorlestirme.py
```

### 9. TF-IDF benzerlik analizi için:
```bash
python tfidf_benzerlik_lemmatized.py
python tfidf_benzerlik_stemmed.py
```

### 10. Word2Vec benzerlik analizi için:
```bash
python word2vec_benzerlik_lemmatized.py
python word2vec_benzerlik_stemmed.py
```
### 11. Jaccard benzerliklerini hesaplamak için:

```bash
python jaccard_benzerlik_hesapla.py
```

# 🧠 Veri Seti Hakkında
- Bu veri seti, oyunlara yapılan kullanıcı yorumlarının analizini içerir. Kullanım amaçları:
- Doğal dil işleme projeleri
- Word2Vec, metin sınıflandırma ve duygu analizi çalışmaları


# 📦 Gerekli Kütüphaneler
- pandas
- gensim
- numpy
- nltk
- csv
- sklearn
- requests
- json
- time
- re
- matplotlib
- collections

Tüm kütüphaneler requirements.txt dosyasında listelenmiştir.
Kurulum:
```bash
pip install -r requirements.txt
```
## 📌 Notlar

- `lemmatized` ve `stemmed` veriler ayrı ayrı değerlendirilmiştir.
- Word2Vec modelleri CBOW ve Skip-gram mimarileriyle, farklı pencere (`window`) ve vektör boyutlarında (`dim`) eğitilmiştir.
- Giriş metni olarak bir oyun yorumu seçilmiş, bu metne en çok benzeyen yorumlar bulunmuştur.

## 👨‍💻 Proje Sahibi

- Vahit Semih Meriç
- Gümüşhane Üniversitesi / Doğal Dil İşleme

# 🎮 Oyun Yorum Analizi — Word2Vec ile Vektörleştirme

Bu proje, oyunlara yapılan yorumların metin işleme (NLP) teknikleriyle analiz edilmesini ve Word2Vec modelleriyle vektörleştirilmesini amaçlar.

## 🧠 Amaç

Bu proje kapsamında:
- İngilizce oyun yorumları **stemmed** ve **lemmatized** olarak ön işlenmiştir.
- Farklı parametre kombinasyonları ile modeller eğitilmiştir.

---

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
### 4. Modeli Eğitme Script’ini Çalıştır
```bash
python word2vec_vektorlestirme.py
```

# 🧠 Veri Seti Hakkında
- Bu veri seti, oyunlara yapılan kullanıcı yorumlarının analizini içerir. Kullanım amaçları:
- Doğal dil işleme projeleri
- Word2Vec, metin sınıflandırma ve duygu analizi çalışmaları


# 📦 Gerekli Kütüphaneler
- pandas
- gensim
- numpy
Tüm kütüphaneler requirements.txt dosyasında listelenmiştir.
Kurulum:
```bash
pip install -r requirements.txt
```

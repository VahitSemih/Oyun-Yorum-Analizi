# 🎮 Oyun Yorum Analizi — Word2Vec ile Vektörleştirme

Bu proje, oyunlara yapılan yorumların metin işleme (NLP) teknikleriyle analiz edilmesini ve Word2Vec modelleriyle vektörleştirilmesini amaçlar.

## 🧠 Amaç

Bu proje kapsamında:
- Türkçe oyun yorumları **stemmed** ve **lemmatized** olarak ön işlenmiştir.
- Yorumlar, **CBOW** ve **Skip-Gram** teknikleriyle Word2Vec vektörlerine dönüştürülmüştür.
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

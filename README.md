
# 🎮 Oyun Yorum Analizi - Steam CS2 Projesi

Bu proje, Steam'deki CS2 (Counter-Strike 2) yorumlarını analiz ederek en yaygın şikayetleri ve olumlu geri bildirimleri tespit etmeyi amaçlar.

---

## 📌 Proje Amacı

- Steam yorumlarını metin madenciliği teknikleriyle analiz etmek
- En sık karşılaşılan problemleri ve memnuniyet kaynaklarını ortaya koymak
- Şikayetleri tematik olarak gruplandırmak

---

## 📁 Veri Seti Hakkında

- **Kaynak:** Steam (Kullanıcı yorumları)
- **Dosya:** `cs2_yorumlar_3000.csv`
- **Sütunlar:**
  - `steamid`: Kullanıcı kimliği
  - `yorum`: Yorum içeriği
  - `begeni`: Beğeni sayısı
  - `oynanan_saat`: Kullanıcının oyunu oynama süresi

**Kullanım amacı:** Oyun hakkında kullanıcı deneyimini analiz etmek; performans, bağlantı, hata ve hile gibi sorunları sınıflandırmak.

---

## ⚙️ Kurulum ve Gerekli Kütüphaneler

Proje Python ile yazılmıştır. Aşağıdaki kütüphaneler gereklidir:

```bash
pip install pandas matplotlib nltk scikit-learn
```

Ayrıca NLTK stopwords paketini indirmeniz gerekir:

```python
import nltk
nltk.download('stopwords')
```

---

## 🛠️ Modelin Oluşturulması (Adım Adım)

1. **Veri setini klasöre yerleştirin:** `cs2_yorumlar_3000.csv`
2. **Ana Python dosyasını çalıştırın:** `cs2_negatif_ngram_analiz.py`
3. **Yorumlar temizlenir:** Küfürler ve anlamsız ifadeler filtrelenir.
4. **Negatif ve pozitif yorumlar ayrılır:** Anahtar kelimelere göre.
5. **N-gram analizi yapılır:** 2-gram ve 3-gram kelime grupları çıkarılır.
6. **Anahtar kelime sıklığı analiz edilir.**
7. **Tematik kümeleme yapılır:** Yorumlar performans, bağlantı vb. temalara göre gruplanır.
8. **Otomatik rapor ve grafikler oluşturulur.**
9. **Sunum dosyası (`.pptx`) hazır hale getirilir.**

---

## 📊 Çıktılar

- Grafikler (N-gram, tema bazlı sayım, pasta grafik)
- Örnek yorumlar ve sorun tipi etiketleri
- Sunuma hazır PowerPoint dosyası (`oyun_yorum_analizi_final.pptx`)

---

## 📌 Not

Bu proje eğitim ve analiz amaçlıdır. Herhangi bir ticari amaç güdülmemektedir.

---

## 🙏 Teşekkürler

Katkılarınız ve geri bildirimleriniz için teşekkür ederim!

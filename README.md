# 🎮 Oyun Yorum Analizi

Bu proje, oyunlara ait kullanıcı yorumlarını doğal dil işleme (NLP) teknikleriyle analiz etmeyi amaçlamaktadır. Yorumlar ön işleme adımlarından geçirilmiş ve Word2Vec yöntemi ile vektörleştirilerek benzerlik analizi yapılmıştır.

---

## 📌 Amaç

Bu proje ile:

- Oyunlar hakkında yapılan kullanıcı yorumları analiz edilebilir,
- Metin verileri anlamlı kelime vektörlerine dönüştürülebilir,
- Sentiment analysis veya tavsiye sistemlerinde kullanılabilecek hazır embedding modelleri elde edilebilir.

---

## 🗂️ Veri Seti

Veri seti iki şekilde hazırlanmıştır:

- **Stemmed**: Yorumlardaki kelimelerin köklerine indirgenmiş hali.
- **Lemmatized**: Kelimelerin sözlük temelli kök hallerine indirgenmiş hali.

Veri seti, kullanıcı yorumlarının daha verimli analiz edilebilmesi için ön işleme (preprocessing) aşamalarından geçirilmiştir. Bu veri seti, Türkçe metin işleme projelerinde kullanılabilir.

---

## 🛠️ Gerekli Kütüphaneler

Projede kullanılan başlıca Python kütüphaneleri:

```txt
pandas
gensim
numpy
scikit-learn

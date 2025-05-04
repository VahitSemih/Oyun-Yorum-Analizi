# Oyun Yorumları Üzerinden Word2Vec Modeli Eğitimi

Bu proje, oyunlara yapılan kullanıcı yorumları üzerinden doğal dil işleme teknikleri kullanarak kelime vektörleri (Word2Vec) üretmeyi amaçlamaktadır. Projede hem **lemmatize** hem de **stem** edilmiş metinler kullanılarak CBOW ve Skip-gram mimarileriyle farklı parametre kombinasyonlarında modeller eğitilmiştir.

---

## 🔧 Model Nasıl Oluşturulur?

### 1. Gerekli Dosyalar
Projede aşağıdaki CSV dosyalarının bulunması gerekir:
- `yorumlar_stemmed.csv`
- `yorumlar_lemmatized.csv`

Her dosya şu sütunları içermelidir:
- `yorum`: Ham kullanıcı yorumu
- `stemmed` veya `lemmatized`: Ön işlenmiş yorumlar

### 2. Adım Adım Model Eğitimi

1. **Sanal Ortam Oluşturun ve Aktif Edin:**

   Windows PowerShell'de:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

2. **Gerekli Kütüphaneleri Yükleyin:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Modeli Eğitin:**
   Aşağıdaki Python dosyasını çalıştırın:
   ```bash
   python word2vec_vektorlestirme.py
   ```

   Bu script, lemmatize ve stemmed veriler için farklı parametrelerde Word2Vec modelleri oluşturur ve `.model` uzantılı olarak kaydeder.

---

## 🎯 Veri Seti Amacı

Veri seti, oyunlara yapılan kullanıcı yorumlarından oluşmaktadır. Metin madenciliği çalışmaları, doğal dil işleme (NLP), duygu analizi ve öneri sistemleri geliştirme gibi çeşitli akademik ve ticari amaçlarla kullanılabilir.

---

## 📦 Gerekli Kütüphaneler ve Kurulum

### requirements.txt (örnek içeriği):
```txt
pandas
gensim==4.3.1
numpy
```

Yüklemek için:
```bash
pip install -r requirements.txt
```

---

## 📁 Çıktılar

Script çalıştırıldığında `word2vec_*.model` formatında 8 farklı model dosyası oluşturulur. Örnek:
- `word2vec_lemmatized_cbow_win2_dim100.model`
- `word2vec_stemmed_skipgram_win4_dim300.model`

Bu modeller, `gensim` kullanılarak kolayca yüklenebilir ve kelime benzerlikleri, vektör aritmetiği gibi işlemlerde kullanılabilir.

---

## 📌 Notlar

- Python 3.10 ile test edilmiştir.
- Gensim ve NumPy uyumsuzluklarına dikkat edin. Sorun yaşarsanız `pip install numpy==1.23.5` önerilir.

---

## 🧑‍💻 Katkıda Bulunun

Pull request'ler memnuniyetle karşılanır. Her türlü geri bildirim ve katkı için teşekkür ederiz.

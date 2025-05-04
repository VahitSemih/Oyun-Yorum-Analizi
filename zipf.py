import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import string

# CSV dosyasını oku
df = pd.read_csv("cs2_yorumlar_ingilizce_5000.csv")

# Sütun adını kontrol et
print(df.columns)

# Yorumları birleştir
all_text = " ".join(df['yorum'].astype(str).tolist())

# Noktalama temizliği ve küçük harf
translator = str.maketrans('', '', string.punctuation)
all_text = all_text.translate(translator).lower()

# Kelimelere ayır
words = all_text.split()

# Frekans hesapla
word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1

# Sıralama ve log-log verisi
sorted_freqs = sorted(word_freq.values(), reverse=True)
ranks = np.arange(1, len(sorted_freqs) + 1)

# Grafik
plt.figure(figsize=(8, 6))
plt.loglog(ranks, sorted_freqs, marker="o", linestyle="none", markersize=4, alpha=0.7, color="b")
plt.xlabel("Kelime Sırası (log)")
plt.ylabel("Frekans (log)")
plt.title("CS2 Yorumları İçin Zipf Yasası")
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.show()
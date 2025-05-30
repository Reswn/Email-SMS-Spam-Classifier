
# 📧 Email/SMS Classifier

Aplikasi ini digunakan untuk mengklasifikasikan apakah sebuah pesan teks (email atau SMS) termasuk **Spam** atau **Ham** (bukan spam). Cocok untuk membantu menyaring pesan masuk secara otomatis menggunakan model Machine Learning.

---

## 🚀 Fitur Utama

- **🧠 Klasifikasi teks secara real-time** (Spam vs Ham)
- **✍️ Input pesan langsung dari pengguna**
- **📊 Akurasi tinggi** dengan model Machine Learning
- **⚙️ Bisa dijalankan melalui antarmuka web menggunakan Streamlit**
- **🔐 Aman, ringan, dan mudah dipakai**

---

## 🛠 Teknologi yang Digunakan

- **Python 3.x**
- **Streamlit** – Untuk antarmuka aplikasi web
- **Scikit-learn** – Pipeline model klasifikasi
- **Pandas & Numpy** – Pengolahan data
- **NLTK** – Preprocessing teks
- **TfidfVectorizer** – Ekstraksi fitur teks
- **MultinomialNB** – Model klasifikasi

---

## 📦 Instalasi

1. **Clone repositori:**

```bash
git clone https://github.com/username/email-sms-classifier.git
cd email-sms-classifier
```

2. **Install dependensi:**

```bash
pip install -r requirements.txt
```

3. **Jalankan aplikasi Streamlit:**

```bash
streamlit run app.py
```

---

## 📂 Struktur Proyek

```
email-sms-classifier/
├── app.py                # Aplikasi utama Streamlit
├── model.pkl             # Model Machine Learning yang telah dilatih
├── vectorizer.pkl        # TF-IDF Vectorizer untuk ekstraksi fitur
├── spam.csv              # Dataset asli berisi SMS/email berlabel
├── requirements.txt      # Daftar dependensi Python
└── README.md             # Dokumentasi ini
```

---

## 💡 Cara Kerja Aplikasi

1. Pengguna memasukkan teks pesan.
2. Teks diproses:
   - Lowercasing
   - Stopword removal
   - Stemming
3. Teks diubah menjadi vektor numerik menggunakan **TF-IDF**.
4. Model klasifikasi memprediksi apakah pesan tersebut **Spam** atau **Ham**.
5. Hasil prediksi ditampilkan langsung ke pengguna.

---

## 🔍 Contoh Prediksi

| Input Pesan | Output |
|-------------|--------|
| "You won $1000! Click here to claim now." | ❌ Spam |
| "Hi, meeting is at 10 AM tomorrow." | ✅ Ham |

---

## 📊 Dataset

Dataset yang digunakan berasal dari:

### SMS Spam Collection
- Sumber: [UCI Machine Learning Repository](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)
- Jumlah data: ±5.5k pesan SMS berlabel
- Format: Teks biasa + label (`spam` / `ham`)

---

## 🧠 Model yang Digunakan

- **Model:** Multinomial Naive Bayes
- **Vectorizer:** TF-IDF
- **Akurasi model:** ±97–99% pada data uji

---

## 🔒 Catatan Keamanan & Batasan

- Jangan gunakan untuk memfilter email asli secara langsung tanpa pengujian menyeluruh.
- Model ini berbasis statistik dan mungkin belum 100% akurat untuk semua bahasa/pesan.
- Disarankan untuk melakukan validasi manual terhadap hasil prediksi sebelum digunakan dalam produksi.

---

## 🤝 Kontribusi

Kontribusi sangat terbuka! Silakan fork repo ini, lakukan perubahan, dan kirimkan **Pull Request (PR)**. Berikut beberapa ide kontribusi:
- Menambahkan model lain seperti Logistic Regression, SVM, atau LSTM
- Mendukung bahasa Indonesia
- Menambahkan UI/UX yang lebih interaktif

---

## 📬 Kontak

- **Email:** renisuwandi1011@gmail.com  
- **GitHub:** [@Reswn](https://github.com/Reswn)

---



## 🙏 Terima Kasih!

Terima kasih telah menggunakan Email/SMS Classifier ini. Jika ada pertanyaan atau ingin berkontribusi, jangan ragu untuk hubungi saya via email atau GitHub. Semoga proyek ini bermanfaat bagi Anda! 🚀

---

# Dashboard Daily-Bike-Sharing ✨

## Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis dataset penyewaan sepeda yang mencakup jumlah penyewaan sepeda per jam dan per hari antara tahun 2011 dan 2012 dalam sistem berbagi sepeda di ibu kota. Dataset ini juga menyertakan informasi terkait cuaca dan musim.

## Dataset
Dataset ini berisi informasi berikut:
- **Instant**: Indeks record
- **Dteday**: Tanggal
- **Season**: Musim (1: Spring, 2: Summer, 3: Fall, 4: Winter)
- **Yr**: Tahun (0: 2011, 1: 2012)
- **Mnth**: Bulan (1 hingga 12)
- **Holiday**: Apakah hari tersebut adalah hari libur
- **Weekday**: Hari dalam seminggu
- **Workingday**: Apakah hari tersebut bukan akhir pekan atau hari libur (1: Ya, 0: Tidak)
- **Weathersit**: 
  - 1: Cuaca Cerah, Beberapa Awan, Sebagian Besar Awan
  - 2: Kabut + Awan, Kabut + Awan Pecah, Kabut + Beberapa Awan
  - 3: Salju Ringan, Hujan Ringan + Petir + Awan Tersebar, Hujan Ringan + Awan Tersebar
  - 4: Hujan Berat + Palet Es + Petir + Kabut, Salju + Kabut
- **Temp**: Suhu yang dinormalisasi dalam Celsius
- **Atemp**: Suhu terasa yang dinormalisasi dalam Celsius
- **Hum**: Kelembapan yang dinormalisasi
- **Windspeed**: Kecepatan angin yang dinormalisasi
- **Casual**: Jumlah pengguna kasual
- **Registered**: Jumlah pengguna terdaftar
- **Cnt**: Total jumlah sepeda sewaan, termasuk kasual dan terdaftar

## Tujuan Analisis
- Menganalisis pola penyewaan sepeda berdasarkan musim dan cuaca
- Mengetahui pengaruh hari kerja vs. akhir pekan terhadap penyewaan sepeda
- Menerapkan model RFM (Recency, Frequency, Monetary) untuk segmentasi pengguna

## Instalasi
Untuk menjalankan aplikasi Streamlit ini, pastikan Anda memiliki Python dan pip terinstal di sistem Anda. Kemudian, ikuti langkah-langkah berikut:

1. Clone repository ini:
```
git clone <URL_REPO>
cd <NAMA_FOLDER>
```
2. install dependensi yang diperlukan:
```
pip install -r requirements.txt
```
3. jalankan Streamlit:
```
streamlit run app.py
```
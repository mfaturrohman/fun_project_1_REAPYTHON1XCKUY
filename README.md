# fun_project_1_REAPYTHON1XCKUY

# 🎯 Mini Kuis Karir - Aplikasi Streamlit

Aplikasi web sederhana berbasis [Streamlit](https://streamlit.io/) untuk membantu pengguna mengenali potensi karir mereka berdasarkan minat dan preferensi melalui 5 pertanyaan interaktif.

---

## 🚀 Fitur

- ✅ 5 Pertanyaan seputar minat dan preferensi
- ✅ Kategori karir: **Programmer**, **Designer**, dan **Data Scientist**
- ✅ Hasil akhir ditampilkan dengan GIF animasi dan deskripsi menarik
- ✅ Tampilan skor lengkap dengan visual bar
- ✅ Menangani hasil imbang (imbang ditampilkan dalam kolom)
- ✅ UI sederhana, responsive, dan langsung bisa dijalankan secara lokal

---

## 🧠 Logika Skoring

Setiap jawaban menambahkan 1 poin ke salah satu kategori karir. Total skor dihitung dari semua pertanyaan, dan kategori dengan skor tertinggi akan direkomendasikan sebagai potensi karir.

Jika terjadi skor **imbang**, maka semua karir dengan skor tertinggi akan ditampilkan.

---

## 📦 Instalasi

1. **Clone repository ini** atau salin file script `.py` ke folder lokal.
2. **Buat dan aktifkan environment (opsional)**:
   `python -m venv myenv`

   `source myenv/bin/activate` MacOS / linux

   `myenv\Scripts\activate` Windows

3. **Install Streamlit** ketikkan `pip install streamlit`
4. **Jalankan aplikasi** ketikkan `streamlit run app.py`
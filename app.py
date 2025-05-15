import streamlit as st

st.set_page_config(page_title="Mini Kuis Karir", page_icon="🎯")
st.title("🎯 Mini Kuis Karir")
st.write("Jawablah pertanyaan berikut untuk mengetahui potensi karir kamu!")

# Inisialisasi skor
scores = {
    "Programmer": 0,
    "Designer": 0,
    "Data Scientist": 0
}

# Pertanyaan
st.markdown("#### 1. Apa aktivitas yang paling kamu sukai?")
q1 = st.radio("", [
    "Membuat aplikasi atau program",
    "Menggambar atau mendesain",
    "Menganalisis data atau grafik"
])
if q1 == "Membuat aplikasi atau program":
    scores["Programmer"] += 1
elif q1 == "Menggambar atau mendesain":
    scores["Designer"] += 1
else:
    scores["Data Scientist"] += 1

st.markdown("#### 2. Mata pelajaran favorit kamu di sekolah?")
q2 = st.radio("", [
    "Matematika atau logika",
    "Seni atau desain",
    "Statistika atau IPA"
])
if q2 == "Matematika atau logika":
    scores["Programmer"] += 1
elif q2 == "Seni atau desain":
    scores["Designer"] += 1
else:
    scores["Data Scientist"] += 1

st.markdown("#### 3. Kamu lebih suka bekerja dengan...")
q3 = st.radio("", [
    "Kode dan komputer",
    "Warna, bentuk, dan estetika",
    "Angka dan informasi"
])
if q3 == "Kode dan komputer":
    scores["Programmer"] += 1
elif q3 == "Warna, bentuk, dan estetika":
    scores["Designer"] += 1
else:
    scores["Data Scientist"] += 1

st.markdown("#### 4. Kamu ingin membuat sesuatu yang bisa...")
q4 = st.radio("", [
    "Otomatisasi tugas",
    "Menarik dan enak dilihat",
    "Memberi wawasan dari data"
])
if q4 == "Otomatisasi tugas":
    scores["Programmer"] += 1
elif q4 == "Menarik dan enak dilihat":
    scores["Designer"] += 1
else:
    scores["Data Scientist"] += 1

st.markdown("#### 5. Hobi kamu paling dekat dengan...")
q5 = st.radio("", [
    "Ngoprek teknologi",
    "Menggambar atau edit foto",
    "Main-main data atau grafik"
])
if q5 == "Ngoprek teknologi":
    scores["Programmer"] += 1
elif q5 == "Menggambar atau edit foto":
    scores["Designer"] += 1
else:
    scores["Data Scientist"] += 1

# Tampilkan hasil
if st.button("Lihat Hasil"):
    # Cari nilai skor tertinggi
    max_score = max(scores.values())

    # Ambil semua kategori yang skornya sama dengan skor tertinggi (jika imbang)
    recommended_roles = [role for role, score in scores.items() if score == max_score]

    # Deskripsi
    deskripsi = {
        "Programmer": "👨‍💻 **Programmer** adalah orang yang menciptakan perangkat lunak dan aplikasi. "
                    "Mereka memiliki kemampuan untuk memecahkan masalah dan menciptakan solusi inovatif dengan menggunakan bahasa pemrograman.",
        "Designer": "🎨 **Designer** adalah orang yang menciptakan tampilan visual, baik dalam bentuk digital maupun cetak. "
                    "Mereka memiliki kepekaan terhadap estetika dan kemampuan menyampaikan pesan melalui desain.",
        "Data Scientist": "📊 **Data Scientist** adalah orang yang menganalisis dan menginterpretasi data untuk mengambil keputusan. "
                        "Mereka menggunakan statistik, pemrograman, dan machine learning untuk menemukan pola dan wawasan dari data."
    }

    # Tampilkan GIF berdasarkan hasil
    gif_paths = {
        "Programmer": "https://media.giphy.com/media/qgQUggAC3Pfv687qPC/giphy.gif",
        "Designer": "https://media.giphy.com/media/3ohs4BSacFKI7A717y/giphy.gif",
        "Data Scientist": "https://media.giphy.com/media/du3J3cXyzhj75IOgvA/giphy.gif"
    }

    # Tampilkan balon ulang tahun
    st.balloons()

    # Tampilkan hasil
    if len(recommended_roles) == 1:
        role = recommended_roles[0]
        st.success(f"🌟 Kamu cocok menjadi seorang **{role}**! 🚀")
        st.image(gif_paths[role], caption=role, use_container_width=True)
        st.markdown(deskripsi[role])
    else:
        st.success("🌟 Kamu cocok di beberapa karir berikut! 🚀")  # Pesan hasil imbang

        # Buat kolom sebanyak kategori yang imbang
        cols = st.columns(len(recommended_roles))

        # Tampilkan tiap kategori dalam kolom terpisah
        for col, role in zip(cols, recommended_roles):
            with col:
                st.subheader(f"💼 {role}")
                st.image(gif_paths[role], caption=role, use_container_width=True)
                st.markdown(deskripsi[role])

# Tampilkan skor lengkap dengan expander dan gaya
    with st.expander("🔍 Lihat Skor Lengkap"):
        st.markdown("### 📊 Skor Kategori Karir:")
        for role, score in scores.items():
            emoji = "💻" if role == "Programmer" else "🎨" if role == "Designer" else "📈"
            bar = "🟩" * score + "⬜" * (5 - score)
            st.markdown(f"**{emoji} {role}**\n\n{bar} `{score}/5`", unsafe_allow_html=True)
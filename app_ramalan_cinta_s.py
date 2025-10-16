import streamlit as st
# Mengimpor fungsi hitung_nilai_nama dari file app_ramalan_cinta.py
# Pastikan file app_ramalan_cinta.py berada di folder yang sama
from app_ramalan_cinta import hitung_nilai_nama 

# Fungsi utama untuk antarmuka Streamlit
def main_ramalan_web():
    """Menampilkan antarmuka web dan menghitung ramalan berdasarkan pilihan pengguna."""
    st.set_page_config(page_title="Ramalan Cinta", page_icon="💘", layout="centered")
    
    st.markdown(
        """
        <style>
        .stButton>button {
            background-color: #FF5A5F;
            color: white;
            border-radius: 12px;
            padding: 10px 20px;
            font-size: 18px;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #E04C52;
            transform: scale(1.02);
        }
        .stTextInput>div>div>input {
            border-radius: 8px;
            border: 1px solid #FF5A5F;
            padding: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("💘 Aplikasi Ramalan Cinta Berbasis Nama")
    st.subheader("Masukkan nama Anda dan pasangan untuk melihat ramalan.")

    # --- Input Nama ---
    # Menggunakan key agar input unik
    nama_anda = st.text_input("Nama Lengkap Anda:", key="input_anda", placeholder="Contoh: Budi")
    nama_pasangan = st.text_input("Nama Lengkap Pasangan Anda:", key="input_pasangan", placeholder="Contoh: Cinta")

    # --- Pilihan Ramalan ---
    opsi_ramalan = st.selectbox(
        "Pilih Jenis Ramalan yang Anda Inginkan:",
        [
            "Ramalan Jodoh",
            "Ramalan Kelanggengan Pernikahan",
            "Ramalan Memiliki Anak Laki-laki & Perempuan",
            "Ramalan Jumlah Anak",
            "Ramalan Rezeki Pernikahan",
            "Ramalan Musibah Pernikahan",
        ]
    )

    # --- Tombol Proses ---
    if st.button("Hitung Ramalan"):
        if not nama_anda or not nama_pasangan:
            st.error("⚠️ Silahkan masukkan kedua nama terlebih dahulu untuk memulai perhitungan.")
            return

        # Hitung Nilai
        nilai_anda = hitung_nilai_nama(nama_anda)
        nilai_pasangan = hitung_nilai_nama(nama_pasangan)
        total_nilai = nilai_anda + nilai_pasangan
        persentase = min(total_nilai, 100) # Batas maksimal 100%

        # --- Tampilkan Hasil ---
        st.markdown("<hr/>", unsafe_allow_html=True)
        st.subheader(f"✨ Hasil Ramalan untuk {opsi_ramalan}")
        
        # Logika Ramalan Sesuai dengan file app_ramalan_cinta.py

        if opsi_ramalan == "Ramalan Jodoh":
            if 70 <= persentase <= 100:
                pesan = "Anda dan Pasangan Anda **Sangat Berjodoh** 💖"
                st.success(pesan)
            elif 41 <= persentase <= 69:
                pesan = "Anda dan Pasangan Anda **Lumayan Berjodoh** 👍"
                st.info(pesan)
            else: # 0-40%
                pesan = "Anda dan Pasangan Anda **Kurang Berjodoh** 💔"
                st.warning(pesan)
            st.metric(label="Persentase Jodoh", value=f"{persentase}%")
            
        elif opsi_ramalan == "Ramalan Kelanggengan Pernikahan":
            if 70 <= persentase <= 100:
                pesan = "Anda dan Pasangan Anda Akan **Langgeng** Pernikahannya Hingga **20 Tahun Mendatang** 🎉"
                st.success(pesan)
            elif 41 <= persentase <= 69:
                pesan = "Anda dan Pasangan Anda **Lumayan Langgeng** Hingga **5 Tahun Mendatang** 💍"
                st.info(pesan)
            else: # 0-40%
                pesan = "Maaf, Anda dan Pasangan Anda Berpotensi **Tidak Langgeng** Hingga **1 Tahun Mendatang** 😥"
                st.error(pesan)
            st.metric(label="Persentase Kelanggengan", value=f"{persentase}%")

        elif opsi_ramalan == "Ramalan Memiliki Anak Laki-laki & Perempuan":
            if 75 <= persentase <= 100:
                pesan = f"Anda dan Pasangan **Berpotensi Memiliki Anak Laki-laki & Perempuan** 👶👦👧"
                st.success(pesan)
            elif 61 <= persentase <= 74:
                pesan = f"Anda dan Pasangan **Berpotensi Memiliki Anak Perempuan** saja 👧👧👧"
                st.info(pesan)
            else: # 0-60%
                pesan = f"Anda dan Pasangan **Berpotensi Memiliki Anak Laki-laki** saja 👦👦👦"
                st.warning(pesan)
            st.metric(label="Persentase Potensi Anak", value=f"{persentase}%")
            st.caption(f"Tingkat potensi yang dihasilkan: {persentase}%")

        elif opsi_ramalan == "Ramalan Jumlah Anak":
            # Logika: (persentase - 1) // 10 + 1 jika > 0, jika 0 maka 0
            jumlah_anak = (persentase - 1) // 10 + 1 if persentase > 0 else 0
            
            if jumlah_anak > 0:
                pesan = f"Anda dan Pasangan **Berpotensi Memiliki {jumlah_anak} Anak** 👨‍👩‍👧‍👦"
                st.success(pesan)
            else:
                pesan = "Anda dan Pasangan **Berpotensi belum memiliki anak**."
                st.warning(pesan)
            st.metric(label="Potensi Jumlah Anak", value=jumlah_anak)
            st.caption(f"Diambil dari total nilai ramalan: {total_nilai}")
            
        elif opsi_ramalan == "Ramalan Rezeki Pernikahan":
            if 70 <= persentase <= 100:
                pesan = "Anda dan Pasangan Anda Berpotensi Memiliki **Rezeki Yang Melimpah** Dalam Pernikahan 💰"
                st.success(pesan)
            elif 41 <= persentase <= 69:
                pesan = "Anda dan Pasangan Anda Berpotensi Memiliki **Rezeki Yang Cukup** Dalam Pernikahan 💵"
                st.info(pesan)
            else: # 0-40%
                pesan = "Maaf, Anda dan Pasangan Anda Berpotensi Memiliki **Kesulitan Dalam Rezeki** Dalam Pernikahan 💸"
                st.error(pesan)
            st.metric(label="Persentase Rezeki", value=f"{persentase}%")

        elif opsi_ramalan == "Ramalan Musibah Pernikahan":
            st.metric(label="Potensi Musibah", value=f"{persentase}%")
            if persentase <= 20:
                st.success(f"Potensi Musibah Rendah. Hanya **{persentase}%** Anda dan Pasangan Berpotensi Memiliki Musibah Dalam Pernikahan. Tetap Waspada.")
            elif persentase <= 50:
                 st.info(f"Potensi Musibah Sedang. **{persentase}%** Anda dan Pasangan Berpotensi Memiliki Musibah Dalam Pernikahan. Perlu Komunikasi Lebih Baik.")
            else:
                st.error(f"Potensi Musibah Tinggi. **{persentase}%** Anda dan Pasangan Berpotensi Memiliki Musibah Dalam Pernikahan. Tingkatkan Kehati-hatian.")


if __name__ == "__main__":
    main_ramalan_web()

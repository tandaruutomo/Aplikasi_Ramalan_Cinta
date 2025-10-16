# -*- coding: utf-8 -*-

def hitung_nilai_nama(nama):
    """
    Fungsi ini menghitung nilai numerik dari sebuah nama berdasarkan aturan yang diberikan.
    - Huruf vokal (A, I, U, E, O) nilainya 0.
    """
    vokal = "AIUEO"
    # DIKEMBALIKAN: Nilai konsonan dikembalikan sesuai permintaan awal Anda.
    # Ini akan memberikan perhitungan yang benar dan konsisten.
    konsonan_nilai = {
        'B': 5, 'C': 12, 'D': 3, 'F': 4, 'G': 5, 'H': 6, 'J': 7, 'K': 8, 'L': 9, 'M': 10,
        'N': 5, 'P': 5, 'Q': 3, 'R': 4, 'S': 5, 'T': 6, 'V': 7, 'W': 8, 'X': 9,
        'Y': 20, 'Z': 21
    }
    
    total_nilai = 0
    # PERBAIKAN: Menggunakan .upper() pada nama yang diinput
    # Ini memastikan semua huruf, baik besar maupun kecil, akan dihitung dengan benar.
    # Contoh: 'Ahmad' dan 'ahmad' akan menghasilkan nilai yang sama.
    for huruf in nama.upper():
        if huruf in vokal:
            total_nilai += 0
        elif huruf in konsonan_nilai:
            total_nilai += konsonan_nilai[huruf]
            
    return total_nilai

def dapatkan_nama_dan_hitung_persentase():
    """
    Meminta nama pengguna dan pasangan, lalu menghitung persentase ramalan.
    Hasil persentase dibatasi maksimal 100%.
    """
    nama_anda = input("Silahkan Tulis Nama Lengkap Anda : ")
    nama_pasangan = input("Silahkan Tulis Nama Lengkap Pasangan Anda : ")
    
    nilai_anda = hitung_nilai_nama(nama_anda)
    nilai_pasangan = hitung_nilai_nama(nama_pasangan)
    
    total_nilai = nilai_anda + nilai_pasangan
    
    # Hasil dalam bentuk %, jika nilai lebih dari 100% maka tetap 100%
    persentase = min(total_nilai, 100)
    
    print("\nHasil Dari Ramalan Anda Adalah :")
    return persentase

def jalankan_ramalan_lagi():
    """Menanyakan kepada pengguna apakah ingin melakukan ramalan lagi."""
    while True:
        pilihan = input("\nApakah Anda Ingin Melakukan Ramalan Lagi (iya/tidak) : ").lower()
        if pilihan == "iya":
            return True
        elif pilihan == "tidak":
            return False
        else:
            print("Input tidak valid. Silahkan masukkan 'iya' atau 'tidak'.")

def ramalan_jodoh():
    """Program untuk Opsi 1: Ramalan Jodoh."""
    while True:
        print("\n--- Selamat Datang Di Ramalan Jodoh ---")
        persentase = dapatkan_nama_dan_hitung_persentase()
        
        pesan = ""
        if 70 <= persentase <= 100:
            pesan = "Anda dan Pasangan Anda Sangat Berjodoh"
        elif 41 <= persentase <= 69:
            pesan = "Anda dan Pasangan Anda Lumayan Berjodoh"
        else: # 0-40%
            pesan = "Anda dan Pasangan Anda Kurang Berjodoh"
            
        print(f"Hasil dari Ramalan Jodoh Anda Adalah {persentase}%")
        print(pesan)
        
        if not jalankan_ramalan_lagi():
            break

def ramalan_kelanggengan():
    """Program untuk Opsi 2: Ramalan Kelanggengan Pernikahan."""
    while True:
        print("\n--- Selamat Datang Di Ramalan Kelanggengan Pernikahan ---")
        persentase = dapatkan_nama_dan_hitung_persentase()
        
        pesan = ""
        if 70 <= persentase <= 100:
            pesan = "Anda dan Pasangan Anda Akan Langgeng Pernikahannya Hingga 20 Tahun Mendatang"
        elif 41 <= persentase <= 69:
            pesan = "Anda dan Pasangan Anda Lumayan Langgeng Hingga 5 Tahun Mendatang"
        else: # 0-40%
            pesan = "Maaf Anda dan Pasangan Anda Tidak Langgeng Hingga 1 Tahun Mendatang"
        
        print(pesan)
        
        if not jalankan_ramalan_lagi():
            break

def ramalan_anak_gender():
    """Program untuk Opsi 3: Ramalan Memiliki Anak Laki-laki & Perempuan."""
    while True:
        print("\n--- Selamat Datang Di Ramalan Memiliki Anak Laki-laki & Perempuan ---")
        persentase = dapatkan_nama_dan_hitung_persentase()

        pesan = ""
        if 75 <= persentase <= 100:
            pesan = f"{persentase}% Anda dan Pasangan Berpotensi Memiliki Anak Laki-laki & Perempuan"
        elif 61 <= persentase <= 74:
            pesan = f"{persentase}% Anda dan Pasangan Berpotensi Memiliki Anak Perempuan"
        else: # 0-60%
            pesan = f"{persentase}% Anda dan Pasangan Berpotensi Memiliki Anak Laki-laki"
            
        print(pesan)

        if not jalankan_ramalan_lagi():
            break

def ramalan_jumlah_anak():
    """Program untuk Opsi 4: Ramalan Jumlah Anak."""
    while True:
        print("\n--- Selamat Datang Di Ramalan Jumlah Anak ---")
        persentase = dapatkan_nama_dan_hitung_persentase()

        jumlah_anak = (persentase - 1) // 10 + 1 if persentase > 0 else 0
        
        if jumlah_anak > 0:
            pesan = f"Anda dan Pasangan Berpotensi Memiliki {jumlah_anak} Anak"
        else:
            pesan = "Anda dan Pasangan Berpotensi belum memiliki anak."
            
        print(pesan)

        if not jalankan_ramalan_lagi():
            break

def ramalan_rezeki():
    """Program untuk Opsi 5: Ramalan Rezeki Pernikahan."""
    while True:
        print("\n--- Selamat Datang Di Ramalan Rezeki Pernikahan ---")
        persentase = dapatkan_nama_dan_hitung_persentase()
        
        pesan = ""
        if 70 <= persentase <= 100:
            pesan = "Anda dan Pasangan Anda Berpotensi Memiliki Rezeki Yang Melimpah Dalam Pernikahan"
        elif 41 <= persentase <= 69:
            pesan = "Anda dan Pasangan Anda Berpotensi Memiliki Rezeki Yang Cukup Dalam Pernikahan"
        else: # 0-40%
            pesan = "Maaf Anda dan Pasangan Anda Berpotensi Memiliki Kesulitan Dalam Rezeki Dalam Pernikahan"
        
        print(pesan)
        
        if not jalankan_ramalan_lagi():
            break

def ramalan_musibah():
    """Program untuk Opsi 6: Ramalan Musibah Pernikahan."""
    while True:
        print("\n--- Selamat Datang Di Ramalan Musibah Pernikahan ---")
        persentase = dapatkan_nama_dan_hitung_persentase()
        
        print(f"{persentase}% Anda dan Pasangan Berpotensi Memiliki Musibah Dalam Pernikahan")
        
        if not jalankan_ramalan_lagi():
            break

def tampilkan_menu_utama():
    """Menampilkan menu utama aplikasi."""
    print("\n========================================")
    print(" Selamat Datang Di Aplikasi Ramalan Cinta")
    print("========================================")
    print("Berikut Adalah Opsi Ramalan:")
    print("1. Ramalan Jodoh")
    print("2. Ramalan Kelanggengan Pernikahan")
    print("3. Ramalan Memiliki Anak Laki-laki & Perempuan")
    print("4. Ramalan Jumlah Anak")
    print("5. Ramalan Rezeki Pernikahan")
    print("6. Ramalan Musibah Pernikahan")
    print("7. Keluar Dari Aplikasi")

def main():
    """Fungsi utama untuk menjalankan seluruh aplikasi."""
    while True:
        tampilkan_menu_utama()
        pilihan = input("Silahkan Pilih Opsi Ramalan Anda : ")
        
        if pilihan == '1':
            ramalan_jodoh()
        elif pilihan == '2':
            ramalan_kelanggengan()
        elif pilihan == '3':
            ramalan_anak_gender()
        elif pilihan == '4':
            ramalan_jumlah_anak()
        elif pilihan == '5':
            ramalan_rezeki()
        elif pilihan == '6':
            ramalan_musibah()
        elif pilihan == '7':
            print("\nTerimakasih Telah Mengunakan Aplikasi Ramalan Cinta")
            break
        else:
            print("\nOpsi Yang Anda Masukkan Tidak Ada")
            print("Silahkan Pilih Opsi Antara Opsi Nomer 1 hingga Opsi Nomer 7")

# Menjalankan program utama
if __name__ == "__main__":
    main()



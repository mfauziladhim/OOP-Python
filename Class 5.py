
#Di dalam Kelas

class Mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self._nilai = nilai  # Variabel dengan satu underscore

    # Method ini berada DI DALAM kelas
    def tampilkan_dan_ubah_dari_dalam(self, nilai_baru):
        print(f"Nilai awal (diakses dari dalam): {self._nilai}")
        
        # Mengubah nilai dari DALAM kelas
        self._nilai = nilai_baru
        print(f"Nilai setelah diubah (di dalam): {self._nilai}")


# Membuat objek
mhs = Mahasiswa("Andi", 80)

# Memanggil method dari luar untuk menjalankan proses di dalam kelas
mhs.tampilkan_dan_ubah_dari_dalam(90)



#Di Luar Kelas

class Mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self._nilai = nilai  # Variabel dengan satu underscore


# Membuat objek
mhs = Mahasiswa("Budi", 85)

# 1. Mengakses variabel _nilai dari LUAR kelas
print(f"Nilai sebelum diubah (diakses dari luar): {mhs._nilai}")

# 2. Mengubah nilai secara langsung dari LUAR kelas
mhs._nilai = 95

# Memeriksa hasil perubahan dari luar
print(f"Nilai setelah diubah (dari luar): {mhs._nilai}")


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

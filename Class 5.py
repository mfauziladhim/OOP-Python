
#membahas cara Python menyembunyikan kode yaitu ada protected dan private 
#1. protected
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


#2. private

class DompetDigital:
    def __init__(self, pemilik, saldo_awal):
        self.pemilik = pemilik
        self.__saldo = saldo_awal  # Variabel private dengan dua underscore

    # Method ini berada DI DALAM kelas dan bisa mengubah variabel private __saldo
    def tambah_saldo(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah  # Mengubah nilai __saldo dari DALAM kelas
            print(f"Berhasil menambah saldo. Saldo sekarang: {self.__saldo}")
        else:
            print("Jumlah penambahan harus lebih dari 0.")

    # Method untuk melihat saldo dari dalam kelas
    def cek_saldo(self):
        print(f"Saldo saat ini: {self.__saldo}")


# --- BAGIAN DI LUAR KELAS ---

# Membuat objek
dompet_budi = DompetDigital("Budi", 100000)

# 1. Mengakses saldo melalui method di dalam kelas (BERHASIL)
dompet_budi.cek_saldo()

# 2. Mengubah nilai __saldo dari DALAM kelas menggunakan method (BERHASIL)
dompet_budi.tambah_saldo(50000)

# 3. Jika Anda mencoba mengubah atau mengakses __saldo langsung dari LUAR kelas:
# print(dompet_budi.__saldo) -> AKAN ERROR (AttributeError)
# dompet_budi.__saldo = 999999 -> AKAN ERROR / Membuat variabel baru di luar, bukan mengubah yang di dalam



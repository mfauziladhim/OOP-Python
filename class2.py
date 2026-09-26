class Grocery:
    def __init__ (self, fruit, amount_a, vegetable, amount_b, Toko):
        self.fruit = fruit
        self.amount_a = amount_a
        self.vegetable = vegetable
        self.amount_b = amount_b
        self.toko = Toko
        
    def final(self):
        print(
        f"Kamu membeli {self.fruit} sebanyak {self.amount_a}"
        f"dan {self.vegetable} sebanyak {self.amount_b}"
        f"di toko {self.toko.nama_toko} yang berada di {self.toko.alamat}"
        )
        
        
class Toko:
    def __init__ (self, nama_toko, alamat):
        self.nama_toko = nama_toko
        self.alamat = alamat
        
    
        
        
      
toko1 = Toko("Berkah Langit", "Jalan Godhong nomor 5")
grocery1 = Grocery("banana", 5, "carrot", 5, toko1)
#grocery1.fruit
#grocery1.amount_a
#grocery1.vegetable
#grocery1.amount_b
#toko1.nama_toko
#toko1.alamat
    
    
toko2 = Toko("Doa Ibu", "Jalan Ahmad Yani nomor 1")
grocery2 = Grocery("watermelon", 1, "mustard", 5, toko2)
#grocery2.fruit
#grocery2.amount_a
#grocery2.vegetable
#grocery2.amount_b
#toko2.nama_toko
#toko2.alamat
    
#grocery1.final()

grocery1.final()
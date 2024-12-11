from Animal import *
from ular import *
class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, bunyi, jenis):
        super().__init__(nama, makanan, hidup, berkembang_biak,)
        self.jenis = jenis
        self.bunyi = bunyi
        
    def cetak_burung(self):
        super().cetak()
        print("jenis \t\t\t\t\t\t : ", self.jenis,
              "\nbunyi \t\t\t\t\t\t : ", self.bunyi)
        
gereja = Burung("gereja", "beras", "amazon", "bertelur", "klutukklutuk", "jenis")
gereja.cetak_burung()
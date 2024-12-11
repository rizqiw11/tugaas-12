from Animal import *
# from ular import *
class ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis_air, jenis):
        super().__init__(nama, makanan, hidup, berkembang_biak,)
        self.jenis_air = jenis_air
        self.jenis = jenis
        
    def cetak_ikan(self):
        super().cetak()
        print("jenis \t\t\t\t\t\t : ", self.jenis,
              "\nbunyi \t\t\t\t\t\t : ", self.jenis_air)
        
lele = ikan("gereja", "pelet", "air", "bertelur", "tawar", "lele")
lele.cetak_ikan()
class Mobil:
    _Merk = ""
    _Tipe = ""
    _KapasitasBBM = ""
    _JenisBahanBakar = ""
    
    def __init__(self,merk,tipe):
        self._Merk = merk
        self._Tipe = tipe
        self._KapasitasBBM = None
        self._JenisBahanBakar = None
    
    

    def setJenisBahanBakar(self,JenisBahanBakar):
        self._JenisBahanBakar = JenisBahanBakar
    
    def setKapasitasBBM(self,KapasitasBBM):
        self._KapasitasBBM = KapasitasBBM

    def getMerk(self):
        return self._Merk
    def getTipe(self):
        return self._Tipe
    def getKapasitasBBM(self):
        return self._KapasitasBBM
    def getJenisBahanBakar(self):
        return self._JenisBahanBakar

    

    def printInfo(self):
        print("============ INFO ============ ")
        print("Merk             :",self.getMerk())
        print("Tipe             :",self.getTipe())
        print("Bahan Bakar      :",self.getJenisBahanBakar())
        print("Kapasitas BBM    :",self.getKapasitasBBM())
    
    def isiBBM(self,rupiah):
        if self.getKapasitasBBM() == None or self.getJenisBahanBakar() == None:
            print("ERROR! Kapasotas BBM atau Jenis Bahan Bakar belum di inputkan!!")
        else:
            print("Mengisi", self.getKapasitasBBM(),"Liter")
            total = rupiah * self.getKapasitasBBM()
            print("Total Harga : ", "Rp"+str(total))
    

if __name__ == "__main__":
    mobil1 = Mobil("Toyota", "Avanza")
    mobil1.printInfo()

    mobil2 = Mobil("Nissan", "Grand Livina")
    mobil2.setJenisBahanBakar("Bensin")
    mobil2.setKapasitasBBM(20)
    mobil2.printInfo()

    mobil1.isiBBM(14500)
    mobil2.isiBBM(14500)

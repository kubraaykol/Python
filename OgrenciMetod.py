class Ogrenci:
    def __init__(self,adi=None, soyadi=None, sinifi=2):
        self.adi=adi
        self.soyadi=soyadi
        self.sinifi=sinifi
        self.universite="medipol"

    def sinifYukselt(self):
        self.sinifi +=1

    def universiteAdiYazdir(self):
        print(self.universite)

    def toString(self):
        print(self.adi,end=" , ")
        print(self.soyadi,end=" , ")
        print(self.sinifi)

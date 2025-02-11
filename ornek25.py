class Ogretmen:

   def __init__(self, isim, soyisim, yas, maas, uzmanlik, tel):
       self.isim = isim
       self.soyisim = soyisim
       self.yasi = yas
       self.__maas = maas  # özel değişken
       self.uzmanlik = uzmanlik
       self._tel = tel # yarı özel


ogr = Ogretmen("Ali", "YILMAZ", 34, 5000, "Matematik","0544 234 45 56")
print(ogr._tel)



ogr=Ogretmen("Ali","YILMAZ",34,5000,"Matematik")
print(ogr.isim)
print(ogr.getMaas())
ogr.setMaas(6000)
print(ogr.getMaas())

ogr=Ogretmen("Ali","YILMAZ",34,5000,"Matematik")
print("{} {} {} yaşında ve {} maaşı olan bir {} öğretmenidir.".format(ogr.isim,ogr.soyisim,ogr.yas,ogr.maas,ogr.uzmanlık))



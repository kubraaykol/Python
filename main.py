print("merhaba main")
print("üç tırnak",sep="aykol")
print("üç", "tırnak",sep="aykol")
isim=input("isim gir:")
print("isminiz:",isim)
isim=input("Adınızı giriniz:")
soyisim=input("Soyadınızı giriniz:")
okulNo=input("Okul no Girinizi:")
bolumunuz=input("Bölümünüzü Giriniz:")
print(isim+soyisim+okulNo+bolumunuz)
*********************
Ad=input("Adınız:")
Soyad=input("Soyad:")
No=input("No:")
Bölüm=input("Bölüm:")

print(Bölüm,"bölümünden",No,"numaralı öğrencimiz:" ,Ad,Soyad)

**********************
isim = input("Adınızı Giriniz : ")
soyad = input("Soyadınızı giriniz : ")
num = input("Öğrenci No : ")
bolum = input("Bölümünüzü giriniz : ")

print("{} bölümünden {} numaralı öğrencimiz : {} {} ".format(bolum,num,isim,soyad))

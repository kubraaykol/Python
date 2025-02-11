
#Kullanıcıdan reelini ve imajinarini isteyip 3 tane karmaşık sayı oluşturup toplamını veren program
reel1 = int(input("1. sayının reel kısmını girin : "))
imajiner1 = int(input("1. sayının imajiner kısmını girin : "))
sayi1 = complex(reel1,imajiner1)

reel2 = int(input("2. sayının reel kısmını girin : "))
imajiner2 = int(input("2. sayının imajiner kısmını girin : "))
sayi2 = complex(reel2,imajiner2)

reel3 = int(input("3. sayının reel kısmını girin : "))
imajiner3 = int(input("3. sayının imajiner kısmını girin : "))
sayi3 = complex(reel3,imajiner3)


print("Karmaşık sayıların toplamı : ", sayi1+sayi2+sayi3)
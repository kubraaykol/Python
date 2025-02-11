def asalSayi(sayi):
        if sayi <= 1:
        for x in range(2, sayi):
            if sayi % x == 0:
                sayi = int(input("Bir sayı girin: "))
                return
            if asalSayi(sayi):
                print(f"{sayi} bir asal sayıdır.")
            else:
                print(f"{sayi} bir asal sayı değildir.")
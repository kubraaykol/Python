def main():
    yagisMiktari = []
    for ay in range(1, 13):
        miktar = float(input(f"{ay}. ay için yağış miktarını giriniz: "))
        yagisMiktari.append(miktar)


    yillikToplam = sum(yagisMiktari)


    aylikOrt = yillikToplam / 12


    enYuksek = max(yagisMiktari)
    enDusuk = min(yagisMiktari)
    enYuksekAy = yagisMiktari.index( enYuksek) + 1
    enDusukyAy = yagisMiktari.index(enDusuk) + 1

    print(f"Yıllık Toplam Yağış Miktarı: {yillikToplam} metre küp")
    print(f"Aylık Ortalama Yağış Miktarı: {aylikOrt} metre küp")
    print(f"En Yüksek Yağış Miktarı ({enYuksek} metre küp), {enYuksekAy}. ayda")
    print(f"En Düşük Yağış Miktarı ({enDusuk} metre küp), {enDusukyAy}. ayda")

if __name__ == "__main__":
    main()

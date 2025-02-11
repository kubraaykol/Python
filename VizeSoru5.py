def haftalikSatisHesapla(satislar):
    toplamSatis = sum(satislar)
    return toplamSatis

def main():
    gunler = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]
    satislar = []

    for gun in gunler:
        satis = float(input(f"{gun} günü için satış miktarını girin: "))
        satislar.append(satis)

    haftalikSatis = haftalikSatisHesapla(satislar)

    print("Haftalık toplam satış:", haftalikSatis)

if __name__ == "__main__":
    main()

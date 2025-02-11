def enCokTekrarEdenHarf(metin):
    harfTekrari = {}
    for harf in metin:
        if harf.isalpha():
            harfTekrari[harf] = harfTekrari.get(harf, 0) + 1

    enTekrarHarf = max(harfTekrari, key=harfTekrari.get)
    tekrarEden = harfTekrari[enTekrarHarf]

    return enTekrarHarf, tekrarEden

metin = input("Lütfen en az 7 kelimeli bir metin girin: ")

enTekrarHarf, tekrarEden = enCokTekrarEdenHarf(metin)

print(f"Girilen Metinde En Çok Tekrar Eden Harf: {enTekrarHarf}, Tekrar Sayısı: {tekrarEden}")

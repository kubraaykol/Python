def pigLatinCumle(cumle):
    cumleListesi = cumle.split()
    pigLatinCumle = []
    for kelime in cumleListesi:
        ilkHarf = kelime[0]
        kelime = kelime[1:] + ilkHarf.lower() + "ay"
        pigLatinCumle.append(kelime)
    return " ".join(pigLatinCumle)


cumle = input("Adınızı ve Soyadınızı Giriniz: ")
pigLatin = pigLatinCumle(cumle)
print("Pig Latin:", pigLatin)

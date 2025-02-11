A = ("cat", "bird", "dolphin", "giraffe", "elephant", "dog")

enUzunKelime = ""
enUzunKelimeUzunlugu = 0

for kelime in A:
    kelimeUzunlugu = len(kelime)
    if kelimeUzunlugu > enUzunKelimeUzunlugu:
        enUzunKelimeUzunlugu = kelimeUzunlugu
        enUzunKelime = kelime

print("En uzun kelime:", enUzunKelime)
print("En uzun kelimenin uzunluğu:", enUzunKelimeUzunlugu)

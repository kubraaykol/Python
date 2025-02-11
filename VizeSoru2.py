def OgrenciNoEkle(liste, ogrenciNo):
    for i in range(len(liste)):
        if isinstance(liste[i], list):
            OgrenciNoEkle(liste[i], ogrenciNo)
        elif liste[i] == 6000:
            liste[i] = [6000, ogrenciNo]

liste1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

ogrenciNo = input("Öğrenci numaranızın son 3 hanesini giriniz: ")

OgrenciNoEkle(liste1, ogrenciNo)

print("Yeni liste görüntüsü:", liste1)


liste = input("Sayı listesi").split(',')
karesiniAl = lambda x: int(x)**2
kare = map(karesiniAl, liste)
print("Listedeki sayıların kareleri:", list(kare))
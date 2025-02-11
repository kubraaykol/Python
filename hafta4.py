#%1 kültür %12 trt %18 kdv %40 ötv

fiyat =float(input("iPhone fiyatı giriniz :"))

kulturb = (fiyat*0.01)
trt= fiyat*0.12
kdv =fiyat*0.20
otv =fiyat*0.50
diger = fiyat*0.206

vergi =kulturb + trt + kdv + otv + diger
toplam = vergi + fiyat

print("Kültür Bakanlığı(%1) :", kulturb)
print("TRT Bandrol(%12) : ", trt)
print("KDV(%20) : ", kdv)
print("ÖTV(%50) : ", otv)
print("Diğer Vergiler(%20.6) : ", diger)
print("Toplam Vergi(%103.6) : ", vergi)
print("Toplam Fiyat : ", toplam)
"Başlangıç ve bitiş değerleri kullanıcıdan alınarak aradaki tek sayıları ekrana yazdıran program."

baslangic = int(input("Başlangıç değerini girin: "))
bitis = int(input("Bitiş değerini girin: "))

while baslangic <= bitis:
    if baslangic % 2 == 1:
        print(baslangic)
    baslangic += 1

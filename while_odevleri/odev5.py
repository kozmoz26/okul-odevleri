"Bilgisayar kullanıcıdan 5 sayı girmesini isteyecek, giriş işlemi tamamlandığında ekrana bu 5 sayınınortalamasını veren program."

i = 0
toplam = 0

while i < 5:
    i = i+1
    sayi = int(input("{}. sayıyı giriniz: ".format(i)))
    toplam = toplam+sayi

ortalama = toplam/5
print(ortalama)



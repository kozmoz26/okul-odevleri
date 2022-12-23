"Kullanıcının girdiği bir sayıya kadarki çift sayıların toplamını ekrana yazdıran program."

sayi = int(input("son sayıyı giriniz: "))

i = 0
toplam = 0

while i < sayi:
    if i % 2 == 0:
        toplam = toplam+i
    i = i+1

print(toplam)

"""
while döngüsünü kullanarak Kullanıcı istediği kadar sayıyı toplamak istemektedir.
Toplama işlemini sonlandırmak için “q” değeri,
devam etmek için “c” değeri girmesi istensin.
“q” girildiğinde ekranda toplam değeri versin ve program bitsin.
"""

toplam = 0

while True:
    while True:
        kullanici_giris = input("Sayı giriniz (q çıkmak için): ")

        if kullanici_giris == "q" or kullanici_giris.isdigit():
            break
        # Kullanıcı "q" ve sayı haricinde başka bir değer girdiyse
        else:
            print("Geçersiz giriş. Lütfen sayı veya q giriniz.")

    if kullanici_giris == "q":
        print("Toplam:", toplam)
        break

    # Kullanıcı "q" girmediyse
    else:
        toplam += int(kullanici_giris)

    kullanici_giris = input("Devam etmek için c, çıkmak için q giriniz: ")

    if kullanici_giris != "c":
        if kullanici_giris == "q":
            print("Toplam:", toplam)
            break

        # Kullanıcı "c" ve "q" haricinde başka bir değer girdiyse
        else:
            print("Geçersiz giriş. Lütfen c veya q giriniz.")
            continue

    # Kullanıcı "c" girdiyse
    else:
        # Döngüyü yeniden başlat
        continue


"Bilgisayara kullanıcının girdiği bir sayının faktöriyel hesabını yapan program. (örn. sayı=5 faktöriyel=5*4*3*2*1)"
while True:

    sayi = int(input("Lütfen bir sayı girin: "))

    faktoriyel = 1

    while sayi > 0:
        faktoriyel = faktoriyel * sayi
        sayi = sayi - 1

    print("Faktöriyel:", faktoriyel)

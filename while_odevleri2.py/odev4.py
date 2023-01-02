"""
“Pythonda string verileri küçük harfe çevirmek için hangi metod kullanılır" 
Yukarıdaki soruyu cevaplamak için kullanıcıya 3 hak verilecektir.
Cevabı bilirse çıktı ekranında “Tebrikler bildiniz”, yalnış yanıtlarsa "Yanlış! .....hakkın kaldı",
üç hak sonucu da bilemezse "Maalesef bilemediniz” yazsın.
"""

i = 2
while True:

    soru = input(
        "Pythonda string verileri küçük harfe çevirmek için hangi metod kullanılır?: ")

    if soru == "lower()" or soru == ".lower()" or soru == ".lower":
        print("Tebrikler bildiniz")
        break
    elif i == 0:
        print("Maalesef bilemediniz")
        break
    else:
        print("Yanlış!", i, "hakkın kaldı")
        i=i-1
        continue

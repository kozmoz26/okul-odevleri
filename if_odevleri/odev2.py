"""
Kullanıcının yaş bilgisi alınıp 
12 yaşından küçükse: çocuk
12-40 yaş arası ise: genç
40-60 yaş arası ise: orta yaşlı
60 yaştan büyükse: yaşlı
şeklinde ekrana yazdıran programın python kodlarını yazınız.
"""

age = int(input("Lütfen yaşınızı giriniz: "))

if age < 12:
  print("Çocuk")
elif age >= 12 and age <= 40:
  print("Genç")
elif age > 40 and age <= 60:
  print("Orta yaşlı")
else:
  print("Yaşlı")

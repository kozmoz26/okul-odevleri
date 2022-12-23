"""
Bir sinema salonunda kullanılan program şu şekilde çalışmaktadır:
Kişi 6-12 yaş arası ise ekranda 10 TL
13-18 ise 15 TL
18 den büyükse 20 TL
olacak şekilde uyarı vermektedir. Buna göre bu programın python kodları nasıl olmalıdır.
"""

age = int(input("Lütfen yaşınızı giriniz: "))  # Kullanıcıdan yaş bilgisi alınır

if age >= 6 and age <= 12:
  print("Bilet fiyatı: 10 TL")
elif age >= 13 and age <= 18:
  print("Bilet fiyatı: 15 TL")
else:
  print("Bilet fiyatı: 20 TL")

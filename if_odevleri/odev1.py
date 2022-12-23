"""
Bir otoparkın ücret tarifesi aşağıdaki gibidir:
1 saate kadar: 5 TL
1-5 saat arası: Saat başı 4 TL
5 saatten fazla: Saat başı 3 TL
Buna göre kullanıcının girdiği otoparkta kalınan saat süresine göre ödenecek miktarı bularak ekrana
yazdırınız.
"""

parked_hours = float(input("Otoparkta kalınan süre (saat): "))

if parked_hours <= 1:
  payment = 5 # 1 saate kadar 5 TL
elif parked_hours <= 5:
  payment = 4 * parked_hours # Saat başı 4 TL
else:
  payment = 3 * parked_hours # Saat başı 3 TL

print("Otopark ödemeniz: " + str(payment) + " TL")

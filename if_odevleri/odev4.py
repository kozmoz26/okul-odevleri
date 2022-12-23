"""
Bir internet sitesine üye girişi yapmak için önce kullanıcı adı girmesi, kullanıcı adı doğru girilmiş ise
ardından şifresi girmesi istenir. Kullanıcı adının veya şifrenin yanlış girildiği durumlarda "Siteye girişiniz
durduruldu" uyarısı gelir. İki bilgiyi de doğru girdiği durumda ancak "Giriş Başarılı" uyarısı gelecektir.
Bu koşullu durumu pythonda kodlayınız.
"""

# Kullanıcı adı ve şifre girdilerini alın
username = input("Lütfen kullanıcı adınızı giriniz: ")
password = input("Lütfen şifrenizi giriniz: ")

# Girilen kullanıcı adı ve şifre kombinasyonunun doğruluğunu kontrol edin
if (username == "ornek") and (password == "12345"):
  print("Giriş Başarılı")
elif (username == "ornek") and (password != "12345"):
  print("Şifre hatalı")
elif (username != "ornek") and (password == "12345"):
  print("Kullanıcı adı hatalı")
else:
  print("Siteye girişiniz durduruldu")

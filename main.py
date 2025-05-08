from fonksiyonlar import asal
from fonksiyonlar import oneto100
from fonksiyonlar import name as ela
from fonksiyonlar import tek_çift

while True:
    print("1. Asal Sayı Kontrolü")
    print("2. 1'den 100'e kadar sayılar")
    print("3. İsim Yazdırma")
    print("4. Tek Çift Kontrolü")
    print("5. Çıkış")
    secim = input("Bir seçenek girin (1-5): ")
    if secim == "1":
        asal.asal()
    elif secim == "2":
        oneto100.oneto100()
    elif secim == "3":
        ela.name()
    elif secim == "4":
        tek_çift.tek_çift()
    elif secim == "5":
        print("Çıkılıyor...")
        break
    else:
        print("Geçersiz seçim, lütfen tekrar deneyin.")



sayi=float(input("Lütfen bir sayı giriniz: "))
durum=0<sayi<100
if durum:
    print("Sayı 0 ile 100 arasındadır.")
else:
    print("Sayı 0 ile 100 arasında değildir.")

sayi2=int(input("lütfen bir tam sayı giriniz: "))
durum2=sayi2%2==0
if durum2:
    print("Sayı çifttir.")
else:
    print("Sayı tektir.")

email='email@sadikturan.com'
parola='abc123'
girilenEmail=input("Lütfen email adresinizi giriniz: ")
girilenParola=input("Lütfen parolanızı giriniz: ")
if girilenEmail==email:
    if girilenParola==parola:
        print("Giriş başarılı.")
    else:
        print("Parola yanlış.")
else:
    if girilenParola==parola:
        print("Email adresi yanlış.")
    else:
        print("Email adresi ve parola yanlış.")

sayi3=int(input("Lütfen bir sayı giriniz: "))
sayi4=int(input("Lütfen bir sayı daha giriniz: "))
sayi5=int(input("Lütfen bir sayı daha giriniz: "))

if (sayi3>sayi4) and (sayi3>sayi5):
    print("En büyük sayı: ",sayi3)
elif (sayi4>sayi3) and (sayi4>sayi5):
    print("En büyük sayı: ",sayi4)
elif (sayi5>sayi3) and (sayi5>sayi4):
    print("En büyük sayı: ",sayi5)
else:
    print("Sayıların hepsi eşit veya bazıları eşittir.Lütfen farklı sayılar giriniz.")

vize1=int(input("Lütfen 1. vize notunuzu giriniz: "))
vize2=int(input("Lütfen 2. vize notunuzu giriniz: "))
final=int(input("Lütfen final notunuzu giriniz: "))
ortalama=(vize1+vize2)/2*0.6+final*0.4
if ortalama>=50 and final>=50:
    print("Dersi geçtiniz. Ortalamanız: ",ortalama)
elif final>=70:
    print("Dersi geçtiniz. Ortalamanız: ",ortalama)
else:
    print("Dersi geçemediniz. Ortalamanız: ",ortalama)

Ad=input("Lütfen adınızı giriniz: ")
kilo=float(input("Lütfen kilonuzu giriniz: "))
boy=float(input("Lütfen boyunuzu metre cinsinden giriniz: "))
vki=kilo/(boy**2)
if 0<=vki<=18.4:
    print("Zayıf")
elif 18.5<=vki<=24.9:
    print("Normal")
elif 25<=vki<=29.9:
    print("Fazla kilolu")
elif 30<=vki<=34.9:
    print("Obez")
elif not 0<kilo or  not 0<boy:
    print("Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.")
else:
    print("İksir golemiiiiiii!!!")
name=input('Adınızı giriniz: ')
yas=int(input('Yaşınızı giriniz: '))
okuldurumu=int(input('Okul durumunuz (1-İlkokul Mezunu, 2-Ortaokul Mezunu, 3-Lise Mezunu, 4-Üniversite Mezunu): '))
if yas >= 18 and okuldurumu >= 3:
    print(f"Tebrikler:{name}, ehliyet alabilirsiniz.")
else:
    print(f"Üzgünüz:{name}, ehliyet alamazsınız.")

sinav1=int(input('Sınav 1 notunuzu giriniz: '))
sinav2=int(input('Sınav 2 notunuzu giriniz: '))
ortalama=(sinav1+sinav2)/2
if sinav1<0 or sinav1>100 or sinav2<0 or sinav2>100:
    print('Hatalı not girdiniz. Lütfen 0-100 arasında bir değer giriniz.')
elif 0<=ortalama<=24:
    print(f'Sınav notunuz: 0')
elif 25<=ortalama<=44:
    print(f'Sınav notunuz: 1')
elif 45<=ortalama<=54:
    print(f'Sınav notunuz: 2')
elif 55<=ortalama<=69:
    print(f'Sınav notunuz: 3')
elif 70<=ortalama<=84:
    print(f'Sınav notunuz: 4')
elif 85<=ortalama<=100:
    print(f'Sınav notunuz: 5') 

from datetime import date
gun=int(input('Trafiğe çıkış günü: '))
ay=int(input('Trafiğe çıkış ayı: '))
yil=int(input('Trafiğe çıkış yılı: '))
tarih= date(yil, ay, gun)
istek=int(input('1. 2. veya 3. bakım tarihinden hangisini görmek istersiniz? (1/2/3): '))
if istek==1:
    bakim=tarih.replace(year=tarih.year+1)
    print(f'1. bakım tarihi: {bakim}')
elif istek==2:
    bakim=tarih.replace(year=tarih.year+2)
    print(f'2. bakım tarihi: {bakim}')
elif istek==3:
    bakim=tarih.replace(year=tarih.year+3)
    print(f'3. bakım tarihi: {bakim}')

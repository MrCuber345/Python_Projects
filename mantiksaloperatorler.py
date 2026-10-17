x=int(input("Bir sayı giriniz: "))
sart= x>0 and x<100
print("Sayı 0 ile 100 arasında mı? ", sart)

y=int(input("Bir sayı giriniz: "))
sart2=x>0 and x % 2 == 0
print("Sayı pozitif ve çift mi? ", sart2)

email='efecinar2345@gmail.com'
parola='123456'
email_girisi=input("Email adresinizi giriniz: ")
parola_girisi=input("Parolanızı giriniz: ")
sart3=email_girisi==email and parola_girisi==parola
print("Email ve parola doğru mu? ", sart3)

vize1=int(input("Vize 1 notunuzu giriniz: "))
vize2=int(input("Vize 2 notunuzu giriniz: "))
final=int(input("Final notunuzu giriniz: "))
ortalama=(vize1+vize2)/2*0.6+final*0.4
gectimi=(ortalama>=50 and final>=50) or final>=70
print("Dersten geçtiniz mi? ", gectimi)

ad=input("Adınızı giriniz: ")
boy=float(input("Boyunuzu giriniz (m): "))
kilo=int(input("Kilonuzu giriniz (kg): "))
vki=kilo/(boy**2)
zayif=0<=vki<=18.4
normal=18.5<=vki<=24.9
fazlakilolu=25<=vki<=29.9
obez=30<=vki<=34.9
print("Vki endeksiniz: ", vki)
print("Zayıf mısınız? ", zayif)
print("Normal misiniz? ", normal)
print("Fazla kilolu musunuz? ", fazlakilolu)
print("Obez misiniz? ", obez)


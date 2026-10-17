liste = ["1","2","5a","10b","abc","10","50"]
liste2 = []

for i in liste:
    try:
        i=int(i)
        liste2.append(i)
    except ValueError:
        print(f"Tam sayı olmayan bir değer bulundu: {i}")

print("Tam sayılar:", liste2)

while True:
    deger = input("Tam sayı giriniz (çıkmak için 'q' tuşlayın): ")
    if deger.lower() == 'q':
        print("Programdan çıkılıyor.")
        break
    try:
        deger = int(deger)
        print(f"Girdiğiniz tam sayı: {deger}")
    except ValueError:
        print("Hata: Girilen değer bir tam sayı değildir.")

parolalici = input("Lütfen Türkçe karakter içermeyen bir parola giriniz: ")
try:
    if any(char in parolalici for char in "çğıöşüÇĞİÖŞÜ"):
        raise ValueError("Parola Türkçe karakter içeriyor.")
    print("Parola geçerli.")
except ValueError as e:
    print(f"Hata: {e}")

from math import factorial
def faktoriyel_alici(x):
    try:
        if x < 0:
            raise ValueError("Negatif sayıların faktöriyeli alınamaz.")
        if x == 0:
            raise ValueError("Sıfırın faktöriyeli alınamaz.")
        print(factorial(x))
    except ValueError as e:
        print(f"Hata: {e}")
while True:
    x = input("Faktöriyeli alınacak tam sayıyı giriniz(çıkmak için 'q' tuşlayın): ")
    if x.lower() == 'q':
        print("Programdan çıkılıyor.")
        break
    else:
        try:
            x = int(x)
            if x<0:
                raise ValueError("Negatif sayıların faktöriyeli alınamaz.")
            if x==0:
                raise ValueError("Sıfırın faktöriyeli alınamaz.")
            faktoriyel_alici(x)
        except Exception as e:
            if type(x) == str:
                print("Hata: Girilen değer bir tam sayı değildir.")
            else:
                print(f"Hata: {e}")








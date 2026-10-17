sayilar = [1,3,5,7,9,12,19,21]
toplam=0

for sayi in sayilar:
    if sayi % 3 == 0:
        print(sayi)

for sayi in sayilar:
    toplam += sayi
print(toplam)

for sayi in sayilar:
    if sayi % 2 == 1:
        print(sayi**2)
        
sehirler=["kocaeli","istanbul","ankara","izmir","rize"]

for sehir in sehirler:
    if len(sehir)<=5:
        print(sehir)

urunler=[
{"name":"samsung s6","fiyat":"3000"},
{"name":"samsung s7","fiyat":"4000"},
{"name":"samsung s8","fiyat":"5000"},
{"name":"samsung s9","fiyat":"6000"},
{"name":"samsung s10","fiyat":"7000"}
]
toplam2=0

for urun in urunler:
    if int(urun["fiyat"]) <= 5000:
        print(urun["name"])

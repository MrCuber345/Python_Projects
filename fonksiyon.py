
def kelimegosterici():
    name = input("Adınızı girin: ")
    sayac = int(input("Kaç kere tekrarlansın: "))
    sayi=0
    while sayi < sayac:
        print(name)
        sayi+=1
kelimegosterici()

def listeleyici():
    liste=list(input("Bir liste oluştur,virgülle elemanları ayır(Boşluk Bırakma): ").split(","))
    print(liste)
listeleyici()

def asal_bulucu():
    girdi = input("Sayılar girin, virgülle ayırın: ")
    sayilar = [int(s.strip()) for s in girdi.split(",")]
    
    for sayi in sayilar:
        if sayi < 2:
            print(f"{sayi} asal değildir.")
            continue
            
        durum = True
        for bolen in range(2, int(sayi**0.5) + 1):
            if sayi % bolen == 0:
                durum = False
                break
        
        if durum:
            print(f"{sayi} asaldır.")
        else:
            print(f"{sayi} asal değildir.")

asal_bulucu()

def bolunenarayici():
    liste=[]
    sayi=int(input("Bir sayı giriniz: "))
    bolen=1
    while bolen<=sayi:
        if sayi%bolen==0:
            liste.append(bolen)
        bolen+=1
    print(liste)
bolunenarayici()



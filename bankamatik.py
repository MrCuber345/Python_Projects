SadıkHesap={
    "ad":"Sadık",
    "hesapno":"123",
    "bakiye":3000,
    "ekhesap":2000
}
AliHesap={
    "ad":"Ali",
    "hesapno":"456",
    "bakiye":2000,
    "ekhesap":1000
}

durum=False
istek=int(input("İşlem yapmak ister misiniz(evet için 1 ,hayır için 0 tuşlayın): "))
if istek==1:
    hesapistek=input("Hesap adınızı giriniz: ")
    adistek=input("Adınızı giriniz: ")
    hesapnoistek=input("Hesap no giriniz: ")

if hesapistek!="SadıkHesap" and hesapistek!="AliHesap":
    print("Hatalı hesap adı!")
elif hesapistek=="SadıkHesap":
    if adistek=="Sadık" and hesapnoistek=="13245678":
        print("Hoşgeldin SadıkHesap")
        durum=True
    else:
        print("Yeniden deneyiniz.")
elif hesapistek=="AliHesap":
    if adistek=='Ali' and hesapnoistek=="12345678":
        print("Hoşgeldin AliHesap")
        durum=True
    else:
        print("Yeniden deneyiniz.")

def hesapcek():
    istenentutar=int(input("Kaç lira çekeceksiniz: "))
    if hesapistek=="SadıkHesap":
        if istenentutar>SadıkHesap["bakiye"]:
            print("Yetersiz Bakiye")
            istek2=int(input("Ek hesap kullanmayı ister misiniz(Evet için 1,Hayır için 2 tuşlayın: )"))
            if istek2==1:
                if istenentutar>SadıkHesap["bakiye"]+SadıkHesap["ekhesap"]:
                    print("Yetersiz bakiye")
                else:
                    print("Para yeterli para aktarıldı")
                    SadıkHesap["ekhesap"]-=istenentutar-SadıkHesap["bakiye"]
                    SadıkHesap["bakiye"]=0
        else:
            print("Para yeterli para aktarıldı")
            SadıkHesap["bakiye"]-=istenentutar
    if hesapistek=="AliHesap":
        if istenentutar>AliHesap["bakiye"]:
            print("Yetersiz Bakiye")
            istek2=int(input("Ek hesap kullanmayı ister misiniz(Evet için 1,Hayır için 2 tuşlayın: )"))
            if istek2==1:
                if istenentutar>AliHesap["bakiye"]+AliHesap["ekhesap"]:
                    print("Yetersiz bakiye")
                else:
                    print("Para yeterli para aktarıldı")
                    AliHesap["ekhesap"]-=istenentutar-AliHesap["bakiye"]
                    AliHesap["bakiye"]=0
        else:
            print("Para yeterli para aktarıldı")
            AliHesap["bakiye"]-=istenentutar
if durum==True:
    hesapcek() 
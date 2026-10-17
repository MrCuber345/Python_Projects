liste = {
    "ekatalog":{
        "gıda":{
            "elma":{"fiyat": 15,"stok": 100,"aciklama": "Taze elma"},
            "ekmek":{"fiyat": 17,"stok": 50,"aciklama": "Taze ekmek"},
        },
        "kırtasiye":{
            "kalem":{"fiyat": 5,"stok": 200,"aciklama": "Kurşun kalem"},

            "defter":{"fiyat": 20,"stok": 150,"aciklama": "Çizgili defter"},
        }
    }
}

parametre = True

yoneticisifre = "123"

def listegoster():
    print(f"Ürün Listesi: {liste}")

def urungoster():
    print(liste["ekatalog"].keys())
    secilen_kategori = input("Lütfen bir kategori seçin: ")
    if secilen_kategori in liste["ekatalog"]:
        print(liste["ekatalog"] [secilen_kategori].keys())
        secilen_urun = input("Lütfen bir ürün seçin: ")
        if secilen_urun in liste["ekatalog"][secilen_kategori]:
            print("Ürün Detayları: fiyat, stok, aciklama")
            secilen_detay = input("Lütfen bir detay seçin: ")
            if secilen_detay in liste["ekatalog"][secilen_kategori][secilen_urun]:
                print(f"{secilen_detay}: {liste['ekatalog'][secilen_kategori][secilen_urun][secilen_detay]}")
            else:
                print("Geçersiz detay seçimi.")
        else:
            print("Geçersiz ürün seçimi.")
    else:
        print("Geçersiz kategori seçimi.")

def urunekle():
    verilen_sifre = input("Lütfen yönetici şifresini girin: ")
    if verilen_sifre == yoneticisifre:
        kategori = input("Lütfen ürünün kategorisini girin: ")
        urun_adi = input("Lütfen ürünün adını girin: ")
        fiyat = float(input("Lütfen ürünün fiyatını girin: "))
        stok = int(input("Lütfen ürünün stok miktarını girin: "))
        aciklama = input("Lütfen ürünün açıklamasını girin: ")
        if kategori not in liste["ekatalog"]:
            liste["ekatalog"][kategori] = {}
        liste["ekatalog"][kategori][urun_adi] = {
            "fiyat": fiyat,
            "stok": stok,
            "aciklama": aciklama
        }
        print(f"{urun_adi} adlı ürün başarıyla eklendi.")
    else:
        print("Hatalı şifre. Ürün ekleme yetkiniz yok.")
while parametre== True:
    istenen_islem = input("Lütfen yapmak istediğiniz işlemi seçin (listegoster, urungoster, urunekle): ")
    if istenen_islem == "listegoster":
        listegoster()
    elif istenen_islem == "urungoster":
        urungoster()
    elif istenen_islem == "urunekle":
        urunekle()
    else:
        print("Geçersiz işlem seçimi.")
    devam_mi = input("Başka bir işlem yapmak ister misiniz? (evet/hayır): ")
    if devam_mi== "hayır":
        parametre = False
        print("Programdan çıkılıyor.")
        continue
    if devam_mi== "evet":
        parametre = True
        continue

    
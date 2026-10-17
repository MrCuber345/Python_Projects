import random

class bankahesabi():

    def __init__(self,kullanici_adi=None,hesap_no=None,bakiye=0):
        self.kullanici_adi = kullanici_adi
        self.hesap_no = hesap_no
        self.bakiye = bakiye                 
                                             

    def hesap_olustur(self):
        self.kullanici_adi=input("Merhaba, banka hesabınızı oluşturmak için kullanıcı adınızı girin: ")
        self.hesap_no = random.randint(1000,2000)
        kullanici_listesi[self.hesap_no] = self
        print("Hesap oluşturuldu. Kullanıcı adı: ",self.kullanici_adi," Hesap numarası: ",self.hesap_no)

    def profil_goruntule(self):
            print("Kullanıcı adı: ",self.kullanici_adi)
            print("Hesap numarası: ",self.hesap_no)
            print("Bakiye: ",self.bakiye)

    def bakiyesorgula(self):
        print("Bakiyeniz: ",self.bakiye)

    def para_yatir(self,miktar):
        self.bakiye += miktar
        print("Yeni bakiyeniz: ",self.bakiye)   
        return self.bakiye
    
    def para_cek(self,miktar):
        if self.bakiye >= miktar:
            self.bakiye -= miktar
            print("Yeni bakiyeniz: ",self.bakiye)
            return self.bakiye
        else:
            print("Yetersiz bakiye. İşlem gerçekleştirilemedi.")
            return self.bakiye

eski_hesap1 = bankahesabi("Ali", 1234, 1000)
eski_hesap2 = bankahesabi("Ayşe", 5678, 500)
eski_hesap3 = bankahesabi("Mehmet", 9012, 2000)

kullanici_listesi = {
    1234: eski_hesap1,
    5678: eski_hesap2,
    9012: eski_hesap3
}

parametre = True

while parametre==True :
    istenen_islem = input("Hoşgeldiniz! Lütfen yapmak istediğiniz işlemi seçin: \n1. Hesap OLuştur 2. İşlem Yap")
    if istenen_islem.isdigit() and istenen_islem == "1":
        yeni_hesap = bankahesabi()
        yeni_hesap.hesap_olustur()
    elif istenen_islem == "2":
        hesap_no = int(input("Lütfen işlem yapmak istediğiniz hesap numarasını girin: "))
        if hesap_no in kullanici_listesi:
            secilen_hesap = kullanici_listesi[hesap_no]
            islem_secimi = input("Lütfen yapmak istediğiniz işlemi seçin: \n1. Profil Görüntüle 2. Bakiye Sorgula 3. Para Yatır 4. Para Çek")
            if islem_secimi == "1":
                secilen_hesap.profil_goruntule()
            elif islem_secimi == "2":
                secilen_hesap.bakiyesorgula()
            elif islem_secimi == "3":
                miktar = float(input("Yatırmak istediğiniz miktarı girin: "))
                secilen_hesap.para_yatir(miktar)
            elif islem_secimi == "4":
                miktar = float(input("Çekmek istediğiniz miktarı girin: "))
                secilen_hesap.para_cek(miktar)
            else:
                print("Geçersiz işlem seçimi.")
        else:
            print("Hesap bulunamadı.")





    
ogrenciler= {
    '120': {
        'ad':'Ali',
        'soyad':'Yilmaz',
        'telefon':'532'
    },
    '125': {
        'ad':'Can',
        'soyad':'Korkmaz',
        'telefon':'533'
    },
    '128':{
        'ad':'Volkan',
        'soyad':'Yükselen',
        'telefon':'534'
    }
}
numara=input('Okul Numaranız: ')
konu=input('İstediğiniz Bilgi Nedir{ad,soyad,telefon}')
print(ogrenciler[str(numara)][konu])

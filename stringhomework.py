website = 'http://www.sadikturan.com'
course = 'Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)'
length1 = len(course)

print(length1)
print(website[7:10])
print(website[-3:])
print(course[0:15])
print(course[-16:-1])
print(course[::-1])

ad,soyad,yas,meslek = 'Bora' , 'Yılmaz' , 32 , 'mühendis'
print(f"Benim adım {ad} {soyad}, yaşım {yas} ve mesleğim {meslek}.")

metin = 'Hello world'
metin = metin.replace('w','W')
print(metin)
alfabe = 'abc'
print(alfabe+alfabe+alfabe)
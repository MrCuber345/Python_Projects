website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"
selam=' Hello World '

selam = selam.strip()
print(selam)

website = website.strip('http://www.').strip('.com')
print(website)

course = course.lower()
print(course)

sayi = website.count('a')
print(sayi)

isfound = website.startswith('www')
print(isfound)

index = website.find('com')
print(index)

isalpha = website.isalpha()
print(isalpha)

ekstrametin = 'Contents'
ekstrametin = ekstrametin.center(50,'*')
print(ekstrametin)

course = course.replace(' ','-')
print(course)

selam = selam.replace('World','There')
print(selam)

course = course.replace('-',' ')
course = course.split(' ')
print(course)
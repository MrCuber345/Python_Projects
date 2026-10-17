names = ['Ali', 'Yağmur','Hakan','Deniz']
years = [1998, 2000, 1998, 1987]

names.append('Cenk')
print(names)

names.insert(0, 'Sena')
print(names)

names.remove('Deniz')
print(names)

index = names.index('Ali')
print(index)

names = names[::-1]
print(names)

names.sort()
print(names)

years.sort()
print(years)

str = ['Chevrolet,Dacia']
print(str)

print(years[0])
print(years[-1])

print(years.count(1998))
years.clear()
print(years)

favaraba1=input('Fav Arabadan Birini Söyle')
favaraba2=input('Başka Fav Araba Söyle')
favaraba3=input('Başka Fav Araba Söyle')
markalist=[favaraba1+', '+favaraba2+', '+favaraba3]
print(markalist)



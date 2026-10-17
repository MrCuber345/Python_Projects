arabalist = ['Bmw', 'Mercedes', 'Opel', 'Mazda']
length = len(arabalist)
print(length)

alinacakarabalar = arabalist[0]+ ', ' + arabalist[3]
print(alinacakarabalar)

arabalist[3] = arabalist[3].replace('Mazda', 'Toyota')
print(arabalist)

index = arabalist.index('Mercedes')
print(index)

print(arabalist[-2])

print(arabalist[0:3])

arabalist[2]= 'Toyota'
arabalist[3] = 'Renault'
print(arabalist)

arabalist.append('Audi')
arabalist.append('Nissan')
print(arabalist)

arabalist.remove('Nissan')
print(arabalist)

arabalist = arabalist[::-1]
print(arabalist)

studenta = ['Yiğit', 'Bilgi', 2010, [70, 60, 70]]
studentb = ['Sena', 'Turan', 1999, [80, 80, 70]]
studentc = ['Ahmet', 'Turan', 1998, [80, 70, 90]]
arsiv = [studenta, studentb, studentc]
print(arsiv)
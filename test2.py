try:
    with open("new3.txt","x",encoding="utf-8") as file:
        pass
    with open("new3.txt","a+",encoding="utf-8") as file:
        file.write("Ahmet 31\n")
        file.write("Ayşe 67\n")
        file.write("Mehmet 33\n")
except Exception:
    pass
else:
    print("Yeni dosya oluşturuldu!")

with open("new3.txt","r+",encoding="utf-8") as file:
    metin=file.read()
    print(metin)


    

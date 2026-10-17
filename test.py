try:
    with open("new2.txt","x",encoding="utf-8") as file:
        pass
except Exception:
    pass

with open("new2.txt","a+",encoding="utf-8") as file:
      file.write("Merhaba Mistik Dünya!\n")
      file.seek(0)
      metinokuma= file.read()
      print(metinokuma)

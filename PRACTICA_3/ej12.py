import re
txt = input("Insertar cadena de texto: ")
lpat= [" ", "_", ":"]
for p in lpat:
    txt = re.sub(p ,"|", txt)
print(txt)

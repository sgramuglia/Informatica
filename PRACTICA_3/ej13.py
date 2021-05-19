import re
txt = input("Insertar cadena de texto: ")
pat = "[0-9](.{2})"
txt = re.sub(pat,"_",txt)
print(txt)
import re
txt = input("Insertar cadena de texto: ")
pat = "[0-9]"
print(re.findall(pat,txt))
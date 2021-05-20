import re
txt = input("Insertar cadena de texto: ")
pat = "-(.*?)-"
print(re.findall(pat,txt))
import re
txt = input("Insertar cadena de texto: ")
pat = " "
pat2 = "\t"
txt = re.sub(pat,";",txt)
txt = re.sub(pat2,";",txt)
print(txt)
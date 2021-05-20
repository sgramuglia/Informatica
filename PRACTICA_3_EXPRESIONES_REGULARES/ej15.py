import re
txt = input("Insertar correo eletrónico: ")
pat = "@(.*).com"
if re.search(pat,txt):
    print("Formato correcto")
else:
    print("El formato no es correcto")
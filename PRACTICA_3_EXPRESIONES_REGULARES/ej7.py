import re
pat = "[^a-zA-Z0-9\s]"
txt = input("Insertar cadena de texto: ")
if re.search(pat,txt):
    print("No contiene solamente letras minúsculas, mayúsculas, espacios y números")
else: 
    print("Contiene solamente letras minúsculas, mayúsculas, espacios y números")
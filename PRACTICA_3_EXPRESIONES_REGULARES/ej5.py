import re
txt = input("Insertar cadena de texto: ")
num = "[0-9]"
if txt[0] == num:
    print("El texto empieza con " + txt[0])
else:
    print("El texto no empieza con un número")
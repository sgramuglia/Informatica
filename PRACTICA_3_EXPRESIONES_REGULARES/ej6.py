import re
l1=["hola","mamá"]
l2=["tengo","hambre"]
txt = input("Insertar cadena de texto: ")
for w in l1:
    re.search(w,txt)
for w in l2:
    re.search(w,txt)
txt = input("Insertar nombre y dos apellidos: ")
nmbr = txt.split(' ')
mayus = ''
for wrd in nmbr:
    mayus += wrd[0]
print(mayus.upper())
txt = input("instertar string de minimo 6 letras: ")
if len(txt) >= 6:
    print(txt[4].upper())
    print(txt[5].upper())
else:
    print("error, escribi minimo 6 letras")
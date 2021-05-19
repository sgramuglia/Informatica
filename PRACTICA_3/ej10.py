import re
txt = input("Insertar cadena de texto: ")
lpat = ["@(.*?)@","@(.*?)&","&(.*?)@","&(.*?)&",]
ans = []
for p in lpat:
    list.append(ans, re.findall(p,txt))
print(ans)

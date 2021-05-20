i = 0
ls1 = []
ls2 = []
ls3 = []
while i < 5:
    num = int(input("Instertar número: "))
    ls1.append(num)
    i+=1
i = 0
while i < 5:
    num = int(input("Instertar número: "))
    ls2.append(num)
    i+=1
for n in range(len(ls1)):
    nm = ls1[n] + ls2[n]
    ls3.append(nm)
print(ls3)

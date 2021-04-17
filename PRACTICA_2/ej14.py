def medTemp(min, max):
    return (min+max)/2

qnt = int(input("Cantidad de días: "))
days = {}

for day in range(qnt):
    mn = int(input("Temperatura mínima: "))
    mx = int(input("Temperatura máxima: "))
    mt = medTemp(mn,mx)
    days[day+1] = mt

print(days)

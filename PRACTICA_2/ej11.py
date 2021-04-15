cnt = {}
alph = "qwertyuiopasdfghjklñzxcvbnm"
for l in alph + alph.upper():
    cnt[l] = 0
ch = input("Insertar string: ")
for c in ch:
    if c.lower() in alph:
        cnt[c] += 1
for ky, vl in cnt.items():
    print(ky,vl)
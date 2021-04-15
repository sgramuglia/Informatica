cnt = {}
ch = input("Insertar cadena: ")
for c in ch:
    if c in cnt:
        cnt[c] += 1
    else: 
        cnt[c] = 1
for ky, val in cnt.items():
    print(ky,"->",val)
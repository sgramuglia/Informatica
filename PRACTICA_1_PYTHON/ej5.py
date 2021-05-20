num = input("Insertar 3 numeros: ")
if num.find(' '):
    num = num.replace(' ', '')
def sum():  
    ttl = 0  
    for nmbr in num:  
        ttl += int(nmbr)  
    return ttl  
print(sum()/3)

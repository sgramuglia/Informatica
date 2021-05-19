route = r"C:\Users\sofig\Desktop\info\Informatica\txtmanip.txt"
n = int(input("Insertar número de lineas a imprimir: "))
with open(route,"r") as txt:
    lines = txt.readlines()
    for l in lines:
        if lines.index(l) < n:
            print(l)
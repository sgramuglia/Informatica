route = r"C:\Users\sofig\Desktop\info\Informatica\txtmanip.txt"
with open(route,"r") as txt:
    data = txt.read()
    words = data.split()
    print('Número de palabras en el archivo:', len(words))
folder = r"C:\Users\sofig\Desktop\info\Informatica\PRACTICA_4\texts"
newf = r"C:\Users\sofig\Desktop\info\Informatica\PRACTICA_4\texts\foldercomb.txt"
newfile = ""
with open(folder,"r") as f:
    for arch in f:
        txt = arch.read()
        newfile += txt + "\n"
with open(newf,"a") as nf:
    nf.write(newfile)
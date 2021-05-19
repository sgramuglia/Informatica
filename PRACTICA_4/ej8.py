r1 = r"C:\Users\sofig\Desktop\info\Informatica\txtmanip.txt"
r2 = r"C:\Users\sofig\Desktop\info\Informatica\newtxtmanip.txt"
r1_r2 = r"C:\Users\sofig\Desktop\info\Informatica\comb.txt"
with open(r1,"r") as txt1:
    t1 = txt1.read()
with open(r2,"r") as txt2:
    t2 = txt2.read()
t1 += "\n" + t2
with open(r1_r2,"w") as comb:
    comb.write(t1)
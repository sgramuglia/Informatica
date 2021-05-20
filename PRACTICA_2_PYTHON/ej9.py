ln = []
la = []
nm = "s"
while nm != "*":
    nm = input("Instertar nombre: ")
    if nm != "*":
        ln.append(nm)
        la.append(int(input("Instertar edad: ")))
hg = la[0]
pshg = 0
for i in range(len(ln)):
    if hg < la[i]:
        hg = la[i]
        pshg = i
print("Mayor edad: ", hg)
print("Estudiante mayor: ", ln[pshg])
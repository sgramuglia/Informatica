mrks = {}
qnt = int(input("Cantidad de alumnos: "))
nm = ""
mrk = 0
for i in range(qnt):
    mrklist = []
    nm = input("Nombre: ")
    mrk = int(input("Nota: "))
    if nm not in mrks.keys():
       while mrk > 0:
            mrklist.append(mrk)
            mrks[nm] = mrklist
            mrk = int(input("Nota: "))
            print(mrklist)
    else:
        print("Alumno ya cargado")

for nm in mrks.keys(): 
    marks = 0
    qn = 0
    for ex in mrks[nm]:
        marks += ex
        qn += 1
    print("Promdedio de: ", nm, ":", marks/qn)

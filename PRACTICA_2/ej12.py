mrks = {}
qnt = int(input("Cantidad de alumnos: "))
mrklist = []
#nm = input("Nombre: ")
mrk = int(input("Nota: "))
for i in range(qnt):
    nm = input("Nombre: ")
    if nm not in mrks.keys():
       while mrk > 0:
            mrklist.append(mrk)
            mrks[nm] = mrklist
            mrk = int(input("Nota: "))
    else:
        print("Alumno ya cargado")
for nm, mrk in mrks.items(): 
    marks = 0
    qn = 0
    for ex in mrklist:
        marks += ex
        qn += 1
    print("Promdedio de: ", nm, ":", marks/qn)

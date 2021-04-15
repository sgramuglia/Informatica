mrks = {}
qnt = int(input("Cantidad de alumnos: "))
for i in range(qnt):
    nm = input("Nombre: ")
    mrk = int(input("Nota: "))
    while mrk >= 0:
        mrk = int(input("Nota: "))
        mrks[nm] = mrk
for nm, mrk in mrks.items(): 
    marks = 0
    qn = 0
    for ex in mrks.values():
        marks += ex
        qn += 1
    print("Promdedio de: ", nm, ":", marks/qn)
    print(marks)
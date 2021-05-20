members = [
    {
        "Socio número" : 1,
        "Nombre" : "Florencia Ocampo",
        "Fecha de ingreso" : "14/09/2001",
        "Cuota al día" : True

    },
    {
        "Socio número" : 2,
        "Nombre" : "David Estévez",
        "Fecha de ingreso" : "14/09/2001",
        "Cuota al día" : True
    },
    {
        "Socio número" : 3,
        "Nombre" : "Sofía Cáceres",
        "Fecha de ingreso" : "14/09/2001",
        "Cuota al día" : True
    }
]

def howMany():
    return len(members)

def addMember():
    num = howMany() + 1
    name = input("Nombre: ")
    date = input("Fecha de ingreso: ")
    members.append({
        "Socio número" : num,
        "Nombre" : name,
        "Fecha de ingreso" : date,
        "Cuota al día" : True
    })
    #printMembers()
  
def feeCorr():
    n = int(input("Número de socio: "))
    i = n + 1
    member = members[i]
    fee = member.get("Cuota al día")
    if fee:
        print("Las cuotas están todas al día")
    else:
        print("Las cuotas no están al día")

def changeDate():
    for member in members:
        date = member.get("Fecha de ingreso")
        if date == "21/10/2017":
            date = "22/10/2017"

def terminateMembership():
    name = input("Nombre y apellido de socio: ")
    for member in members:
        n = member.get("Nombre")
        if n == name:
            members.remove(member)
    #printMembers()

def printMembers():
    for member in members:
        name = member.get("Nombre")
        print(name)

print("¿Qué acción desea realizar?")
print("1 - Agregar miembro")
print("2 - Obtener cantidad de miembros totales")
print("3 - Corroborar las cuotas de un miembro")
print("4 - Dar de baja a un miembro")
print("5 - Ver listado de miembros")
quest = input("Inserte el número correspondiente a la acción: ")

if quest == "1":
    addMember()
elif quest == "2":
    print(howMany())
elif quest == "3":
    feeCorr()
elif quest == "4":
    terminateMembership()
elif quest == "5":
    printMembers()
else:
    print("Error, vuelva a intentar insertar un número del 1-5")
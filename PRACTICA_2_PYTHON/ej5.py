dy = int(input("Instertar día de la semana: "))
dys = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
if dy > 0 and dy < 8:
    print(dys[dy-1])
else:
    print("Insertar numero del 1 al 7")
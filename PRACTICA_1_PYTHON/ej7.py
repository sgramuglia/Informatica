v1 = int(input("Insertar ganancia por venta: "))
v2 = int(input("Insertar ganancia por venta: "))
v3 = int(input("Insertar ganancia por venta: "))
v4 = int(input("Insertar ganancia por venta: "))
s = int(input("Insertar sueldo: "))
prc = 0.10
com = v1 * prc + v2 * prc + v3 * prc + v4 *prc
print ("Comisión por ventas: ", com)
print ("Ganancia final: ", com + v1 + v2 + v3 + v4 + s)
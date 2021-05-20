gr = int(input("Inserte el peso(gr) del paquete: "))
if gr > 5000:
    print("Lamentmos informarle que el paquete no puede ser transportado debido a que viola nuestras politicas de entrega. El paquete debe pesar menos de cinco kilogramos.")
else: 
    zn = int(input("Inserte la zona a la que corresponde: "))
    if zn > 0 and zn < 6:
        if zn == 1:
            print("costo del paquete: $", 10000 * gr)
        elif zn == 2:
            print("costo del paquete: $", 15000 * gr)
        else:
            print("costo del paquete: $", (zn*6000) * gr)
    else:
        print("1 - América del Sur ; 2 - América Central ; 3- América del Norte ; 4 - Europa ; 5- Asia")

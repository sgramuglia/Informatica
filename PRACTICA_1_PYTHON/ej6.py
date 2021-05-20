num = int(input("Insertar minutos: "))
if num < 60:
    print('0'+" "+str(num))
else:
    if num>=60:
        time = num*(1/60)
        time1 = (format(time, '.2f'))
        print(str(time1).replace('.',':'))


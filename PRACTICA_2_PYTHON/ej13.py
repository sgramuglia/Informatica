def esMultiplo(n1,n2):
    if n1 % n2 == 0:
        print(n1, " es multiplo de ", n2)
    elif n2 % n1 == 0: 
        print(n2, " es multiplo de ", n1)
    else:
        print("No son multiplos")

num1 = int(input("Primer numero entero: "))
num2 = int(input("Segundo numero entero: "))
esMultiplo(num1,num2)
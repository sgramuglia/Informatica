num = int(input("instertar número: "))
if num > 0 and num % 2 == 0:
    print("El número es positivo y par")
elif num > 0 and num % 2 != 0:
    print("El número es positivo e impar")
elif num < 0 and num % 2 != 0:
    print("El número es negativo e impar")
elif num < 0 and num % 2 == 0:
    print("El número es negativo y par")
else:
    print("El número es cero y par")
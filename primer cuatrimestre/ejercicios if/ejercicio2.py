# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.



numero_evaluado = int(input("Ingrese un numero para determinar si es par o impar: "))
comprobacion = numero_evaluado % 2

if comprobacion == 0:
    print("el numero es par")

else:
    print("el numero es impar")
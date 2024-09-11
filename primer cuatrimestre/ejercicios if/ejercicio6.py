# Escribir un programa que pida al usuario dos números y devuelva su división. Si el usuario introduce el divisor cero debera imprimir un mensaje de error.

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

if numero2 == 0:
    print("No puede hacerse una division por cero")

else:
    division = numero1 / numero2
    print(f"el resultado de la division es {division}")


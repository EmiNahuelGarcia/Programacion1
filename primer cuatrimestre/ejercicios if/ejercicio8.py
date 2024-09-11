# Escribí un programa que solicite al usuario el ingreso de dos números diferentes y muestre en pantalla al mayor de los dos.
# Y si son iguales tambien mostrar por pantalla que son iguales.

numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))

if numero1 > numero2:
    print(f"El numero mayor es: {numero1}")
elif numero2 > numero1:
    print(f"El numero mayor es: {numero2}")
else:
    print("los numeros son iguales iguales.")

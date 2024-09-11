'''Ejercicio 9 Tenemos que crear un programa que deberá obtener el importe que ingrese el usuario por consola(input)
transformar en número y mostrar el importe actualizado con un descuento del 20% utilizando print.'''


importe = int(input("Ingrese el importe al que aplicara el descuento: "))
descuento = 20

importe_descuento = importe - (importe * descuento) /100


print(f"el importe total con el descuento de {descuento} % aplicado es de {importe_descuento}")
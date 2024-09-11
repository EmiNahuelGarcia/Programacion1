'''Ejercicio 10 Tenemos que crear un programa que deberán obtener el importe y el descuento que ingrese el usuario por consola
transformarlos en números y mostrar el importe actualizado con el descuento utilizando print.'''

importe = int(input("ingrese el importe: "))

descuento = int(input("ingrese el porcentaje de descuento que desea aplicar: "))

importe_con_descuento = importe - (importe * descuento) / 100

print(f"el importe final con el descuento del {descuento}% es de {importe_con_descuento}")


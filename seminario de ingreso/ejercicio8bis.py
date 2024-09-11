#Cree un programa que permite ingresar el nombre de un producto, el
#precio y que calcule el IVA.

nombre_producto=(input("ingrese nombre de su producto por favor: "))
precio_producto=float(input("ahora ingrese el valor del producto comprado: "))
porcentajeIVA= "21%"
IVA=float(precio_producto * 0.21)
valor_total= precio_producto + IVA
print("El IVA actual es", porcentajeIVA)
print("Su", nombre_producto,"tiene un IVA de",IVA)
print("El valor total de la compra es", valor_total)
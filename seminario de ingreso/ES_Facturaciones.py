#Enunciado:
#Para el departamento de facturación:
#A. Ingresar tres precios de productos y mostrar la suma de los mismos.



precio1=float(input("ingrese el valor del primer producto: "))
precio2=float(input("ingrese el valor del segundo producto: "))
precio3=float(input("ingrese el valor del tercer producto: "))
suma_total= precio1 + precio2 + precio3
print("el total de los productos es:", suma_total)
#B. Ingresar tres precios de productos y mostrar el promedio de los mismos.

precio1=float(input("ingrese el valor del primer producto: "))
precio2=float(input("ingrese el valor del segundo producto: "))
precio3=float(input("ingrese el valor del tercer producto: "))
suma_total= precio1 + precio2 + precio3
promedio_total= suma_total / 3
print("el promedio de los productos es:", promedio_total)
#C. ingresar tres precios de productos sumarlos y mostrar el precio final (más IVA 21%)

precio1=float(input("ingrese el valor del primer producto: "))
precio2=float(input("ingrese el valor del segundo producto: "))
precio3=float(input("ingrese el valor del tercer producto: "))
IVA_porcentaje= 0.21
suma_total= precio1 + precio2 + precio3
IVA= suma_total * IVA_porcentaje
precio_final= IVA + suma_total
print("Siendo IVA un 21% de",suma_total , "dando", IVA, ",el precio final es:", precio_final) #no se por que el % se pone de color

#estuve tentado a usar int en iva y precio final, porque con cuentas grandes tiene mala visibilidad tantos decimales
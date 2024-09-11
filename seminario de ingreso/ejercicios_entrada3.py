'''3) Escribe un programa que pida al usuario el total de una cuenta en un restaurante
y el porcentaje de propina que desea dejar. 
El programa debe calcular y mostrar la cantidad de propina y el total a pagar
antes y luego de la misma:
Precio: x
Propina: x
Precio con propina: x'''

cuenta = float(input("Ingrese el total de su cuenta: "))
porcentaje_propina = float(input("¿Cual es el porcentaje de propina que le gustaria dejar?: "))
propina = (cuenta * porcentaje_propina) / 100
total = cuenta + propina

mensaje = f'''
----------------------------------------------------
El total de la comida sin propina es {cuenta}
la propina que dejara es de {propina}.
El total de la cuenta con la propina es de {total}
----------------------------------------------------
'''

print(mensaje)
'''

Ejercicio 8

Tenemos que obtener los valores (por input) que el usuario nos ingrese (sueldo e incremento),

transformarlos en números enteros y mostrar el importe de sueldo actualizado con el
incremento porcentual utilizando print.
'''
sueldo = int(input("Cual es tu sueldo actualmente?: "))
incremento= int(input("Ingrese el porcentaje de incremento: "))
sueldo_aumentado = sueldo + (sueldo * incremento) / 100

print(f"su sueldo actualizado es {sueldo_aumentado}")
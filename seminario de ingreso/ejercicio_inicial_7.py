'''Ejercicio 7 Tenemos que obtener el sueldo (por input) que el usuario nos ingrese
transformarlo en número entero y mostrar el importe de sueldo actualizado con el incremento del 15% utilizando print.'''


sueldo = int(input("Ingrese su sueldo de este mes: "))
incremento = 0.15
sueldo_aumentado = sueldo + (sueldo * incremento)

print(sueldo_aumentado)
print(incremento)
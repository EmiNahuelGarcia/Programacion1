from os import system
system ("cls")
'''Tenemos que obtener los valores (por input) que el usuario nos ingrese (operador_a y operador_b)
transformarlos en números enteros, realizar la operación suma y luego mostrar el resultado de la misma utilizando print. 
Ej: "El resultado de la suma es: 755"'''

valor_a = int(input("Introduzca el primer valor de la suma: "))
valor_b = int(input("Introduzca el segundo valor de la suma: "))
suma = valor_a + valor_b

print("El resultado de su suma es:", suma)
'''Ejercicio 6 Tenemos que obtener los valores (por input) que el usuario nos ingrese (operador_a y operador_b), 
transformarlos en números enteros, realizar la operación que nos permita obtener el resto de una división
y luego mostrar el resultado de la misma utilizando print. 
Ej: "El resto de dividir 7 por 2 es: 1'''

operador_a = int(input("Ingrese el primer valor: "))
operador_b = int(input("Ingrese el segundo valor: "))
operacion = operador_a % operador_b

print(f"el resto de dividir {operador_a} por {operador_b} es {operacion}")
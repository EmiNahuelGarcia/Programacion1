'''Se deberá crear un programa que muestre cada operación (suma, resta, multiplicación, y división)
tenemos que obtener los valores (por input) que el usuario nos ingrese (operador_a y operador_b)
transformarlos en números enteros, realizar dicha operación y luego mostrar el resultado de la misma utilizando print
Ej: "El resultado de la …… es: 755"'''

operacion = input("¿que operacion desea realizar? suma, resta, multiplicacion, division: ")
operador_a = int(input("Introduzca el primer valor: "))
operador_b = int(input("Introduzca el segundo valor: "))

resultado = 0
if operacion == "suma":
    resultado = operador_a + operador_b
elif operacion == "resta":
    resultado = operador_a - operador_b
elif operacion == "multiplicacion":
    resultado = operador_a * operador_a
elif operacion == "division":
    resultado = operador_a / operador_b
else:
    print("opcion incorrecta, por favor, reintente")

print(f"El resultado de la operacion es {resultado}")
'''
Ejercicios Integradores Agencia de viaje: Para saber el costo de un viaje necesitamos el siguiente algoritmo
sabiendo que el precio por kilo de pasajero es 1000 pesos
Se ingresan todos los datos por PROMPT los datos a solicitar de dos personas son:
nombre, edad y peso Se pide armar el siguiente mensaje: "Hola jose y maria , sus pesos son 80 kilos y 60 kilos respectivamente, sumados da 140 kilos
el promedio de edad es 33 y su viaje vale 140000 pesos "
'''

precio_por_kilo = 1000
nombre_a = input("Ingrese el nombre del primer pasajero: ")
edad_a = int(input("Ingrese la edad del primer pasajero: "))
peso_a = int(input("Ingrese el peso del primer pasajero: "))

nombre_b = input("Ingrese el nombre del segundo pasajero: ")
edad_b = int(input("Ingrese la edad del segundo pasajero: "))
peso_b = int(input("Ingrese el peso del segundo pasajero: "))

suma_peso = peso_a + peso_b
promedio_edad = (edad_a + edad_b) / 2
valor_viaje = precio_por_kilo * suma_peso

print(f'''Hola {nombre_a} y {nombre_b}, sus pesos son {peso_a} kilos y {peso_b} kilos respectivamente, sumados da {suma_peso} kilos.
El promedio de edad es {promedio_edad} y su viaje vale {valor_viaje} pesos''')
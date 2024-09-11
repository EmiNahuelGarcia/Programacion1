# Crea una variable numérica y si esta entre 0 y 10, mostrar un mensaje indicándolo.

variable = int(input("Ingrese un numero del 0 al 10: "))

if variable > -1 and variable < 11:
    print("El numero esta entre 0 y 10")

else:
    print("No se encuentra entre el rango de numeros pedido")


# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y 
# quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. 
# El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. 
# Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 80 ARS y si es mayor de 18 años, 150 ARS.

edad = int(input("Ingrese su edad: "))
precio = 0

if edad > 18:
    precio = 150
    
elif edad > 3:
    precio = 80
    
else:
    precio = "gratis"

mensaje = f"el boleto sale {precio} ARS"

if precio == "gratis":
    mensaje = "los menores pasan gratis" 

print(mensaje)
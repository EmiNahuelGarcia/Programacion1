# Escribir una función a la que se le pase una cadena <nombre> y 
# muestre por pantalla el saludo ¡hola <nombre>!.
# Llamarla dos veces con diferentes cadenas (nombre) en cada llamada

def saludar(nombre: str) -> None:
    '''
    funcion para saludar al usuario
    acepta str y va a imprimir un saludo
    
    '''
    print(f"¡Hola {nombre}!")

for _ in range(2):
    
    nombre = input("Ingrese su nombre: ")
    saludar(nombre)
# Debe crear un programa que permita ingresar una edad (entre 1 y 99 años, validar mediante una funcion) 
# y un género (‘F’, ‘M’,  ‘X’, validar mediante una funcion). En caso de ingresar valores erróneos 
# (edad fuera de rango, o generos inexistentes), informar de esa situación mostrando un mensaje
#  y terminar el programa. Si todos los datos fueron bien ingresados, 
# el programa debe ser capas de indicar, sabiendo que las mujeres se jubilan a los 60 años o mas, 
# los hombres con 65 años o mas, para los no binarios establecemos un promedio de ambas edades.
# Determinar mediante funciones si una persona puede o no jubilarse.

EDAD_MINIMA = 1
EDAD_MAXIMA = 99
FEMENINO = "F"
MASCULINO = "M"
NO_BINARIO = "X"

def validar_edad(edad: int) -> None:
    
    if edad > EDAD_MAXIMA or edad < EDAD_MINIMA:
        return "edad invalida, debe ser entre 1 y 99 años"
    
    return None


def validar_genero(genero: str) -> None:
    if genero != FEMENINO and genero != MASCULINO and genero != NO_BINARIO:
        return "genero invalido, debe ser F, M o X"
    
    return None
    

def jubilar(edad: int, genero: str) -> str:
    edad_m = 65
    edad_f = 60
    edad_x = (edad_m + edad_f) / 2
    
    if genero == MASCULINO:
        if edad >= edad_m:
            return "usted puede jubilarse"
        else:
            return "usted no cumple con la edad minima"

    elif genero == FEMENINO:
        if edad >= edad_f:
            return "usted puede jubilarse"
        else:
            return "usted no cumple con la edad minima"

    else:
        if edad >= edad_x:
            return "usted puede jubilarse"
        else:
            return "usted no cumple con la edad minima"

edad = int(input("Ingrese su edad por favor: "))


error_edad = validar_edad(edad)

if error_edad:
    print(error_edad)
else:
    
    genero = input("Ingrese su género (F, M, X): ").upper()
    error_genero = validar_genero(genero)
    if error_genero:
        print(error_genero)
    else:
        
        mensaje = jubilar(edad, genero)
        print(mensaje)



    

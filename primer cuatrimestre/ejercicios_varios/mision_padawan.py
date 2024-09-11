'''
¡Atención, jovenes Padawan!

¿Están listos para un desafío épico? Este sábado, les proponemos una misión de código que pondrá a prueba sus habilidades.

Nuestra misión:
Crear un algoritmo en Python que imprima por pantalla si un año es bisiesto o no lo es.

Para esta misión nos proporcionan la siguiente ayuda:
El año es bisiesto si es divisible por 4 y no es divisible por 100 o es divisible por 400.

'''
def bisiesto(year:int)->bool:
    '''
    verifica si el año es bisiesto asegurandose
    que pueda dividirse por  4 o 400 y no por 100
    acepta parametros int y devuelve un bool

    '''
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

year = int(input("Ingrese el año a evaluar si es bisiesto: "))


if bisiesto(year):
    print(f"el año {year} es bisiesto")
else:
    print(f"el año {year} no es bisiesto")
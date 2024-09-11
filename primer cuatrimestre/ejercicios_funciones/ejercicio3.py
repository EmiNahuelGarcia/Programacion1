# Realiza una función llamada area_rectangulo() que devuelva 
# el área del rectángulo a partir de una base y una altura. 
# Calcula el área de un rectángulo de 15 de base y 10 de altura
# Ayuda: El área de un rectángulo se obtiene al multiplicar la base por la altura.

def area_rectangulo(base: float, altura: float) -> float:
    '''
    calcula el area de un rectangulo
    acepta parametros tipo float
    devuelve un float
    
    '''

    calculo = base * altura

    return calculo


base = 15

altura = 10

area = area_rectangulo(base, altura)

print(f"el area del rectangulo es {area}")

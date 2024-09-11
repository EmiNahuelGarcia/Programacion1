# Realiza una función llamada relacion() que a partir de dos números cumpla lo siguiente:

# Si el primer número es mayor que el segundo, debe devolver 1.
# Si el primer número es menor que el segundo, debe devolver -1.
# Si ambos números son iguales, debe devolver un 0.

# Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'

def relacion(num1: int, num2: int) ->int:
    '''
    Compara dos numeros.
    
    acepta dos parametros int
    
    devuelve un int
    1 si num1 es mayor que num2, -1 si num1 es menor que num2, y 0 si son iguales.
    '''
    
    if num1 == num2:
        return 0
    elif num1 > num2:
        return 1
    else:
        return -1
    

print(relacion(5, 10))

print(relacion(10, 5))

print(relacion(5, 5))
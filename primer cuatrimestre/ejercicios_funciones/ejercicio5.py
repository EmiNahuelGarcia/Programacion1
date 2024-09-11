# Realizar una función llamada par_o_impar:

# 1-Recibirá un número por parámetro
# 2-Imprimirá Par si el número es par
# 3-Imprimirá Impar si el número es impar
# 4-Si se ingresa algo que no sea número debe indicar 
# que se ingrese un número. (Para pensar un poco más)

def par_o_impar(num: int) -> None:
    '''
    funcion para evaluar si un numero es par
    acepta numeros int
    no retorna nada, imprime el resultado
    
    '''
    if num % 2 == 0:
        print("es par")
        
    else:
        print("es impar")


while True:
    try:

        num_evaluado = int(input("Ingrese un numero para ver si es par: "))

        par_o_impar(num_evaluado)
        
        break

    except ValueError:
        print("solo puede ingresar numeros")
        


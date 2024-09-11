# Escribe una función llamada calculadora que tome tres argumentos:
# dos números y un operador (+, -, *, /). La función debe realizar 
# la operación correspondiente y devolver el resultado.
# Deben tener en cuenta el error de la division por 0 y que no ocurra.

# Extra: se puede realizar un breve menu en donde el usuario puede
# seleccionar:
#  1. Utilizar calculador
#  2. Salir
# si el usuario no ingresa 1 o 2, mostrarle un mensaje que no es una
# opcion correcta.


def calculadora(num1:float,num2:float,operador:str) -> float:
    '''
    funcion que realiza operaciones matematicas simples entre dos numeros
    recibe dos argumentos float y un operador str para realizar la operacion matematica
    devuelve un float con el resultado de la operacion
    
    '''

    match operador:

        case "+":
            return num1 + num2
    
        case "-":
            return num1 - num2
    
        case "*":
            return num1 * num2
        
        case "/":
            if num2 == 0:
                return "syntax error"
            else:
                return num1 / num2
        case _:
            return "operador desconocido"
        


def sistema() -> None:
    '''
    Esta función presenta las opciones de uso
    
    cuando el usuario elige la primera opcion, se le solicita dos numeros y un operador
    luego llama a la funcion calculadora, realiza la operacion y muestra el resultado
    
    la funcion maneja posibles errores con valores no numericos y opciones erroneas
    no devuelve ningun valor, sigue ejecutandose hasta que el usuario elija salir
    
    '''

    while True:

        print("Bienvenido al calculador de emi: ")
        print("1. Utilizar calculador")
        print("2. Salir")

        eleccion = input("")

        match eleccion:
    
            case "1":
                try:
                    num1 = float(input("Ingrese el primer numero: "))

                    num2 = float(input("Ingrese el segundo numero: "))

                    operador = input("ingrese el operador: ")

                    print(calculadora(num1, num2, operador))

                except ValueError:
                    print("Error, solo puede operar con numeros")

            case "2":
                print("Gracias por usar")
                break

            case _:
                print("opcion erronea")

sistema()
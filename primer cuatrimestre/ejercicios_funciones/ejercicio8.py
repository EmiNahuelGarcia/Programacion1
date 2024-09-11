# Escribe una función llamada calculo_de_imc que reciba una altura y el peso
# e indique el indice de masa CORPORAL (IMC) de una persona.
# Peso inferior al normal	imc < de 18.5
# Normal imc entre 18.5 – 24.9
# Peso superior al normal  imc entre 25.0 – 29.9
# Obesidad	imc > de 30.0

def calculo_de_imc(peso: float, altura: float) -> float:
    imc = peso/(altura**2)
    if imc > 30.0:
        print("Perteneces al grupo de obesidad")
    elif imc > 25.0:
        print("Perteneces al grupo de peso superior al normal")
    elif imc > 18.5:
        print("Perteneces al grupo DE PESO NORMAL")
    else:
        print("Tenes un peso inferior al normal")

    return imc

                                
peso = float(input("Ingrese por favor su peso en kilogramos: "))

altura = float(input("Ingrese por favor su altura en metros: "))

imc = calculo_de_imc(peso,altura)

print(f"Su imc es {imc}")

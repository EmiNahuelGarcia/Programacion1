# Importar la librería de aleatoriedad random:
# import random # arriba de todo el código

# import random

# Hacer una función que se llame tirarLaMoneda y reciba como parámetro 
# un booleano llamado estaCargada.
import random


def tirar_la_moneda(estaCargada: bool):
    
    if estaCargada:
        resultado = "cara"
    
    else:

        resultado = random.choice(["cara", "cruz"])

    return resultado

estaCargada = True

#Por si la quiero hacer aleatoria luego de 10 veces
'''
for estaCargada in range(10):
    estaCargada = random.choice([True, False])
    print(estaCargada)

'''
    

print(tirar_la_moneda(estaCargada))


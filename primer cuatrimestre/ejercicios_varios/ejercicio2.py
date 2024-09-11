import os
os.system("cls")


# Dado un número n, verifica si es múltiplo de 3 y, 
# al mismo tiempo, si es mayor que 50. Muestra el 
# resultado de ambas comparaciones en una sola expresión.


n = 4

resultado = (n > 50) and (n % 3 == 0)

print(resultado)
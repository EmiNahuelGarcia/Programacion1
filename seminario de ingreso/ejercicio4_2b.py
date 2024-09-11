#4) Crear unprogramaquesolicite al usuario que ingrese una letra. 
# Se deberá validar que la letra sea ‘U’, ‘T’ o ‘N’ 
# (en mayusculas). Encaso nocoincidir con ninguna de las letras,
#  volver a solicitarla hasta que la condición se cumpla.

letra= input("Ingrese una letra en mayusculas entre UTN: ")

while letra != "U" and letra != "T" and letra != "N":
    letra= input("Error, ingrese nuevamente una letra en mayusculas entre UTN:  ")


print("gracias, su letra fue",letra)
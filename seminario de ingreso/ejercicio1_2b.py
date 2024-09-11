#Crear un programa que pueda sumar los números pares comprendidos entre el 1 y el 10.
suma_total_pares= 0
contador= 1

while contador <= 10:
    if contador % 2 == 0:
        suma_total_pares += contador
    
    contador+=1

print("la suma de pares es ", suma_total_pares)
        



#Crear unprogramaquesolicite 5 números mediante prompt. 
# Calcular la suma acumulada y el promedio de los números ingresados.

contador= 0
suma= 0
num= 0

while contador < 5:
    num= int(input("Ingrese un numero: "))
    suma += num
    contador +=1


promedio_Suma= suma / contador
print("la suma total es", int(suma),"\nel promedio total es", int(promedio_Suma))
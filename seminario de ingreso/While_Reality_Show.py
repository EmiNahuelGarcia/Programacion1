#Enunciado:

#De los 3 Jugadores de un Reality Show, se registra:
#nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibió en la etapa de votos
#Informar:
#a. nombre del candidato con más votos
#b. nombre y edad del candidato con menos votos
#c. el promedio de edades de los candidatos
#d. total de votos emitidos.
#Todos los datos se ingresan mediante input()

participantes = 0
max_votado = float('-inf') #participante mas votado
min_votado = float('inf') #participante menos votado
nombre_part_max = "" #nombre de participante mas votado
nombre_part_min = "" #nombre del participante menos votado
edad_min = 0 #edad del menos votado
suma_edad = 0
total_votos = 0



while participantes < 3:
    
    nombre = input("ingrese nombre del participante: ")
    
    edad = int(input("ingrese edad del participante, mayor de 25: "))
    while edad < 25:
        print("debe ser mayor de 25")
        edad = int(input("ingrese edad del participante, mayor de 25: "))
    
    suma_edad = suma_edad + edad 
    
    votos = int(input("ingrese cantidad de votos: "))
    while votos < 0:
        print("no puede haber voto negativo")
        votos = int(input("ingrese cantidad de votos: "))
    
    total_votos = total_votos + votos
    
    if votos > max_votado:
        max_votado = votos
        nombre_part_max = nombre
    
    elif votos < min_votado:
        min_votado = votos
        nombre_part_min = nombre
        edad_min = edad

    participantes += 1

promedio_edades= suma_edad / participantes

print("===========================================================================")
print("El participante con mas votos fue:",nombre_part_max) 
print("El participante con menos votos fue:",nombre_part_min ,"con",edad_min,"años")
print("El promedio de edad de los participantes es de:",promedio_edades)
print("El total de votos conseguidos entre los participantes fue:",total_votos)
print("===========================================================================")
'''

Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por input y los resultados por print 
'''

respuesta = "si"
flag = True
total_votos = 0
votos_total = 0
edades_total = 0
candidatos = 0

while respuesta == "si":
    nombre = input("Ingrese el nombre del candidato: ")
    
    edad = int(input("Ingrese la edad del candidato (mayor a 25): "))
    while edad < 26:
        edad = int(input("Edad erronea, reingrese: "))
    
    votos = int(input("Ingrese la cantidad de votos del candidato (no menor a cero): "))
    while votos < 0:
        votos = int(input("Votos incorrectos, reingrese: "))
    if flag == True:
        flag = False
        nombre_max = nombre
        votos_max = votos
        nombre_min = nombre
        votos_min = votos
        edad_min = edad
    
    if votos > votos_max:
            nombre_max = nombre
            votos_max = votos
    elif votos < votos_min:
            nombre_min = nombre
            edad_min = edad
            votos_min = votos 
    
    votos_total += votos
    edades_total += edad
    candidatos += 1
    respuesta = input("¿Desea ingresar otro candidato? (si/no): ")

promedio_edad = edades_total / candidatos
mensaje = f'''
el nombre del candidato con mas votos es {nombre_max} con {votos_max} votos
el candidato con menos votos es {nombre_min} de {edad_min} años, con {votos_min} votos
el promedio de las edades es de {promedio_edad}
el total de votos emitidos fue de {votos_total}
'''
print(mensaje)
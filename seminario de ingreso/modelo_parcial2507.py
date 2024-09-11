from os import system
system ("cls")
'''

La municipalidad de la ciudad está realizando un estudio de mercado para determinar cuál
será la nueva actividad recreativa que se difundirá. Las posibles actividades son las
siguientes: Clases de Yoga, Cine al Aire Libre, Taller de Pintura.
Para ello, se realizará una encuesta mediante un sistema de voto electrónico, con el
propósito de conocer cuáles son las preferencias de los encuestados (no se sabe cuántos):
Se ingresa de cada encuestado:
● Nombre
● Edad (no menor a 18)
● Está jubilado (si-no)
● Género (Masculino - Femenino - Otro)
● Voto (YOGA, CINE, PINTURA)
Se necesita saber:
1. Cantidad de encuestados no jubilados que votaron por CINE o PINTURA, cuya edad
esté entre 25 y 50 años inclusive.
2. Nombre y voto del encuestado de género Masculino con menor edad.
3. Porcentaje de votos de cada género.
4. Promedio de edad de los encuestados de género Femenino que votaron PINTURA.
5. Determinar cuál fue el género que tuvo más encuestados
'''

flag_menor_masculino = True
respuesta = "si"
contador_no_jubilado = 0
contador_voto_masculino = 0
contador_voto_femenino = 0
contador_voto_otro = 0
contador_f_pintura = 0
acumulador_f_pintura = 0
votos_total = 0
porcentaje_votos_m = 0
porcentaje_votos_f = 0
porcentaje_votos_o = 0
promedio_edad_fpintura = 0
nombre_m_minima = "no hay hombres"
voto_m_minima = "no hay hombres"

while respuesta == "si":
    nombre = input("Ingrese su nombre: ")
    
    edad = int(input("Ingrese su edad: "))
    while edad < 18:
        edad = int(input("Edad incorrecta,reingrese: "))
    
    jubilado = input("Esta jubilado: (si/no): ")
    while jubilado != "si" and jubilado != "no":
        jubilado = input("Opcion erronea, reingrese: ")
    
    genero = input("Ingrese su genero (masculino/femenino/otro): ")
    while genero != "masculino" and genero != "femenino" and genero != "otro": 
        genero = input("Opcion erronea, reingrese")

    voto = input("Voto yoga/cine/pintura: ")
    while voto != "yoga" and voto != "cine" and voto != "pintura":
        voto = input("Opcion erronea, reingrese: ")

    if jubilado == "no":
            if voto != "yoga" and edad < 56 and edad > 24:
                contador_no_jubilado += 1
    
    if genero == "masculino":
        if flag_menor_masculino == True:
            flag_menor_masculino = False
            edad_m_minima = edad
            nombre_m_minima = nombre
            voto_m_minima = voto

        elif edad < edad_m_minima:
            edad_m_minima = edad
            nombre_m_minima = nombre
            voto_m_minima = voto

        contador_voto_masculino += 1


    elif genero == "femenino":
        if voto == "pintura":
            contador_f_pintura += 1
            acumulador_f_pintura += edad
        
        contador_voto_femenino +=1
        
        
    else:
        contador_voto_otro +=1    

    votos_total += 1

    respuesta = input("Desea ingresar otro encuestado?: ")

if contador_voto_masculino > 0:
    porcentaje_votos_m = (contador_voto_masculino / votos_total) * 100

if contador_voto_femenino > 0:
    porcentaje_votos_f = (contador_voto_femenino / votos_total) * 100

if contador_voto_otro > 0:
    porcentaje_votos_o = (contador_voto_otro / votos_total) * 100

genero_mas_encuestado = "otro"

if contador_voto_masculino > contador_voto_femenino  and contador_voto_masculino > contador_voto_otro:
    genero_mas_encuestado = "masculino"

elif contador_voto_femenino > contador_voto_otro:
    genero_mas_encuestado = "femenino"



if contador_f_pintura > 0:
    promedio_edad_fpintura = acumulador_f_pintura / contador_f_pintura  



mensaje = \
f''' la cantidad de encuestados no jubilados entre 25 y 50 inclusive que votaron por cine o pintura fueron {contador_no_jubilado}
el masculino mas chico se llama {nombre_m_minima} y voto {voto_m_minima}
el porcentaje de votos de cada genero es masculino {porcentaje_votos_m}%, femenino {porcentaje_votos_f}% y otro {porcentaje_votos_o}%
el promedio de edad de los encuestados de genero femenino que votaron pintura fue {promedio_edad_fpintura}
el genero con mas encuestados fue {genero_mas_encuestado}
'''
#if nombre_m_minima == "-1"
        #print("no hay hombres")
print(mensaje)



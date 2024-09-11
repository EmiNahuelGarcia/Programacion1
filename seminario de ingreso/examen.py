respuesta = "si"
contador_m = 0
contador_f = 0
contador_f_ikea = 0
acumulador_f_ikea = 0
contador_o = 0
contador_general = 0
flag_m_menor = True
edad_m_menor = -1
contador_desempleados = 0


while respuesta == "si":

    nombre = input("Ingrese nombre: ")

    edad = int(input("Ingrese edad: "))
    while edad < 18:
        edad = int(input("Menor de edad, reingrese: "))

    empleado = input("Esta empleado (si/no): ")
    while empleado != "si" and empleado != "no":
        empleado = input("Opcion incorrecta, reingrese: ")

    genero = input("Ingrese genero (m/f/o): ")
    while genero != "m" and genero != "f" and genero != "o":
        genero = input("Opcion incorrecta, reingrese: ")

    voto = input("Ingrese voto (apple / dunkin / ikea): ")
    while voto != "apple" and voto != "dunkin" and voto != "ikea":
        voto = input("Opcion incorrecta, reingrese: ")

    if empleado != "si" and voto != "apple":

        if edad > 24 and edad <  51:
            contador_desempleados += 1


    if genero == "m":
        contador_m += 1

        if flag_m_menor == True:
            flag_m_menor = False
            nombre_m_menor = nombre
            voto_m_menor = voto
            edad_m_menor = edad

        elif edad < edad_m_menor:
            nombre_m_menor = nombre
            voto_m_menor = voto
            edad_m_menor = edad



    elif genero == "f":
        contador_f += 1

        if voto == "ikea":
            contador_f_ikea += 1
            acumulador_f_ikea += edad

    
    else:
        contador_o += 1


    contador_general += 1

    respuesta = input("Desea ingresar otro encuestado (si/no): ")

porcentaje_m = contador_m  * 100 / contador_general
porcentaje_f = contador_f  * 100 / contador_general
porcentaje_o = contador_o  * 100 / contador_general

genero_mas_voto = "otro"


if contador_m > contador_f and contador_m > contador_o:
    genero_mas_voto = "masculino"
    

elif contador_f > contador_o:
    genero_mas_voto = "femenino"


if contador_desempleados != 0:
    print(f"la cantidad de encuestados desempleado entre 25 y 50 años que votaron por DUNKIN o IKEA son {contador_desempleados}")
else:
    print("No se ingresaron hombres desempleados entre 25/50 años que votaron por DUNKIN o IKEA")

if edad_m_menor != -1:
    print(f"el nombre del masculino con menor edad es {nombre_m_menor} tiene {edad_m_menor} años y voto {voto_m_menor}")
else:
    print(f"no se ingresaron masculinos")


print(f"el porcentaje de hombres es {porcentaje_m}% de mujer {porcentaje_f}% y de otro genero {porcentaje_o}%")

if contador_f_ikea != 0:
    promedio_f_ikea = acumulador_f_ikea / contador_f_ikea
    print(f"Promedio de edad de los encuestados de género Femenino que votaron IKEA: {promedio_f_ikea} años")
else:
    print("No se ingresaron mujeres que votaron IKEA")
    
print(f"el genero que mas voto fue {genero_mas_voto} ")





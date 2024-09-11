'''
En el ingreso a un viaje en crucero nos solicitan 
nombre , 
edad(mayores de 18), 
sexo("f" o "m") y 
estado civil("soltero", "casado" o "viudo");
Se debe Informar al usuario lo siguiente:
a)El nombre del hombre casado más joven.
b)El sexo y nombre del pasajero/a más viejo.
c)La cantidad de mujeres que hay casadas o viudas.
d)El promedio de edad entre las mujeres.
e)El promedio de edad entre los hombres solteros.

'''

respuesta = "si"
flag_hombre_casado = True
flag_pasajero_viejo = True
acumulador_casadas = 0
acumulador_viudas = 0
acumulador_edad_mujer = 0
contador_mujer = 0
contador_hombre_soltero = 0
acum_edad_hombre_soltero = 0
nombre_casado_joven = "ninguno"


while respuesta == "si":
    nombre = input("Ingrese el nombre del pasajero: ")

    edad = int(input("Ingrese edad del pasajero: "))
    while edad < 19 or edad > 120:
        edad = int(input("Edad invalida, reingrese: "))

    sexo = input("Ingrese su sexo (f/m): ")
    while sexo != "f" and sexo != "m":
        sexo = input("Sexo invalido, reingrese: ")

    estado_civil = input("Ingrese su estado civil (soltero, casado o viudo): ")
    while estado_civil != "soltero" and estado_civil != "casado" and estado_civil != "viudo":
        estado_civil = input("estado civil invalido, reingrese: ")

    if sexo == "m":
        if estado_civil == "casado":
            if flag_hombre_casado == True:
                flag_hombre_casado = False
                edad_casado_joven = edad
                nombre_casado_joven = nombre
        
            if edad < edad_casado_joven:
                edad_casado_joven = edad
                nombre_casado_joven = nombre
        
        elif estado_civil == "soltero":
            acum_edad_hombre_soltero += edad
            contador_hombre_soltero += 1
    elif sexo == "f":
        acumulador_edad_mujer += edad
        if estado_civil == "casado":
            acumulador_casadas += 1
        elif estado_civil == "viudo":
            acumulador_viudas += 1

        contador_mujer += 1    

    if flag_pasajero_viejo == True:
        flag_pasajero_viejo = False
        edad_pasajero_viejo = edad
        sexo_pasajero_viejo = sexo
        nombre_pasajero_viejo = nombre

    if  edad > edad_pasajero_viejo:
        edad_pasajero_viejo = edad
        sexo_pasajero_viejo = sexo
        nombre_pasajero_viejo = nombre
        
    respuesta = input("Desea seguir ingresando personas? (si/no): ")

promedio_edad_mujeres = 0
if contador_mujer > 0:
    promedio_edad_mujeres = acumulador_edad_mujer / contador_mujer

promedio_edad_h_solteros = 0
if contador_hombre_soltero > 0:
    promedio_edad_h_solteros = acum_edad_hombre_soltero / contador_hombre_soltero


mensaje = f'''
el nombre del hombre casado mas joven es {nombre_casado_joven}
el pasajero/a mas grande se llama {nombre_pasajero_viejo} y es {sexo_pasajero_viejo}
la cantidad de mujeres casadas es {acumulador_casadas} y viudas {acumulador_viudas}
el promedio de edad entre mujeres es {promedio_edad_mujeres}
el promedio de edad entre hombres solteros es {promedio_edad_h_solteros}


'''
print(mensaje)



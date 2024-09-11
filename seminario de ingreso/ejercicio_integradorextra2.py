from os import system
system ("cls")


'''
Nos encargan el desarrollo de una aplicación que le permita a sus usuarios operar en la
bolsa de valores:
De los inversionistas, no se sabe cuántos, registrar:
● Nombre
● Monto en pesos de la operación (no menor a $10000)
● Cantidad de instrumentos
● Tipo (CEDEAR, BONOS, MEP)
Calcular e informar:
a. Tipo de instrumento que más se operó.
b. Cantidad de usuarios que compraron entre 150 y 200 BONOS y que invirtieron más
de $50000.
c. Nombre y cantidad de instrumentos del usuario que compró BONOS o MEP, que
menos dinero invirtió.
d. Porcentaje de usuarios que invirtieron en MEP, siempre y cuando el monto se
encuentre entre $20000 y $50000.


'''

respuesta = "si"
contador_cedear = 0
contador_bonos = 0
usuarios_bonos_50mil = 0
contador_mep = 0
flag_menor_inversion = True
usuarios_mep_porcentaje = 0
total_usuarios = 0
porcentaje_mep = 0



while respuesta == "si":
    nombre = input("Ingrese nombre: ")

    monto_pesos = int(input("Ingrese monto (no menor a 10.000): "))
    while monto_pesos < 10000:
        monto_pesos = int(input("Error, reingrese: "))

    cantidad_instrumentos = int(input("Cantidad de instrumentos: "))

    tipo = input("Ingrese tipo (cedear/bonos/mep): ")
    while tipo != "cedear" and tipo != "bonos" and tipo != "mep":
        tipo = input("Error, reingrese: ")


    if tipo == "cedear":
        contador_cedear += 1

    elif tipo == "bonos":
        contador_bonos += 1
        if cantidad_instrumentos > 150 and cantidad_instrumentos < 200 and monto_pesos > 50000:
            usuarios_bonos_50mil += 1

    else:
        contador_mep += 1
        if monto_pesos > 20000 and monto_pesos < 50000:
            usuarios_mep_porcentaje += 1



    if tipo != "cedear":
        if flag_menor_inversion == True:
            flag_menor_inversion = False
            monto_menor_inversion = monto_pesos
            cantidad_menor_inversion = cantidad_instrumentos
            nombre_menor_inversion = nombre

        elif monto_pesos < monto_menor_inversion:
            monto_menor_inversion = monto_pesos
            cantidad_menor_inversion = cantidad_instrumentos
            nombre_menor_inversion = nombre




        total_usuarios += 1


    respuesta = input("Desea ingresar otro usuario (si/no): ")

instrumento_mas_operado = "cedear"

if contador_bonos > contador_mep and contador_bonos > contador_cedear:
    instrumento_mas_operado = "bonos"

elif contador_mep > contador_cedear:
    instrumento_mas_operado = "mep"


porcentaje_mep = (usuarios_mep_porcentaje / total_usuarios) * 100 


print(f"Tipo de instrumento que más se operó: {instrumento_mas_operado}")
print(f"Cantidad de usuarios que compraron entre 150 y 200 BONOS y que invirtieron más de $50000: {usuarios_bonos_50mil}")
print(f"Nombre y cantidad de instrumentos del usuario que compró BONOS o MEP, que menos dinero invirtió: {nombre_menor_inversion}, {cantidad_menor_inversion}")
print(f"Porcentaje de usuarios que invirtieron en MEP entre $20000 y $50000: {porcentaje_mep}%")
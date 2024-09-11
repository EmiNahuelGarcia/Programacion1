from os import system
system ("cls")

'''
Una librería que se especializa en venta de libros importados desea calcular ciertas
métricas en base a las ventas de sus productos.
Se ingresa de cada venta:
Título del libro
Género: (Ciencia ficción - Drama - Terror)
Material del libro (rústica - tapa dura)
Importe (No pueden ser números negativos ni mayor a los 30000)
Se pide:
a) El libro más barato de drama con su importe.
b) Del libro más caro, el título.
c) Porcentaje de libros de cada género
d) La cantidad de libros que sean de ciencia ficción y cuesten menos de $700.

'''
respuesta = "SI"
flag_libro_drama_barato = True
flag_libro_mas_caro = True
libros_total = 0
contador_cf = 0
contador_cf_menor700 = 0
contador_drama = 0
contador_terror = 0
importe_drama_barato = 0

while respuesta == "SI":

    titulo_libro = input("Titulo del libro: ")

    genero_libro = input("Genero del libro (CF/DRAMA/TERROR): ")
    while genero_libro != "CF" and genero_libro != "DRAMA" and genero_libro != "TERROR":
        genero_libro = input("Invalido,ingrese nuevamente: ")

    material_libro = input("Material del libro (RUSTICA/TAPA DURA): ")
    while material_libro != "RUSTICA" and material_libro != "TAPA DURA":
        material_libro = input("Invalido,ingrese nuevamente: ")

    importe_libro = int(input("Importe del libro: "))
    while importe_libro < 1 or importe_libro > 30000:
        importe_libro = int(input("Invalido,ingrese nuevamente: "))

    
    if flag_libro_mas_caro == True:
        flag_libro_mas_caro = False
        importe_libro_caro = importe_libro
        titulo_libro_caro = titulo_libro

    elif importe_libro > importe_libro_caro:
        importe_libro_caro = importe_libro
        titulo_libro_caro = titulo_libro

    
    if genero_libro == "DRAMA":
        if flag_libro_drama_barato == True:
            flag_libro_drama_barato = False
            importe_drama_barato = importe_libro
            nombre_drama_barato = titulo_libro

        elif importe_libro < importe_drama_barato:
            importe_drama_barato = importe_libro
            nombre_drama_barato = titulo_libro
        
        contador_drama += 1


    elif genero_libro == "CF":
        if importe_libro < 700:
            contador_cf_menor700 += 1

        contador_cf += 1

    else:
        contador_terror += 1

    libros_total += 1

    respuesta = input("Desea introducir otro libro (SI/NO): ")

porcentaje_drama = contador_drama  * 100 / libros_total
porcentaje_cf = contador_cf  * 100 / libros_total
porcentaje_terror = contador_terror  * 100 / libros_total

if importe_drama_barato == 0:
    print(f"No se compraron libros de drama")

else:
    print(f"el libro mas barato de drama vale {importe_drama_barato} y se llama {nombre_drama_barato}")

print(\
f'''el libro mas caro vale {importe_libro_caro} y se llama {titulo_libro_caro}
el porcentaje de cada genero es DRAMA: {porcentaje_drama},CF: {porcentaje_cf} y TERROR: {porcentaje_terror}''')

if contador_cf_menor700 == 0:
    print(f"No se compraron libros de ciencia ficcion menores a 700")

else:
    print(f"la cantidad de libros de ciencia ficcion menor a 700 es {contador_cf_menor700}")




'''
a) El libro más barato de drama con su importe.
b) Del libro más caro, el título.
c) Porcentaje de libros de cada género
d) La cantidad de libros que sean de ciencia ficción y cuesten menos de $700.
'''
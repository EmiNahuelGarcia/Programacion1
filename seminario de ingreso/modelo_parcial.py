'''
Debemos realizar la carga de productos de prevención de contagio hasta que el usuario quiera, 
de cada una debo obtener los siguientes datos: 
el tipo (validar "barbijo" , "jabón" o "alcohol") , 
el precio (validar entre 100 y 300),
la cantidad de unidades (no puede ser 0 o negativo y no debe superar las 1000 unidades), 
la Marca y el fabricante. 
Se debe Informar al usuario lo siguiente:

a) Del más caro de los Barbijos, la cantidad de unidades y el fabricante
b) Del ítem con más unidades, el fabricante 
c) Cuántas unidades de jabones hay en total
d) Porcentaje de barbijos 
e) Cual fue el tipo de producto más comprado

'''

respuesta = "si"
acum_unidades_barbijo = 0
flag_unidades = True
flag_Barbijo = True
acum_unidades_jabon = 0
acum_unidades_alcohol = 0
acum_unidades_gral = 0

while (respuesta == "si"):
    tipo = input("tipo: ")
    while (tipo != "barbijo" and (tipo != "jabon" and tipo != "alcohol")):
        tipo = input("Invalido,ingrese nuevamente: ")
        
    precio = int(input("Precio: "))
    while precio < 100 or precio > 300:
        print("Invalido")
        precio = int(input("Ingrese nuevamente: "))

    unidades = int(input("Unidades: "))
    while unidades < 1 or unidades > 1000:
        unidades = int(input("Invalido: "))
    
    fabricante = input("Fabricante: ")
    marca = input("Marca: ")

    respuesta = input("Quiere ingresar otro producto? (si): ")

    if tipo == "barbijo":
        acum_unidades_barbijo += unidades
        if flag_barbijo == True:
            flag_barbijo = False
            barbijo_mas_caro_cantidad = unidades
            barbijo_mas_caro_fabricante = fabricante
            barbijo_mas_caro_precio = precio
        
        elif precio > barbijo_mas_caro_precio:
            barbijo_mas_caro_cantidad = unidades
            barbijo_mas_caro_fabricante = fabricante
            barbijo_mas_caro_precio = precio
    

    if flag_unidades == True:
        flag_unidades = False
        cant_max_unidades = unidades
        cant_max_unidades_fabri = fabricante
    
    if unidades > cant_max_unidades:
        cant_max_unidades = unidades
        cant_max_unidades_fabri = fabricante

    
    if tipo == "jabon":
        acum_unidades_jabon += unidades

    else:
        acum_unidades_alcohol += unidades

    acum_unidades_gral += unidades

tipo_producto_mas_comprado = "alcohol"

if acum_unidades_barbijo > acum_unidades_jabon and acum_unidades_barbijo > acum_unidades_alcohol:
    tipo_producto_mas_comprado = "barbijo"

elif acum_unidades_jabon > acum_unidades_alcohol:
    tipo_producto_mas_comprado = "jabon"


if acum_unidades_barbijo > 0:
    porcentaje_barbijos = (acum_unidades_barbijo / acum_unidades_gral) * 100
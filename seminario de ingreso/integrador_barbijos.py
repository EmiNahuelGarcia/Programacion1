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
flag_barbijo = True
barbijo_mas_caro_cantidad = 0
barbijo_mas_caro_fabricante = ""
barbijo_mas_caro_precio = 0
porcentaje_barbijos = 0
calculador_max_item = 0
acum_barbijos = 0
acum_jabon = 0
acum_alcohol = 0
acum_unidades_gral = 0
fabricante_item_mas_unidades = ""
tipo_producto_mas_comprado = ""
pregunta_si_no = "si"
flag_unidades = True



while pregunta_si_no == "si":
    tipo_producto = input("introduzca el tipo de producto (barbijo,jabon,alcohol): ")
    while tipo_producto != "barbijo" and tipo_producto != "jabon" and tipo_producto != "alcohol":
        tipo_producto = input("tipo invalido, ingrese nuevamente: ")
        
    precio_producto = int(input("Ingrese el precio del producto: "))
    while precio_producto < 100 or precio_producto > 300:
        precio_producto = int(input("Precio invalido, ingrese nuevamente: "))
        
    cantidad_producto = int(input("Ingrese la cantidad del producto: "))
    while cantidad_producto < 1 or cantidad_producto > 1000:
        cantidad_producto = int(input("Cantidad erronea, ingrese nuevamente: "))
    
    marca_producto = input("Ingrese la marca del producto: ")
    
    fabricante_producto = input("Ingrese el fabricante del producto: ")
    
    if (flag_unidades == True):
        flag_unidades = False

        cant_max_unidades = cantidad_producto
        cant_max_unidades_fabri = fabricante_producto
    if (cantidad_producto > cant_max_unidades):
        cant_max_unidades = cantidad_producto
        cant_max_unidades_fabri = fabricante_producto
    
    if tipo_producto == "barbijo":
        acum_barbijos += cantidad_producto
        if flag_barbijo == True:
            flag_barbijo = False
            barbijo_mas_caro_cantidad = cantidad_producto
            barbijo_mas_caro_fabricante = fabricante_producto
            barbijo_mas_caro_precio = precio_producto
            
        elif precio_producto > barbijo_mas_caro_precio:
            barbijo_mas_caro_cantidad = cantidad_producto
            barbijo_mas_caro_fabricante = fabricante_producto
            barbijo_mas_caro_precio = precio_producto
    
    elif tipo_producto == "jabon":
        acum_jabon += cantidad_producto
        
    
    else:
        acum_alcohol += cantidad_producto
        
        
        
        
        
    acum_unidades_gral += cantidad_producto
    
    pregunta_si_no = input("desea ingresar otro producto? (si/no): ")
    
tipo_producto_mas_comprado = "alcohol"

if acum_barbijos > acum_jabon and acum_barbijos > acum_alcohol:
    tipo_producto_mas_comprado = "barbijo"

elif acum_jabon > acum_alcohol:
    tipo_producto_mas_comprado = "jabon"
    
if acum_barbijos > 0:
    porcentaje_barbijos = (acum_barbijos / acum_unidades_gral) * 100
    
mensaje = \
f'''
del mas caro de los barbijos, la cantidad de unidades es {barbijo_mas_caro_cantidad} y el fabricante es {barbijo_mas_caro_fabricante}
del item con mas unidades su fabricante es {fabricante_item_mas_unidades}
el total de unidades de jabones es {acum_jabon}
el porcentaje total de barbijos es {porcentaje_barbijos}%
el tipo de producto mas comprado es {tipo_producto_mas_comprado}
'''
print(mensaje)
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
while respuesta == "si":
    nombre = input("Ingrese su nombre: ")

    respuesta = input("Desea ingresar otro nombre? si/no: ")
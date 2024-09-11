'''1) Una panadería vende barras de pan a 3.49$ cada una. El pan que no es el día tiene un descuento del 60%. 
Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se 
le hace por no ser fresca y el coste final total.'''

precio_pan = 3.49
descuento = 0.60

pan_duro_vendido = int(input("¿Cuantas barras de pan que no son del dia se vendieron?: "))



descuento_pan = precio_pan * descuento
precio_descuento = precio_pan - descuento_pan
importe_total = pan_duro_vendido * precio_descuento



mensaje = f'''
el precio habitual de cada barra de pan es {precio_pan}
el descuento es de {descuento_pan}
valiendo en total {importe_total}"
'''
print(mensaje)

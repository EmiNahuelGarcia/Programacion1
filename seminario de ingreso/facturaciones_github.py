'''

TP: ES_Facturaciones
---
Enunciado:
Para el departamento de facturación:
    A.	Ingresar tres precios de productos y mostrar la suma de los mismos.
    B.	Ingresar tres precios de productos y mostrar el promedio de los mismos.
	C.	ingresar tres precios de productos sumarlos y mostrar el precio final (más IVA 21%). 

'''

contador = 0 
suma = 0
iva = 0.21

while contador < 3:
    precio = float(input("Coloque el precio del producto: "))
    while precio < 0:
        precio = float(input("Precio incorrecto, ingrese nuevamente: "))
    suma += precio

    contador += 1
    
promedio = suma / contador
iva = suma * iva
precio_final_iva = suma + iva


mensaje = \
f'''la suma de los tres productos es {suma}
el promedio de los productos es de {promedio} 
el precio final de los productos mas el iva de 21% es {precio_final_iva}
'''
print(mensaje)

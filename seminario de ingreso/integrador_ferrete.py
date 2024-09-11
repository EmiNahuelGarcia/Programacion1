'''
Ferrete Lámparas


En una ferretería se quiere implementar un sistema que permita a los usuarios saber cuánto deberán pagar por la compra de lámparas de bajo consumo. Se tiene en cuenta que todas las lámparas cuestan $800.

A partir de la cantidad y marca de las lámparas compradas (solo se puede comprar una marca por vez) se aplicará el siguiente descuento:

Si compra 6 o más  lámparas bajo consumo tiene un descuento del 50%. 

Si compra 5  lámparas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.

Si compra 4  lámparas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.

Si compra 3  lámparas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.

Por otro lado, si el importe final con descuento suma más de $4000  se obtiene un descuento adicional de 5%.

Mostrar por pantalla: 

Marca, cantidad de lámparas, total a pagar sin descuento, el descuento obtenido si corresponde, el descuento adicional (si corresponde) y el total a pagar con descuento.
'''

valor_lamp = 800
descuento = 0
cant_lamp = int(input("cuantas lamparitas comprara?: "))
marca_lamp = input("que marca comprara? ArgentinaLuz,FelipeLamparas u otra?: ")

if cant_lamp > 5:
    descuento = 0.50
elif cant_lamp == 5:
    if marca_lamp == "ArgentinaLuz":
       descuento = 0.40
    else:
       descuento = 0.30
elif cant_lamp == 4:
    if marca_lamp == "ArgentinaLuz" or marca_lamp == "FelipeLamparas":
        descuento = 0.25
    else:
        descuento = 0.20
elif cant_lamp == 3:
    if marca_lamp == "ArgentinaLuz":
        descuento = 0.15
    elif marca_lamp == "FelipeLamparas":
        descuento = 0.10
    else:
        descuento = 0.05

total = cant_lamp * valor_lamp
importe_final = total - (total * descuento)
descuento_adicional = 0

if importe_final > 4000:
    descuento_adicional = importe_final * 0.10
    
importe_final_descuento_adicional = importe_final + descuento_adicional

mensaje = f'''
-----------------------------------------------------------------------
descuento adicional: {descuento_adicional}
Precio final sin descuento: {total}
Precio final con descuento: {importe_final}
Precio final con descuento + descuento extra: {importe_final_descuento_adicional}
Cantidad de lamparas compradas : {cant_lamp}
Marca de las lamparas : {marca_lamp}

-----------------------------------------------------------------------
'''
print(mensaje)
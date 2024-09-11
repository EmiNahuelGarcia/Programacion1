#FERRETE ILUMINACION

#Para el departamento de iluminación:
#Tomando en cuenta que todas las lámparas están en oferta al mismo precio de $35 pesos final.
#A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
#B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
#C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
#D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz" el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
#E.	Si el importe final con descuento suma más de $120  se debe sumar un 10% de ingresos brutos en informar del impuesto con el siguiente mensaje:

#Usted pago X de IIBB.”, siendo X el impuesto que se pagó.
#Precio final sin descuento: 
#Precio final con descuento: 
#Precio final con descuento + IIBB: 
#Cant lamparas compradas
#Marca de las lamparas


valor_lamp = 35
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
iibb = 0

if importe_final > 120:
    iibb = importe_final * 0.10
    
importe_final_iibb = importe_final + iibb

mensaje = f'''
-----------------------------------------------------------------------
Usted pago {iibb} de IIBB,
Precio final sin descuento: {total}
Precio final con descuento: {importe_final}
Precio final con descuento + IIBB: {importe_final_iibb}
Cantidad de lamparas compradas : {cant_lamp}
Marca de las lamparas : {marca_lamp}

-----------------------------------------------------------------------
'''
print(mensaje)





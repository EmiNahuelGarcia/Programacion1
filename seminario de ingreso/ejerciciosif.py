'''A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa 
deberá determinar la posición del jugador en la cancha, considerando los siguientes parametros:

Menos de 160 cm: Base
Entre 160 cm y 179 cm: Escolta
Entre 180 cm y 199 cm: Alero
200 cm o más: Ala-Pívot o Pívot'''

altura = int(input("Ingrese su altura en centimetros: "))

if (altura < 140 or altura > 230):
    print("altura no permitida")
elif (altura > 199):
    print("Tu posicion es Ala-pivot")
elif (altura > 179):
    print("Tu posicion es Alero")
elif (altura > 159):
    print("Tu posicion es Escolta")
else:
    print("Tu posicion es base")
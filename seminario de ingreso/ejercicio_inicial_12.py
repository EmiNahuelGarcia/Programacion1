'''
Empresa de Camiones: Para el departamento de logística: 
A. Es necesario saber la cantidad de camiones que harían falta para transportar los materiales que se utilizarán para la construcción de un edificio. 
Para ello, se ingresa la cantidad de toneladas necesarias de materiales a transportar. 
El programa deberá informar la cantidad de camiones, sabiendo que cada uno de ellos puede transportar por viaje 3500kg. 
B. Apartir del ingreso de la cantidad de kilómetros que tiene que recorrer estos camiones para llegar al destino de la obra
necesitamos que el programa informe cual es el tiempo (en horas) que tardará cada uno de los camiones
si sabemos que cada camión puede ir a una velocidad máxima y constante de 90 km/h.
'''

camion_capacidad_carga = 3500
materiales = int(input("Ingrese la cantidad de toneladas necesarias para la construccion (ej 1,2,3 toneladas): ")) * 1000
camiones_necesarios = (materiales + camion_capacidad_carga - 1) // camion_capacidad_carga
kilometros = float(input("Ingrese la cantidad de kilometros necesarios para llegar al destino:  "))
kilometros_por_hora = 90
tiempo_recorrido = kilometros / kilometros_por_hora

mensaje = f'''
la cantidad de camiones necesarios para transportar las {materiales} toneladas son {camiones_necesarios}
la cantidad de horas que tardaran los camiones en recorrer los {kilometros}km son {tiempo_recorrido} horas'''

print(mensaje)
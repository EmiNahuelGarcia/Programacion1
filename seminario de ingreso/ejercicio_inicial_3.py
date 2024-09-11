from os import system
system ("cls")
'''Se deberá obtener tanto el nombre como la edad usando input y luego mostrar los datos concatenados con print. 
Ej: "Usted se llama José y su edad es 66 años"'''


nombre = input("introduzca su nombre por favor: ") 
edad = int(input("Introduzca su edad por favor: "))

mensaje = f"su nombre es {nombre}, usted tiene {edad} años"

print(mensaje)
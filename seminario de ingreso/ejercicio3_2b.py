#Crear unprogramaquesolicite al usuario que ingrese un número. 
# Se deberá validar que se encuentre entre 0 y 9 inclusive. 
# En caso no coincidir con el rango, volverlo a solicitar hasta que la condición se cumpla.

num= int(input("Ingrese un numero entre 0 y 9: "))

while num < 0 or num > 9:
    print("ingrese nuevamente")
    num= int(input("Ingrese un numero entre 0 y 9: "))
    



print("el numero se encuentra validado, es", num)
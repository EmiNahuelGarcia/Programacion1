#Crear un programa que solicite al usuario que ingrese una contraseña mediante prompt. 
# Comprobar que la contraseña ingresada sea ‘utn750’. En caso de no coincidir
# volver a solicitarla hasta que coincidan.

password= input("ingrese su contraseña: ")


while password != "utn750":
    print("ERROR, ingrese nuevamente ")
    password= input("ingrese su contraseña: ")
    

print("Bienvenido usuario")
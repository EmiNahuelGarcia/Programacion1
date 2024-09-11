# Escribí un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje “Es vocal”. 

letra = input("Ingrese una letra vocal: ").lower()

if letra != "a" and letra != "e" and letra != "i" and letra != "o" and letra != "u":
    print("La letra no es una vocal")
else:
    print("La letra es una vocal")

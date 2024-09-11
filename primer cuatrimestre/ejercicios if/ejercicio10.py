# Dos equipos de futbol están disputando el saque inicial del juego. 
# Los capitanes de cada equipo deciden jugar el clásico juego "Piedra, papel o tijera" para definir quien hace el saque. 
# Las reglas son las usuales: Piedra vence a Tijera, Tijera vence a Papel y Papel vence a Piedra.
# Juegan una sola vez.

capitan1 = input("Ingrese su eleccion (piedra, papel, tijera): ").lower()
capitan2 = input("Ingrese su eleccion (piedra, papel, tijera): ").lower()

if capitan1 == capitan2:
    print("empate")

elif capitan1 == "piedra" and capitan2 == "tijera" or capitan1 == "papel" and capitan2 == "piedra" or capitan1 == "tijera" and capitan2 == "papel":
    print("El primer capitan gano")

else:
    print("el segundo capitan gano")
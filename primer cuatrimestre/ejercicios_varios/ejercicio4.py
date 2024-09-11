# Calcular el IMC de una persona
nombre = input("Ingrese su nombre: ")
peso = int(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
formula_imc = peso / (altura ** 2)

print(f"hola {nombre} su IMC es {formula_imc}")

if formula_imc > 34.9:
    print(f"{nombre} usted pertenece al grupo de obesidad grado 2")

elif formula_imc > 29.9:
    print(f"{nombre} usted pertenece al grupo de obesidad grado 1")

elif formula_imc > 24.9:
    print(f"{nombre} usted pertenece al grupo de sobrepeso")

elif formula_imc > 18.4:
    print(f"{nombre} usted pertenece al grupo de peso adecuado")

else:
    print(f"{nombre} usted pertenece al grupo de bajo peso")


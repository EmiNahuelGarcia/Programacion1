# Cree un programa que calcule el IMC (Indice de masa corporal). Formula --> IMC=Peso/Altura2 (Peso sobre altura al cuadrado)
# El usuario debera ingresar su peso y su altura (su nombre si quieren y despues imprimirlo concatenado) y el programa ademas de 
# calcular el IMC debera decir en que clasificacion se encuentra.
# La clasificacion la encontraran el archivo de imagen: IMC_clasificacion.jpg

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



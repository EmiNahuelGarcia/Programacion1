#Crear un programa que al ingresar un número puede calcular si es mayor,
#niño/a(menor de 10) o pre-adolescente (edad entre 10 y 13 años)
#adolescente (edad entre 13 y 17 años) de edad.

edad = int(input("Ingrese su edad: "))
if edad <= 0 and edad >= 101:
    print("La edad no es valida")
elif edad >= 18:
    print("Usted es mayor")
elif edad >= 13 and edad <= 17:
    print("Usted es adolescente")
elif edad >= 10 and edad <= 12:
    print("Usted es preadolescente")
else:
    print("Usted es un niño")

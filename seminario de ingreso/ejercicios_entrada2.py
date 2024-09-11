from os import system
system ("cls")
#2) Para el departamento de Pinturas:
#A.	Se ingresa una temperatura en Fahrenheit y la debemos mostrar en Centígrados con un mensaje concatenado 
        #(0 °F − 32) × 5/9 = -17,78 °C
#B.	Se ingresa una temperatura en Centígrados debemos mostrar la temperatura en Fahrenheit 
        #(0 °C × 9/5) + 32 = 32 °F

temp_f = float(input("Ingrese una temperatura en Fahrenheit: "))
temp_c = float(input("Ingrese una temperatura en Centigrados: "))


conv_a_centigrados = (temp_f - 32) * 5/9
conv_a_fahrenheit = (temp_c * 9/5) + 32

mensaje = f'''
el ingreso de la temperatura {temp_f} de grados Fahrenheit, convertido da un total de {conv_a_centigrados} grados Centigrados
la temperatura ingresada de {temp_c} de grados Centigrados, convertido da un total de {conv_a_fahrenheit} grados Fahrenheit
'''

print(mensaje)
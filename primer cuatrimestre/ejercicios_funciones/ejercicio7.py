# Escribe una función llamada celsius_a_fahrenheit que tome una temperatura 
# en grados Celsius como argumento y devuelva su equivalente en grados Fahrenheit.

def celsius_a_fahrenheit(celcius: float) ->float:
    convertir_c = (9/5 * celcius) + 32
    return convertir_c


celcius = float(input("Ingrese los grados celcius a convertir: "))

resultado = celsius_a_fahrenheit(celcius)

print(f"{celcius}° celcius convertido a fahrenheit es: {resultado}°")


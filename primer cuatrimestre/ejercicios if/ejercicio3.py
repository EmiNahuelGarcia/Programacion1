# Para pagar un determinado impuesto se debe ser mayor de 18 años y tener unos 
# ingresos iguales o superiores a 20000 ARS mensuales. Escribir un programa que pregunte 
# al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que pagar un impuesto o no.



edad = int(input("Ingrese su edad: "))

ingresos = int(input("Ingrese la cantidad mensual de ingresos: "))

if edad > 17 and ingresos > 19999:
    print("Usted debe pagar el impuesto")

else:
    print("Usted no debe pagar el impuesto")
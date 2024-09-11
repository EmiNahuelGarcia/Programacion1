# cree un programa que calcule el promedio de un alumno, ingresando su
#nombre apellido, 3 notas, que muestre al final las leyendas pertinentes

nombre_alumno=input("Ingrese nombre y apellido del alumno: ")
nota1=float(input("Ingrese la primera nota: "))
nota2=float(input("ingrese la segunda nota: "))
nota3=float(input("ingrese la tercera nota: "))
promedio_final=(nota1 + nota2 + nota3) / 3
print("Su nombre es: ",nombre_alumno)
print("El promedio de sus notas es: ", promedio_final)



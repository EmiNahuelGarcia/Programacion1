nombre=input("Ingrese su nombre completo: ")
num_comision=input("Ingrese a que comision pertenece: ")
asig=input("Ingrese asignatura perteneciente: ")
profesor=input("Ingrese nombre de su profesor: ")
presente=input("asistio a la clase (si o no): ")

mensaje = f"nombre del alumno es !" 

'''print("nombre del alumno: "+ nombre + ", su comision es " + num_comision)
print("Pertenece a la asignatura " + asig + ", cuyo profesor es " + profesor)
print("¿estuvo presente en la clase?: "+ presente)'''

print(f"nombre del alumno: {nombre}\nPertenece a la asignatura {asig}\
      \nestuvo presente en la clase? {presente} ")
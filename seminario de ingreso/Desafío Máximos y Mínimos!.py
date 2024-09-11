

contador=0
min_numero = float('inf')
max_numero= float('-inf')

while(contador<4):
    num = int(input("Ingrese un numero: "))

    if num < min_numero:
        min_numero = num
    
    if num > max_numero:
        max_numero= num
    


    contador+=1

print("ejecuciones: ",contador)
print("el valor min es: ", min_numero)
print("el valor max es: ", max_numero)
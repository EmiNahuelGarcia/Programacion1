'''La juguetería El MUNDO DE CHARLY nos encarga un programa para conocer qué cantidad de materiales se necesita para la fabricación de distintos juguetes.

CONFECCIÓN DE UN COMETA: 

Medidas:

AB = Diágonal mayor

DC = Diágonal menor

BD y BC = lados menores

AD y AC = lados mayores

El usuario ingresará las medidas  BC, CD y DA.

Detalles de construcción

Debemos tener en cuenta que la estructura del cometa estará dada 
por un perímetro de varillas de plástico y los correspondientes entrecruces (DC y AB) del mismo material para mantener la forma del cometa.
El cometa estará construido con papel de alta resistencia. La cola del mismo se construirá con el mismo papel que el cuerpo y representará un 10% adicional del necesario para el cuerpo.
Necesitamos saber cuántos Mts de varillas de plástico y cuántos de papel son necesarios para la construcción en masa de 10 cometas.
Tener en cuenta que los valores de entrada están expresados en Cms.
'''



diag_menor = float(input('Ingrese los centímetros de la diagonal menor: '))
lado_menor = float(input('Ingrese los centímetros del lado menor: '))
lado_mayor = float(input('Ingrese los centímetros del lado mayor: '))
dc = diag_menor
bc = lado_menor
da = lado_mayor


diag_mayor1 = (((lado_menor**2) - ((diag_menor / 2) ** 2)) ** 0.5)
diag_mayor2 = (((lado_mayor ** 2) - ((diag_menor / 2) ** 2)) ** 0.5)
diag_mayor = diag_mayor1 + diag_mayor2

varillas = ((lado_menor * 2) + (lado_mayor * 2) + diag_menor + diag_mayor) / 100

cometa1 = (diag_mayor1 * (diag_menor / 2)) + (diag_mayor2 * (diag_menor / 2))
papel_cola = cometa1 * 0.1

varillas10 = varillas * 10 
total_papel = (cometa1 + papel_cola) * 10 / 10000 

print(f"Se requeriran {varillas10} mts. de varillas y {total_papel} mts. cuadrados de papel")
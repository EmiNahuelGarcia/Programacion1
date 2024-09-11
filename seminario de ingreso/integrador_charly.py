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
cd = diag_menor
bc = lado_menor
da = lado_mayor


diag_mayor1 = (lado_menor ** 2 + (diag_menor / 2) ** 2 ) ** 0.5
diag_mayor2 = (lado_mayor ** 2 + (diag_menor / 2) ** 2 ) ** 0.5
diag_mayor = diag_mayor1 + diag_mayor2

perimetro = 2 * (lado_menor + lado_mayor) + diag_menor + diag_mayor

area_cometa = (diag_mayor * diag_menor) / 2

papel_cola = area_cometa * 0.10

varillas = perimetro / 100
varillas_total = varillas * 10

papel_por_cometa = (area_cometa + papel_cola) / 10000 
total_papel = papel_por_cometa * 10

print(f'''
Se requerirán en total {varillas_total:} metros de varillas de plastico
asi como se requerida un total de {total_papel:} metros cuadrados de papel para todos los 10 cometas''')











'''perimetro barillas= todos los lados del cometa
barillas del centro = dc y ab
cola del cometa = 10% adicional del papel del cuerpo
metros de varilla de plastico
metros de papel
cometas = 10'''
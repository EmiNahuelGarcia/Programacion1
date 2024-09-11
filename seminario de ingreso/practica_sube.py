colectivo=300
tren=320
subte=650

total_dia= colectivo+tren+subte

print(total_dia)

total_mes= total_dia * 44

print("sin descuentos "+ str(total_mes))

desc_trenIDA= 160
desc_subteIDA= 162.5

total_diadesc= colectivo + desc_trenIDA + desc_subteIDA
print(" con descuentos viaje por ida es ", total_diadesc )

desc_trenVuelta= 160
desc_coleVuelta= 75

total_diadescvuelta= subte + desc_trenVuelta + desc_coleVuelta
print("total en el dia con descuentos en la vuelta es", total_diadescvuelta )
total_mesdescIDA= total_diadesc * 22
total_mesVUELTA= total_diadescvuelta * 22
totalultimo= total_mesdescIDA + total_mesVUELTA

print(" gastas en sube al mes ", totalultimo)
print(" ta re quebrada la argentina guacho")


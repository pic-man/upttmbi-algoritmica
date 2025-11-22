#Tienes ventas mensuales del año
#Encuentra que mes tuvo las ventas mas altas
#Cual fue su posicion en el año 
#Calcula el promedio de ventas anual
#<>
ventas = [1200,1500,980,2100,1800,1650,2300,1900,1750,2000,2200,2500]
meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
comparacion = 0
indice = 0

for venta in ventas:
    if ventas[ventas.index(venta)] >= comparacion:
        comparacion = venta

print(f'El mes con mas ventas fue: {meses[(ventas.index(comparacion))]}, ventas del mes: {comparacion}')
indice = ventas.index(comparacion) +1

print(f'Posicion del año: {indice}')

promedio = (sum(ventas))/len(ventas)

print(f'El promedio de ventas anual fue:{promedio}')
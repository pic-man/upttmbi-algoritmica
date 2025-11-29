'''
Ejercicio 15: ANÁLISIS DE VENTAS
Estudiante: Eva Sofia Linares Medina
GitHub: @evalinaresm25-wq
Fecha: 2025-11-26

Descripción:
Encuentra el mes con más ventas, su posición y el promedio anual.

Métodos usados:
- max()
- index()
- sum()
- len()
'''
ventas = [1200, 1500, 980, 2100, 1800, 1650, 2300, 1900, 1750, 2000, 2200, 2500]
meses = ["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"]

max_venta = max(ventas)
mes_max = meses[ventas.index(max_venta)]
promedio = sum(ventas) / len(ventas)

print("Mes con más ventas:", mes_max)
print("Promedio anual:", promedio)

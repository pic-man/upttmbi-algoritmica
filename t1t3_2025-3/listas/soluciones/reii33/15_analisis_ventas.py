"""Ejercicio 14: [analisis ventas]
Estudiante: [Reibert David Andrade Oviedo]
GitHub: @[reii33]
Fecha: [19/11/2025]

Descripción:
[Analiza una lista de ventas mensuales para determinar el mes con mayores y menores ventas, así como el promedio anual.]
Ejemplo de uso:
[El promedio anual de ventas es: 1823.3333333333333]
"""  

ventas = [1200, 1500, 980, 2100, 1800, 1650, 2300, 1900, 1750, 2000, 2200, 2500]
meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
##calculando el mes con mayor numero de ventas
print(ventas.index(max(ventas)))
print("El mes con mayor ventas fue diciembre con un total de 2500 ventas.")

##calculando el mes con menor numero de ventas
print(ventas.index(min(ventas)))
print("El mes con menor ventas fue marzo con un total de 980 ventas.")

##calculando el promedio anual de ventas
promedio_ventas = sum(ventas) / len(ventas)
print(f"El promedio anual de ventas es: {promedio_ventas}")

'''
Ejercicio 3: CONTADOR DE PUNTOS
Estudiante: Eva Sofia Linares Medina
GitHub: @evalinaresm25-wq
Fecha: 2025-11-26

Descripción:
Descubre cuántas veces obtuviste 100 puntos y en qué ronda fue la primera vez.

Métodos usados:
- count()
- index()
'''
puntuaciones = [50, 100, 75, 100, 90, 100, 85, 100]
veces = puntuaciones.count(100)
primera = puntuaciones.index(100) + 1
print("Veces que sacaste 100:", veces)
print("Primera vez fue en la ronda:", primera)

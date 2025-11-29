'''
Ejercicio 6: RANKING DE JUGADORES
Estudiante: Eva Sofia Linares Medina
GitHub: @evalinaresm25-wq
Fecha: 2025-11-26

Descripción:
Ordena los puntajes de mayor a menor y muestra los tres primeros.

Métodos usados:
- sort()
'''
puntajes = [450, 890, 320, 670, 1200, 550, 890]
puntajes.sort(reverse=True)
print("Top 3:", puntajes[:3])

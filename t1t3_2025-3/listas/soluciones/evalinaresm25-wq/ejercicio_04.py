'''
Ejercicio 4: INVERSIÓN TEMPORAL
Estudiante: Eva Sofia Linares Medina
GitHub: @evalinaresm25-wq
Fecha: 2025-11-26

Descripción:
Muestra los eventos del más reciente al más antiguo y crea una copia para otra línea temporal.

Métodos usados:
- list()
- reversed()
- copy()
'''
eventos = ["Nacimiento", "Escuela", "Universidad", "Trabajo", "Jubilación"]
eventos_invertidos = list(reversed(eventos))
linea_alternativa = eventos_invertidos.copy()
print(eventos_invertidos)
print(linea_alternativa)

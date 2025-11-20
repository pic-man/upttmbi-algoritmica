"""Ejercicio 09: [Dados]
Estudiante: [Reibert David Andrade Oviedo]
GitHub: @[reii33]
Fecha: [20/11/2025]

Descripción:
[Simula el lanzamiento de un dado de seis caras 20 veces y cuenta cuántas veces aparece cada cara.]
Ejemplo de uso:
[Lanzamientos: [3, 5, 2, 6, 1, 4, 3, 2, 5, 6, 1, 4, 2, 3, 5, 6, 1, 4, 2, 3]
"""  
import random
lanzamientos = [random.randint(1, 6) for _ in range(20)]

from collections import Counter
conteo = Counter(lanzamientos)

print(f"Lanzamientos:{lanzamientos}")
for cara in range(1, 7):
    print(f"{cara}: {conteo.get(cara, 0)} veces")
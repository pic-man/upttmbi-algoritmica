'''
Ejercicio 9: JUEGO DE DADOS
Estudiante: Eva Sofia Linares Medina
GitHub: @evalinaresm25-wq
Fecha: 2025-11-26

Descripción:
Simula 20 lanzamientos de dados y muestra cuántas veces salió cada número.

Métodos usados:
- random.randint()
- count()
'''
import random

lanzamientos = [random.randint(1, 6) for _ in range(20)]
for numero in range(1, 7):
    print(numero, "salió", lanzamientos.count(numero), "veces")

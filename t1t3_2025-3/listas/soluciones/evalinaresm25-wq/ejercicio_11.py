'''
Ejercicio 11: LIMPIEZA DE LISTA
Estudiante: Eva Sofia Linares Medina
GitHub: @evalinaresm25-wq
Fecha: 2025-11-26

Descripción:
Crea una versión limpia sin duplicados ni valores None.

Métodos usados:
- list()
- set()
'''
lista_sucia = [1, 2, None, 3, 2, 4, None, 1, 5, 3]
lista_limpia = list(set([x for x in lista_sucia if x is not None]))
print("Lista limpia:", lista_limpia)

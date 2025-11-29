'''
Ejercicio 10: CINE NOSTÁLGICO
Estudiante: Eva Sofia Linares Medina
GitHub: @evalinaresm25-wq
Fecha: 2025-11-26

Descripción:
Ordena películas por año y elimina las tres más antiguas una por una.

Métodos usados:
- sort()
- pop()
'''
peliculas = [
    ("Matrix", 1999),
    ("Inception", 2010),
    ("Titanic", 1997),
    ("Avatar", 2009)
]

peliculas.sort(key=lambda x: x[1])
for _ in range(3):
    vista = peliculas.pop(0)
    print("Has visto:", vista[0])
print("Películas restantes:", peliculas)

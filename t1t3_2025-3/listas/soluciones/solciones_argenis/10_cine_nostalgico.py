"""Ejercicio 10: [cine nostalgico]
Estudiante: [Reibert David Andrade Oviedo]
GitHub: @[reii33]
Fecha: [20/11/2025]

Descripción:
[Gestiona una lista de películas clásicas, permitiendo agregar, eliminar y mostrar películas en orden cronológico.]
Ejemplo de uso:
[Peliculas en orden cronologico[('Titanic', 1997), ('Matrix', 1999), ('Avatar', 2009), ('Inception', 2010)]
"""  
peliculas = [
    ("Matrix", 1999),
    ("Inception", 2010),
    ("Titanic", 1997),
    ("Avatar", 2009)
]

#ordenando por orden cronologico
peliculas_ordenadas = sorted(peliculas, key=lambda x: x[1])

print(f'Peliculas en orden cronologico{peliculas_ordenadas}')

#eliminando las tres mas viejas una por una
peliculas_ordenadas.pop(0)
peliculas_ordenadas.pop(0)
peliculas_ordenadas.pop(0)


print(f'Eliminando las tres mas viejas {peliculas_ordenadas}')
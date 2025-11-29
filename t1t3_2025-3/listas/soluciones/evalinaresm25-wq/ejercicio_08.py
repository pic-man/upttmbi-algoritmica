'''
Ejercicio 8: BIBLIOTECA PERSONAL
Estudiante: Eva Sofia Linares Medina
GitHub: @evalinaresm25-wq
Fecha: 2025-11-26

Descripción:
Organiza la lista de libros del más corto al más largo.

Métodos usados:
- sorted()
'''
libros = [
    {"titulo": "El Hobbit", "paginas": 310},
    {"titulo": "1984", "paginas": 328},
    {"titulo": "El Principito", "paginas": 96}
]

libros_ordenados = sorted(libros, key=lambda x: x["paginas"])
for libro in libros_ordenados:
    print(libro["titulo"], "-", libro["paginas"], "páginas")

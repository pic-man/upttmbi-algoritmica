"""Ejercicio 08: [ Biblioteca personal]
Estudiante: [Reibert David Andrade Oviedo]
GitHub: @[reii33]
Fecha: [20/11/2025]

Descripción:
[Crea una lista de libros con su título y número de páginas, y ordénalos por número de páginas]
Ejemplo de uso:
[   Se muestra la lista de libros ordenada por número de páginas]
""" 
#Organiza una lista de libros por número de páginas, del más corto al más largo.

libros = [
    {"titulo": "El Hobbit", "paginas": 310},
    {"titulo": "1984", "paginas": 328},
    {"titulo": "El Principito", "paginas": 96}
]


##Ordenando libros

libros_ordenados = sorted(libros, key=lambda x: x['paginas'])
print("Libros ordenados por páginas de menor a mayor:")
for libro in libros_ordenados:
    print(f"{libro['titulo']}: {libro['paginas']} páginas")
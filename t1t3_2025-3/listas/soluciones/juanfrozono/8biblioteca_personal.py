#Organiza una lista de libros por numero de paginas
#Del mas corto al mas largo
#Los libros tienen titulo y cantidad de paginas

libros = [
    {"titulo":"El Hobbit","paginas": 310},
    {"titulo": "1984","paginas":328},
    {"titulo": "El Principito","paginas":96}
]
print("Mi biblioteca personal ")

libros_ordenados = sorted(libros, key=lambda libro:  libro["paginas"])
print("Biblioteca Desordenada: ")
for libro in libros:
    print(f'{libro["titulo"]} - {libro["paginas"]} paginas')
print("-"*50)
print("Ordenando paginas...")
print("-"*50)
print("Biblioteca Ordenada:")

for libro in libros_ordenados:
    print(f'{libro["titulo"]} - {libro["paginas"]} paginas')

print("-"*50)
Media = sum(libro["paginas"]for libro in libros) / len(libros)

print("Estadisticas: ")
libro_largo = libros_ordenados[-1]
libro_corto = libros_ordenados[0]
print(f'Libro mas corto:{libro_corto["titulo"]}:{libro_corto["paginas"]} paginas')
print(f'Libro mas largo:{libro_largo["titulo"]}:{libro_largo["paginas"]} paginas') 
print(f'el promedio es: {Media}')   


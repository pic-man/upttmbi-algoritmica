'''
Ejercicio 12: PALETA DE COLORES
Estudiante: Eva Sofia Linares Medina
GitHub: @evalinaresm25-wq
Fecha: 2025-11-26

Descripción:
Agrega blanco y negro a la lista, crea una versión invertida y retorna ambas.

Métodos usados:
- insert()
- append()
- list()
- reversed()
'''
def paleta(colores):
    colores.insert(0, "blanco")
    colores.append("negro")
    invertida = list(reversed(colores))
    return colores, invertida

colores = ["rojo", "verde", "azul", "amarillo"]
original, invertida = paleta(colores)
print(original)
print(invertida)

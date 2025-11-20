"""Ejercicio 12: [paleta colores]
Estudiante: [Reibert David Andrade Oviedo]
GitHub: @[reii33]
Fecha: [19/11/2025]

Descripción:
[Gestiona una lista de colores, permitiendo agregar, eliminar y mostrar la lista en orden inverso.]
Ejemplo de uso:
[Lista original: ['rojo', 'verde', 'azul', 'amarillo']
"""  

colores = ["rojo", "verde", "azul", "amarillo"]

def procesar_colores(colores):
    ##modificando colores
    colores_modificados = colores.copy()
    colores_modificados.insert(0, "blanco")
    colores_modificados.append("negro")
    ##inviertiendo colores
    colores_invertidos = colores_modificados[::-1]
    return colores_modificados, colores_invertidos


modificados, invertidos = procesar_colores(colores)

# Mostrar resultados
print("Lista original:", colores)
print("Lista modificada:", modificados)
print("Lista invertida:", invertidos)
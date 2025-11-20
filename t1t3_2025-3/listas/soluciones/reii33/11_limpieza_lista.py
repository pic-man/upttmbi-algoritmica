"""Ejercicio 11: [limpieza lista]
Estudiante: [Reibert David Andrade Oviedo]
GitHub: @[reii33]
Fecha: [19/11/2025]

Descripción:
[Limpia una lista de elementos eliminando duplicados y valores nulos.]
Ejemplo de uso:
[lista original[1, 2, None, 3, 2, 4, None, 1, 5, 3]
"""  

elementos = [1, 2, None, 3, 2, 4, None, 1, 5, 3]

print(f'lista original{elementos}')
print('duplicados detectados:1, 2, 3, None')

#Eliminando duplicados

dulplicados_eliminados = set(elementos)

print(f'duplicados eliminados {dulplicados_eliminados}')
"""Ejercicio 03: [Contador de puntuaciones]
Estudiante: [Reibert David Andrade Oviedo]
GitHub: @[reii33]
Fecha: [19/11/2025]

Descripción:
[Piezzeria que permite agregar y eliminar ingredientes de una lista]

Ejemplo de uso:
[obtuviste 100 puntos X veces]
"""  
# Lista de puntuaciones
puntuaciones = [85, 100, 76, 100, 92, 100, 88, 100, 95]

# 1. Contar cuántas veces obtuviste 100 puntos
veces100 = puntuaciones.count(100)

# 2. Encontrar en qué ronda fue la primera vez
primeraVez = None
for i, puntuacion in enumerate(puntuaciones, start=1):
    if puntuacion == 100:
        primera_vez = i
        break
# Mostrar resultados
print(f"Obtuviste 100 puntos {veces100} veces")
if primera_vez:
    print(f"La primera vez fue en la ronda {primeraVez}")
else:
    print("Nunca obtuviste 100 puntos")
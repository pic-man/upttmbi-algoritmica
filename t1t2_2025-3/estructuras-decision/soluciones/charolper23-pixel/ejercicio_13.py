"""
Ejercicio 13: Clasificación de Videojuego
Determina la clasificación ESRB según la edad del jugador.
"""

# Solicitar la edad del jugador
edad = int(input("Ingresa tu edad: "))

if edad < 0:
    print( "Edad no válida")
if edad < 7:
    print("Clasificación recomendada: E (Everyone)")
elif edad < 13:
    print("Clasificación recomendada: E10+ (Everyone 10+)")
elif edad < 17:
    print("Clasificación recomendada: T (Teen)")
elif edad >= 18 and edad <= 120:
    print("Clasificación recomendada: M (Mature)")
else:
    print("Edad no válida")
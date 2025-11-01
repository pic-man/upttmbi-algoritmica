"""
Ejercicio 9: Entrada al Parque
Determina si una persona puede subir a una atracción según su estatura.
"""

# Solicitar la estatura al usuario
estatura = int(input("Ingresa tu estatura en centímetros: "))

# Determinar si puede subir a la atracción
if estatura < 0:
    print("Lo siento, la estatura no puede ser negativa")
elif estatura < 120:
    print("Lo siento, no puedes subir a la atracción")
elif estatura > 200:
    print("Lo siento, eres demasiado alto para esta atracción")
else:
    print("¡Puedes subir a la atracción!")

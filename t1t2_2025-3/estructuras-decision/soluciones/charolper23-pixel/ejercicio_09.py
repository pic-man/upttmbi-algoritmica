"""
Ejercicio 9: Entrada al Parque
Estudiante: Yudith Perdomo
GitHub: @charolper23-pixel
Fecha: 29-10-2025

Descripción:
Determina si una persona puede subir a una atracción según su estatura.

Ejemplo de uso:
Entrada: 120
Salida: ¡Puedes subir a la atracción!
"""

# Solicitar la estatura al usuario
estatura = int(input("Ingresa tu estatura en centímetros: "))

# Determinar si puede subir a la atracción
if estatura < 0:
    print("Lo siento, la estatura no puede ser negativa")
elif estatura < 120:
    print("Lo siento, no puedes subir a la atracción")
elif estatura > 240:
    print("Lo siento, eres demasiado alto para esta atracción")
else:
    print("¡Puedes subir a la atracción!")

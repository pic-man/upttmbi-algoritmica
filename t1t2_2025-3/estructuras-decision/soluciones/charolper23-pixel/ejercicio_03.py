"""
Ejercicio 3: Aprobado o Reprobado
Determina si un estudiante aprobó o reprobó según su calificación.
"""

# Solicitar la calificación al usuario
calificacion = float(input("Ingresa tu calificación (0-10): "))

# Verificar si la calificación es válida
if calificacion < 0 or calificacion > 10:
    print("Calificación no válida. Debe estar entre 0 y 10.")
else:
    # Determinar si aprobó o reprobó, siendo 6 la calificacion minima para aprobar
    if calificacion >= 6:
        print("Aprobado")
    else:
        print("Reprobado")
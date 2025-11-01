"""
Ejercicio 6: Turno de Trabajo
Estudiante: Yudith Perdomo
GitHub: @charolper23-pixel
Fecha: 28-10-2025

Descripción:
Determina el turno de trabajo según la hora ingresada.

Ejemplo de uso:
Entrada: 23
Salida: Turno nocturno
"""

# Solicitar la hora al usuario
hora = int(input("Ingresa la hora (0-23): "))

# Determinar el turno según la hora
if 6 <= hora <= 13:
    print("Turno matutino")
elif 14 <= hora <= 21:
    print("Turno vespertino")
elif 22 <= hora <= 23 or 0 <= hora <= 5:
    print("Turno nocturno")
else:
    print("Hora no válida. Debe estar entre 0 y 23.")
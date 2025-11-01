"""
Ejercicio 8: Fiebre o No
Estudiante: Yudith Perdomo
GitHub: @charolper23-pixel
Fecha: 29-10-2025

Descripción:
Determina si una persona tiene fiebre, hipotermia o temperatura normal.

Ejemplo de uso:
Entrada: 35
Salida: tienes hipotermia
"""

# Solicitar la temperatura corporal al usuario
temperatura = float(input("Ingresa la temperatura corporal en grados Celsius: "))

# Clasificar la temperatura corporal
if temperatura < 36.0:
    print("Tienes hipotermia")
elif temperatura <= 37.5:
    print("Tu temperatura es normal")
else:
    print("Tienes fiebre")
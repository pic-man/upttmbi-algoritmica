"""
Ejercicio 8: Fiebre o No
Determina si una persona tiene fiebre, hipotermia o temperatura normal.
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
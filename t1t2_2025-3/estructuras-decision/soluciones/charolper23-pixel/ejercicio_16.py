"""
Ejercicio 16: Necesitas Paraguas
Estudiante: Yudith Perdomo
GitHub: @charolper23-pixel
Fecha: 01-11-2025

Descripción:
Determina si se necesita un paraguas según la probabilidad de lluvia.

Ejemplo de uso:
Entrada: 70
Salida: Lleva paraguas por si acaso
"""

# Solicitar el porcentaje de probabilidad de lluvia
try:
    probabilidad = float(input("Ingresa el porcentaje de probabilidad de lluvia (0-100): "))
    
    # Validar que el porcentaje esté en el rango correcto
    if probabilidad < 0 or probabilidad > 100:
        print("Error: El porcentaje debe estar entre 0 y 100")
    # Recomendar según el porcentaje de probabilidad
    elif probabilidad < 30:
        print("No necesitas paraguas")
    elif probabilidad <= 70:
        print("Lleva paraguas por si acaso")
    else:
        print("Definitivamente lleva paraguas")
except ValueError:
    print("Error: Debes ingresar un número válido")
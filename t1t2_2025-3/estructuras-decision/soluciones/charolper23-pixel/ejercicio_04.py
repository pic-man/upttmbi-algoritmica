"""
Ejercicio 4: Número Positivo, Negativo o Cero
Estudiante: Yudith Perdomo
GitHub: @charolper23-pixel
Fecha: 28-10-2025

Descripción:
Determina si un número es positivo, negativo o cero.

Ejemplo de uso:
Entrada: -5
Salida: El número es negativo.
"""

# Solicitar el número al usuario
numero = float(input("Ingresa un número: "))

# Determinar si es positivo, negativo o cero
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")
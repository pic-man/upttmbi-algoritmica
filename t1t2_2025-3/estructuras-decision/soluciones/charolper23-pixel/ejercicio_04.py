"""
Ejercicio 4: Número Positivo, Negativo o Cero
Determina si un número es positivo, negativo o cero.
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
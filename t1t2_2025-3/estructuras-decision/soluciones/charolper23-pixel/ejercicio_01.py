"""
Ejercicio 1: Edad Válida
Verifica si una edad es válida y determina si es menor o mayor de edad.
"""

# Solicitar la edad al usuario
edad = int(input("Ingresa tu edad: "))

# Validar y clasificar la edad
if edad < 0:
    print("Edad no válida")
elif edad < 18:
    print("Eres menor de edad")
elif edad <= 120:
    print("Eres mayor de edad")
else:
    print("Edad no válida")
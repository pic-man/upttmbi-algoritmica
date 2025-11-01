"""
Ejercicio 1: Edad Válida
Estudiante: Yudith Perdomo
GitHub: @charolper23-pixel
Fecha: 28-10-2025

Descripción:
Verifica si una edad es válida y determina si es menor o mayor de edad.

Ejemplo de uso:
Entrada: 15
Salida: Eres menor de edad
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
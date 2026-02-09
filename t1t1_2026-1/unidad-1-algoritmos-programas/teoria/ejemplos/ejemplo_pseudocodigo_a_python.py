"""
Ejemplo: De Pseudocódigo a Python
Unidad 1: Algoritmo y Programas

Este ejemplo muestra cómo traducir un pseudocódigo a Python.

PSEUDOCÓDIGO ORIGINAL:
----------------------
ALGORITMO DeterminarMayor
    VARIABLES
        num1, num2, mayor: ENTERO
    INICIO
        ESCRIBIR "Ingrese el primer número:"
        LEER num1
        ESCRIBIR "Ingrese el segundo número:"
        LEER num2
        
        SI num1 > num2 ENTONCES
            mayor ← num1
        SINO
            mayor ← num2
        FIN SI
        
        ESCRIBIR "El mayor es:", mayor
    FIN
FIN ALGORITMO
"""

# ============================================
# CÓDIGO PYTHON (Traducción del pseudocódigo)
# ============================================

print("=== Determinar el Mayor de Dos Números ===\n")

# ESCRIBIR "Ingrese el primer número:"
# LEER num1
num1 = int(input("Ingrese el primer número: "))

# ESCRIBIR "Ingrese el segundo número:"
# LEER num2
num2 = int(input("Ingrese el segundo número: "))

# SI num1 > num2 ENTONCES
#     mayor ← num1
# SINO
#     mayor ← num2
# FIN SI

if num1 > num2:
    mayor = num1
else:
    mayor = num2

# ESCRIBIR "El mayor es:", mayor
print(f"\nEl mayor es: {mayor}")

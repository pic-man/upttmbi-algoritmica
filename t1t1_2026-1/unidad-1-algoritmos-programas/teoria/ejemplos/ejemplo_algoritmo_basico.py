"""
Ejemplo: Algoritmo Básico - Calcular el área de un rectángulo
Unidad 1: Algoritmo y Programas

Este ejemplo muestra las tres partes de un algoritmo:
- ENTRADA: base y altura
- PROCESO: calcular área
- SALIDA: mostrar el resultado
"""

# ============================================
# ENTRADA
# ============================================
# Solicitamos los datos necesarios al usuario
print("=== Calculadora de Área de Rectángulo ===\n")

base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))

# ============================================
# PROCESO
# ============================================
# Realizamos el cálculo
area = base * altura

# ============================================
# SALIDA
# ============================================
# Mostramos el resultado
print(f"\n--- Resultado ---")
print(f"Base: {base}")
print(f"Altura: {altura}")
print(f"Área: {area}")

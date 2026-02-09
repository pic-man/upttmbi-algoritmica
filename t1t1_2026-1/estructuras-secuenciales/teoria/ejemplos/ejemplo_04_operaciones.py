# ==============================================
# Ejemplo 4: Operaciones Aritméticas
# Cómo hacer cálculos matemáticos en Python
# ==============================================

# --- Operaciones básicas con números fijos ---
print("=== Operaciones básicas ===")
a = 15
b = 4

print(f"a = {a}, b = {b}")
print(f"Suma: {a} + {b} = {a + b}")
print(f"Resta: {a} - {b} = {a - b}")
print(f"Multiplicación: {a} × {b} = {a * b}")
print(f"División: {a} ÷ {b} = {a / b}")
print(f"División entera: {a} // {b} = {a // b}")
print(f"Residuo (módulo): {a} % {b} = {a % b}")
print(f"Potencia: {a} ** 2 = {a ** 2}")

# --- Calculadora simple ---
print()
print("=== Calculadora simple ===")
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

suma = num1 + num2
resta = num1 - num2
producto = num1 * num2
cociente = num1 / num2

print()
print("Resultados:")
print(f"{num1} + {num2} = {suma}")
print(f"{num1} - {num2} = {resta}")
print(f"{num1} × {num2} = {producto}")
print(f"{num1} ÷ {num2} = {cociente}")

# --- Ejemplo práctico: Área de un rectángulo ---
print()
print("=== Área de un rectángulo ===")
base = float(input("Base del rectángulo: "))
altura = float(input("Altura del rectángulo: "))

area = base * altura
perimetro = 2 * (base + altura)

print(f"Área: {area}")
print(f"Perímetro: {perimetro}")

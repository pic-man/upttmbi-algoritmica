# ==============================================
# Ejemplo 3: Entrada y Salida
# Cómo pedir datos al usuario y mostrar resultados
# ==============================================

# --- Parte 1: Pedir texto ---
print("=== Pidiendo texto ===")
nombre = input("¿Cómo te llamas? ")
print(f"¡Hola, {nombre}! Bienvenido al curso.")

# --- Parte 2: Pedir números enteros ---
print()
print("=== Pidiendo un número entero ===")
edad = int(input("¿Cuántos años tienes? "))
print(f"Tienes {edad} años.")

# --- Parte 3: Pedir números decimales ---
print()
print("=== Pidiendo un número decimal ===")
estatura = float(input("¿Cuánto mides (en metros)? "))
print(f"Mides {estatura} metros.")

# --- Parte 4: Resumen final ---
print()
print("=" * 30)
print("RESUMEN DE TUS DATOS")
print("=" * 30)
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(f"Estatura: {estatura} m")

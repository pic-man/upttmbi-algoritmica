"""
Ejemplo: Tipos de Datos en Python
Unidad 3: Datos y Entidades Primitivas

Este ejemplo demuestra los diferentes tipos de datos
y sus operaciones básicas.
"""

print("=" * 50)
print("DEMOSTRACIÓN DE TIPOS DE DATOS")
print("=" * 50)

# ============================================
# 1. DATOS NUMÉRICOS
# ============================================
print("\n--- DATOS NUMÉRICOS ---")

# Enteros (int)
edad = 25
cantidad = -10
poblacion = 7_800_000_000  # Se pueden usar _ para legibilidad

print(f"Entero (edad): {edad} - Tipo: {type(edad)}")
print(f"Entero negativo: {cantidad}")
print(f"Entero grande: {poblacion:,}")

# Reales (float)
precio = 19.99
pi = 3.14159
temperatura = -5.5

print(f"\nReal (precio): {precio} - Tipo: {type(precio)}")
print(f"Pi: {pi}")
print(f"Temperatura: {temperatura}")

# ============================================
# 2. DATOS ALFANUMÉRICOS
# ============================================
print("\n--- DATOS ALFANUMÉRICOS ---")

# Cadenas (str)
nombre = "María García"
mensaje = 'Hola, mundo!'
parrafo = """Este es un texto
de múltiples líneas"""

print(f"Cadena (nombre): '{nombre}' - Tipo: {type(nombre)}")
print(f"Longitud del nombre: {len(nombre)} caracteres")
print(f"En mayúsculas: {nombre.upper()}")
print(f"Primera letra: {nombre[0]}")

# ============================================
# 3. DATOS LÓGICOS
# ============================================
print("\n--- DATOS LÓGICOS (Booleanos) ---")

activo = True
tiene_permiso = False

print(f"Booleano (activo): {activo} - Tipo: {type(activo)}")
print(f"Booleano (tiene_permiso): {tiene_permiso}")

# Resultados de comparaciones
print(f"\n5 > 3 = {5 > 3}")
print(f"10 == 10 = {10 == 10}")
print(f"'a' < 'b' = {'a' < 'b'}")

# ============================================
# 4. CONVERSIONES DE TIPO
# ============================================
print("\n--- CONVERSIONES DE TIPO ---")

# String a número
texto_numero = "42"
numero = int(texto_numero)
print(f"'{texto_numero}' convertido a int: {numero}")

# Número a string
precio = 99.99
precio_texto = str(precio)
print(f"{precio} convertido a str: '{precio_texto}'")

# Float a int (trunca)
decimal = 3.9
entero = int(decimal)
print(f"{decimal} convertido a int: {entero}")

# Valores a booleano
print(f"\nbool(0) = {bool(0)}")
print(f"bool(1) = {bool(1)}")
print(f"bool('') = {bool('')}")
print(f"bool('texto') = {bool('texto')}")

# ============================================
# 5. VERIFICAR TIPOS
# ============================================
print("\n--- VERIFICACIÓN DE TIPOS ---")

valor = 3.14
print(f"¿Es int? {isinstance(valor, int)}")
print(f"¿Es float? {isinstance(valor, float)}")
print(f"¿Es numérico? {isinstance(valor, (int, float))}")

print("\n" + "=" * 50)
print("FIN DE LA DEMOSTRACIÓN")
print("=" * 50)

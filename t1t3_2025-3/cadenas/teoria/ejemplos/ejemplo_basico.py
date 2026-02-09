"""
Ejemplo Básico - Cadenas en Python
==================================

Muestra operaciones fundamentales con strings.
Objetivo: Limpiar y formatear datos de contacto.
"""

print("=" * 50)
print("FICHA DE CONTACTO")
print("=" * 50)

# Datos de origen (simulan entrada del usuario)
nombre_raw = "aNa carLos"
correo_raw = "  usuario@example.com  "
telefono_raw = "  51-987-654-321  "

print("\n📥 Datos originales:")
print(f"Nombre: '{nombre_raw}'")
print(f"Correo: '{correo_raw}'")
print(f"Teléfono: '{telefono_raw}'")

# Normalizar nombre (capitalizar cada palabra)
nombre = " ".join(parte.capitalize() for parte in nombre_raw.split())

# Limpiar espacios laterales
direccion_correo = correo_raw.strip()
telefono = telefono_raw.strip().replace("-", "")

# Validaciones sencillas
print("\n🔍 Validaciones:")
print(f"Correo válido: {direccion_correo.endswith('@example.com')}")
print(f"Teléfono contiene solo dígitos: {telefono.isdigit()}")

# Formateo final
telefono_formateado = f"(+{telefono[:2]}) {telefono[2:5]}-{telefono[5:8]}-{telefono[8:]}"

print("\n✅ Registro normalizado:")
print(f"Nombre: {nombre}")
print(f"Correo: {direccion_correo.lower()}")
print(f"Teléfono: {telefono_formateado}")

print("\n" + "=" * 50)
print("SUGERENCIAS DE PRÁCTICA")
print("=" * 50)
print("1. Cambia el dominio del correo y valida.")
print("2. Detecta si el teléfono tiene longitud incorrecta.")
print("3. Usa replace() para estandarizar prefijos telefónicos.")

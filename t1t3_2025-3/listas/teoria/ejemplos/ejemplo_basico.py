"""
Ejemplo Básico - Listas en Python
===================================

Este ejemplo muestra operaciones fundamentales con listas.

Objetivo: Gestionar una lista de compras simple.
"""

print("="*50)
print("LISTA DE COMPRAS")
print("="*50)

# Crear lista vacía
compras = []

# Agregar elementos
print("\n📝 Agregando artículos...")
compras.append("leche")
compras.append("pan")
compras.append("huevos")
compras.append("café")
print(f"Lista actual: {compras}")

# Insertar al inicio
compras.insert(0, "agua")
print(f"\n✅ Agregado 'agua' al inicio: {compras}")

# Verificar existencia
print("\n🔍 Verificando artículos...")
if "pan" in compras:
    print("✓ Sí tenemos pan en la lista")

if "arroz" not in compras:
    print("✗ No tenemos arroz")

# Contar elementos
total = len(compras)
print(f"\n📊 Total de artículos: {total}")

# Acceder a elementos
print(f"\nPrimer artículo: {compras[0]}")
print(f"Último artículo: {compras[-1]}")

# Eliminar elemento comprado
comprado = compras.pop(0)
print(f"\n💰 Compramos: {comprado}")
print(f"Quedan: {compras}")

# Mostrar lista final
print("\n" + "="*50)
print("LISTA ACTUALIZADA:")
print("="*50)
for i, articulo in enumerate(compras, 1):
    print(f"{i}. {articulo}")

# EJERCICIOS PARA PRACTICAR:
# 1. Agrega 3 artículos más a la lista
# 2. Ordena la lista alfabéticamente
# 3. Elimina el penúltimo elemento
# 4. Cuenta cuántas veces aparece "pan" (si lo agregas varias veces)


"""
Ejemplo Básico - Estructuras de Decisión
==========================================

Este ejemplo muestra el uso básico de if, elif y else.

Objetivo: Clasificar la edad de una persona.
"""

print("="*50)
print("CLASIFICADOR DE EDAD")
print("="*50)

# Solicitar la edad al usuario
edad = int(input("\nIngresa tu edad: "))

# Estructura de decisión simple
if edad < 0:
    print("❌ Edad no válida (no puede ser negativa)")
elif edad <= 12:
    print("👶 Eres un niño")
elif edad <= 17:
    print("🧒 Eres un adolescente")
elif edad <= 64:
    print("👨 Eres un adulto")
elif edad <= 120:
    print("👴 Eres un adulto mayor")
else:
    print("❌ Edad no válida (demasiado alta)")

print("\n" + "="*50)
print("Fin del programa")
print("="*50)

# EJERCICIOS PARA PRACTICAR:
# 1. Modifica el programa para que acepte edades decimales (float)
# 2. Agrega una categoría "joven adulto" (18-30 años)
# 3. Agrega validación para que solo acepte números


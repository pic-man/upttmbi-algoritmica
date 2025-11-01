"""
Ejercicio 7: Contador de Frutas
Estudiante: Yudith Perdomo
GitHub: @charolper23-pixel
Fecha: 28-10-2025

Descripción:
Muestra el precio por kilogramo de la fruta seleccionada.

Ejemplo de uso:
Entrada: manzana
Salida: Precio: $15 por kg
"""

# Solicitar la fruta al usuario
fruta = input("Ingresa el nombre de una fruta: ").lower()

# Mostrar el precio según la fruta
if fruta == "manzana":
    print("Precio: $15 por kg")
elif fruta == "naranja":
    print("Precio: $12 por kg")
elif fruta == "plátano" or fruta == "platano":
    print("Precio: $10 por kg")
else:
    print("No tenemos información de precio para esa fruta")
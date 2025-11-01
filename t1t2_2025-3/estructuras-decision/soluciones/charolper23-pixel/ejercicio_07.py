"""
Ejercicio 7: Contador de Frutas
Muestra el precio por kilogramo de la fruta seleccionada.
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
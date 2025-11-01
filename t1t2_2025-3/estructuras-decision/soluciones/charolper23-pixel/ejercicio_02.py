"""
Ejercicio 2: Precio con Descuento Simple
Calcula el precio final de un producto aplicando descuento según el monto.
"""

# Solicitar el precio del producto
precio = float(input("Ingresa el precio del producto: $"))

# Se aplica el descuento, si corresponde
if precio > 50:
    descuento = 0.10  # 10% de descuento
    precio_final = precio - (precio * descuento)
    print(f"Precio original: ${precio:.2f}")
    print(f"Descuento aplicado: 10%")
    print(f"Precio final: ${precio_final:.2f}")
else:
    print(f"Precio original: ${precio:.2f}")
    print("Descuento aplicado: 0%")
    print(f"Precio final: ${precio:.2f}")
"""
Ejercicio 15: Tipo de Tarjeta
Muestra los beneficios asociados a cada tipo de tarjeta.
"""

print("=== BENEFICIOS DE TARJETA DE CRÉDITO ===\n")
print("Tipos disponibles: básica, oro, platino")

# Solicitar el tipo de tarjeta
tipo = input("Ingresa el tipo de tarjeta: ").lower()

# Mostrar beneficios según el tipo
if tipo == "básica" or tipo == "basica":
    print("BENEFICIOS: 1% de cashback")
elif tipo == "oro":
    print("BENEFICIOS: 2% de cashback + seguro")
elif tipo == "platino":
    print("BENEFICIOS: 3% de cashback + seguro + VIP")
else:
    print("Tipo de tarjeta no válido")
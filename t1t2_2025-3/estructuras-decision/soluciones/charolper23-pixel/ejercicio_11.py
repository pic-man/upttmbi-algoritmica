"""
Ejercicio 11: Tamaño de Pizza
Calcula el precio según el tamaño de pizza elegido.
"""

# Solicitar el tamaño de pizza al usuario
tamano = input("Elige un tamaño de pizza (chica/mediana/grande): ").lower()

# Calcular el precio según el tamaño
if tamano == "chica":
    precio = 80
    print(f"Precio de la pizza chica: ${precio}")
elif tamano == "mediana":
    precio = 120
    print(f"Precio de la pizza mediana: ${precio}")
elif tamano == "grande":
    precio = 150
    print(f"Precio de la pizza grande: ${precio}")
else:
    print("Tamaño no disponible. Elige chica, mediana o grande.")
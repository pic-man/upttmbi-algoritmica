"""
Ejercicio 19: Mezcla de Colores Primarios
Determina el color resultante al mezclar dos colores primarios.
"""

print("=== MEZCLADOR DE COLORES PRIMARIOS ===\n")

# Solicitar los colores a mezclar
color1 = input("Ingresa el primer color primario (rojo/azul/amarillo): ").lower()
color2 = input("Ingresa el segundo color primario (rojo/azul/amarillo): ").lower()

# Validar que sean colores primarios
colores_primarios = ["rojo", "azul", "amarillo"]

if color1 not in colores_primarios or color2 not in colores_primarios:
    print("error, color no primario")
elif color1 == color2:
    print("error, mismo color")
# Determinar el color resultante
elif (color1 == "rojo" and color2 == "azul") or (color1 == "azul" and color2 == "rojo"):
    print("Rojo + Azul = Morado")
elif (color1 == "rojo" and color2 == "amarillo") or (color1 == "amarillo" and color2 == "rojo"):
    print("Rojo + Amarillo = Naranja")
elif (color1 == "azul" and color2 == "amarillo") or (color1 == "amarillo" and color2 == "azul"):
    print("Azul + Amarillo = Verde")

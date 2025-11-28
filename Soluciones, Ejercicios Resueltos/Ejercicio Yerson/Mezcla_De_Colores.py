#Ejercico 19: Mezcla de colores
#Estudiante:Yerson Josue Saavedra Barrios
#GitHub:Yerson17
#Fecha:2025-11-16
print("=== MEZCLADOR DE COLORES ===")
print()
print("Colores primarios: rojo, azul, amarillo")
print()

color1 = input("Primer color: ").lower()
color2 = input("Segundo color: ").lower()
print()

COLORES_PRIMARIOS = ["rojo", "azul", "amarillo"]

if color1 not in COLORES_PRIMARIOS:
    print(" Error: Usa solo colores primarios")
    print(f"{color1.capitalize()} no es un color primario")
    print("Colores válidos: rojo, azul, amarillo")

elif color2 not in COLORES_PRIMARIOS:
    print(" Error: Usa solo colores primarios")
    print(f"{color2.capitalize()} no es un color primario")
    print("Colores válidos: rojo, azul, amarillo")


elif color1 == color2:
    print(" Error: No se puede mezclar el mismo color")
    print("Por favor, elige dos colores diferentes")


elif (color1 == "rojo" and color2 == "azul") or (color1 == "azul" and color2 == "rojo"):
    print(" RESULTADO: Morado 💜")
    print("Mezcla: Rojo + Azul = Morado")
    print("Tipo: Color secundario")
    print("Uso común: realeza, creatividad, misterio")

elif (color1 == "rojo" and color2 == "amarillo") or (color1 == "amarillo" and color2 == "rojo"):
    print(" RESULTADO: Naranja ")
    if color1 == "amarillo":
        print("Mezcla: Amarillo + Rojo = Naranja")
    else:
        print("Mezcla: Rojo + Amarillo = Naranja")
    print("Tipo: Color secundario")
    print("Uso común: energía, entusiasmo, calidez")

elif (color1 == "azul" and color2 == "amarillo") or (color1 == "amarillo" and color2 == "azul"):
    print(" RESULTADO: Verde ")
    print("Mezcla: Azul + Amarillo = Verde")
    print("Tipo: Color secundario")
    print("Uso común: naturaleza, crecimiento, frescura")
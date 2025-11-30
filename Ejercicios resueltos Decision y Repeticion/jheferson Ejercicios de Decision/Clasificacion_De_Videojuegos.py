#Ejercico 13: Clasificacion Juego
#Estudiante : Jheferson Manuel Duran Marin
#GitHub: Jheferson1213
#Fecha:2025,11,30
print("=== CLASIFICACIÓN DE VIDEOJUEGOS ===")
print()
edad = int(input("Ingresa tu edad: "))
print()

print("Tu clasificación recomendada:")

if edad < 7:
    print(" CLASIFICACIÓN Edad (Edad baja 10-)")
    print("Descripción: Contenido apto para todas las edades")
    print("Ejemplos de juegos:")
    print("- Mario Kart")
    print("- Minecraft")
    print("- Animal Crossing")
    print("- Roblox")
elif edad <= 12:
    print("CLASIFICACIÓN Edad (Edad media 10+)")
    print("Descripción: Contenido apto para mayores de 10 años")
    print("Puede contener: violencia/lenguaje leve")
    print("Ejemplos de juegos:")
    print("- Sonic")
    print("- Pokemon")
    print("- Splatoon")
elif edad <= 17: 
    print("CLASIFICACIÓN Edad (Mayoria de Edad 13+)")
    print("Descripción: Contenido apto para mayores de 13 años")
    print("Puede contener: violencia leve, lenguaje moderado")
    print("Ejemplos de juegos:")
    print("- Fortnite")
    print("- Rocket League")
    print("- Zelda Ocarine Of Time")
else:
    print(" CLASIFICACIÓN Edad (Mayor de Edad 18+)")
    print("Descripción: Contenido apto solo para adultos (18+)")
    print("Puede contener: violencia intensa, lenguaje fuerte, contenido adulto")
    print("Ejemplos de juegos:")
    print("- Grand Theft Auto V")
    print("- Call of Duty")
    print("- The Last of Us")
    print("- Blood Strike")
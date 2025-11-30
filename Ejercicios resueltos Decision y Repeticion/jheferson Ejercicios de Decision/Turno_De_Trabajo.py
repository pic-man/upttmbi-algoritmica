#Ejercico 6: Turno Trabajo
#Estudiante : Jheferson Manuel Duran Marin
#GitHub: Jheferson1213
#Fecha:2025,11,30
hora = int(input("Ingresa la hora (0-23): "))
if 6 <= hora <= 13:
    print("Turno matutino ")
elif 14 <= hora <= 21:
    print("Turno vespertino ")
else:
    print("Turno nocturno ")
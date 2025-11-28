#Ejercico 6: Turno Trabajo
#Estudiante:Yerson Josue Saavedra Barrios
#GitHub:Yerson17
#Fecha:2025-11-16
hora = int(input("Ingresa la hora (0-23): "))
if 6 <= hora <= 13:
    print("Turno matutino ")
elif 14 <= hora <= 21:
    print("Turno vespertino ")
else:
    print("Turno nocturno ")
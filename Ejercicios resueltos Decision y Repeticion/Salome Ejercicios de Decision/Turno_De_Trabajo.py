#Ejercico 6: Turno Trabajo
#Estudiante : Yoeleiny Mariasalome Barrios Zambrano
#GitHub: Yoeleiny205
#Fecha:2025,11,16
hora = int(input("Ingresa la hora (0-23): "))
if 6 <= hora <= 13:
    print("Turno matutino ")
elif 14 <= hora <= 21:
    print("Turno vespertino ")
else:
    print("Turno nocturno ")
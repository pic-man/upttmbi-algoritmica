#Ejercico 9: Entradas Parque
#Estudiante : Yoeleiny Mariasalome Barrios Zambrano
#GitHub: Yoeleiny205
#Fecha:2025,11,16
estatura = float(input("Ingresa tu estatura en cm: "))

if estatura >= 1.20:
    print("¡Puedes subir a la atracción! ")
    if estatura == 1.20:
        print("Tu estatura:",estatura," cm (estatura mínima)")
    else:
        print("Tu estatura:",estatura,"cm")
else:
    faltan = 1.20 - estatura
    print("Lo sentimos, no puedes subir a la atracción")
    print("Estatura mínima requerida: 1.20 cm")
    print("Tu estatura:",faltan,"cm")
    print("Te faltan:",faltan,"cm")
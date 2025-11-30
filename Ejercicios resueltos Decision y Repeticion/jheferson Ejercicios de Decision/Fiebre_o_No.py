#Ejercico 8: Temperatura
#Estudiante : Jheferson Manuel Duran Marin
#GitHub: Jheferson1213
#Fecha:2025,11,30
temperatura = float(input("Ingresa tu temperatura corporal (°C): "))
if temperatura < 36:
    print("¡Hipotermia! ")
    print("Tu temperatura es:",temperatura,"°C")
    print("Recomendación: Busca atención médica inmediata")
elif temperatura <= 37.5:
    print("Temperatura normal ")
    print("Tu temperatura es:",temperatura,"°C")
else: 
    print("¡Tienes fiebre! ")
    print("Tu temperatura es:",temperatura,"°C")
    print("Recomendación: Consulta a un médico")
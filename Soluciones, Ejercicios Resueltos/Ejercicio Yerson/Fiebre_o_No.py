#Ejercico 8: Temperatura
#Estudiante:Yerson Josue Saavedra Barrios
#GitHub:Yerson17
#Fecha:2025-11-16
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
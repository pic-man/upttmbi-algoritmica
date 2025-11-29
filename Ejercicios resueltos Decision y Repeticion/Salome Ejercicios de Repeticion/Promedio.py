#Ejercico 5: Promedio hasta cero
#Estudiante:Yoeleiny MariaSalome Barrios Zambrano
#GitHub:Yoeleiny205
#Fecha:2025-11-28
print("Calcula tu Promedio")
suma_total = 0
conteo = 0
numero = -1 
while numero != 0:
    numero_U = input("Ingresa un número (0 para terminar): ")
    numero = int(numero_U)
    if numero != 0:
        suma_total += numero
        conteo += 1
if conteo == 0:
    print("No se ingresaron datos para calcular el promedio.")
else:
    promedio = suma_total / conteo
    print("Promedio:", round(promedio, 2))
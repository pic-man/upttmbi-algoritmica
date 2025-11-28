#Ejercico 11: Mayor Menor
#Estudiante:Yerson Josue Saavedra Barrios
#GitHub:Yerson17
#Fecha:2025-11-28
print("Mayor y Menor")
numero1 = ""
mayor = None
menor = None
conteo = 0
while numero1.lower() != "fin":
    numero1= input("Ingresa un número (o 'fin' para terminar): ")
    if numero1.lower() == "fin":
        break
    numero = int(numero1)
    conteo += 1
    if conteo == 1:
        mayor = numero
        menor = numero
    else:
        if numero > mayor:
            mayor = numero
        if numero < menor:
            menor = numero
if conteo == 0:
    print("No se ingresaron números.")
else:
    print("Mayor:", mayor)
    print("Menor:", menor)

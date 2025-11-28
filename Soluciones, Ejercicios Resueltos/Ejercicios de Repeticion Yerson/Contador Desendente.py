#Ejercico 2: Contador Decendiente
#Estudiante:Yerson Josue Saavedra Barrios
#GitHub:Yerson17
#Fecha:2025-11-28
print("Contador Desendente")
n = input("Ingresa un número entero: ")
n1= int(n)
if n1 >= 0:
    contador = n1
    while contador >= 0:
        print(contador, end=" ")
        contador -= 1 
else:
    print("Entrada no válida. Usa un número entero mayor o igual que cero.")
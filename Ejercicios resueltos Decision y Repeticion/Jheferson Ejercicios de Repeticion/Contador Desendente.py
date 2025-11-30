#Ejercico 2: Contador Decendiente
#Estudiante : Jheferson Manuel Duran Marin
#GitHub: Jheferson1213
#Fecha:2025,11,30
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
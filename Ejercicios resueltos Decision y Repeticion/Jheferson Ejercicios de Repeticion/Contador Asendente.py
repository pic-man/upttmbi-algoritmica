#Ejercico 1: Contador ascendente
#Estudiante : Jheferson Manuel Duran Marin
#GitHub: Jheferson1213
#Fecha:2025,11,30
print("Contador Asendente")
n = input("Ingresa un número entero positivo: ")
n1 = int(n)
if n1 > 0:
    contador = 1   
    while contador <= n1:
        print(contador, end=" ")
        contador += 1
else:
    print("Entrada no válida. Debes ingresar un entero mayor que cero.")
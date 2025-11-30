#Ejercico 3: Suma de Numeros
#Estudiante : Jheferson Manuel Duran Marin
#GitHub: Jheferson1213
#Fecha:2025,11,30
print("Suma de enteros")
n1 = input("Ingresa un número entero positivo: ")
n = int(n1)
if n >= 1:
    suma_total = 0
    for i in range(1, n + 1):
        suma_total += i
    print("La suma de 1 a", n, "es:", suma_total)
else:
    print("Entrada no válida. Necesitas un entero mayor o igual a 1.")
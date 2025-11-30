#Ejercico 9:Suma de pares
#Estudiante : Jheferson Manuel Duran Marin
#GitHub: Jheferson1213
#Fecha:2025,11,30
print("Suma de Pares")
n1 = input("Ingresa un número entero positivo: ")
n = int(n1)
if n >= 1:
    suma_total = 0
    for numero in range(1, n + 1):
        if numero % 2 == 0:
            suma_total += numero
    print("La suma de pares entre 1 y", n, "es:", suma_total)
else:
    print("Entrada no válida. Debes ingresar un entero mayor o igual a 1.")

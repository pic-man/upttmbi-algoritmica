#Ejercico 6: Factorial interactivo
#Estudiante : Jheferson Manuel Duran Marin
#GitHub: Jheferson1213
#Fecha:2025,11,30
print("Factorial Iterativo")
Factor = input("Ingresa un número entero: ")
n = int(Factor)
if n >= 0:
    if n == 0:
        resultado = 1
    else:
        resultado = 1
        contador = 1
        while contador <= n:
            resultado *= contador
            contador += 1
    print(n, "! =", resultado)
else:
    print("Entrada no válida. El número debe ser 0 o positivo.")
#Ejercico 6: Factorial interactivo
#Estudiante:Yoeleiny MariaSalome Barrios Zambrano
#GitHub:Yoeleiny205
#Fecha:2025-11-28
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
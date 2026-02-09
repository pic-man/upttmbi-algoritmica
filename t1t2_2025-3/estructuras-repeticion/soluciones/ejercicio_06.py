# Ejercicio 6: Factorial Iterativo
n = int(input("Ingresa un número entero: "))
factorial = 1
contador = 1
while contador <= n:
    factorial = factorial * contador
    contador = contador + 1
print(f"{n}! = {factorial}")

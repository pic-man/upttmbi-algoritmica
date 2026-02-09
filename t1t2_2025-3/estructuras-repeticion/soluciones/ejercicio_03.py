# Ejercicio 3: Suma de Números
n = int(input("Ingresa un número entero positivo: "))
suma = 0
for i in range(n):
    suma = suma + (i + 1)
print(f"La suma de 1 a {n} es: {suma}")

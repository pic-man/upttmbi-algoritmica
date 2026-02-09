# Ejercicio 9: Suma de Pares
n = int(input("Ingresa un número entero positivo: "))
suma = 0
for i in range(n):
    if (i + 1) % 2 == 0:
        suma = suma + (i + 1)
print(f"La suma de pares entre 1 y {n} es: {suma}")

# Ejercicio 5: Promedio hasta Cero
suma = 0
cantidad = 0
numero = int(input("Ingresa un número (0 para terminar): "))
while numero != 0:
    suma = suma + numero
    cantidad = cantidad + 1
    numero = int(input("Ingresa un número (0 para terminar): "))
print(f"Promedio: {suma / cantidad:.2f}")

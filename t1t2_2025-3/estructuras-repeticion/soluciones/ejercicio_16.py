# Ejercicio 16: Conversión a Binario
n = int(input("Ingresa un número entero: "))
binario = ""
numero = n
while numero > 0:
    binario = str(numero % 2) + binario
    numero = numero // 2
if binario == "":
    binario = "0"
print(f"Binario: {binario}")

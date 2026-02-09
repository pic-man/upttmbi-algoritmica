# Ejercicio 19: Conteo de Dígitos
n = int(input("Ingresa un número entero: "))
numero = n
if numero < 0:
    numero = -numero
cantidad = 0
while numero > 0:
    cantidad = cantidad + 1
    numero = numero // 10
if cantidad == 0:
    cantidad = 1
print(f"Cantidad de dígitos: {cantidad}")

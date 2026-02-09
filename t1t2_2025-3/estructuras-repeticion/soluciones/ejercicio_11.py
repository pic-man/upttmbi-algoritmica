# Ejercicio 11: Mayor y Menor
mayor = None
menor = None
entrada = input("Ingresa un número (o 'fin' para terminar): ")
while entrada.lower() != "fin":
    numero = int(entrada)
    if mayor == None or numero > mayor:
        mayor = numero
    if menor == None or numero < menor:
        menor = numero
    entrada = input("Ingresa un número (o 'fin' para terminar): ")
print(f"Mayor: {mayor}\nMenor: {menor}")

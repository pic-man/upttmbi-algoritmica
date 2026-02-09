# Ejercicio 10: Potencia por Multiplicación
base = int(input("Ingresa la base: "))
exponente = int(input("Ingresa el exponente: "))
resultado = 1
contador = 0
while contador < exponente:
    resultado = resultado * base
    contador = contador + 1
print(f"{base}^{exponente} = {resultado}")

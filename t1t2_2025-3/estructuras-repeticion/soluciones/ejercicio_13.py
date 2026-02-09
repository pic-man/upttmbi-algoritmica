# Ejercicio 13: Juego de Adivinanza
import random
secreto = random.randint(1, 100)
intentos = 0
print("Adivina el número entre 1 y 100.")
numero = int(input("Tu intento: "))
while numero != secreto:
    intentos = intentos + 1
    if numero > secreto:
        print("Demasiado alto.")
    else:
        print("Demasiado bajo.")
    numero = int(input("Tu intento: "))
print(f"¡Correcto! Lo lograste en {intentos + 1} intentos.")

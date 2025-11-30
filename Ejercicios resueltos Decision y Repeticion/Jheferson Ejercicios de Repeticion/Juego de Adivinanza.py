#Ejercico 13: Juego de Adivinanza
#Estudiante : Jheferson Manuel Duran Marin
#GitHub: Jheferson1213
#Fecha:2025,11,30
NUMERO_SECRETO = 37
intentos = 0
adivinado = False
print("Estoy pensando en un número entre 1 y 50.")
while not adivinado:
    numero = input("Adivina el número: ")
    adivinanza = int(numero)
    intentos += 1
    if adivinanza < 1 or adivinanza > 50:
        print("Fuera de rango. Intenta otra vez.")
        intentos -= 1
    if adivinanza == NUMERO_SECRETO:
        adivinado = True
        print("Lo lograste en", intentos, "intento/s.")
    elif adivinanza > NUMERO_SECRETO:
        print("Demasiado alto.")
    else:
        print("Demasiado bajo.")

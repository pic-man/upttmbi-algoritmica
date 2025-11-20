"""Ejercicio 14: [maquina tragamonedas]
Estudiante: [Reibert David Andrade Oviedo]
GitHub: @[reii33]
Fecha: [19/11/2025]

Descripción:
[Simula una máquina tragamonedas que muestra tres símbolos aleatorios y determina si el jugador gana un premio mayor, un premio menor o nada.]
Ejemplo de uso:
[Símbolos: 🍒 | 🍋 | 🍒 No obtuviste nada. ¡Inténtalo de nuevo!]
"""  
import random
simbolos_posibles = ["🍒", "🍋", "🔔", "💎", "7️⃣"]

def jugar_tragamonedas():
    while True:
        simbolos = [random.choice(simbolos_posibles) for _ in range(3)]
        print(f"Símbolos: {simbolos[0]} | {simbolos[1]} | {simbolos[2]}")
        if simbolos[0] == simbolos[1] == simbolos[2]:
            print("¡Jackpot! ¡Felicidades Has ganado el premio mayor! ¡Tu premio es de 1000$!")
        elif simbolos[0] == simbolos[1] or simbolos[0] == simbolos[2] or simbolos[1] == simbolos[2]:
            print("¡Premio menor! Has ganado 50$.")
        else:
            print("No obtuviste nada. ¡Inténtalo de nuevo!")
        jugar_otra_vez = input("¿Quieres jugar otra vez? (s/n): ").lower()
        if jugar_otra_vez != 's':
            break

jugar_tragamonedas()
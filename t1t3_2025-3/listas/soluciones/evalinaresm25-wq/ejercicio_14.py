'''
Ejercicio 14: MÁQUINA TRAGAMONEDAS
Estudiante: Eva Sofia Linares Medina
GitHub: @evalinaresm25-wq
Fecha: 2025-11-26

Descripción:
Genera 3 símbolos aleatorios y determina si ganaste.

Métodos usados:
- random.choice()
- len()
- set()
'''
import random

simbolos_posibles = ["🍒", "🍋", "🔔", "💎", "7️⃣"]
tirada = [random.choice(simbolos_posibles) for _ in range(3)]
print("Resultado:", tirada)

if tirada[0] == tirada[1] == tirada[2]:
    print("Jackpot")
elif len(set(tirada)) == 2:
    print("Premio menor")
else:
    print("Sin premio")

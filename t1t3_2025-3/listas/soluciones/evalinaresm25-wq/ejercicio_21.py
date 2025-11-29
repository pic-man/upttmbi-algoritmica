'''
Ejercicio 21: JUEGO DE BATALLA POR TURNOS
Estudiante: Eva Sofia Linares Medina
GitHub: @evalinaresm25-wq
Fecha: 2025-11-26

Descripción:
Dos equipos pelean por turnos hasta que uno quede sin personajes.

Métodos usados:
- random.randint()
- pop()
- append()
'''
import random

equipo_a = ["Guerrero", "Mago", "Arquero"]
equipo_b = ["Orco", "Goblin", "Troll"]

vidas = {p: 100 for p in equipo_a + equipo_b}

while equipo_a and equipo_b:
    a = equipo_a[0]
    b = equipo_b[0]

    daño_a = random.randint(20, 50)
    daño_b = random.randint(20, 50)

    vidas[b] -= daño_a
    vidas[a] -= daño_b

    if vidas[a] <= 0:
        print(a, "ha muerto")
        equipo_a.pop(0)
    else:
        equipo_a.append(equipo_a.pop(0))

    if vidas[b] <= 0:
        print(b, "ha muerto")
        equipo_b.pop(0)
    else:
        equipo_b.append(equipo_b.pop(0))

print("Ganador:", "Equipo A" if equipo_a else "Equipo B")

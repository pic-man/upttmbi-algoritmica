'''
Ejercicio 13: CARRERA DE ATLETAS
Estudiante: Eva Sofia Linares Medina
GitHub: @evalinaresm25-wq
Fecha: 2025-11-26

Descripción:
Bruno adelanta dos posiciones y Diana adelanta una.

Métodos usados:
- pop()
- insert()
- index()
'''
atletas = ["Ana", "Bruno", "Carlos", "Diana", "Elena"]

bruno = atletas.pop(1)
atletas.insert(1 - 2, bruno)

diana = atletas.pop(atletas.index("Diana"))
atletas.insert(atletas.index("Carlos"), diana)

print("Orden final:", atletas)

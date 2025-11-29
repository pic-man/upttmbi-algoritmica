'''
Ejercicio 17: INVENTARIO DE JUEGO RPG
Estudiante: Eva Sofia Linares Medina
GitHub: @evalinaresm25-wq
Fecha: 2025-11-26

Descripción:
Permite recoger, verificar, usar y organizar objetos.

Métodos usados:
- append()
- count()
- remove()
- sorted()
'''
inventario = []

def recoger(objeto):
    inventario.append(objeto)

def contar(objeto):
    return inventario.count(objeto)

def usar(objeto):
    if objeto in inventario:
        inventario.remove(objeto)

def mostrar():
    print(sorted(inventario))

recoger("poción")
recoger("espada")
recoger("poción")
usar("poción")
mostrar()

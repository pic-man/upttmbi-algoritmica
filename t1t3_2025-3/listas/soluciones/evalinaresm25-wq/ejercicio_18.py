'''
Ejercicio 18: DJ AUTOMÁTICO
Estudiante: Eva Sofia Linares Medina
GitHub: @evalinaresm25-wq
Fecha: 2025-11-26

Descripción:
Gestiona una cola de reproducción musical.

Métodos usados:
- extend()
- pop()
- insert()
'''
cola_reproduccion = []

def agregar_album(album):
    cola_reproduccion.extend(album)

def reproducir():
    if cola_reproduccion:
        print("Reproduciendo:", cola_reproduccion.pop(0))

def agregar_urgente(cancion):
    cola_reproduccion.insert(0, cancion)

def mostrar():
    print("Próximas canciones:", cola_reproduccion[:3])

agregar_album(["A", "B", "C", "D"])
agregar_urgente("Z")
mostrar()
reproducir()

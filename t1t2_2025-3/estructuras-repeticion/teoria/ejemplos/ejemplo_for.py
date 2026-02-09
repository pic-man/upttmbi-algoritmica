"""
Ejemplo Básico de ciclo for
Recorre una lista de tareas y muestra su estado.
"""

tareas = ["Preparar café", "Leer correo", "Revisar código", "Planificar sprint"]

print("Lista de tareas pendientes:")
for indice, tarea in enumerate(tareas, start=1):
    print(f"{indice}. {tarea}")

print("\n¡Todas las tareas listadas!")


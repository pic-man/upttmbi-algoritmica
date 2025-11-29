'''
Ejercicio 5: EL MAGO DE LAS LISTAS
Estudiante: Eva Sofia Linares Medina
GitHub: @evalinaresm25-wq
Fecha: 2025-11-26

Descripción:
Haz desaparecer el último número y luego el primero. Muestra cuántos quedan y cuáles desaparecieron.

Métodos usados:
- list()
- range()
- pop()
'''
numeros_magicos = list(range(1, 11))
ultimo = numeros_magicos.pop()
primero = numeros_magicos.pop(0)
print("Desaparecieron:", primero, "y", ultimo)
print("Quedan:", numeros_magicos)

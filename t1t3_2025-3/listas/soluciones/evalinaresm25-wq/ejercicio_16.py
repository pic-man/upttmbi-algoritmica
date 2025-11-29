'''
Ejercicio 16: MALABARISTA DE NÚMEROS
Estudiante: Eva Sofia Linares Medina
GitHub: @evalinaresm25-wq
Fecha: 2025-11-26

Descripción:
Toma el último elemento y ponlo al inicio tres veces.

Métodos usados:
- pop()
- insert()
'''
def malabares(numeros):
    for _ in range(3):
        ultimo = numeros.pop()
        numeros.insert(0, ultimo)
    return numeros

print(malabares([1, 2, 3, 4, 5]))

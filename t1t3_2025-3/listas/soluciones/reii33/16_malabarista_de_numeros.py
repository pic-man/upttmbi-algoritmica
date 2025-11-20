"""Ejercicio 16: [malabarista de numeros]
Estudiante: [Reibert David Andrade Oviedo]
GitHub: @[reii33]
Fecha: [19/11/2025]

Descripción:
[Realiza una serie de "malabares" con una lista de números, moviendo el último elemento al inicio tres veces consecutivas.]
Ejemplo de uso:
[Primer truco [3, 4, 5, 1, 2]
"""  
def malabares(lista):
    for _ in range(3):
        ultimo_elemento = lista.pop()
        lista.insert(0, ultimo_elemento) 
    return lista

print(f'Primer truco {malabares([1, 2, 3, 4, 5])}') 
print(f'segundo truco {malabares([10, 2, 30, 0])}')  
print(f'Tercer truco {malabares([7, 8, 9])}')      
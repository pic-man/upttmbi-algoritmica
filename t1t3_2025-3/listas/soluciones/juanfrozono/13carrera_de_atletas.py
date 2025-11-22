#Simula una carrera donde los atletas pueden adelantarse
#Modifica el orden de la lista segun estos cambios:
#Bruno adelanta 1 posiciones 
#Diana adelanta 1 posicion 
#Muestra el orden final de llegada

import time

atletas = ["Ana","Bruno","Carlos","Diana","Elena"]

def impr_orden():
    numero = 1
    for atleta in atletas:
        print(f'{numero} - {atleta}')
        numero += 1


print("Orden Inicial: ")

impr_orden()

posicion_B = atletas.index("Bruno")
atletas.insert(0,"Bruno")
atletas.pop(posicion_B + 1)    

print("-" * 50)
print("Bruno adelanta 1 posicion")
print("De posicion 2 a posicion 1")
print("-" * 50)
print("Orden temporal: ")

impr_orden()


posicion_D = atletas.index("Diana")
atletas.insert(posicion_D - 1,"Diana")
atletas.pop(posicion_D + 1) 

print("-" * 50)
print("Diana adelanta 1 posicion")
print("De posicion 4 a posicion 3")
print("-" * 50)
print("Orden Final: ")

impr_orden()
print("-" * 50)

print("Podio: ")

print(f'{atletas[0]} Medalla de Oro')
print(f'{atletas[1]} Medalla de Plata')
print(f'{atletas[2]} Medalla de Bronce')
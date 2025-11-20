"""Ejercicio 13: [carrera atletas]
Estudiante: [Reibert David Andrade Oviedo]
GitHub: @[reii33]
Fecha: [19/11/2025]

Descripción:
[Gestiona una lista de atletas en una carrera, permitiendo modificar sus posiciones según eventos específicos.]
Ejemplo de uso:
[Orden inicial ['Ana', 'Bruno', 'Carlos', 'Diana', 'Elena']]
"""  
##lista inicial

atletas = ["Ana", "Bruno", "Carlos", "Diana", "Elena"]

print(f'Orden inicial {atletas}')
atletas2 = atletas.copy()

##Moviendo a bruno a la posición 0

atletas2.index('Bruno')
atletas2.pop(1)
atletas2.insert(0, 'Bruno') 

print(f'Bruno encabeza la carrera {atletas2}')
##Moviendo a diana a la posición 2
atletas3 = atletas2.copy()

atletas3.pop(3)
atletas3.insert(2, 'Diana')

print(f'Diana adelanta una posición {atletas3}')




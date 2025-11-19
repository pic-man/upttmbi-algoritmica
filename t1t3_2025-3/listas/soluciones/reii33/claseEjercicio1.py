"""Ejercicio 01: [Piezzeria]
Estudiante: [Reibert David Andrade Oviedo]
GitHub: @[reii33]
Fecha: [19/11/2025]

Descripción:
[Piezzeria que permite agregar y eliminar ingredientes de una lista]

Ejemplo de uso:
[1 para agregar nuevos ingredientes 2 para eliminar 3 para mostrar lista 4 salir]
"""  

ingredientes = ['queso', 'anchoas', 'tomate', 'jamon']


while True :
    usuario = float(input("1 para agregar nuevos ingredientes 2 para eliminar 3 para mostrar lista 4 salir"))
    if usuario == 1 :
        ingredienteI = input('Que ingrediente quieres agregar?')
        ingredientes.append(ingredienteI)
        print('Ingrediente agregado')
    elif usuario == 2 :
        eliminar = input('Que deseas eliminar?')
        ingredientes.remove(eliminar)
        print("Ingrediente eliminado")
    elif  usuario == 3:
        print(ingredientes)
    elif usuario == 4 :
        print('saliste')
        break





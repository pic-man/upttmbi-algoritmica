"""Ejercicio 01: [Piezzeria]
Estudiante: [Argenis Saul Linares Moncayo]
GitHub: @[argenis183]
Fecha: [27/11/2025]

Descripción:
[Piezzeria que permite agregar y eliminar ingredientes de una lista]

Ejemplo de uso:
[1 para agregar nuevos ingredientes 2 para eliminar 3 para mostrar lista 4 salir]
"""  
##lista inicial de ingredientes
ingredientes = ['queso', 'anchoas', 'tomate', 'jamon', 'aceitunas']


while True :
    usuario = float(input("1 para agregar nuevos ingredientes 2 para eliminar 3 para mostrar lista 4 salir"))
    if usuario == 1 :
        ##agregar ingrediente
        ingredienteI = input('Que ingrediente quieres agregar?')
        ingredientes.append(ingredienteI)
        print('Ingrediente agregado')
    elif usuario == 2 :
        ##eliminar ingrediente
        eliminar = input('Que deseas eliminar?')
        if eliminar != ingredientes:
            print("El ingrediente no se encuentra en la lista")
        elif eliminar == ingredientes:
            ingredientes.remove(eliminar)
            print("Ingrediente eliminado")
            ##mostrar lista
    elif  usuario == 3:
        print(ingredientes)
        ##salir del programa
    elif usuario == 4 :
        print('saliste')
        break





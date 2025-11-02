##tienes una lista de ingredientes para pizza. Agrega 3 ingredientes mas, elimina las anchoas
## y muestra el resultado final

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
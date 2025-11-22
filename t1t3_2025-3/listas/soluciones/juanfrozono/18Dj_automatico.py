#Crea una funcion que gestiona una cola de reproduccion musical:
#Agregar albumes completos(multiples canciones)
#Reproducir la siguiente cancion (se elimina de la cola)
#Agregar canciones urgentes  que suenen inmediatamente
#Mostrar siempre las proximas 3 canciones en cola

cola_reproduccion = []
albumes = []

def agg_album():
    albumes.append(str(input("que album desea añadir: ")))
    while True:
        print("agregar cancion (a)")
        print("listo           (b)")
        opcion = str(input("elegir opcion: "))

        if opcion == "a":
            cola_reproduccion.append(str(input("que cancion desea añadir: ")))
        elif opcion == "b":
            print(f'album:{albumes[-1]} añadido')
            break

def repro_siguiente():
    if len(cola_reproduccion) != 0:
        print(f'reproduciendo: {cola_reproduccion[0]}...')
        cola_reproduccion.pop(0)
        print("canciones siguientes:")
        for cancion in cola_reproduccion:
            print(f'-{cancion}')

    else:
        print("cola vacia....")

def urgenteimportante():
    urgente = []
    while True:
        print("agregar cancion (a)")
        print("listo           (b)")
        opcion = str(input("elegir opcion: "))

        if opcion == "a":
            cola_reproduccion.insert(0,str(input("que cancion desea añadir: ")))
            print(f'cancion:{cola_reproduccion[0]} sera la siguiente en reproducirse')

        elif opcion == "b":
            break

def mostrar_album():
    for album in albumes:
        print(album)

def menu():
    while True:
        print("-"*50)
        print("menu")
        print("-"*50)

        print("1-agregar album")
        print("2-reproducir cancion")
        print("3-añadir urgente")
        print("4-mostrar albumes")
        print("5-salir")
        
        print("-"*50)
        opcion = str(input("elegir opcion: "))

        if opcion == "1":
            agg_album()

        if opcion == "2":
            repro_siguiente()

        if opcion == "3":
            urgenteimportante()

        if opcion == "4":
            mostrar_album()

        if opcion == "5":
            print("saliendo")
            break

menu()



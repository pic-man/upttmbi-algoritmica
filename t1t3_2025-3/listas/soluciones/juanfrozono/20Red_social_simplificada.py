#Crea un sistema de post de red social que:
#Agregue nuevos post al inicio(los mas recientes primero)
#puede ordenar posts por cantidad de likes
#Mantenga solo los ultimos 10 posts(elimina los antiguos)
#Permita buscar un post especifico por texto

import random

publis = []
while True:
    print("-"*50)
    print("1. Crear post")
    print("2. Ordenar por likes")
    print("3. Buscar post")
    print("4. Ver post recientes")
    opcion = input("Que desea hacer?: ")
    print("-"*50)

    if opcion == "1":
        publi = []
        print("En que estas pensando?")
        texto = input()
        print("-"*50)
        likes = random.randint(1,1000)
        publi.append(likes)
        publi.append(texto)
        print(f"Tu publicacion obtuvo {likes} likes!")
        publis.append(publi)
        if len(publis) > 10:
            publis.pop(0)

    elif opcion == "2":
        for publi in sorted(publis)[::-1]:
            print(f"Publicacion: {publi[1]}")
            print(f"Likes: {publi[0]}")
            print("-"*50)

    elif opcion == "3":
        print("Que esta buscando?")    
        buscar = input()
        for publi in publis:
            if publi[1] == buscar:
                print(f"Publicacion: {publi[1]}")
                print(f"Likes: {publi[0]}")        

    elif opcion == "4":
        for publi in publis[::-1]:
            print(f"Publicacion: {publi[1]}")
            print(f"Likes: {publi[0]}")
            print("-"*50)
                        
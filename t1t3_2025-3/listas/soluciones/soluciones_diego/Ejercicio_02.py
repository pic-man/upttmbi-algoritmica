def Playlist():
    op=""
    lista = []
    while op!="4":
        print(lista)
        print("Elige Opciones: ")
        print("1.Agregar Canción")
        print("2.Eliminar Canción")
        print("3.Mover a un extremo")
        print("4.Salir")
        op=input("Ingresar Opción: ")
        if op=="1":
            valor=input("Ingresar Canción: ")
            lista.append(valor)
        elif op=="2":
            valor=input("Ingresar dato a eliminar: ")
            j=0
            if len(lista)==0:
                print("Lista Vacia")
            else:
                for i in lista:
                    if i==valor:
                        lista.pop(j)
                        break
                    else:
                        j+=1
                    if j==len(lista):
                        print("Ese dato (a eliminar) no existe")
        elif op=="3":
            if len(lista)==0:
                print("Lista Vacia")
            elif len(lista)<2:
                print("No puedes mover items")
            else:
                valor=input("Ingresar dato a reubicar: ")
                lugar=input("Ingresar ubicacion (0=llevar a izquierda,1=llevar a la derecha): ")
                j=0
                for i in lista:
                    if i==valor:
                        if lugar=="0":
                            lista.pop(j)
                            lista.insert(0,valor)
                            break
                    elif lugar=="1":
                        lista.pop(j)
                        lista.insert(len(lista),valor)
                        break
                    else:
                        j+=1
                    if j==len(lista):
                        print("Ese objeto (a reubicar) no existe")
                else:
                    print("Ingrese opción valida")
        elif op=="4":
            print("Adios")
        else:
            print("Ingrese opción valida")
Playlist()


def DJ():
    lista = []
    op=""
    while op!="3":
        if len(lista)<3:
            print("-----------------------------------------------")
            for i in lista:
                print(i)
            print("-----------------------------------------------")
        else:
            print("-----------------------------------------------")
            for i in range(3):
                print(lista[i])
            print("-----------------------------------------------")
        print("Elige Opciones: ")
        print("1.Agregar Canciones")
        print("2.Reproducir (Eliminar) Canción")
        print("3.Salir")
        op=input("Ingresar Opción: ")
        if op=="1":
            o=input("Ingresar Canción: ")
            p=input("Ingresar Urgentemente (0) // Canción guardada a la cola (1): ")
            if p=="0":
                print("-----------------------------------------------")
                print(o)
                print("-----------------------------------------------")
            elif p=="1":
                lista.append(o)
            else:
                print("-----------------------------------------------")
                print("Ingrese opción valida")
                print("-----------------------------------------------")
        elif op=="2":
            if len(lista)>0:
                print("---------------------------------------------")
                print(lista[0])
                print("---------------------------------------------")
                lista.pop(0)
            else:
                print("-----------------------------------------------")
                print("Lista vacia")
                print("-----------------------------------------------")
        elif op=="3":
            print("Adios")
        else:
            print("-----------------------------------------------")
            print("Ingresar opción valida")
            print("-----------------------------------------------")
DJ()
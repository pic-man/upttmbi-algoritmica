def RPG():
    lista=[]
    op=""
    while op!="5":
        print(lista)
        print("Elige Opciones: ")
        print("1.Agregar Item al Inventario")
        print("2.Verificar si un Item existe")
        print("3.Eliminar Item")
        print("4.Organizar Alfabeticamente")
        print("5.Salir")
        op=input("Ingresar Opción: ")
        if op=="1":
            o=input("Ingresar Item a Lista: ")
            lista.append(o)
        elif op=="2":
            valor=input("Ingresar Item a Verificar: ")
            j=0
            if len(lista)==0:
                print("-----------------------------------------------")
                print("Lista Vacia")
                print("-----------------------------------------------")
            else:
                for i in lista:
                    if i==valor:
                        print("-----------------------------------------------")
                        print("Ese Item si existe en la Lista")
                        print("-----------------------------------------------")
                        break
                    else:
                        j+=1
                    if j==len(lista):
                        print("-----------------------------------------------")
                        print("Ese Item no existe en la Lista")
                        print("-----------------------------------------------")
        elif op=="3":
            valor=input("Ingresar Item a eliminar: ")
            j=0
            if len(lista)==0:
                print("-----------------------------------------------")
                print("Lista Vacia")
                print("-----------------------------------------------")
            else:
                for i in lista:
                    if i==valor:
                        lista.pop(j)
                        break
                    else:
                        j+=1
                    if j==len(lista):
                        print("-----------------------------------------------")
                        print("Ese dato (a eliminar) no existe")
                        print("-----------------------------------------------")
        elif op=="4":
            print("-----------------------------------------------")
            print("Lista original:",lista)
            def ordenar_lista(lista):
                lista.sort()
                return lista
            print("Lista Organizada Alfabeticamente:",ordenar_lista(lista))
            print("-----------------------------------------------")
        elif op=="5":
            print("Adios")
        else:
            print("Ingresar opción valida")
RPG()
def Mago():
    lista = list(range(1, 11))
    op=""
    while op!="2":
        f=lista
        e=[]
        print(lista)
        print("Elige Opciones: ")
        print("1.Desaparecer primer y ultimo numero")
        print("2.Salir")
        op=input("Ingresar Opción: ")
        if op=="1":
            if len(lista)>0:
                e.append(lista[0])
                e.append(len(lista))
                f.pop(0)
                f.pop()
                print("Lista:",f)
                print("Items Eliminados:",e)
            else:
                print("Lista vacia")
        elif op=="2":
            print("Adios")
        else:
            print("Ingresar opción valida")
Mago()
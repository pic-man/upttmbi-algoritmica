def Fusion():
    lista=[]
    lista1=["hamburguesa", "pizza", "ensalada", "sopa"]
    lista2=["pizza", "pasta", "ensalada", "tacos"]
    print(lista1)
    print(lista2)
    print("Elige Opciones: ")
    print("1.Fusionar Listas")
    print("2.Salir")
    op=input("Ingresar Opción: ")
    if op=="1":
        for i in lista1:
            k=0
            for j in lista2:
                if i==j:
                    lista2.pop(k)
                else:
                    k+=1
        lista=lista1+lista2
        print(lista)
        op="2"
    elif op=="2":
        print("Adios")
    else:
        print("Ingrese opción valida")
Fusion()
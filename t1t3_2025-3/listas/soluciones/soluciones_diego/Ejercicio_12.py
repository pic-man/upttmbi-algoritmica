def Colores():
    lista = ["rojo", "verde", "azul", "amarillo"]
    op=""
    while op!="3":
        print(lista)
        print("Elige Opciones: ")
        print("1.Agregar Color")
        print("2.Mostrar Listas de Colores")
        print("3.Salir")
        op=input("Ingresar Opción: ")
        if op=="1":
            p=input("Ingresar Color: ")
            o=input("Ingresar Ubicación (0=izquierda,1=derecha): ")
            if o=="0":
                lista.insert(0,p)
            elif o=="1":
                lista.append(p)
            else:
                print("Ingrese opción valida")
            print(lista)
        elif op=="2":
            j=[]
            h=len(lista)
            while h > 0:
                j.append(lista[h-1])
                h-=1
            print("-------------------------------------------------")
            print(lista)
            print(j)
            print("-------------------------------------------------")
        elif op=="3":
            print("Adios")
        else:
            print("Ingresar opción valida")
Colores()
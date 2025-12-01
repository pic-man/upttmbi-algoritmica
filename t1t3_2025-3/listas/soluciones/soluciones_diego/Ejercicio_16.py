def Numeros():
    lista=[]
    j=[]
    op=""
    while op!="3":
        print(lista)
        print("Elige Opciones: ")
        print("1.Agregar Numeros a la Lista")
        print("2.Realizar Truco")
        print("3.Salir")
        op=input("Ingresar Opción: ")

        if op=="1":
            o=input("Ingresar Número a Lista: ")
            lista.append(o)
            j.append(o)
        elif op=="2":
            h=0
            for i in range(3):
                if len(lista)>4:
                    lista.insert(0,lista[len(lista)-1])
                    lista.pop()
                    h=1
                else:
                    print("Lista carente de items suficientes para realizar truco (necesita al menos 5 items)")
                    break
            if h==1:
                print("Lista original:",j)
                print("Lista Trucada:",lista)
                op="3"
        elif op=="3":
            print("Adios")
        else:
            print("Ingresar opción valida")
Numeros()
def PizzeriaLoca():
    op=""
    lista = ["queso", "tomate", "anchoas", "jamón"]
    while op!="3":
        print(lista)
        print("Elige Opciones: ")
        print("1.Agregar Ingrediente")
        print("2.Eliminar Ingrediente")
        print("3.Salir")
        op=input("Ingresar Opción: ")
        if op=="1":
            valor=input("Ingresar Ingrediente: ")
            lista.append(valor)
        elif op=="2":
            valor=input("Ingresar dato a eliminar: ")
            j=0
            for i in lista:
                if i==valor:
                    lista.pop(j)
                    break
                else:
                    j+=1
                if j==len(lista):
                    print("Ese dato (a eliminar) no existe")
        elif op=="3":
            print("Adios")
        else:
            print("Ingrese opción valida")
PizzeriaLoca()


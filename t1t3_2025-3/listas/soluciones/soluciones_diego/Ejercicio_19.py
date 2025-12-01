def SM():
    lista1 = []
    lista2 = {"manzana": 2, "pan": 1.5, "leche": 3, "huevos": 4}
    op=""
    while op!="5":
        print(lista1)
        print("Elige Opciones: ")
        print("1.Agrega un producto (manzana (2$) / pan (1.5$) / leche (3$) / huevos (4$))")
        print("2.Calcular la Cantidad de cada Producto")
        print("3.Eliminar un Producto de la Lista")
        print("4.Calcular Precio Total de Lista de Compras")
        print("5.Salir")
        op=input("Ingresar Opción: ")

        if op=="1":
            o=input("Ingresar Producto: ")
            if o=="manzana" or o=="pan" or o=="leche" or o=="huevos":
                lista1.append(o)
            else:
                print("--------------------------------------------")
                print("Producto no Disponible")
                print("--------------------------------------------")
        elif op=="2":
            if len(lista1)>0:
                j=0
                k=0
                l=0
                m=0
                for i in lista1:
                    if i=="manzana":
                        j+=1
                    if i=="pan":
                        k+=1
                    if i=="leche":
                        l+=1
                    if i=="huevos":
                        m+=1
                print("--------------------------------------------")
                print("Cantidad de manzanas:",j)
                print("Cantidad de panes:",k)
                print("Cantidad de leche:",l)
                print("Cantidad de huevos:",m)
                print("--------------------------------------------")
            else:
                print("-----------------------------------------------")
                print("Lista Vacia")
                print("-----------------------------------------------")
        elif op=="3":
            valor=input("Ingresar Producto a eliminar: ")
            j=0
            if len(lista1)==0:
                print("-----------------------------------------------")
                print("Lista Vacia")
                print("-----------------------------------------------")
            else:
                for i in lista1:
                    if i==valor:
                        lista1.pop(j)
                        break
                    else:
                        j+=1
                    if j==len(lista1):
                        print("-----------------------------------------------")
                        print("Ese Producto (a eliminar) no existe")
                        print("-----------------------------------------------")
        elif op=="4":
            if len(lista1)>0:
                j=0
                for i in lista1:
                    if i=="manzana":
                        j+=2
                    if i=="pan":
                        j+=1.5
                    if i=="leche":
                        j+=3
                    if i=="huevos":
                        j+=4
                print("--------------------------------------------")
                print("Precio Total de la Lista de Compras:",j,"$")
                print("--------------------------------------------")
            else:
                print("-----------------------------------------------")
                print("Lista Vacia")
                print("-----------------------------------------------")
        elif op=="5":
            print("Adios")
        else:
            print("Ingresar opción valida")
SM()
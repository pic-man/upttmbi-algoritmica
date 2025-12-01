def RSS():
    lista1 = []
    lista2 = []
    op=""
    while op!="5":
        if len(lista1)>0:
            k=0
            print("----------------------------------------")
            for i in lista1:
                print(i,lista2[k])
                k+=1
            print("----------------------------------------")
        else:
            print(lista1)
        print("Elige Opciones: ")
        print("1.Chatear y Publicar")
        print("2.Ordenar por likes")
        print("3.Eliminar Post Antiguos (Los diez más antiguos)")
        print("4.Buscar Post")
        print("5.Salir")
        op=input("Ingresar Opción: ")

        if op=="1":
            o=input("Ingresar Post: ")
            p=int(input("Ingresar Likes del Post (Numeros): "))
            lista1.append(o)
            lista2.append(p)
        elif op=="2":
            if len(lista1)>0:
                for e in lista2:
                    k=0
                    for i in lista2:
                        if i<lista2[k+1]:
                            g=lista2[k+1]
                            lista2[k+1]=lista2[k]
                            lista2[k]=g
                            ###################################
                            g=lista1[k+1]
                            lista1[k+1]=lista1[k]
                            lista1[k]=g

                            if k<len(lista2)-2:k+=1
                        else:
                            if k<len(lista2)-2:k+=1
            else:
                print("Chat vacio")
        elif op=="3":
            if len(lista1)>10:
                for i in range(10):
                    lista1.pop(0)
                    lista2.pop(0)
            elif len(lista1)>0:
                print("----------------------------------------")
                print("Chat muy corto como para eliminar posts (debe tener más de diez posts para poder eliminar posts)")
            else:
                print("Chat vacio")
        elif op=="4":
            if len(lista1)>0:
                o=input("Ingresar Post a Buscar: ")
                k=0
                for i in lista1:
                    if i==o:
                        print("El Post",o,"Existe y es el número",k+1,"(hacia abajo)")
                        break
                    else:
                        k+=1
                    if k==len(lista1):print("Ese Post no existe en el Chat")
            else:
                print("Chat vacio")
        elif op=="5":
            print("----------------------------------------")
            print("De vuelta al Menú")
            print("----------------------------------------")
        else:
            print("----------------------------------------")
            print("Ingresar opción valida")
            print("----------------------------------------")
RSS()
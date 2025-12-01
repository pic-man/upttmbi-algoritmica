def Carrera():
    lista = ["Ana", "Bruno", "Carlos", "Diana", "Elena"]
    j = ["Ana", "Bruno", "Carlos", "Diana", "Elena"]
    op=""
    while op!="2":
        print(lista)
        print("Elige Opciones: ")
        print("1.Adelantar Atleta")
        print("2.Salir")
        op=input("Ingresar Opción: ")
        if op=="1":
            o=input("Elegir Atleta: ")
            p=input("Elige la cantidad de posiciones que ese Atleta se adelanta: ")
            k=0
            g=0
            for i in j:
                if o==i:
                    if k+int(p)>=len(j):
                        print("Cantidad de posiciones mayor a la cantidad de items de la lista")
                        break
                    else:
                        g=j[k+int(p)]
                        j[k+int(p)]=j[k]
                        j[k]=g
                        print("-------------------------------------------------")
                        print(lista)
                        print(j)
                        print("-------------------------------------------------")
                        break
                else:
                    k+=1
                if k==len(j):
                    print("Nombre de Atleta inexistente")
        elif op=="2":
            print("Adios")
        else:
            print("Ingresar opción valida")
Carrera()
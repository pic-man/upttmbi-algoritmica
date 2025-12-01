def Cleaner():
    lista = [1, 2, None, 3, 2, 4, None, 1, 5, 3]
    op=""
    while op!="2":
        print(lista)
        print("Elige Opciones: ")
        print("1.Limpiar Lista")
        print("2.Salir")
        op=input("Ingresar Opción: ")
        if op=="1":
            g=0
            for i in lista:
                if i==None:
                    lista.pop(g)
                g+=1
            g=0
            for i in lista:
                e=0
                while e<len(lista):
                    if i==lista[g]:
                        lista.pop(g)
                    e+=1
            print(lista)
            op="2"
        elif op=="2":
            print("Adios")
        else:
            print("Ingresar opción valida")
Cleaner()
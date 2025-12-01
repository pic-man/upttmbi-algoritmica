def Ranking():
    lista = [450, 890, 320, 670, 1200, 550, 890]
    op=""
    while op!="2":
        print(lista)
        print("Elige Opciones: ")
        print("1.Rankear Lista")
        print("2.Salir")
        op=input("Ingresar Opción: ")
        j=0
        k=0
        g=0
        if op=="1":
            if len(lista)>2:
                for i in lista:
                    if i > j:
                        j=i
                for i in lista:
                    if i > g and i != j:
                        g=i
                for i in lista:
                    if i > k and i != j and i != g:
                        k=i
                print("Primer Lugar:",j)
                print("Segundo Lugar:",g)
                print("Tercer Lugar:",k)
            else:
                print("Lista vacia")
        elif op=="2":
            print("Adios")
        else:
            print("Ingresar opción valida")
Ranking()
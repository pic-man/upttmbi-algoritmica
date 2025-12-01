def Invertir():
    lista = ["Nacimiento", "Escuela", "Universidad", "Trabajo", "Jubilación"]
    e=[]
    j=len(lista)
    #print(lista)
    op=""
    while op!="2":
        print(lista)
        print("Elige Opciones: ")
        print("1.Invertir")
        print("2.Salir")
        op=input("Ingresar Opción: ")
        if op=="1":
            while j > 0:
                e.append(lista[j-1])
                j-=1
            print("----------------------------------------------------------------")
            print(lista)
            print(e)
            print("----------------------------------------------------------------")
        elif op=="2":
            print("Adios")
        else:
            print("Ingresar opción valida")
Invertir()
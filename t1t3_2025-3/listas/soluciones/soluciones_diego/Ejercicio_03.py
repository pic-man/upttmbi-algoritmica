def Score():
    op=""
    lista = ["50", "100", "75", "100", "90", "100", "85", "100"]
    while op!="2":
        print(lista)
        print("Elige Opciones: ")
        print("1.Saber la frecuencia con la que aparece un puntaje")
        print("2.Salir")
        op=input("Ingresar Opción: ")
        if op=="1":
            valor=input("Ingresar dato para saber su recurrencia en la lista: ")
            j=0
            k=0
            for i in lista:
                if i==valor:
                    j+=1
                else:
                    if j==0:
                        k+=1
            if j==0:
                k=j
            else:
                k+=1
            print("Ese valor aparece",j,"veces y su primera apareción fue en la posición:",k)
        elif op=="2":
            print("Adios")
        else:
            print("Ingrese opción valida")
Score()


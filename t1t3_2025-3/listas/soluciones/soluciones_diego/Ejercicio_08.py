def Biblioteca():
    lista = [
    {"titulo": "El Hobbit", "paginas": 310},
    {"titulo": "1984", "paginas": 328},
    {"titulo": "El Principito", "paginas": 96}
    ]
    op=""
    while op!="2":
        print(lista)
        print("Elige Opciones: ")
        print("1.Organizar Lista")
        print("2.Salir")
        op=input("Ingresar Opción: ")
        if op=="1":
            j=lista
            k=1
            for i in j:
                if i["paginas"]<j[k]["paginas"]:
                    print(i["paginas"],j[k]["paginas"])
                    e=i
                    g=j[k]
                    j[k-1]=g
                    j[k]=e
                if k < len(j)-1:k+=1
            print("-------------------------------------")
            for i in j:
                print("Libro:",i["titulo"],"paginas:",i["paginas"])
            print("-------------------------------------")
            op="2"
        elif op=="2":
            print("Adios")
        else:
            print("Ingresar opción valida")
Biblioteca()
def Cine():
    lista = [
    ("Matrix", 1999),
    ("Inception", 2010),
    ("Titanic", 1997),
    ("Avatar", 2009)
    ]
    j=lista
    op=""
    while op!="2":
        print(lista)
        print("Elige Opciones: ")
        print("1.Organizar Películas")
        print("2.Salir")
        op=input("Ingresar Opción: ")
        if op=="1":
            print(lista)
            j=lista
            for p in j:
                k=1
                for i in j:
                    if i[1]<j[k][1]:
                        e=i
                        g=j[k]
                        j[k-1]=g
                        j[k]=e
                    if k < len(j)-1:k+=1
            print(j)
            while len(j)>1:
                j.pop()
            print(j)
            op="2"
        elif op=="2":
            print("Adios")
        else:
            print("Ingresar opción valida")
Cine()

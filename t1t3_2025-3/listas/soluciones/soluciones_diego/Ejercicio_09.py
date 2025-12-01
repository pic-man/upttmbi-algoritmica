import random
def Dados():
    op=""
    while op!="2":
        lista=[]
        j=[]
        g=[]
        for i in range(20):lista.append(random.randint(1,6))
        for i in range(7):j.append(i)
        for i in range(7):g.append(0)
        j.pop(0)
        g.pop(0)
        print("Elige Opciones: ")
        print("1.Tirar los dados")
        print("2.Salir")
        op=input("Ingresar Opción: ")
        if op=="1":
            print(lista)
            k=0
            for i in j:
                for e in lista:
                    if e == i:
                        g[k]+=1
                k+=1
            for i in j:
                print("Numero:",i,"veces en las que se repite:",g[i-1])
        elif op=="2":
            print("Adios")
        else:
            print("Ingresar opción valida")
Dados()
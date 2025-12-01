import random
def Rol():
    lista1=["Guerrero", "Mago", "Arquero"]
    lista2=[100,100,100]
    lista3=["Orco", "Goblin", "Troll"]
    lista4=[100,100,100]
    op=""
    while op!="2":
        if len(lista1)>0 and len(lista3)>0:
            print("----------------------------------------")
            print(lista1[0],"PH",lista2[0],"⚔️ ",lista3[0],"PH",lista4[0])
            print("----------------------------------------")
            k=0
            while k<len(lista1):
                print(lista1[k],"PH",lista2[k])
                k+=1
            k=0
            print("----------------------------------------")
            while k<len(lista3):
                print(lista3[k],"PH",lista4[k])
                k+=1
            print("----------------------------------------")
        elif len(lista2)>0:
            print("----------------------------------------")
            print("Y el ganador es:",lista1)
            print("----------------------------------------")
            op="2"
        elif len(lista4)>0:
            print("----------------------------------------")
            print("Y el ganador es:",lista3)
            print("----------------------------------------")
            op="2"
        if op!="2":
            print("Elige Opciones: ")
            print("1.Play (batalla)")
            print("2.Salir")
            op=input("Ingresar Opción: ")
        if op=="1":
            if len(lista1)>0 and len(lista3)>0:
                a=random.randint(20,50)
                b=random.randint(20,50)
                lista2[0]-=a
                lista4[0]-=b
                if lista2[0]<=0:
                    lista1.pop(0)
                    lista2.pop(0)
                if lista4[0]<=0:
                    lista3.pop(0)
                    lista4.pop(0)
                if len(lista2)>0:
                    if lista2[0]>0:
                        lista2.append(lista2[0])
                        lista2.pop(0)
                        #########################################
                        lista1.append(lista1[0])
                        lista1.pop(0)
                if len(lista4)>0:
                    if lista4[0]>0:
                        lista4.append(lista4[0])
                        lista4.pop(0)
                        #########################################
                        lista3.append(lista3[0])
                        lista3.pop(0)
        elif op=="2":
            print("----------------------------------------")
            print("De vuelta al Menú")
            print("----------------------------------------")
        else:
            print("----------------------------------------")
            print("Ingresar opción valida")
            print("----------------------------------------")
Rol()
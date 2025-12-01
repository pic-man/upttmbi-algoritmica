import random
def Tragamonedas():
    lista = ["🍒", "🍋", "🔔", "💎", "7️⃣ "]
    op=""
    while op!="2":
        print(lista)
        print("Elige Opciones: ")
        print("1.Probar suerte")
        print("2.Salir")
        op=input("Ingresar Opción: ")
        if op=="1":
            a=random.randint(1,5)
            b=random.randint(1,5)
            c=random.randint(1,5)
            a=lista[a-1]
            b=lista[b-1]
            c=lista[c-1]
            d=""
            e=""
            if a==b and b==c:
                d="Todos Iguales"
                e="💰"
            elif a==b or b==c:
                d="Un par Iguales"
                e="🎁"
            else:
                d="Todos Diferentes"
                e="😢"
            print("-------------------------------------------------")
            print(a,":",b,":",c)
            print(d,":",e)
            print("-------------------------------------------------")
        elif op=="2":
            print("Adios")
        else:
            print("Ingresar opción valida")
Tragamonedas()
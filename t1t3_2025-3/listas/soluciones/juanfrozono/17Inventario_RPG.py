#Crea un sistema de inventario para un juego RPG que permita:
#1 Recoger objetos (pueden ser del mismo tipo)
#2 Verificar si tienes un objeto especifico y cuantos
#3 Usar/Vender objetos(elimina uno a la vez)
#4 Organizar el inventario alfabeticamente

inventario = []

def recoger(x):
    inventario.append(x)
    print(f'Has agarrado {x}')


def ver():
    inventario2 = []
    for objeto in inventario:
        if objeto not in inventario2:
            inventario2.append(objeto)
   
    print("Tu inventario: ")
    for objeto in inventario2:        
        print(f'{objeto} x{inventario.count(objeto)}')
       

def usar_vender(x):
    if x in inventario:
        inventario.remove(x)
        print(f'Se ha removido {x}')
    else:
        print("El objeto que deseas eliminar no está en tu inventario")    
    


def organizar():
    inventario.sort()    
    print("Se ha organizado")

def menu():
    while True:
        print("-"*50)

        print("Menu: ")
        print("a-Recoger objeto")
        print("b-Ver inventario")
        print("c-Usar/Vender objetos")
        print("d-Organizar inventario")
        print("e-Salir") 
        print("-"*50)
        op = input(str("Elige una opcion: "))
        print("-"*50)

        if op == "a":
            recoger(input(str("que objeto deseas recoger: ")))
        if op == "b":
            ver()
        if op == "c":
            usar_vender(input(str("que objeto quieres vender o usar: ")))
        if op == "d":
            organizar()
        if op == "e":
            print("Saliste del inventario")
            break 
        

menu()


































































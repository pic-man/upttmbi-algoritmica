#Crea un sistema que maneje un carrito de compras donde:
#Puedas agregar productos (pueden repetirse)
#Calcule la cantidad de cada producto
#Puedas eliminar productos especificos uno a uno
#Calcule el total de la compra agrupando por producto

carrito = []


productos = ["manzana","pan","leche","huevos"]
precios   = [2,1.5,3,4]

def agg(producto):
    if producto in productos:
        carrito.append(producto)
        print(f'{producto} agregado al carrito')
    else:
        print("no hay ese producto")

def ver_carrito():
    carrito2 = []
    for producto in carrito:
        if producto not in carrito2:
            carrito2.append(producto)
   
    print("Tus compras: ")
    for producto in carrito2:
        print(f'{producto} x{carrito.count(producto)}')

def eliminar_p(producto):
    if producto in carrito:
        carrito.remove(producto)
        print(f'Se ha eliminado {producto}')
    else:
        print("No tienes ese producto en tu carrito")  

def costo():
    costo_total = 0
    
    for producto in carrito:
        costo_total += precios[productos.index(producto)]

    print(f'El costo total es:{costo_total}')

def menu():
    while True:
        print("-"*50)

        print("Menu: ")
        print("1-Agregar producto")
        print("2-Ver carrito")
        print("3-Eliminar producto")
        print("4-Costo total")
        print("5-Salir") 
        print("-"*50)
        op = int(input("Elige una opcion: "))
        print("-"*50)

        if op == 1:
            agg(input(str("que producto deseas comprar: ")))
        if op == 2:
            ver_carrito()
        if op == 3:
            eliminar_p(input(str("que producto ya no quieres comprar: ")))
        if op == 4:
            costo()
        if op == 5:
            print("Saliste del supermercado")
            break 
        

menu()





















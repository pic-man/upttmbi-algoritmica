"""
Ejemplo avanzado combinando for, while, break y continue.
Simula un sistema de inventario básico con menú interactivo.
"""

inventario = {"manzanas": 10, "naranjas": 8, "bananas": 5}

MENU = """
=== Inventario de Frutas ===
1) Mostrar inventario
2) Registrar entrada
3) Registrar salida
4) Buscar producto
5) Salir
Selecciona una opción: """


def mostrar_inventario():
    print("\nInventario actual:")
    if not inventario:
        print("No hay productos registrados.")
        return
    for producto, cantidad in inventario.items():
        print(f"- {producto.title()}: {cantidad} unidades")
    print()


def registrar_movimiento(accion):
    producto = input("Nombre del producto: ").strip().lower()
    if not producto:
        print("Nombre inválido.\n")
        return

    try:
        unidades = int(input("Cantidad: "))
    except ValueError:
        print("La cantidad debe ser un número entero.\n")
        return

    if unidades <= 0:
        print("La cantidad debe ser positiva.\n")
        return

    if accion == "entrada":
        inventario[producto] = inventario.get(producto, 0) + unidades
        print(f"Se agregaron {unidades} {producto}. Total: {inventario[producto]}.\n")
    else:
        if producto not in inventario:
            print("El producto no existe en el inventario.\n")
            return
        if inventario[producto] < unidades:
            print("No hay suficiente stock para realizar la salida.\n")
            return
        inventario[producto] -= unidades
        print(f"Se retiraron {unidades} {producto}. Total: {inventario[producto]}.\n")
        if inventario[producto] == 0:
            print("Producto agotado. Se eliminará del inventario.")
            del inventario[producto]
            print()


def buscar_producto():
    termino = input("¿Qué producto buscas?: ").strip().lower()
    coincidencias = [p for p in inventario if termino in p]
    if coincidencias:
        print("Coincidencias encontradas:")
        for producto in coincidencias:
            print(f"- {producto.title()}: {inventario[producto]} unidades")
        print()
    else:
        print("No se encontraron coincidencias.\n")


while True:
    opcion = input(MENU).strip()

    if opcion == "1":
        mostrar_inventario()
    elif opcion == "2":
        registrar_movimiento("entrada")
    elif opcion == "3":
        registrar_movimiento("salida")
    elif opcion == "4":
        buscar_producto()
    elif opcion == "5":
        print("Hasta luego. ¡Sigue practicando!")
        break
    else:
        print("Opción no válida. Intenta nuevamente.\n")


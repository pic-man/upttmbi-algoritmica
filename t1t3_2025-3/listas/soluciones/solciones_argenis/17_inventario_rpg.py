"""Ejercicio 17: [Inventario RPG]
Estudiante: [Argenis Saul Linares Moncayo]
GitHub: @[argenis183]
Fecha: [27/11/2025]

Descripción:
[Permite al usuario gestionar un inventario RPG]
Ejemplo de uso:
[Selecciona una opccion del 1 al 6]"""
inventario =[]
def recojer_objeto(objeto):
    global inventario
    while True:
        opcion = float(input('Ingresa 1 para agregar el objeto al inventario o 2 para salir: '))
        if opcion == 1:
            objeto_agregado = input('Ingresa el objeto a agregar: ')
            inventario.append(objeto_agregado)
        elif opcion == 2:
            break
        return opcion
    
def contar_objetos():
    global inventario
    while True:
        opcion = float(input('Ingresa 1 para contar un objeto en el inventario o 2 para salir: '))
        if opcion == 1:
            objeto_a_contar = input('Ingresa el objeto a contar: ').lower()
            cantidad = inventario.count(objeto_a_contar)
            print(f'El inventario tiene {cantidad} {objeto_a_contar}(s).')
        elif opcion == 2:
            break
        return opcion

def usar_objeto():
    global inventario
    while True:
        opcion = input('Ingresa 1 para usar un objeto del inventario o 2 para salir: ')
        if opcion == '1':
            objeto_a_usar = input('Ingresa el objeto a usar: ').lower()
            if objeto_a_usar in inventario:
                inventario.remove(objeto_a_usar)
                print(f'Has usado un {objeto_a_usar}.')
            else:
                print(f'{objeto_a_usar} no esta el inventario.')
        elif opcion == '2':
            break
        return opcion

def organizar_inventario():
    global inventario
    while True:
        opcion = float(input('Ingresa 1 para organizar el inventario o 2 para salir: '))
        if opcion == 1:
            inventario.sort()
            print('Inventario organizado:', inventario)
        elif opcion == 2:
            break
        return opcion

def mostrar_inventario(inventario):
    while True:
        opcion = float(input('Ingresa 1 para mostrar el inventario o 2 para salir: '))
        if opcion == 1:
            print('Inventario actual:', inventario)
        elif opcion == 2:
            break
        return opcion

def main():
    while True:
        print('\n--- Menu de Inventario RPG ---')
        print('1. Recojer objeto')
        print('2. Contar objetos')
        print('3. Usar objeto')
        print('4. Organizar inventario')
        print('5. Mostrar inventario')
        print('6. Salir')
        
        eleccion = float(input('Selecciona una opcion (1-6): '))
        
        if eleccion == 1:
            recojer_objeto(objeto=None)
        elif eleccion == 2:
            contar_objetos()
        elif eleccion == 3:
            usar_objeto()
        elif eleccion == 4:
            organizar_inventario()
        elif eleccion == 5:
            mostrar_inventario(inventario)
        elif eleccion == 6:
            print('Saliendo del inventario RPG. ¡Hasta luego!')
            break
        else:
            print('Opcion no valida. Por favor, intenta de nuevo.')

main()
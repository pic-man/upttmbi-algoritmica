#Ejercico 20: Menu Interactivo
#Estudiante : Jheferson Manuel Duran Marin
#GitHub: Jheferson1213
#Fecha:2025,11,30
print("Menú Interactivo")
contador_visitas = 0
while True:
    contador_visitas += 1
    print("--- Menú Principal ---")
    print("1) Mostrar saludo")
    print("2) Calcular cuadrado de un número")
    print("3) Mostrar contador de visitas")
    print("4) Salir")
    opcion1 = input("Selecciona una opción: ")
    opcion = int(opcion1)
    if opcion == 1:
        print("Hola, bienvenido al menú interactivo.")
    elif opcion == 2:
        num1 = input("Ingresa un número: ")
        num = int(num1)
        cuadrado = num * num
        print(num, "al cuadrado es", cuadrado, ".")
    elif opcion == 3:
        print("Has consultado el menú", contador_visitas, "veces.")
    elif opcion == 4:
        print("Saliendo... ¡Hasta luego!")
        break 
    else:
        print("Opción no válida. Inténtalo de nuevo.")

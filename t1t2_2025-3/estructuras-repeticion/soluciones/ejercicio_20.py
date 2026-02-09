#opcion = "4"
while opcion != "4":
    print("1) Saludo  2) Cuadrado  3) Par/Impar  4) Salir")
    opcion = input("Opción: ")
    if opcion == "1":
        nombre = input("Tu nombre: ")
        print(f"¡Hola, {nombre}!")
    elif opcion == "2":
        num = float(input("Número: "))
        print(f"Cuadrado: {num * num}")
    elif opcion == "3":
        num = int(input("Número: "))
        if num % 2 == 0:
            print("Es PAR")
        else:
            print("Es IMPAR")
print("¡Hasta luego!")
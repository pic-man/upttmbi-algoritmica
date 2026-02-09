# Ejercicio 17: Simulación de Cajero
saldo = 1000.00
opcion = ""
while opcion != "4":
    print("\n1) Consultar  2) Depositar  3) Retirar  4) Salir")
    opcion = input("Opción: ")
    if opcion == "1":
        print(f"Saldo: ${saldo:.2f}")
    elif opcion == "2":
        monto = float(input("Monto: "))
        saldo = saldo + monto
    elif opcion == "3":
        monto = float(input("Monto: "))
        saldo = saldo - monto
print("¡Gracias!")

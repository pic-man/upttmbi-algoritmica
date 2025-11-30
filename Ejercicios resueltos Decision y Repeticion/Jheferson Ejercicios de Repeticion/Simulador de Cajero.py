#Ejercico 17: Cajero Automatico
#Estudiante : Jheferson Manuel Duran Marin
#GitHub: Jheferson1213
#Fecha:2025,11,30
print(" Simulación de Cajero")
saldo = 1000.00
opcion = 0
while True:
    print("--- Cajero Automático ---")
    print("1) Consultar saldo")
    print("2) Depositar")
    print("3) Retirar")
    print("4) Salir")
    opcion_1 = input("Selecciona una opción: ")
    opcion = int(opcion_1)
    if opcion == 1:
        print("Saldo actual:", round(saldo, 2))
    elif opcion == 2:
        monto_deposito_1 = input("Monto a depositar: ")
        monto_deposito = float(monto_deposito_1)
        if monto_deposito > 0:
            saldo += monto_deposito
            print("Depósito exitoso. Nuevo saldo:", round(saldo, 2))
        else:
            print("Monto de depósito no válido.")
    elif opcion == 3:
        monto_retiro_1 = input("Monto a retirar: ")
        monto_retiro = float(monto_retiro_1)
        if monto_retiro <= 0:
            print("Monto de retiro no válido.")
        elif monto_retiro > saldo:
            print("Fondos insuficientes. Tu saldo es de", round(saldo, 2))
        else:
            saldo -= monto_retiro
            print("Retiro exitoso. Nuevo saldo:", round(saldo, 2))    
    elif opcion == 4:
        print("¡Gracias por usar el cajero!")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")

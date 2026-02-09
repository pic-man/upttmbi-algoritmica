# Ejercicio 12: Intentos de Contraseña
CONTRASENA = "python123"
intentos = 0
acceso = False
while intentos < 3 and acceso == False:
    entrada = input("Ingresa la contraseña: ")
    intentos = intentos + 1
    if entrada == CONTRASENA:
        acceso = True
    else:
        print(f"Incorrecta. Intentos restantes: {3 - intentos}")
if acceso:
    print("¡Acceso concedido!")
else:
    print("Acceso bloqueado.")

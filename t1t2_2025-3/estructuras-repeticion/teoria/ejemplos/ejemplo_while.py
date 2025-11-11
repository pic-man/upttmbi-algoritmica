"""
Ejemplo Básico de ciclo while
Solicita al usuario una contraseña con un máximo de intentos.
"""

PASSWORD = "python123"
MAX_INTENTOS = 3

intentos = 0
acceso_concedido = False

while intentos < MAX_INTENTOS:
    ingreso = input("Ingresa la contraseña: ")
    intentos += 1

    if ingreso == PASSWORD:
        acceso_concedido = True
        break

    intentos_restantes = MAX_INTENTOS - intentos
    if intentos_restantes:
        print(f"Contraseña incorrecta. Intentos restantes: {intentos_restantes}")

if acceso_concedido:
    print("✅ Acceso concedido.")
else:
    print("❌ Acceso bloqueado. Intenta más tarde.")


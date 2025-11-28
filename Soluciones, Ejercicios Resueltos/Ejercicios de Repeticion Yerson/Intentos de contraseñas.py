#Ejercico 12: Intentos Contraseña
#Estudiante:Yerson Josue Saavedra Barrios
#GitHub:Yerson17
#Fecha:2025-11-28
print("Intentos de Contraseñas")
CONTRASENA_SECRETA = "algoritmica"
MAX_INTENTOS = 3
intentos = 0
acceso_concedido = False
while intentos < MAX_INTENTOS:
    contrasena_ingresada = input("Ingresa la contraseña: ")
    intentos += 1
    if contrasena_ingresada == CONTRASENA_SECRETA:
        acceso_concedido = True
        break
    else:
        intentos_restantes = MAX_INTENTOS - intentos
        if intentos_restantes > 0:
            print("Contraseña incorrecta. Intentos restantes:", intentos_restantes)
if acceso_concedido:
    print("¡Acceso concedido!")
else:
    print("Acceso bloqueado. Intenta más tarde.")

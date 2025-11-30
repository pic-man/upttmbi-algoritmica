#Ejercico 10: Login Simple
#Estudiante : Jheferson Manuel Duran Marin
#GitHub: Jheferson1213
#Fecha:2025,11,30
USUARIO_CORRECTO = "admin"
PASSWORD_CORRECTA = "1234"
print("=== SISTEMA DE LOGIN ===")
print()
usuario = input("Usuario: ")
password = input("Contraseña: ")
print()
if usuario == USUARIO_CORRECTO and password == PASSWORD_CORRECTA:
    print("¡Acceso concedido!")
    print("Bienvenido,",usuario)
elif usuario != USUARIO_CORRECTO and password != PASSWORD_CORRECTA:
    print(" Acceso denegado")
    print("Usuario y contraseña incorrectos")
elif usuario != USUARIO_CORRECTO:
    print(" Acceso denegado")
    print("Usuario incorrecto")
else: 
    print(" Acceso denegado")
    print("Contraseña incorrecta")
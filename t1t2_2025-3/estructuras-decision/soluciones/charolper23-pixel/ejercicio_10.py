"""
Ejercicio 10: Login Simple
Estudiante: Yudith Perdomo
GitHub: @charolper23-pixel
Fecha: 29-10-2025

Descripción:
Verifica las credenciales de usuario.

Ejemplo de uso:
Entrada: usuario123, contraseña456
Salida: Contraseña incorrecta
"""

# Definir credenciales correctas
usuario_correcto = "admin"
contrasena_correcta = "12345"

# Solicitar credenciales al usuario
usuario = input("Ingresa tu nombre de usuario: ")
contrasena = input("Ingresa tu contraseña: ")

# Verificar credenciales
if usuario != usuario_correcto:
    print("Nombre de usuario incorrecto")
elif contrasena != contrasena_correcta:
    print("Contraseña incorrecta")
else:
    print("Inicio de sesión exitoso")

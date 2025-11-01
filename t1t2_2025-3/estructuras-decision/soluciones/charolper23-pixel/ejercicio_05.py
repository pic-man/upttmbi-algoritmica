"""
Ejercicio 5: Elegir Deporte
Muestra un deporte según el número elegido por el usuario.
"""

# Solicitar un número al usuario del 1 al 3
numero = int(input("Ingresa un número del 1 al 3: "))

# Mostrar el deporte correspondiente
if numero == 1:
    print("Fútbol")
elif numero == 2:
    print("Basquetbol")
elif numero == 3:
    print("Natación")
else:
    print("Opción no válida, debe ser 1,2 o 3")
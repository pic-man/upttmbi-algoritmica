"""
Ejercicio 20: Menú del Día
Estudiante: Yudith Perdomo
GitHub: @charolper23-pixel
Fecha: 01-11-2025

Descripción:
Muestra el platillo especial según el día de la semana.

Ejemplo de uso:
Entrada: lunes
Salida: Platillo del día: Enchiladas verdes
"""

print("=== RESTAURANTE YUDITH ===\n")

# Solicitar el día de la semana
dia = input("Por favor ingrese un dia para obtener el menú disponible: ").lower()

# Mostrar el platillo según el día
if dia == "lunes":
    print("Platillo del día: Enchiladas verdes")
elif dia == "martes":
    print("Platillo del día: Tacos al pastor")
elif dia == "miércoles" or dia == "miercoles":
    print("Platillo del día: Pozole")
elif dia == "jueves":
    print("Platillo del día: Mole con pollo")
elif dia == "viernes":
    print("Platillo del día: Pescado a la veracruzana")
elif dia == "sábado" or dia == "sabado":
    print("Platillo del día: Barbacoa")
elif dia == "domingo":
    print("Platillo del día: Menudo")
else:
    print("Día no válido")
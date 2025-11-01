"""
Ejercicio 14: Distancia a Recorrer
Estudiante: Yudith Perdomo
GitHub: @charolper23-pixel
Fecha: 01-11-2025

Descripción:
Sugiere el medio de transporte más apropiado según la distancia.

Ejemplo de uso:
Entrada: 15
Salida: RECOMENDACION Ve en auto
"""

# Solicitar la distancia
distancia = float(input("¿Cuál es la distancia a recorrer? (km): "))

# Sugerir transporte según la distancia
if distancia < 0:
    print("Distancia no válida")
elif distancia < 1:
    print("RECOMENDACIÓN: Ve caminando")
elif distancia <= 5:
    print("RECOMENDACIÓN: Ve en bicicleta")
elif distancia <= 20:
    print("RECOMENDACIÓN: Ve en auto")
else:
    print("RECOMENDACIÓN: Ve en transporte público")
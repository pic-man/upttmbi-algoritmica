"""
Ejercicio 12: Multa de Biblioteca
Calcula la multa por retraso en la devolución de un libro.
"""

# Solicitar los días de retraso
dias = int(input("Ingresa los días de retraso: "))

# Calcular la multa según los días
if dias < 0 :
    print("Números negativos no válidos")
elif dias == 0:
    print("No hay multa. Gracias por devolver a tiempo.")
elif dias <= 5:
    multa = dias * 5 
    print(f"Multa a pagar: ${multa}")
elif dias <= 10:
    multa = dias * 10
    print(f"Multa a pagar: ${multa}")
else:
    multa = dias * 15
    print(f"Multa a pagar: ${multa}")
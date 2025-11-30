#Ejercico 15:Patron Asterisco
#Estudiante : Jheferson Manuel Duran Marin
#GitHub: Jheferson1213
#Fecha:2025,11,30
print("Patrón de Asteriscos")
altura_1 = input("Ingresa la altura del triángulo: ")
altura = int(altura_1)
if altura >= 1:
    for fila in range(1, altura + 1):
        print("*" * fila)
else:
    print("Entrada no válida. Usa un entero positivo.")

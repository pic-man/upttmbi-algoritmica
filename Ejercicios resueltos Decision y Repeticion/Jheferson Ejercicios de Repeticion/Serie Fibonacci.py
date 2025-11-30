#Ejercico 7: Serie Fibonacci
#Estudiante : Jheferson Manuel Duran Marin
#GitHub: Jheferson1213
#Fecha:2025,11,30
print("FIBONACCI")
F = input("¿Cuántos términos de Fibonacci deseas generar? ")
n = int(F)
if n >= 1:
    a, b = 0, 1
    contador = 0
    
    print("Serie:", end=" ")
    while contador < n:
        if contador == 0:
            termino_actual = a
        elif contador == 1:
            termino_actual = b
        else:
            termino_actual = a + b
            a = b
            b = termino_actual
        print(termino_actual, end=" ")
        contador += 1
    print()
else:
    print("Entrada no válida. Ingresa un entero mayor o igual a 1.")
#Ejercico 10 : Potencia Multiplicacion
#Estudiante:Yerson Josue Saavedra Barrios
#GitHub:Yerson17
#Fecha:2025-11-28
print("Potencia Por Multiplicacion")
base1 = input("Ingresa la base: ")
exponente1 = input("Ingresa el exponente: ")
base = int(base1)
exponente = int(exponente1)
if exponente >= 0:
    if exponente == 0:
        resultado = 1
    else:
        resultado = 1
        contador = 0
        while contador < exponente:
            resultado *= base
            contador += 1
    print(base, "^", exponente, "=", resultado)
else:
    print("Entrada no válida. El exponente debe ser un entero mayor o igual a 0.")

#Ejercico 4: Tabla de Multiplicar
#Estudiante : Jheferson Manuel Duran Marin
#GitHub: Jheferson1213
#Fecha:2025,11,30
print("tabla de multiplicar")
nx = input("Ingresa un número entre 1 y 10: ")
n = int(nx)
if n >= 1 and n <= 10:
    print("Tabla del", n, ":")
    for i in range(1, 11):
        resultado = n * i
        print(n, "x", i, "=", resultado)
else:
    print("Entrada no válida. Debes ingresar un número entero de 1 a 10.")
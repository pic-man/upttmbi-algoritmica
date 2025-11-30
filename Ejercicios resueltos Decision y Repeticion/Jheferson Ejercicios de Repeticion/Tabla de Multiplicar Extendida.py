#Ejercico 14: Tabla Extendida
#Estudiante : Jheferson Manuel Duran Marin
#GitHub: Jheferson1213
#Fecha:2025,11,30
print(" Tabla de Multiplicar Extendida")
inicio1 = input("Ingresa el número inicial (1-10): ")
final1 = input("Ingresa el número final (1-10): ")
inicio = int(inicio1)
final = int(final1)
if inicio >= 1 and inicio <= 10 and final >= 1 and final <= 10 and inicio <= final:
    for n in range(inicio, final + 1):
        print("Tabla del", n)
        for i in range(1, 11):
            resultado = n * i
            print(n, "x", i, "=", resultado)
else:
    print("Rangos inválidos. Ambos números deben estar entre 1 y 10, y el inicial debe ser menor o igual que el final.")

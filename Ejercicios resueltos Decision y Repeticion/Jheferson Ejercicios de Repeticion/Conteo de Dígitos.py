#Ejercico 19: Conteo de Digitos
#Estudiante : Jheferson Manuel Duran Marin
#GitHub: Jheferson1213
#Fecha:2025,11,30
print("Conteo de Dígitos")
n1 = input("Ingresa un número entero: ")
n = int(n1)
if n == 0:
    cantidad_digitos = 1
else:
    numero = abs(n)
    cantidad_digitos = 0
    while numero > 0:
        numero = numero // 10
        cantidad_digitos += 1
print("Cantidad de dígitos:", cantidad_digitos)

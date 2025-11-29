#Ejercico 16:Conversio Binario
#Estudiante:Yoeleiny MariaSalome Barrios Zambrano
#GitHub:Yoeleiny205
#Fecha:2025-11-28
print("Conversión a Binario")
n_1 = input("Ingresa un número entero: ")
n = int(n_1)
if n >= 0:
    if n == 0:
        binario = "0"
    else:
        numero = n
        binario = ""
        while numero > 0:
            residuo = numero % 2
            binario = str(residuo) + binario
            numero = numero // 2
    print("Binario:", binario)
else:
    print("Entrada no válida. Debes ingresar un entero mayor o igual a 0.")

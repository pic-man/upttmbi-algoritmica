# Ejercicio 7: Serie Fibonacci
n = int(input("¿Cuántos términos de Fibonacci? "))
a, b = 0, 1
contador = 0
while contador < n:
    print(a)
    temp = a
    a = b
    b = temp + b
    contador = contador + 1

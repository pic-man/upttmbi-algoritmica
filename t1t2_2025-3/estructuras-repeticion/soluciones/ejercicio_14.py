# Ejercicio 14: Tabla de Multiplicar Extendida
inicio = int(input("Número inicial: "))
fin = int(input("Número final: "))
for base in range(inicio, fin + 1):
    print(f"\nTabla del {base}")
    for i in range(10):
        print(f"{base} x {i + 1} = {base * (i + 1)}")

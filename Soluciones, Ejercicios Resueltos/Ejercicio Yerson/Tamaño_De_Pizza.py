#Ejercico 11: Tamaño Pizza
#Estudiante:Yerson Josue Saavedra Barrios
#GitHub:Yerson17
#Fecha:2025-11-16
print("Tamaños disponibles: pequeña, mediana, grande")
print()
tamano = input("Ingresa el tamaño de pizza: ").lower()
if tamano == "pequeña":
    print("Pizza pequeña: $80")
elif tamano == "mediana":
    print("Pizza mediana: $120")
elif tamano == "grande":
    print("Pizza grande: $150")
else:
    print("Lo sentimos, ese tamaño no está disponible")
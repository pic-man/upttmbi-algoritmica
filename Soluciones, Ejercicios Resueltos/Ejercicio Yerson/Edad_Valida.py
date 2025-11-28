#Ejercico 1: Edad Valida
#Estudiante:Yerson Josue Saavedra Barrios
#GitHub:Yerson17
#Fecha:2025-11-16
edad = int(input("Por favor, introduce tu edad: "))
print("--- Clasificación ---")
if edad < 0:
    print("Edad no válida. La edad no puede ser negativa.")
elif edad <= 17: 
    print("Eres menor de edad")
elif edad <= 120:
    print("Eres mayor de edad") 
else:
    print("Edad no válida. La edad excede el límite máximo (120).")
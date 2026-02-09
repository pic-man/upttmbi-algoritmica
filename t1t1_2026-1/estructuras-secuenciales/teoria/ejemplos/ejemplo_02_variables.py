# ==============================================
# Ejemplo 2: Variables
# Cómo crear y usar variables en Python
# ==============================================

# Crear variables de diferentes tipos
nombre = "Carlos"       # str (texto)
edad = 20               # int (entero)
estatura = 1.75         # float (decimal)

# Mostrar las variables
print("=== Datos del estudiante ===")
print(nombre)
print(edad)
print(estatura)

# Mostrar con texto descriptivo
print()
print("=== Con descripción ===")
print("Nombre:", nombre)
print("Edad:", edad)
print("Estatura:", estatura)

# Mostrar usando f-strings (forma moderna)
print()
print("=== Usando f-strings ===")
print(f"El estudiante {nombre} tiene {edad} años")
print(f"Su estatura es {estatura} metros")

# Las variables pueden cambiar de valor
print()
print("=== Cambiando valores ===")
edad = 21
print(f"Ahora {nombre} tiene {edad} años")

# Ver el tipo de cada variable
print()
print("=== Tipos de datos ===")
print(f"nombre es de tipo: {type(nombre)}")
print(f"edad es de tipo: {type(edad)}")
print(f"estatura es de tipo: {type(estatura)}")

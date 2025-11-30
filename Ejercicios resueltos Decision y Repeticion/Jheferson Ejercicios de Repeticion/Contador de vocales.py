#Ejercico 8: Contar Vocales
#Estudiante : Jheferson Manuel Duran Marin
#GitHub: Jheferson1213
#Fecha:2025,11,30
print("Contador de Vocales")
frase = input("Ingresa una palabra o frase: ")
frase_lower = frase.lower()
vocales_permitidas = "aeiou"
contador_vocales = 0
for caracter in frase_lower:
    if caracter in vocales_permitidas:
        contador_vocales += 1
print("Cantidad de vocales:", contador_vocales)

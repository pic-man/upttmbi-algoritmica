#Ejercico 8: Contar Vocales
#Estudiante:Yoeleiny MariaSalome Barrios Zambrano
#GitHub:Yoeleiny205
#Fecha:2025-11-28
print("Contador de Vocales")
frase = input("Ingresa una palabra o frase: ")
frase_lower = frase.lower()
vocales_permitidas = "aeiou"
contador_vocales = 0
for caracter in frase_lower:
    if caracter in vocales_permitidas:
        contador_vocales += 1
print("Cantidad de vocales:", contador_vocales)

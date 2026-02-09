# Ejercicio 8: Contar Vocales
texto = input("Ingresa una palabra o frase: ").lower()
contador = 0
for caracter in texto:
    if caracter == 'a' or caracter == 'e' or caracter == 'i' or caracter == 'o' or caracter == 'u':
        contador = contador + 1
print(f"Cantidad de vocales: {contador}")

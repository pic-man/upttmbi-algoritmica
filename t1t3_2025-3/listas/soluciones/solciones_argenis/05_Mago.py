"""Ejercicio 05: [Mago]
Estudiante: [Argenis Saul Linares Moncayo]
GitHub: @[argenis183]
Fecha: [27/11/2025]

Descripción:
[Este programa permite al usuario ver una lista de números mágicos del 1 al 10]
Ejemplo de uso:
[Presiona 1 para ver los números mágicos o 0 para salir]"""

while True :
    usuario = input('Escribe 1 para ver los numeros magicos o escribe 0 para terminar: ')
    if usuario == '1' :
        numeros_magicos = list(range(1, 11))
        primer_numero = numeros_magicos.pop(0)
        ultimo_numero = numeros_magicos.pop()
        print(f'numeros que desaparecieron fueron {primer_numero} y {ultimo_numero} ')
        print(f'los numeros restantes son {numeros_magicos}')
        break
    elif usuario == '0' :
        print('saliste')
        break
    else :
        print('opcion no valida, intenta de nuevo')
"""Ejercicio 06: [Ranking de Jugadores]
Estudiante: [Argenis Saul Linares Moncayo]
GitHub: @[argenis183]
Fecha: [27/11/2025]

Descripción:
[Este programa muestra los tres puntajes más altos de una lista de puntajes de jugadores.]
Ejemplo de uso:
[Presiona 1 para ver los números mágicos o 0 para salir]"""
puntajes = [450, 890, 320, 670, 1200, 550, 890]
def puestos():
    puntajes.sort(reverse=True)
    print(f'la medalla de oro es para {puntajes[0]} ')
    print(f'la medalla de plata es para {puntajes[1]}')
    print(f'la medalla de bronce es para {puntajes[2]}')

def main():
    while True :
        eleccion_usario = input('Escribe 1 para ver el ranking de jugadores o escribe 0 para terminar: ')
        if eleccion_usario == '1' :
            puestos()
            break
        elif eleccion_usario == '0' :
            print('saliste')
            break

main()



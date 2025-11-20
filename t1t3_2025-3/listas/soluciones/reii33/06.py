#Tienes una lista de puntajes desordenados. 
#Crea un ranking de mayor a menor y muestra los 3 primeros lugares (medallistas de oro, plata y bronce).

puntajes = [450, 890, 320, 670, 1200, 550, 890]

puntajes.sort(reverse=True)

print(f'la medalla de oro es para {puntajes[0]} ')
print(f'la medalla de plata es para {puntajes[1]}')
print(f'la medalla de bronce es para {puntajes[2]}')







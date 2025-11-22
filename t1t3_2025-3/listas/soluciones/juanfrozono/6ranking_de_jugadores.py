#Tienes una lista de puntajes desordenados 
#Crea un ranking de mayor a menor
#Muestra los 3 primeros lugares (medallistas de oro,plata y bronce)

puntajes = [450,890,320,670,1200,550,890]
mayor_menor = puntajes.copy()

mayor_menor.sort(reverse=True)

print(mayor_menor)

print(f'top 1 : {mayor_menor[0]} Medalla de Oro')
print(f'top 2 : {mayor_menor[1]} Medalla de Plata')
print(f'top 3 : {mayor_menor[2]} Medalla de Bronce')



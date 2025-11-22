#Tienes una lista de puntuaciones de un videojuego 
#Descubre cuantas veces obtuviste 100 pts
#Y en que ronda fue la primera vez

l_puntos = [50,100,75,100,90,100,85,100]
c_100 = l_puntos.count(100)
primeravez =( l_puntos.index(100)) + 1
print(l_puntos)
print(f'el numero 100 aparece {c_100} veces,y aparece por primera vez en la ronda {primeravez}')
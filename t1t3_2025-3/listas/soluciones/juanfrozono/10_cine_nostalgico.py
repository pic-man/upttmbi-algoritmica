#Tienes peliculas con años de estreno 
#Ordenalas cronologicamente de la mas antigua a la mas reciente
#Luego "ve"(elimina) las 3 mas antiguas una por una
import time

peliculas = [
    ("Matrix", 1999),
    ("Inception",2010),
    ("Titanic" , 1997),
    ("Avatar" , 2009)
]

peliculas_ordenadas = sorted(peliculas, key=lambda x: x[1])
print("Peliculas:")
for pelicula in peliculas_ordenadas:
    print(pelicula)

print("-"*50)
print("Viendo las 3 mas antiguas...")
print("-"*50)

print(f'Viendo:{peliculas_ordenadas[0]}')
peliculas_ordenadas.pop(0)
print(f'Viendo:{peliculas_ordenadas[0]}')
peliculas_ordenadas.pop(0)
print(f'Viendo:{peliculas_ordenadas[0]}')
peliculas_ordenadas.pop(0)

print("-"*50)


print("Pelicula pendiente")
for pelicula in peliculas_ordenadas:
    print(pelicula)





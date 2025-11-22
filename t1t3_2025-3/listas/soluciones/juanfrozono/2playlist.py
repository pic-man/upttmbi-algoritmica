#Crea una playlist vacia
#Agrega 5 canciones
#luego colocar la cancion fav en la primera posicion si eliminar las demas

playlist = []
a = 0

while True:
    playlist.append(str(input("Ingrese cancion: ")))
    a += 1

    if a == 4:
        playlist.insert(0,str(input("Ingresa tu cancion fav: ")))
        print(playlist)
        break
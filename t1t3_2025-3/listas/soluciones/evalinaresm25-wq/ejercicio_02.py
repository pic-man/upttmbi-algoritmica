'''
Ejercicio 2: LISTA DE REPRODUCCIÓN
Estudiante: Eva Sofia Linares Medina
GitHub: @evalinaresm25-wq
Fecha: 2025-11-26

Descripción:
Crea una playlist vacía. Agrega 5 canciones y pon tu canción favorita al inicio sin eliminar las demás.

Métodos usados:
- extend()
- insert()
'''
playlist = []
playlist.extend(["canción 1", "canción 2", "canción 3", "canción 4", "canción 5"])
favorita = "canción 3"
playlist.insert(0, favorita)
print("Playlist final:", playlist)

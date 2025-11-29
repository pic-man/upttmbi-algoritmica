'''
Ejercicio 20: RED SOCIAL SIMPLIFICADA
Estudiante: Eva Sofia Linares Medina
GitHub: @evalinaresm25-wq
Fecha: 2025-11-26

Descripción:
Agrega posts, ordénalos por likes, mantén los 10 más recientes y permite buscar por texto.

Métodos usados:
- insert()
- pop()
- sort()
- len()
'''
class Post:
    def __init__(self, texto, likes):
        self.texto = texto
        self.likes = likes

posts = []

def publicar(texto, likes):
    posts.insert(0, Post(texto, likes))
    eliminar_antiguos()

def ordenar_por_likes():
    posts.sort(key=lambda x: x.likes, reverse=True)

def eliminar_antiguos():
    while len(posts) > 10:
        posts.pop()

def buscar_post(texto):
    for p in posts:
        if texto in p.texto:
            return p.texto
    return "No encontrado"

publicar("Hola mundo", 5)
publicar("Python", 12)
ordenar_por_likes()
print(buscar_post("Python"))

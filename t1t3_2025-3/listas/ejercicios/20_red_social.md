# 🎯 Ejercicio 20: Red Social Simplificada

## Dificultad: ⭐⭐⭐ Avanzado

## 📝 Descripción

Crea un sistema de posts de red social que: agregue posts al inicio, ordene por likes, mantenga solo los últimos 10, y busque posts.

## 🎯 Objetivo

Sistema completo con clases y múltiples operaciones.

## 💻 Clase a Implementar

```python
class Post:
    def __init__(self, texto, likes):
        self.texto = texto
        self.likes = likes
```

## 📋 Funciones a Implementar

```python
def publicar(posts, texto, likes=0):
    """Agrega nuevo post al inicio"""
    pass

def ordenar_por_likes(posts):
    """Ordena posts por likes (mayor a menor)"""
    pass

def eliminar_antiguos(posts, maximo=10):
    """Mantiene solo los últimos N posts"""
    pass

def buscar_post(posts, palabra):
    """Busca posts que contengan la palabra"""
    pass
```

## 💻 Ejemplo de Ejecución

```
=== RED SOCIAL PYTHON ===

Publicando posts...
✓ "¡Hola mundo!" (0 likes)
✓ "Python es genial" (5 likes)
✓ "Aprendiendo listas" (10 likes)

📱 FEED (3 posts):
━━━━━━━━━━━━━━━━━━━━
[3] Aprendiendo listas
    ❤️ 10 likes

[2] Python es genial
    ❤️ 5 likes

[1] ¡Hola mundo!
    ❤️ 0 likes
━━━━━━━━━━━━━━━━━━━━

Ordenando por likes...

📈 MÁS POPULARES:
━━━━━━━━━━━━━━━━━━━━
🔥 Aprendiendo listas
   ❤️ 10 likes

⭐ Python es genial
   ❤️ 5 likes

💬 ¡Hola mundo!
   ❤️ 0 likes
━━━━━━━━━━━━━━━━━━━━

Buscando "Python"...
✓ 1 post encontrado:
  - "Python es genial" (5 likes)
```

## 💡 Pistas

1. `insert(0, post)` para agregar al inicio
2. `sorted()` con `key=lambda x: x.likes`
3. `posts = posts[:10]` para límite
4. Usa `in` para buscar en texto

---

**Tiempo estimado**: 60+ minutos  
**Archivo de solución**: `ejercicio_20.py`


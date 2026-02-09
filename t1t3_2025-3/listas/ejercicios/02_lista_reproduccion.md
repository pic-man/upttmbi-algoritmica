# 🎵 Ejercicio 2: Lista de Reproducción

## Dificultad: ⭐ Básico

## 📝 Descripción

Crea una playlist vacía. Agrega 5 canciones, luego pon tu canción favorita en la primera posición sin eliminar las demás.

## 🎯 Objetivo

Practicar `append()` e `insert()`.

## 📋 Especificaciones

1. Crear una lista vacía llamada `playlist`
2. Agregar 5 canciones usando `append()`
3. Insertar una canción favorita al inicio usando `insert()`
4. Mostrar la playlist completa

## 💻 Lista Inicial

```python
playlist = []
```

## 💻 Ejemplo de Ejecución

```
=== MI PLAYLIST ===

Agregando canciones...
✓ Agregada: "Bohemian Rhapsody"
✓ Agregada: "Imagine"
✓ Agregada: "Hotel California"
✓ Agregada: "Sweet Child O' Mine"
✓ Agregada: "Stairway to Heaven"

Moviendo canción favorita al inicio...
⭐ "Shape of My Heart" ahora es la primera

PLAYLIST FINAL:
1. Shape of My Heart ⭐
2. Bohemian Rhapsody
3. Imagine
4. Hotel California
5. Sweet Child O' Mine
6. Stairway to Heaven

Total de canciones: 6
```

## 🧪 Casos de Prueba

Verifica que:
- [ ] La playlist tiene 6 canciones al final
- [ ] La canción favorita está en la primera posición
- [ ] Las demás canciones mantienen su orden

## 💡 Pistas

1. `append()` agrega al final
2. `insert(0, cancion)` inserta al inicio
3. Usa `enumerate()` para numerar la lista

## 🚀 Desafíos Extra

1. Agrega duración de cada canción
2. Calcula el tiempo total de la playlist
3. Permite reproducir canciones aleatorias

---

**Tiempo estimado**: 10-15 minutos  
**Archivo de solución**: `ejercicio_02.py`


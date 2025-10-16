# 📚 Ejercicio 8: Biblioteca Personal

## Dificultad: ⭐⭐ Intermedio

## 📝 Descripción

Organiza una lista de libros por número de páginas, del más corto al más largo.

## 🎯 Objetivo

Practicar `sorted()` con diccionarios y `lambda`.

## 💻 Lista Inicial

```python
libros = [
    {"titulo": "El Hobbit", "paginas": 310},
    {"titulo": "1984", "paginas": 328},
    {"titulo": "El Principito", "paginas": 96}
]
```

## 💻 Ejemplo de Ejecución

```
=== MI BIBLIOTECA ===

Libros desordenados:
- El Hobbit (310 páginas)
- 1984 (328 páginas)
- El Principito (96 páginas)

Ordenando por páginas...

BIBLIOTECA ORDENADA (corto → largo):
1. 📖 El Principito - 96 páginas
2. 📖 El Hobbit - 310 páginas
3. 📖 1984 - 328 páginas

📊 Estadísticas:
- Libro más corto: El Principito (96 págs)
- Libro más largo: 1984 (328 págs)
- Promedio: 244.7 páginas
```

## 💡 Pistas

1. Usa `sorted()` con `key=lambda`
2. `lambda x: x["paginas"]` ordena por páginas

---

**Tiempo estimado**: 15-20 minutos  
**Archivo de solución**: `ejercicio_08.py`


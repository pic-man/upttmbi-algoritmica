# 🎬 Ejercicio 10: Cine Nostálgico

## Dificultad: ⭐⭐ Intermedio

## 📝 Descripción

Tienes películas con años de estreno. Ordénalas cronológicamente y luego "ve" (elimina) las 3 más antiguas una por una.

## 🎯 Objetivo

Practicar `sorted()` con tuplas y `pop()`.

## 💻 Lista Inicial

```python
peliculas = [
    ("Matrix", 1999),
    ("Inception", 2010),
    ("Titanic", 1997),
    ("Avatar", 2009)
]
```

## 💻 Ejemplo de Ejecución

```
=== MARATÓN DE CINE NOSTÁLGICO ===

Películas disponibles:
- Matrix (1999)
- Inception (2010)
- Titanic (1997)
- Avatar (2009)

Ordenando cronológicamente...

📅 ORDEN CRONOLÓGICO:
1. Titanic (1997)
2. Matrix (1999)
3. Avatar (2009)
4. Inception (2010)

🎬 Viendo las 3 más antiguas...

▶️ Viendo: Titanic (1997) ✓
▶️ Viendo: Matrix (1999) ✓
▶️ Viendo: Avatar (2009) ✓

📋 Película pendiente:
- Inception (2010)
```

## 💡 Pistas

1. `sorted(lista, key=lambda x: x[1])` ordena por año
2. Usa `pop(0)` tres veces para eliminar las primeras

---

**Tiempo estimado**: 15-20 minutos  
**Archivo de solución**: `ejercicio_10.py`


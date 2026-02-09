# 🧹 Ejercicio 11: Limpieza de Lista

## Dificultad: ⭐ Básico

## 📝 Descripción

Tienes una lista con elementos duplicados y valores None. Crea una versión limpia sin duplicados ni valores nulos.

## 🎯 Objetivo

Practicar filtrado y eliminación de duplicados.

## 💻 Lista Inicial

```python
lista_sucia = [1, 2, None, 3, 2, 4, None, 1, 5, 3]
```

## 💻 Ejemplo de Ejecución

```
=== LIMPIEZA DE LISTA ===

Lista original (sucia):
[1, 2, None, 3, 2, 4, None, 1, 5, 3]

Elementos: 10
Duplicados detectados: 1, 2, 3
Valores None encontrados: 2

Limpiando...

LISTA LIMPIA:
[1, 2, 3, 4, 5]

✓ Elementos finales: 5
✓ Sin duplicados
✓ Sin valores None
```

## 💡 Pistas

1. Usa list comprehension con `if`
2. Usa `set()` para eliminar duplicados
3. Filtra `None` con `if x is not None`

---

**Tiempo estimado**: 15 minutos  
**Archivo de solución**: `ejercicio_11.py`


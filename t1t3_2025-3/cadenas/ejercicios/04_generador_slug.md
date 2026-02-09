# 🌐 Ejercicio 4: Generador de Slug

## Dificultad: ⭐⭐ Intermedio

## 📝 Descripción

A partir del título de un artículo, genera un *slug* compatible con URL (solo minúsculas, sin acentos ni espacios, usando guiones).

## 🎯 Objetivo

Combinar métodos de limpieza (`lower()`, `strip()`, `replace()`) y normalización básica de caracteres.

## 📋 Especificaciones

1. Recibir el título `titulo_raw`.
2. Eliminar espacios extra.
3. Convertir a minúsculas.
4. Reemplazar vocales tildadas por su versión sin tilde.
5. Reemplazar espacios y guiones dobles por un solo `-`.
6. Eliminar cualquier carácter que no sea letra, número o guion.

## 💻 Datos Iniciales

```python
titulo_raw = "  ¡Lanzamiento: Python 3.12 y más allá!  "
```

## 💻 Ejemplo de Ejecución

```
=== GENERADOR DE SLUG ===
Título original: ¡Lanzamiento: Python 3.12 y más allá!
Slug: lanzamiento-python-3-12-y-mas-alla
```

## 🧪 Casos de Prueba

- [ ] Remueve signos de puntuación.
- [ ] Normaliza tildes correctamente.
- [ ] No genera guiones dobles ni termina con guion.
- [ ] Funciona con títulos solo numéricos o muy cortos.

## 💡 Pistas

1. Crea un diccionario de reemplazos para caracteres acentuados.
2. Recorre cada caracter y verifica si es alfanumérico.
3. Usa `join()` para reconstruir la cadena final.

## ⚠️ Errores Comunes

- ❌ Olvidar quitar espacios al inicio/fin antes de reemplazar.
- ❌ Dejar guiones extra cuando hay múltiples espacios seguidos.
- ❌ No controlar caracteres especiales como `!` o `?`.

## 🎓 Conceptos Practicados

- Sanitización de texto
- Construcción de cadenas paso a paso
- Expresiones regulares (opcional)

## 🚀 Desafíos Extra (Opcional)

1. Implementa una versión usando `re` para reemplazo de caracteres no válidos.
2. Limita el slug a 50 caracteres y corta palabras completas.
3. Añade un sufijo numérico si el slug ya existe (lista simulada de slugs ocupados).

---

**Tiempo estimado**: 15 minutos  
**Archivo de solución**: `ejercicio_04.py`  
**Métodos a usar**: `strip()`, `lower()`, `replace()`, `join()`

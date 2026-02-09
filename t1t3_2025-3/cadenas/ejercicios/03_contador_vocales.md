# 🎶 Ejercicio 3: Contador de Vocales

## Dificultad: ⭐ Básico

## 📝 Descripción

Dado un poema corto, cuenta cuántas vocales hay y distingue entre vocales normales y vocales con tilde.

## 🎯 Objetivo

Practicar iteración sobre caracteres y uso de `count()` o acumuladores manuales.

## 📋 Especificaciones

1. Trabaja con la cadena `poema` (puede incluir tildes y mayúsculas).
2. Normaliza a minúsculas.
3. Cuenta cuántas veces aparecen `a, e, i, o, u`.
4. Cuenta cuántas vocales con tilde aparecen (`á, é, í, ó, ú`).
5. Muestra un reporte tabular.

## 💻 Datos Iniciales

```python
poema = "Aún canta el ave y el viento sopla suave"
```

## 💻 Ejemplo de Ejecución

```
=== CONTADOR DE VOCALES ===
Texto: Aún canta el ave y el viento sopla suave

Vocales sin tilde:
- a: 4
- e: 3
- i: 1
- o: 2
- u: 1

Vocales con tilde: 1
Total de vocales: 12
```

## 🧪 Casos de Prueba

- [ ] Suma correctamente todas las vocales.
- [ ] Diferencia vocales con tilde y sin tilde.
- [ ] Controla mayúsculas vs minúsculas.
- [ ] El reporte muestra números consistentes.

## 💡 Pistas

1. Puedes usar `sum(poema.count(v) for v in "aeiou")`.
2. Crea un conjunto con las vocales tildadas.
3. Considera usar un diccionario para almacenar los conteos.

## ⚠️ Errores Comunes

- ❌ Olvidar convertir a minúsculas antes de contar.
- ❌ Contar vocales tildadas como vocales normales.
- ❌ No reiniciar el contador entre ejecuciones.

## 🎓 Conceptos Practicados

- Iteración de strings
- Diccionarios simples (opcional)
- Normalización de texto

## 🚀 Desafíos Extra (Opcional)

1. Muestra porcentajes sobre el total de caracteres.
2. Reemplaza las vocales tildadas por su versión sin tilde y compara el cambio.
3. Crea una función que devuelva el reporte para cualquier texto.

---

**Tiempo estimado**: 12 minutos  
**Archivo de solución**: `ejercicio_03.py`  
**Métodos a usar**: `lower()`, `count()`

# 🌍 Ejercicio 12: Normalizador Unicode

## Dificultad: ⭐⭐⭐ Avanzado

## 📝 Descripción

Recibes nombres de ciudades escritos con combinaciones de acentos y caracteres especiales. Debes normalizarlos a una forma ASCII amigable sin perder información clave.

## 🎯 Objetivo

Aprender a usar `unicodedata.normalize()` y operaciones de reemplazo.

## 📋 Especificaciones

1. Lista `ciudades = ["São Paulo", "München", "Bogotá", "Zürich", "Niño"]`.
2. Normaliza cada ciudad a su versión sin acentos (`Sao Paulo`, `Munchen`, ...).
3. Genera una tabla con columnas: original, normalizado, longitud.
4. Crea un diccionario `alias_ciudad` que mapee original ➜ slug (usa el ejercicio 4 como referencia).

## 💻 Ejemplo de Ejecución

```
=== NORMALIZADOR UNICODE ===
Original       Normalizado    Longitud
--------------------------------------
São Paulo      Sao Paulo      9
München        Munchen        7
...
Alias disponibles: {'São Paulo': 'sao-paulo', ...}
```

## 🧪 Casos de Prueba

- [ ] Elimina diacríticos sin afectar letras normales.
- [ ] Mantiene espacios y mayúsculas iniciales.
- [ ] Genera slugs en minúsculas y con guiones.
- [ ] No pierde ciudades repetidas.

## 💡 Pistas

1. `unicodedata.normalize('NFD', texto)` separa caracteres y tildes.
2. Usa comprensión de listas para filtrar categorías `Mn`.
3. Reutiliza la lógica de slug con una función auxiliar.

## ⚠️ Errores Comunes

- ❌ No importar el módulo `unicodedata`.
- ❌ Quitar letras enteras en vez de solo tildes.
- ❌ Sobrescribir el diccionario alias.

## 🎓 Conceptos Practicados

- Normalización Unicode
- Construcción de tablas
- Funciones reutilizables

## 🚀 Desafíos Extra (Opcional)

1. Detecta si hay caracteres no ASCII restantes.
2. Permite elegir entre varias estrategias (`NFD`, `NFKD`).
3. Genera un CSV con los resultados.

---

**Tiempo estimado**: 20 minutos  
**Archivo de solución**: `ejercicio_12.py`  
**Módulos/Métodos a usar**: `unicodedata`, `normalize()`, `replace()`, `lower()`

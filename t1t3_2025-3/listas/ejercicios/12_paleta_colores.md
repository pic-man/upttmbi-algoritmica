# 🎨 Ejercicio 12: Paleta de Colores

## Dificultad: ⭐ Básico

## 📝 Descripción

Crea una función que tome una lista de colores y: agregue "blanco" al inicio y "negro" al final, cree una versión invertida, y retorne ambas versiones.

## 🎯 Objetivo

Practicar funciones con listas, `insert()` y `reverse()`.

## 💻 Lista Inicial

```python
colores = ["rojo", "verde", "azul", "amarillo"]
```

## 💻 Ejemplo de Ejecución

```
=== PALETA DE COLORES ===

Colores originales:
['rojo', 'verde', 'azul', 'amarillo']

Procesando paleta...

PALETA MODIFICADA:
['blanco', 'rojo', 'verde', 'azul', 'amarillo', 'negro']

PALETA INVERTIDA:
['negro', 'amarillo', 'azul', 'verde', 'rojo', 'blanco']

✓ Ambas paletas tienen 6 colores
```

## 💡 Pistas

1. Crea una función `procesar_paleta(colores)`
2. Usa `insert(0, "blanco")` y `append("negro")`
3. Usa `reverse()` o `[::-1]`
4. Retorna ambas listas

---

**Tiempo estimado**: 15 minutos  
**Archivo de solución**: `ejercicio_12.py`


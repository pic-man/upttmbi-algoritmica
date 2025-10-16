# 🎮 Ejercicio 17: Inventario de Juego RPG

## Dificultad: ⭐⭐⭐ Avanzado

## 📝 Descripción

Crea un sistema de inventario para un juego RPG que permita: recoger objetos, verificar cantidad, usar/vender objetos, y organizar alfabéticamente.

## 🎯 Objetivo

Sistema completo con múltiples operaciones de listas.

## 💻 Lista Inicial

```python
inventario = []
```

## 📋 Funciones a Implementar

```python
def recoger_objeto(inventario, objeto):
    """Agrega un objeto al inventario"""
    pass

def contar_objeto(inventario, objeto):
    """Cuenta cuántos hay de un objeto"""
    pass

def usar_objeto(inventario, objeto):
    """Usa/elimina un objeto del inventario"""
    pass

def organizar_inventario(inventario):
    """Ordena alfabéticamente"""
    pass

def mostrar_inventario(inventario):
    """Muestra el inventario con cantidades"""
    pass
```

## 💻 Ejemplo de Ejecución

```
=== INVENTARIO RPG ===

Menú:
1. Recoger objeto
2. Ver inventario
3. Usar objeto
4. Organizar inventario
5. Salir

Opción: 1
¿Qué recogiste? poción
✓ Recogido: poción

Opción: 1
¿Qué recogiste? espada
✓ Recogido: espada

Opción: 1
¿Qué recogiste? poción
✓ Recogido: poción

Opción: 2

📦 TU INVENTARIO:
- poción x2
- espada x1

Total de objetos: 3

Opción: 4
✓ Inventario organizado alfabéticamente

Opción: 2

📦 TU INVENTARIO:
- espada x1
- poción x2
```

## 💡 Pistas

1. Usa `append()` para recoger
2. Usa `count()` para contar
3. Usa `remove()` para usar (elimina solo uno)
4. Usa `sort()` para organizar
5. Usa `set()` para ver objetos únicos

## 🚀 Desafíos Extra

1. Límite máximo de peso/capacidad
2. Objetos con rareza (común, raro, épico)
3. Sistema de crafteo (combinar objetos)
4. Guardar/cargar inventario en archivo

---

**Tiempo estimado**: 40-60 minutos  
**Archivo de solución**: `ejercicio_17.py`


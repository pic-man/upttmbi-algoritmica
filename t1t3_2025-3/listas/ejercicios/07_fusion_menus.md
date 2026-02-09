# 🍔 Ejercicio 7: Fusión de Menús

## Dificultad: ⭐⭐ Intermedio

## 📝 Descripción

Dos restaurantes se fusionan. Combina sus menús en uno solo y elimina los platos duplicados para que no aparezcan dos veces.

## 🎯 Objetivo

Practicar combinación de listas y eliminación de duplicados.

## 📋 Especificaciones

1. Combinar ambos menús
2. Eliminar duplicados
3. Mostrar el menú fusionado

## 💻 Listas Iniciales

```python
menu_a = ["hamburguesa", "pizza", "ensalada", "sopa"]
menu_b = ["pizza", "pasta", "ensalada", "tacos"]
```

## 💻 Ejemplo de Ejecución

```
=== FUSIÓN DE RESTAURANTES ===

Menú Restaurante A:
- hamburguesa
- pizza
- ensalada
- sopa

Menú Restaurante B:
- pizza
- pasta
- ensalada
- tacos

Fusionando menús...

MENÚ COMBINADO NUEVO:
1. hamburguesa
2. pizza
3. ensalada
4. sopa
5. pasta
6. tacos

✓ Platos únicos: 6
✓ Duplicados eliminados: pizza, ensalada
```

## 💡 Pistas

1. Usa `extend()` o `+` para combinar
2. Usa `set()` para eliminar duplicados
3. Convierte de vuelta a `list()`

---

**Tiempo estimado**: 15 minutos  
**Archivo de solución**: `ejercicio_07.py`


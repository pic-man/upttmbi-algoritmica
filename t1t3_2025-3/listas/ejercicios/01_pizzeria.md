# 🍕 Ejercicio 1: Pizzería

## Dificultad: ⭐ Básico

## 📝 Descripción

Tienes una lista de ingredientes para pizza. Agrega 3 ingredientes más, elimina las anchoas (nadie las quiere), y muestra el resultado final.

## 🎯 Objetivo

Practicar los métodos `append()` y `remove()`.

## 📋 Especificaciones

El programa debe:

1. Partir de la lista dada
2. Agregar 3 ingredientes nuevos
3. Eliminar "anchoas"
4. Mostrar la lista final

## 💻 Lista Inicial

```python
ingredientes = ["queso", "tomate", "anchoas", "jamón"]
```

## 💻 Ejemplo de Ejecución

```
=== PIZZERÍA ===

Ingredientes iniciales:
- queso
- tomate
- anchoas
- jamón

Agregando ingredientes...
✓ Agregado: pepperoni
✓ Agregado: champiñones
✓ Agregado: aceitunas

Eliminando ingredientes no deseados...
✗ Eliminado: anchoas

INGREDIENTES FINALES:
1. queso
2. tomate
3. jamón
4. pepperoni
5. champiñones
6. aceitunas
```

## 🧪 Casos de Prueba

Verifica que tu programa:
- [ ] Agrega correctamente 3 ingredientes
- [ ] Elimina las anchoas
- [ ] Muestra todos los ingredientes finales
- [ ] El orden es lógico

## 💡 Pistas

1. Usa `append()` para agregar ingredientes al final
2. Usa `remove()` para eliminar las anchoas
3. Usa un bucle `for` para mostrar la lista final

## ⚠️ Errores Comunes

- ❌ Intentar eliminar algo que no existe
- ❌ No verificar que el ingrediente exista antes de eliminar
- ❌ Confundir `append()` con `extend()`

## 🎓 Conceptos Practicados

- Método `append()`
- Método `remove()`
- Iteración con `for`
- Listas mutables

## 🚀 Desafíos Extra (Opcional)

1. **Verificación**:
   - Pregunta al usuario qué ingredientes agregar
   - Verifica que no estén duplicados

2. **Menú interactivo**:
   ```
   1. Agregar ingrediente
   2. Eliminar ingrediente
   3. Ver lista
   4. Salir
   ```

3. **Categorías**:
   - Separa los ingredientes por tipo (carnes, vegetales, quesos)

---

**Tiempo estimado**: 10-15 minutos  
**Archivo de solución**: `ejercicio_01.py`  
**Métodos a usar**: `append()`, `remove()`, `for`


# 🎪 Ejercicio 16: Malabarista de Números

## Dificultad: ⭐⭐ Intermedio

## 📝 Descripción

Crea una función que reciba una lista de números y realice el truco del malabarista: toma el último elemento y lo pone al inicio. Repite 3 veces.

## 🎯 Objetivo

Practicar `pop()` e `insert()` en bucle.

## 💻 Función a Implementar

```python
def malabares(numeros):
    # Tu código aquí
    pass

print(malabares([1, 2, 3, 4, 5]))
# Resultado esperado: [3, 4, 5, 1, 2]
```

## 💻 Ejemplo de Ejecución

```
=== MALABARISTA DE NÚMEROS ===

Lista inicial: [1, 2, 3, 4, 5]

🎪 Truco 1: Moviendo 5 al inicio
   [5, 1, 2, 3, 4]

🎪 Truco 2: Moviendo 4 al inicio
   [4, 5, 1, 2, 3]

🎪 Truco 3: Moviendo 3 al inicio
   [3, 4, 5, 1, 2]

🎭 Resultado final: [3, 4, 5, 1, 2]

✓ ¡Truco completado!
```

## 🧪 Casos de Prueba

```python
malabares([1, 2, 3, 4, 5])     # [3, 4, 5, 1, 2]
malabares([10, 20, 30])         # [30, 10, 20]
malabares([1])                  # [1]
```

## 💡 Pistas

1. Usa un bucle `for` 3 veces
2. En cada iteración:
   - `ultimo = lista.pop()` saca el último
   - `lista.insert(0, ultimo)` lo pone al inicio
3. Retorna la lista modificada

---

**Tiempo estimado**: 15-20 minutos  
**Archivo de solución**: `ejercicio_16.py`


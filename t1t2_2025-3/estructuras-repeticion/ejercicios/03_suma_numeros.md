# ➕ Ejercicio 3: Suma de Números

## Dificultad: ⭐ Básico

## 📝 Descripción

Diseña un programa que sume los primeros `n` números naturales (1 hasta `n`) usando un ciclo `for`.

## 🎯 Objetivo

Practicar el uso de `for` con rangos y acumuladores.

## 📋 Especificaciones

El programa debe:

1. Solicitar al usuario un número entero positivo `n`.
2. Validar que `n` sea mayor o igual que 1.
3. Recorrer un ciclo desde 1 hasta `n` acumulando la suma.
4. Mostrar el resultado final.
5. Mostrar un mensaje de error si `n` no es válido.

## 💻 Ejemplo de Ejecución

### Ejemplo 1:
```
Ingresa un número entero positivo: 5
La suma de 1 a 5 es: 15
```

### Ejemplo 2:
```
Ingresa un número entero positivo: 1
La suma de 1 a 1 es: 1
```

### Ejemplo 3:
```
Ingresa un número entero positivo: 0
Entrada no válida. Necesitas un entero mayor o igual a 1.
```

## 🧪 Casos de Prueba

| Entrada | Salida Esperada |
|---------|----------------|
| 1 | 1 |
| 3 | 6 |
| 5 | 15 |
| 10 | 55 |
| 0 | Mensaje de error |

## 💡 Pistas

1. Usa `range(1, n + 1)` para recorrer del 1 al `n`.
2. Inicializa un acumulador en 0 antes del ciclo.
3. En cada iteración suma el valor actual al acumulador.
4. También puedes usar la fórmula `n * (n + 1) / 2` para validar tu resultado.

## ⚠️ Errores Comunes

- ❌ Usar `range(n)` y olvidar sumar el número `n`.
- ❌ Declarar el acumulador dentro del ciclo y reiniciarlo cada vez.
- ❌ No convertir la entrada a `int` antes de usarla.

## 🎓 Conceptos Practicados

- Ciclo `for`
- Función `range`
- Acumuladores

## 🚀 Desafíos Extra (Opcional)

1. Usa un ciclo `while` en lugar de `for`.
2. Muestra la operación completa (ej. `1 + 2 + 3 + 4 + 5 = 15`).
3. Calcula también el promedio de los números sumados.

---

**Tiempo estimado**: 5-10 minutos  
**Archivo de solución**: `ejercicio_03.py`


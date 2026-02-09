# 🔻 Ejercicio 2: Contador Descendente

## Dificultad: ⭐ Básico

## 📝 Descripción

Escribe un programa que cuente desde un número entero positivo dado por el usuario hasta 0.

## 🎯 Objetivo

Practicar ciclos `while` con decrementos y control de límites.

## 📋 Especificaciones

El programa debe:

1. Solicitar un entero positivo `n`.
2. Validar que `n` sea mayor o igual que 0.
3. Imprimir los números desde `n` hasta 0 en orden descendente.
4. Mostrar un mensaje de error si `n` es negativo.

## 💻 Ejemplo de Ejecución

### Ejemplo 1:
```
Ingresa un número entero: 5
5 4 3 2 1 0
```

### Ejemplo 2:
```
Ingresa un número entero: 0
0
```

### Ejemplo 3:
```
Ingresa un número entero: -3
Entrada no válida. Usa un número entero mayor o igual que cero.
```

## 🧪 Casos de Prueba

| Entrada | Salida Esperada |
|---------|----------------|
| 3 | 3 2 1 0 |
| 1 | 1 0 |
| 0 | 0 |
| -1 | Mensaje de error |
| 7 | 7 6 5 4 3 2 1 0 |

## 💡 Pistas

1. Usa `int(input())` para leer el valor.
2. Inicializa el contador en `n` y disminúyelo con `-=` en cada iteración.
3. El ciclo debe continuar mientras el contador sea mayor o igual que 0.
4. Revisa cómo imprimir en la misma línea usando `end=" "`.

## ⚠️ Errores Comunes

- ❌ Decrementar después de imprimir 0 y mostrar valores negativos.
- ❌ Usar `while contador > 0` y omitir el 0.
- ❌ No validar entradas negativas, generando resultados inesperados.

## 🎓 Conceptos Practicados

- Ciclo `while`
- Decrementos controlados
- Validación de entrada

## 🚀 Desafíos Extra (Opcional)

1. Permite especificar el paso del conteo (ej. de 2 en 2).
2. Muestra también la suma de los números contados.
3. Agrega una versión que use un ciclo `for` con `range`.

---

**Tiempo estimado**: 5-10 minutos  
**Archivo de solución**: `ejercicio_02.py`


# 📈 Ejercicio 11: Mayor y Menor

## Dificultad: ⭐⭐ Intermedio

## 📝 Descripción

Desarrolla un programa que lea una cantidad desconocida de números enteros hasta que el usuario ingrese la palabra `fin`, y determine el mayor y el menor valor introducido.

## 🎯 Objetivo

Practicar el uso de ciclos `while` con condición de salida por texto, así como comparaciones iterativas.

## 📋 Especificaciones

El programa debe:

1. Pedir números enteros al usuario de manera repetida.
2. Terminar cuando el usuario escriba `fin` (en cualquier combinación de mayúsculas/minúsculas).
3. Identificar el número mayor y el menor ingresados.
4. Mostrar un mensaje adecuado si no se ingresó ningún número válido.

## 💻 Ejemplo de Ejecución

### Ejemplo 1:
```
Ingresa un número (o 'fin' para terminar): 10
Ingresa un número (o 'fin' para terminar): 3
Ingresa un número (o 'fin' para terminar): 25
Ingresa un número (o 'fin' para terminar): fin
Mayor: 25
Menor: 3
```

### Ejemplo 2:
```
Ingresa un número (o 'fin' para terminar): fin
No se ingresaron números.
```

### Ejemplo 3:
```
Ingresa un número (o 'fin' para terminar): -5
Ingresa un número (o 'fin' para terminar): -1
Ingresa un número (o 'fin' para terminar): fin
Mayor: -1
Menor: -5
```

## 🧪 Casos de Prueba

| Entradas | Salida Esperada |
|----------|-----------------|
| 4, 8, 2, fin | Mayor: 8, Menor: 2 |
| -3, -7, fin | Mayor: -3, Menor: -7 |
| fin | Mensaje sin datos |
| 5, 5, 5, fin | Mayor: 5, Menor: 5 |
| 10, 2, 30, -1, fin | Mayor: 30, Menor: -1 |

## 💡 Pistas

1. Convierte cada entrada con `int()` solo si no es `fin`.
2. Usa variables para seguir el rastro del mayor y menor; inicialízalas con `None`.
3. Recuerda actualizar tanto mayor como menor cuando leas el primer número válido.

## ⚠️ Errores Comunes

- ❌ Intentar convertir `fin` a número antes de verificarlo.
- ❌ No manejar correctamente la primera lectura y obtener `None`.
- ❌ No normalizar el texto (`.lower()`) antes de comparar con `fin`.

## 🎓 Conceptos Practicados

- Ciclo `while` con sentencias condicionales
- Comparación de valores
- Manejo de entradas mixtas (texto y números)

## 🚀 Desafíos Extra (Opcional)

1. Muestra también el promedio de los números ingresados.
2. Guarda todos los valores en una lista y muéstrala al final.
3. Permite que el usuario defina otra palabra clave para terminar.

---

**Tiempo estimado**: 10-15 minutos  
**Archivo de solución**: `ejercicio_11.py`


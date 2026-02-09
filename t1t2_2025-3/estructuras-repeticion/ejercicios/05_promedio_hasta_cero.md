# 🧮 Ejercicio 5: Promedio hasta Cero

## Dificultad: ⭐⭐ Intermedio

## 📝 Descripción

Programa un sistema que solicite números enteros al usuario hasta que ingrese 0, calcule el promedio de los valores introducidos (sin contar el 0) y muestre el resultado.

## 🎯 Objetivo

Practicar el uso de ciclos `while` controlados por un valor sentinela y el manejo de acumuladores y contadores.

## 📋 Especificaciones

El programa debe:

1. Pedir números enteros repetidamente.
2. Detener la lectura cuando el usuario ingrese 0.
3. Calcular y mostrar el promedio de los números ingresados (excluyendo el 0 final).
4. Mostrar un mensaje si no se ingresó ningún número distinto de 0.

## 💻 Ejemplo de Ejecución

### Ejemplo 1:
```
Ingresa un número (0 para terminar): 4
Ingresa un número (0 para terminar): 6
Ingresa un número (0 para terminar): 10
Ingresa un número (0 para terminar): 0
Promedio: 6.67
```

### Ejemplo 2:
```
Ingresa un número (0 para terminar): 5
Ingresa un número (0 para terminar): -5
Ingresa un número (0 para terminar): 0
Promedio: 0.00
```

### Ejemplo 3:
```
Ingresa un número (0 para terminar): 0
No se ingresaron datos para calcular el promedio.
```

## 🧪 Casos de Prueba

| Entradas | Salida Esperada |
|----------|-----------------|
| 4, 6, 10, 0 | 6.67 |
| 2, 2, 2, 2, 0 | 2.00 |
| 5, -5, 0 | 0.00 |
| 0 | Mensaje sin datos |
| 1, 0 | 1.00 |

## 💡 Pistas

1. Usa dos variables: una para sumar y otra para contar.
2. Asegúrate de no dividir entre 0; verifica si se ingresó al menos un número válido.
3. Puedes formatear el promedio con `f"{promedio:.2f}"`.

## ⚠️ Errores Comunes

- ❌ Incluir el 0 final en el promedio.
- ❌ Olvidar actualizar el contador y producir división por cero.
- ❌ No convertir la entrada a entero antes de usarla.

## 🎓 Conceptos Practicados

- Ciclo `while` con sentinela
- Acumuladores y contadores
- Promedios

## 🚀 Desafíos Extra (Opcional)

1. Permite ingresar números decimales usando `float`.
2. Muestra también la cantidad de números ingresados y su suma.
3. Agrega una validación para evitar valores fuera de un rango predefinido.

---

**Tiempo estimado**: 10-15 minutos  
**Archivo de solución**: `ejercicio_05.py`


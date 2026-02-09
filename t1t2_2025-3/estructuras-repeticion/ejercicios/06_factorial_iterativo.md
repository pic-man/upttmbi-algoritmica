# 🎲 Ejercicio 6: Factorial Iterativo

## Dificultad: ⭐⭐ Intermedio

## 📝 Descripción

Crea un programa que calcule el factorial de un número entero no negativo utilizando un ciclo `while`.

## 🎯 Objetivo

Practicar la multiplicación iterativa, el uso de ciclos controlados y la validación de entrada.

## 📋 Especificaciones

El programa debe:

1. Solicitar un número entero `n` mayor o igual a 0.
2. Validar que `n` no sea negativo.
3. Calcular el factorial de `n` mediante un ciclo iterativo.
4. Mostrar el resultado en pantalla.

## 💻 Ejemplo de Ejecución

### Ejemplo 1:
```
Ingresa un número entero: 5
5! = 120
```

### Ejemplo 2:
```
Ingresa un número entero: 0
0! = 1
```

### Ejemplo 3:
```
Ingresa un número entero: -3
Entrada no válida. El número debe ser 0 o positivo.
```

## 🧪 Casos de Prueba

| Entrada | Salida Esperada |
|---------|----------------|
| 0 | 1 |
| 1 | 1 |
| 4 | 24 |
| 6 | 720 |
| -2 | Mensaje de error |

## 💡 Pistas

1. Inicializa el resultado en 1.
2. Usa un contador que vaya desde 1 hasta `n`.
3. Multiplica el resultado acumulado por el valor del contador en cada paso.
4. Recuerda que `0!` vale 1.

## ⚠️ Errores Comunes

- ❌ Iniciar el contador en 0 y obtener siempre 0 como resultado.
- ❌ No manejar el caso `n = 0`.
- ❌ Usar un ciclo infinito por no actualizar la variable de control.

## 🎓 Conceptos Practicados

- Ciclo `while`
- Multiplicación iterativa
- Validación de entrada

## 🚀 Desafíos Extra (Opcional)

1. Implementa una versión con ciclo `for`.
2. Muestra también el desarrollo de la multiplicación (ej. `5 x 4 x 3 x 2 x 1`).
3. Calcula factoriales para varios números en una sola ejecución.

---

**Tiempo estimado**: 10-15 minutos  
**Archivo de solución**: `ejercicio_06.py`


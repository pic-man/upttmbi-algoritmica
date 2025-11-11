# ⚡ Ejercicio 10: Potencia por Multiplicación

## Dificultad: ⭐⭐ Intermedio

## 📝 Descripción

Implementa un programa que calcule `base^exponente` mediante multiplicaciones repetidas, sin usar el operador `**` ni la función `pow`.

## 🎯 Objetivo

Practicar ciclos `while` controlados por contador y operaciones repetidas.

## 📋 Especificaciones

El programa debe:

1. Solicitar dos enteros: `base` y `exponente`.
2. Validar que el exponente sea mayor o igual a 0.
3. Multiplicar la base por sí misma tantas veces como indique el exponente.
4. Mostrar el resultado.
5. Considerar que cualquier número elevado a 0 es 1.

## 💻 Ejemplo de Ejecución

### Ejemplo 1:
```
Ingresa la base: 2
Ingresa el exponente: 5
2^5 = 32
```

### Ejemplo 2:
```
Ingresa la base: 3
Ingresa el exponente: 0
3^0 = 1
```

### Ejemplo 3:
```
Ingresa la base: 5
Ingresa el exponente: -2
Entrada no válida. El exponente debe ser un entero mayor o igual a 0.
```

## 🧪 Casos de Prueba

| Base | Exponente | Salida Esperada |
|------|-----------|-----------------|
| 2 | 3 | 8 |
| 4 | 2 | 16 |
| 5 | 0 | 1 |
| 1 | 10 | 1 |
| 3 | -1 | Mensaje de error |

## 💡 Pistas

1. Inicializa el resultado en 1.
2. Usa un contador que se incremente hasta alcanzar el exponente.
3. En cada iteración, multiplica el resultado por la base.
4. Considera el caso en el que la base sea 0 y el exponente 0 (puedes definirlo como 1).

## ⚠️ Errores Comunes

- ❌ No validar exponentes negativos y generar ciclos infinitos.
- ❌ Usar la base como contador y perder su valor original.
- ❌ Reiniciar el resultado en cada iteración.

## 🎓 Conceptos Practicados

- Ciclos `while`
- Contadores
- Multiplicación repetida

## 🚀 Desafíos Extra (Opcional)

1. Permite exponentes negativos calculando el inverso (resultado en decimales).
2. Muestra el desarrollo paso a paso (ej. `resultado = resultado * base`).
3. Implementa una versión usando un ciclo `for`.

---

**Tiempo estimado**: 10-15 minutos  
**Archivo de solución**: `ejercicio_10.py`


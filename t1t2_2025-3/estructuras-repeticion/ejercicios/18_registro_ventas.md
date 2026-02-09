# 🛒 Ejercicio 18: Registro de Ventas Diarias

## Dificultad: ⭐⭐ Intermedio

## 📝 Descripción

Programa un sistema que lea el monto de ventas de cada día de la semana y calcule el total y el promedio semanal.

## 🎯 Objetivo

Practicar ciclos `for` con listas de valores conocidos y uso de acumuladores.

## 📋 Especificaciones

El programa debe:

1. Recorrer los 7 días de la semana utilizando un ciclo `for`.
2. Solicitar el monto de ventas para cada día (valor `float`).
3. Acumular el total semanal.
4. Calcular el promedio diario al finalizar el ciclo.
5. Mostrar el total y el promedio con dos decimales.

## 💻 Ejemplo de Ejecución

### Ejemplo 1:
```
Ventas del lunes: 120.50
Ventas del martes: 200.00
...
Ventas del domingo: 150.00
Total semanal: $1050.50
Promedio diario: $150.07
```

### Ejemplo 2:
```
Ventas del lunes: 0
...
Ventas del domingo: 0
Total semanal: $0.00
Promedio diario: $0.00
```

### Ejemplo 3:
```
Ventas del lunes: -50
Entrada inválida. Las ventas no pueden ser negativas.
```

## 🧪 Casos de Prueba

| Ventas (Lun-Dom) | Total | Promedio |
|------------------|-------|----------|
| 100,100,100,100,100,100,100 | 700 | 100.00 |
| 0,...,0 | 0 | 0.00 |
| 120.5, 200, 150, 80, 95, 60, 90 | 795.5 | 113.64 |
| Incluye valor negativo | Mensaje de error |
| Valores mixtos | Total y promedio correctos |

## 💡 Pistas

1. Usa una lista con los nombres de los días para mostrar mensajes personalizados.
2. Valida que cada monto sea mayor o igual a 0 antes de sumarlo.
3. Formatea los resultados con `f"{valor:.2f}"`.

## ⚠️ Errores Comunes

- ❌ No reiniciar el acumulador antes del ciclo.
- ❌ Olvidar dividir entre 7 para el promedio.
- ❌ Aceptar montos negativos sin validar.

## 🎓 Conceptos Practicados

- Ciclo `for`
- Acumuladores y promedios
- Manejo de listas

## 🚀 Desafíos Extra (Opcional)

1. Muestra el día con la mayor y menor venta.
2. Permite al usuario ingresar el número de días a registrar.
3. Genera un reporte formateado con columnas.

---

**Tiempo estimado**: 15-20 minutos  
**Archivo de solución**: `ejercicio_18.py`


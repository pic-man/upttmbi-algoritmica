# Ejercicio 10: Intercambiar Valores

## Dificultad: ⭐⭐ Intermedio

## Descripción

Crea un programa que pida dos números y luego intercambie sus valores. Muestra los valores antes y después del intercambio.

## Análisis

| Parte | Descripción |
|-------|-------------|
| **ENTRADA** | Dos números (a y b) |
| **PROCESO** | Intercambiar los valores de a y b |
| **SALIDA** | Valores antes y después del intercambio |

## Ejemplo de Ejecución

```
Ingresa el primer número (a): 10
Ingresa el segundo número (b): 25

Antes del intercambio:
a = 10
b = 25

Después del intercambio:
a = 25
b = 10
```

## Pistas

### Método 1: Usando una variable temporal
```python
temporal = a
a = b
b = temporal
```

### Método 2: Intercambio directo en Python
```python
a, b = b, a
```

## ¿Por qué es importante?

Este ejercicio enseña un concepto fundamental: las variables pueden cambiar de valor, y a veces necesitamos reorganizar datos.

## Entrega

Guarda tu solución como `ejercicio_10.py`

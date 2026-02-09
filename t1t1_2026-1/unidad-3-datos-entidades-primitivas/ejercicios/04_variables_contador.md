# 🔄 Ejercicio 04: Variables Contador y Acumulador

## Nivel: ⭐⭐ Intermedio

## 📝 Descripción

Crea un programa que analice una lista de números y use contadores y acumuladores para calcular estadísticas.

## 🎯 Objetivo

Practicar el uso de variables contador y acumulador en problemas reales.

## 📋 Requisitos

El programa debe:

1. Pedir al usuario que ingrese 10 números
2. Usar un **contador** para contar:
   - Cuántos son positivos
   - Cuántos son negativos
   - Cuántos son cero
   - Cuántos son pares
   - Cuántos son impares

3. Usar un **acumulador** para calcular:
   - La suma de todos los números
   - La suma de los positivos
   - La suma de los negativos
   - El promedio general

## 📤 Ejemplo de Salida

```
=== ANALIZADOR DE NÚMEROS ===

Ingrese el número 1: 5
Ingrese el número 2: -3
Ingrese el número 3: 0
...
Ingrese el número 10: 8

--- ESTADÍSTICAS ---
Contadores:
  Positivos: 6
  Negativos: 3
  Ceros: 1
  Pares: 4
  Impares: 6

Acumuladores:
  Suma total: 25
  Suma positivos: 35
  Suma negativos: -10
  Promedio: 2.5
```

## 💡 Estructura Sugerida

```python
# Contadores (iniciar en 0)
contador_positivos = 0
contador_negativos = 0
contador_ceros = 0

# Acumuladores (iniciar en 0)
suma_total = 0
suma_positivos = 0

# Ciclo para ingresar números
for i in range(10):
    numero = int(input(f"Ingrese número {i+1}: "))
    
    # Actualizar contadores
    if numero > 0:
        contador_positivos += 1
        suma_positivos += numero
    # ... más condiciones
    
    # Actualizar acumuladores
    suma_total += numero
```

## ✅ Criterios de Evaluación

| Criterio | Puntos |
|----------|--------|
| Contadores correctos | 30 |
| Acumuladores correctos | 30 |
| Cálculo del promedio | 15 |
| Código organizado | 15 |
| Documentación | 10 |

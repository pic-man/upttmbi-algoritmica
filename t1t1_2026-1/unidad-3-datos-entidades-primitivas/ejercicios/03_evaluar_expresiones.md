# 🧮 Ejercicio 03: Evaluar Expresiones

## Nivel: ⭐ Básico

## 📝 Descripción

Evalúa las siguientes expresiones manualmente y luego verifica tus respuestas con Python.

## 🎯 Objetivo

Practicar la evaluación de expresiones siguiendo las reglas de precedencia.

## 📋 Expresiones a Evaluar

Evalúa cada expresión **paso a paso** en papel, luego verifica con Python:

```python
# Expresiones aritméticas
a = 5 + 3 * 2
b = (5 + 3) * 2
c = 20 / 4 + 3 * 2
d = 2 ** 3 ** 2
e = 15 % 4 + 10 // 3

# Expresiones relacionales
f = 10 > 5 and 3 < 2
g = 10 > 5 or 3 < 2
h = not (5 == 5)
i = (4 + 3) > (2 * 3)
j = "abc" < "abd"

# Expresiones mixtas
k = 5 + 3 > 7 and 2 * 3 == 6
l = (10 - 5) * 2 == 10 or False
```

## 📝 Formato de Entrega

Para cada expresión:

```
Expresión: 5 + 3 * 2

Evaluación paso a paso:
1. Primero se evalúa 3 * 2 = 6 (multiplicación tiene precedencia)
2. Luego se evalúa 5 + 6 = 11

Resultado esperado: 11
Resultado en Python: [ejecutar y verificar]
¿Coincide? Sí/No
```

## ✅ Criterios de Evaluación

| Criterio | Puntos |
|----------|--------|
| Evaluación correcta de expresiones aritméticas | 30 |
| Evaluación correcta de expresiones relacionales | 30 |
| Evaluación correcta de expresiones mixtas | 20 |
| Explicación paso a paso | 20 |

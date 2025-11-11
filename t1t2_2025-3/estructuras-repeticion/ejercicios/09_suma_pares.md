# 🟦 Ejercicio 9: Suma de Pares

## Dificultad: ⭐ Básico

## 📝 Descripción

Escribe un programa que sume todos los números pares entre 1 y un número `n` ingresado por el usuario.

## 🎯 Objetivo

Practicar ciclos `for`, operadores aritméticos y condiciones dentro de un bucle.

## 📋 Especificaciones

El programa debe:

1. Solicitar un entero positivo `n`.
2. Validar que `n` sea mayor o igual que 1.
3. Recorrer los números del 1 al `n`.
4. Sumar únicamente aquellos que sean pares.
5. Mostrar el resultado final.

## 💻 Ejemplo de Ejecución

### Ejemplo 1:
```
Ingresa un número entero positivo: 6
La suma de pares entre 1 y 6 es: 12
```

### Ejemplo 2:
```
Ingresa un número entero positivo: 1
La suma de pares entre 1 y 1 es: 0
```

### Ejemplo 3:
```
Ingresa un número entero positivo: 0
Entrada no válida. Debes ingresar un entero mayor o igual a 1.
```

## 🧪 Casos de Prueba

| Entrada | Salida Esperada |
|---------|----------------|
| 2 | 2 |
| 5 | 6 |
| 6 | 12 |
| 10 | 30 |
| 1 | 0 |

## 💡 Pistas

1. Usa `range(1, n + 1)` y `if numero % 2 == 0` para detectar pares.
2. También puedes usar `range(2, n + 1, 2)` para iterar solo números pares.
3. Lleva un acumulador y súmale cada número par encontrado.

## ⚠️ Errores Comunes

- ❌ Sumar todos los números en lugar de solo los pares.
- ❌ Empezar el rango en 0 y sumar un valor extra.
- ❌ No validar que `n` sea al menos 1.

## 🎓 Conceptos Practicados

- Ciclo `for`
- Uso de `range`
- Condiciones con módulo

## 🚀 Desafíos Extra (Opcional)

1. Muestra también cuántos números pares fueron sumados.
2. Calcula la suma de los impares en otra variable y muéstrala.
3. Implementa la misma lógica con un ciclo `while`.

---

**Tiempo estimado**: 5-10 minutos  
**Archivo de solución**: `ejercicio_09.py`


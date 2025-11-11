# 🔢 Ejercicio 1: Contador Ascendente

## Dificultad: ⭐ Básico

## 📝 Descripción

Construye un programa que muestre en pantalla los números desde 1 hasta un número entero positivo ingresado por el usuario.

## 🎯 Objetivo

Practicar el uso de ciclos `while` con incrementos simples y validación de entrada.

## 📋 Especificaciones

El programa debe:

1. Solicitar un número entero positivo `n`.
2. Validar que `n` sea mayor que 0.
3. Imprimir los números desde 1 hasta `n`, inclusive, uno por línea o separados por espacios.
4. Mostrar un mensaje de error si `n` no es válido.

## 💻 Ejemplo de Ejecución

### Ejemplo 1:
```
Ingresa un número entero positivo: 5
1 2 3 4 5
```

### Ejemplo 2:
```
Ingresa un número entero positivo: 1
1
```

### Ejemplo 3:
```
Ingresa un número entero positivo: -4
Entrada no válida. Debes ingresar un entero mayor que cero.
```

## 🧪 Casos de Prueba

| Entrada | Salida Esperada |
|---------|----------------|
| 3 | 1 2 3 |
| 5 | 1 2 3 4 5 |
| 1 | 1 |
| 0 | Mensaje de error |
| -2 | Mensaje de error |

## 💡 Pistas

1. Usa `int(input())` para leer el número.
2. Inicializa un contador en 1.
3. Incrementa el contador dentro del ciclo `while` hasta que sea mayor que `n`.
4. Puedes acumular los números en una lista y luego usar `" ".join()` para imprimirlos.

## ⚠️ Errores Comunes

- ❌ Olvidar actualizar el contador dentro del ciclo.
- ❌ No validar la entrada y provocar un ciclo infinito con valores negativos.
- ❌ Empezar desde 0 cuando el ejercicio pide iniciar en 1.

## 🎓 Conceptos Practicados

- Ciclo `while`
- Contadores e incrementos
- Validación de entrada

## 🚀 Desafíos Extra (Opcional)

1. Permite mostrar los números separados por comas.
2. Agrega la opción de iniciar desde un valor diferente a 1.
3. Muestra también la suma total de los números impresos.

---

**Tiempo estimado**: 5-10 minutos  
**Archivo de solución**: `ejercicio_01.py`


# 🌀 Ejercicio 7: Serie Fibonacci

## Dificultad: ⭐⭐ Intermedio

## 📝 Descripción

Genera los primeros `n` términos de la serie de Fibonacci, donde cada número es la suma de los dos anteriores.

## 🎯 Objetivo

Practicar ciclos `while`, actualización de múltiples variables y manejo de secuencias.

## 📋 Especificaciones

El programa debe:

1. Solicitar un entero `n` mayor o igual que 1.
2. Validar que `n` sea positivo.
3. Mostrar los primeros `n` términos de la serie de Fibonacci.
4. Si `n` es 1 o 2, manejar adecuadamente los casos base.

## 💻 Ejemplo de Ejecución

### Ejemplo 1:
```
¿Cuántos términos de Fibonacci deseas generar? 6
Serie: 0 1 1 2 3 5
```

### Ejemplo 2:
```
¿Cuántos términos de Fibonacci deseas generar? 1
Serie: 0
```

### Ejemplo 3:
```
¿Cuántos términos de Fibonacci deseas generar? 0
Entrada no válida. Ingresa un entero mayor o igual a 1.
```

## 🧪 Casos de Prueba

| Entrada | Salida Esperada |
|---------|----------------|
| 1 | 0 |
| 2 | 0 1 |
| 5 | 0 1 1 2 3 |
| 8 | 0 1 1 2 3 5 8 13 |
| 0 | Mensaje de error |

## 💡 Pistas

1. Usa dos variables para almacenar los dos últimos términos (`a` y `b`).
2. Actualiza ambas variables en cada iteración para generar el siguiente número.
3. Lleva un contador de cuántos términos has imprimido.
4. Considera usar una lista para almacenar y luego mostrar la serie completa.

## ⚠️ Errores Comunes

- ❌ Olvidar actualizar las variables y producir la secuencia 0, 1, 1, 1...
- ❌ No manejar el caso en que `n` es 1 o 2.
- ❌ Confundir la serie iniciando en 1, 1 en lugar de 0, 1.

## 🎓 Conceptos Practicados

- Ciclo `while`
- Actualización de múltiples variables
- Generación de secuencias

## 🚀 Desafíos Extra (Opcional)

1. Calcula la suma de los términos generados.
2. Detén la serie cuando se supere un valor máximo ingresado por el usuario.
3. Implementa una versión que use un ciclo `for`.

---

**Tiempo estimado**: 15-20 minutos  
**Archivo de solución**: `ejercicio_07.py`


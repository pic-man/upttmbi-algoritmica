# 🎯 Ejercicio 13: Juego de Adivinanza

## Dificultad: ⭐⭐ Intermedio

## 📝 Descripción

Diseña un juego donde la computadora piense en un número secreto y el usuario deba adivinarlo, recibiendo pistas de "mayor" o "menor" en cada intento.

## 🎯 Objetivo

Practicar ciclos `while`, comparaciones y retroalimentación iterativa al usuario.

## 📋 Especificaciones

El programa debe:

1. Definir un número secreto (por ejemplo, 37) o generarlo aleatoriamente entre 1 y 100.
2. Solicitar al usuario que adivine el número.
3. Indicar si el valor ingresado es mayor o menor que el número secreto.
4. Repetir el proceso hasta que el usuario adivine.
5. Contar y mostrar el número de intentos usados.

## 💻 Ejemplo de Ejecución

### Ejemplo 1:
```
Estoy pensando en un número entre 1 y 100.
Adivina el número: 50
Demasiado alto.
Adivina el número: 25
Demasiado bajo.
Adivina el número: 37
¡Correcto! Lo lograste en 3 intentos.
```

### Ejemplo 2:
```
Estoy pensando en un número entre 1 y 100.
Adivina el número: 37
¡Correcto! Lo lograste en 1 intento.
```

### Ejemplo 3:
```
Estoy pensando en un número entre 1 y 100.
Adivina el número: -5
Fuera de rango. Intenta otra vez.
```

## 🧪 Casos de Prueba

| Entradas | Salida Esperada |
|----------|-----------------|
| 37 | Acierto en 1 intento |
| 50, 40, 37 | Acierto en 3 intentos con pistas |
| -1, 120, 37 | Mensajes de fuera de rango y acierto |
| Varias entradas incorrectas | Pistas y conteo correcto |
| Entrada no numérica | Mensaje de error (si decides manejarlo) |

## 💡 Pistas

1. Usa un `while True` y rompe el ciclo cuando el usuario acierte.
2. Incrementa un contador de intentos en cada iteración válida.
3. Puedes usar `random.randint(1, 100)` para generar el número secreto.
4. Maneja entradas fuera del rango válido mostrando un aviso.

## ⚠️ Errores Comunes

- ❌ No actualizar el contador de intentos correctamente.
- ❌ Olvidar convertir la entrada a entero antes de compararla.
- ❌ No dar pistas claras y confundir al usuario.

## 🎓 Conceptos Practicados

- Ciclo `while` infinito controlado con `break`
- Condicionales anidados
- Validación de rangos

## 🚀 Desafíos Extra (Opcional)

1. Limita la cantidad máxima de intentos y avisa cuando se acaben.
2. Permite al usuario elegir el rango del número secreto.
3. Guarda los intentos en una lista y muéstralos al finalizar.

---

**Tiempo estimado**: 15-20 minutos  
**Archivo de solución**: `ejercicio_13.py`


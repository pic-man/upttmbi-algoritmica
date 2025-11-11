# 🔁 01 - Introducción a las Estructuras de Repetición

## ¿Qué son las estructuras de repetición?

Las estructuras de repetición (o **bucles**) permiten ejecutar un bloque de código varias veces. Son esenciales cuando necesitas realizar tareas repetitivas sin escribir el mismo código múltiples veces.

En Python existen principalmente dos ciclos:

- `for`: Recorre de forma directa los **elementos de un iterable** (listas, strings, rangos, etc.).
- `while`: Repite un bloque **mientras una condición sea verdadera**.

## ¿Por qué son importantes?

- Automatizan tareas repetitivas.
- Reducen la cantidad de código redundante.
- Permiten procesar colecciones de datos de manera eficiente.
- Facilitan cálculos acumulativos (sumas, contadores, promedios).

## ¿Cuándo usar cada uno?

| Situación | Ciclo recomendado | Ejemplo |
|-----------|------------------|---------|
| Recorrer elementos de una lista o rango | `for` | Recorrer estudiantes en una lista |
| Repetir hasta que se cumpla una condición | `while` | Pedir contraseña hasta que sea correcta |
| Necesitas el índice y el valor | `for` con `enumerate` | Mostrar posición y nombre |
| No sabes cuántas repeticiones habrá | `while` | Leer datos hasta que el usuario escriba `fin` |

## Ciclo `for` (visión general)

```python
numeros = [1, 2, 3, 4]
for numero in numeros:
    print(numero)
```

Aquí `numero` toma cada valor de la lista en orden y se ejecuta `print` por cada iteración.

## Ciclo `while` (visión general)

```python
contador = 1
while contador <= 5:
    print(contador)
    contador += 1
```

El ciclo continúa mientras la condición sea verdadera. ¡Recuerda actualizar la variable de control!

## Componentes clave de un bucle

1. **Inicio**: Valores iniciales para contadores o variables de control.
2. **Condición**: La regla que determina si el ciclo continúa o se detiene.
3. **Actualización**: Cambios en variables dentro del ciclo para eventualmente salir.
4. **Cuerpo**: El bloque de instrucciones que se ejecuta en cada iteración.

## Ciclos infinitos

Un ciclo infinito ocurre cuando la condición nunca se vuelve falsa. A veces son útiles (por ejemplo, en menús), pero deben estar controlados con un `break` o una opción de salida.

```python
while True:
    comando = input("Escribe 'salir' para terminar: ")
    if comando == "salir":
        break
```

## Ejemplos cotidianos de bucles

- Contar hasta un número dado.
- Calcular la suma de una lista de calificaciones.
- Repetir un menú hasta que el usuario elija salir.
- Procesar cada carácter de un texto.

## Siguientes pasos

1. Estudia los ciclos `for` y `while` en detalle.
2. Experimenta con ejemplos sencillos.
3. Aprende a combinar ciclos con condicionales.
4. Practica evitando ciclos infinitos o sin condición de salida clara.

---

Continúa con [02 - Ciclo `for`](02_ciclo_for.md) para profundizar en la sintaxis y patrones comunes. ¡Vamos! 🚀


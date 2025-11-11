# 🔁 03 - Ciclo `while` en Python

El ciclo `while` repite un bloque de código **mientras una condición sea verdadera**. Es ideal cuando no sabes cuántas veces necesitarás repetir algo, pero sí conoces la condición de término.

## Sintaxis básica

```python
while condicion:
    # bloque de código
```

- La condición se evalúa **antes** de cada iteración.
- Si la condición es `False`, el ciclo se detiene.

## Ejemplo sencillo

```python
contador = 1
while contador <= 5:
    print(contador)
    contador += 1
```

Salida:
```
1
2
3
4
5
```

Si olvidas incrementar `contador`, el ciclo se vuelve infinito.

## Ciclos controlados por entrada

```python
respuesta = ""
while respuesta != "salir":
    respuesta = input("Escribe 'salir' para terminar: ")
```

La condición depende de lo que ingrese el usuario.

## Validación de datos

```python
edad = int(input("Ingresa tu edad: "))
while edad < 0:
    print("La edad no puede ser negativa.")
    edad = int(input("Ingresa tu edad: "))
```

Se repite hasta obtener un valor válido.

## Uso de sentinela

Un sentinela es un valor especial que indica al programa cuándo detenerse.

```python
total = 0
while True:
    numero = int(input("Ingresa un número (0 para terminar): "))
    if numero == 0:
        break
    total += numero

print(f"Suma total: {total}")
```

## Ciclos infinitos controlados

```python
while True:
    comando = input("> ")
    if comando == "salir":
        print("Hasta luego")
        break
    print(f"Comando recibido: {comando}")
```

Los bucles infinitos son útiles para menús o programas interactivos, siempre y cuando exista una forma de salir.

## Bucle `while` con `else`

El bloque `else` se ejecuta cuando la condición se vuelve falsa **sin usar `break`**.

```python
contador = 3
while contador > 0:
    print(contador)
    contador -= 1
else:
    print("¡Feliz año nuevo!")
```

## Advertencias comunes

- **Ciclos infinitos involuntarios**: asegúrate de que la condición cambie durante la ejecución.
- **Condición mal planteada**: verifica siempre la lógica de salida.
- **Actualización fuera del ciclo**: la variable debe actualizarse dentro del bloque indentado.

## `while` vs `for`

| Pregunta | `for` | `while` |
|----------|-------|---------|
| ¿Conoces la cantidad de repeticiones? | ✅ | ❌ |
| ¿Depende de una condición dinámica? | ❌ | ✅ |
| ¿Recorres una colección? | ✅ | ❌ |
| ¿Necesitas un menú infinito con opción de salida? | ❌ | ✅ |

## Buenas prácticas

- Define con claridad la condición de salida.
- Inicializa variables de control antes del ciclo.
- Usa `break` y `continue` con moderación para mantener la legibilidad.
- Prueba el ciclo con diferentes escenarios para asegurar que termina.

---

Continúa con [04 - Control de Bucles](04_control_bucles.md) para aprender a usar `break`, `continue` y el bloque `else` en bucles. 🛑➡️


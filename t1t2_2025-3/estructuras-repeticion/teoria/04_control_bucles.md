# ⛳ 04 - Control de Bucles: `break`, `continue`, `else`

Además de la condición principal del ciclo, Python ofrece herramientas para controlar la ejecución interna de los bucles. Estas palabras clave permiten modificar el flujo sin modificar la condición general.

## `break`: salir del ciclo inmediatamente

Detiene el bucle incluso si la condición aún es verdadera.

### Ejemplo

```python
while True:
    comando = input("> ")
    if comando == "salir":
        print("Hasta luego.")
        break
    print(f"Comando recibido: {comando}")
```

Sin `break`, este ciclo sería infinito.

## `continue`: saltar a la siguiente iteración

Omite el resto del bloque actual y vuelve a evaluar la condición.

### Ejemplo

```python
for numero in range(1, 11):
    if numero % 2 != 0:
        continue
    print(numero)
```

Este programa imprime solo los números pares del 1 al 10.

## La cláusula `else` en bucles

El bloque `else` se ejecuta cuando el bucle termina **de forma natural** (sin `break`). Funciona tanto con `for` como con `while`.

### Ejemplo con `for`

```python
numeros = [2, 4, 6, 8]
for numero in numeros:
    if numero % 2 != 0:
        print("Encontré un impar.")
        break
else:
    print("Todos los números son pares.")
```

### Ejemplo con `while`

```python
contador = 3
while contador > 0:
    print(contador)
    contador -= 1
else:
    print("Contador en cero, ciclo completado.")
```

Si agregas un `break` antes de terminar, el bloque `else` no se ejecutará.

## Combinando `break` y `continue`

```python
while True:
    numero = int(input("Ingresa un número positivo (0 para salir): "))
    if numero == 0:
        print("Programa terminado.")
        break
    if numero < 0:
        print("Número inválido. Intenta de nuevo.")
        continue
    print(f"Procesando {numero}...")
```

- `break` cierra el programa cuando se ingresa 0.
- `continue` ignora números negativos sin finalizar el ciclo.

## ¿Cuándo usarlos?

- Usa `break` cuando la condición de salida no depende solo de la condición inicial.
- Usa `continue` para saltar casos que no necesitas procesar.
- Usa `else` para ejecutar lógica adicional si el ciclo concluye normalmente.

## Buenas prácticas

1. **Evita abusar de `break`**: si usas demasiados, el código puede volverse difícil de seguir.
2. **Coloca comentarios** cuando el control del flujo no sea evidente.
3. **Combina con funciones** para aislar la lógica del bucle.
4. **Prueba ambos caminos** (con y sin `break`) para verificar que `else` se ejecuta o no según corresponda.

---

Continúa con [05 - Buenas Prácticas](05_buenas_practicas.md) para escribir bucles claros, eficientes y seguros. ✅


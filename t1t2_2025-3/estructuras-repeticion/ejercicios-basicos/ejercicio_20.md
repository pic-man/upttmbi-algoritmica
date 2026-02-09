# Ejercicio 20: Pirámide de asteriscos

## Enunciado

Haz un programa que pida un número N e imprima una pirámide de asteriscos con N filas.

## Ejemplo de ejecución

```
¿Cuántas filas? 5
*
**
***
****
*****
```

## Otro ejemplo

```
¿Cuántas filas? 3
*
**
***
```

## Pista

Necesitas un bucle dentro de otro (bucles anidados):
- El bucle externo controla las filas (1 a N)
- El bucle interno imprime los asteriscos de cada fila

```python
for fila in range(1, n + 1):
    for asterisco in range(fila):
        print("*", end="")
    print()  # Salto de línea al final de cada fila
```

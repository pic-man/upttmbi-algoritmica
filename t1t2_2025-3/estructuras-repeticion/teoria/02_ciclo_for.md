# 🔂 02 - Ciclo `for` en Python

El ciclo `for` es ideal para recorrer colecciones o secuencias de valores (listas, cadenas, rangos, diccionarios, etc.). Python simplifica su uso permitiendo iterar directamente sobre los elementos sin índices manuales.

## Sintaxis básica

```python
for variable in iterable:
    # bloque de código
```

- `variable`: toma el valor de cada elemento en el iterable.
- `iterable`: estructura que contiene elementos (lista, string, `range`, etc.).

## Ejemplo básico

```python
frutas = ["manzana", "pera", "uva"]
for fruta in frutas:
    print(fruta)
```

Salida:
```
manzana
pera
uva
```

## Usando `range`

`range()` genera secuencias de números. Es muy útil para contar o repetir acciones un número específico de veces.

```python
for numero in range(1, 6):
    print(numero)
```

Salida:
```
1
2
3
4
5
```

### Formas de `range`

```python
range(stop)           # 0 a stop-1
range(start, stop)    # start a stop-1
range(start, stop, step)  # paso personalizado
```

Ejemplo con paso:

```python
for numero in range(0, 10, 2):
    print(numero)
```

Salida:
```
0
2
4
6
8
```

## Accediendo al índice y al valor

Usa `enumerate` para obtener el índice junto al valor.

```python
estudiantes = ["Ana", "Luis", "Sara"]
for indice, nombre in enumerate(estudiantes, start=1):
    print(f"{indice}. {nombre}")
```

Salida:
```
1. Ana
2. Luis
3. Sara
```

## Iterar sobre cadenas

```python
mensaje = "Python"
for caracter in mensaje:
    print(caracter)
```

## Comprensiones de listas (mención rápida)

Son una forma compacta de crear listas usando `for`.

```python
cuadrados = [numero ** 2 for numero in range(1, 6)]
print(cuadrados)  # [1, 4, 9, 16, 25]
```

## Ciclos anidados

Puedes combinar bucles para recorrer estructuras bidimensionales.

```python
for fila in range(1, 4):
    for columna in range(1, 4):
        print(f"({fila}, {columna})", end=" ")
    print()
```

## Iterar sobre diccionarios

```python
precios = {"manzana": 1.2, "pera": 0.8, "uva": 1.5}
for fruta, precio in precios.items():
    print(f"{fruta}: ${precio}")
```

## Consejos

- Usa nombres descriptivos para la variable del ciclo.
- Si solo necesitas repetir algo varias veces, `range` es tu aliado.
- Evita modificar la colección que estás recorriendo.
- Combina `for` con condicionales para filtrar o tomar decisiones.

---

Continúa con [03 - Ciclo `while`](03_ciclo_while.md) para aprender a repetir acciones basadas en condiciones dinámicas. 👣


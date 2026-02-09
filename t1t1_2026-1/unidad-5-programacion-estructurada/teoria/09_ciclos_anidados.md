# 📖 09 - Ciclos Anidados

## ¿Qué son los Ciclos Anidados?

Los **ciclos anidados** son ciclos que contienen otros ciclos en su interior. Se utilizan para trabajar con estructuras bidimensionales o para generar combinaciones.

```
┌─────────────────────────────────────────────┐
│ CICLO EXTERNO (i)                           │
│  ┌───────────────────────────────────────┐  │
│  │ CICLO INTERNO (j)                     │  │
│  │   - Se ejecuta completamente          │  │
│  │   - Por cada iteración del externo    │  │
│  └───────────────────────────────────────┘  │
└─────────────────────────────────────────────┘
```

## Ejemplo Básico

```python
for i in range(1, 4):        # Ciclo externo: 3 veces
    for j in range(1, 3):    # Ciclo interno: 2 veces
        print(f"i={i}, j={j}")
    print("---")

# Salida:
# i=1, j=1
# i=1, j=2
# ---
# i=2, j=1
# i=2, j=2
# ---
# i=3, j=1
# i=3, j=2
# ---
```

## Ejemplos Prácticos

### Tabla de multiplicar completa

```python
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i:2} x {j:2} = {i*j:3}", end="  ")
    print()  # Nueva línea después de cada fila
```

### Patrón de asteriscos (triángulo)

```python
filas = 5
for i in range(1, filas + 1):
    for j in range(i):
        print("*", end="")
    print()

# Salida:
# *
# **
# ***
# ****
# *****
```

### Patrón de números

```python
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Salida:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
```

### Matriz (lista de listas)

```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Recorrer e imprimir
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()

# Con índices
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f"matriz[{i}][{j}] = {matriz[i][j]}")
```

### Búsqueda en matriz

```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

buscar = 5
encontrado = False

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == buscar:
            print(f"Encontrado en posición [{i}][{j}]")
            encontrado = True
            break
    if encontrado:
        break

if not encontrado:
    print("No encontrado")
```

## Consideraciones de Rendimiento

```python
# Ejemplo: 1000 x 1000 = 1,000,000 iteraciones
for i in range(1000):
    for j in range(1000):
        # Esta operación se ejecuta 1 millón de veces
        pass

# Consejo: Minimizar las operaciones dentro de ciclos anidados
```

## 📝 Para Recordar

1. El ciclo interno se ejecuta **completamente** por cada iteración del externo
2. El total de iteraciones es: externo × interno
3. Útiles para **matrices** y **tablas**
4. Usar **break** con cuidado (solo sale del ciclo actual)
5. Considerar el **rendimiento** con muchas iteraciones

---

¡Felicidades! Has completado la teoría de estructuras de control.

[Ir a: Ejercicios →](../ejercicios/README.md)

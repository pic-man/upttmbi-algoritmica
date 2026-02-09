# 📖 08 - Ciclo Para (For)

## ¿Qué es el Ciclo For?

El ciclo **for** repite un bloque de instrucciones un **número determinado** de veces o itera sobre una secuencia.

## Sintaxis en Python

```python
# Iterar sobre un rango
for variable in range(inicio, fin, paso):
    # instrucciones

# Iterar sobre una secuencia
for elemento in secuencia:
    # instrucciones
```

## Función range()

```python
range(fin)           # 0, 1, 2, ..., fin-1
range(inicio, fin)   # inicio, inicio+1, ..., fin-1
range(inicio, fin, paso)  # inicio, inicio+paso, ..., hasta fin-1
```

## Ejemplos Básicos

### Contar del 1 al 5

```python
for i in range(1, 6):
    print(i)
# Salida: 1, 2, 3, 4, 5
```

### Contar de 2 en 2

```python
for i in range(0, 10, 2):
    print(i)
# Salida: 0, 2, 4, 6, 8
```

### Cuenta regresiva

```python
for i in range(5, 0, -1):
    print(i)
# Salida: 5, 4, 3, 2, 1
```

### Iterar sobre una lista

```python
frutas = ["manzana", "naranja", "plátano"]
for fruta in frutas:
    print(f"Me gusta la {fruta}")
```

### Iterar sobre una cadena

```python
palabra = "Python"
for letra in palabra:
    print(letra)
```

## Ejemplos Prácticos

### Tabla de multiplicar

```python
numero = 5
print(f"Tabla del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
```

### Sumar números del 1 al 100

```python
suma = 0
for i in range(1, 101):
    suma += i
print(f"La suma es: {suma}")  # 5050
```

### Factorial

```python
n = 5
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"{n}! = {factorial}")  # 120
```

## For con enumerate()

Para obtener índice y valor:

```python
nombres = ["Ana", "Luis", "María"]
for indice, nombre in enumerate(nombres):
    print(f"{indice + 1}. {nombre}")
# Salida:
# 1. Ana
# 2. Luis
# 3. María
```

## For con zip()

Para iterar dos listas en paralelo:

```python
nombres = ["Ana", "Luis", "María"]
edades = [25, 30, 28]

for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")
```

## Ciclos Anidados

```python
# Tabla de multiplicar completa
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print("---")
```

## While vs For

| Característica | while | for |
|----------------|-------|-----|
| Uso ideal | Condición desconocida | Número conocido de iteraciones |
| Control | Manual de variable | Automático con range() |
| Riesgo | Ciclo infinito | Bajo riesgo |

## 📝 Para Recordar

1. **for** es ideal cuando se conoce el número de iteraciones
2. **range()** genera secuencias de números
3. Se puede iterar sobre listas, cadenas, etc.
4. **enumerate()** da índice y valor
5. **zip()** itera en paralelo

## 🔜 Siguiente Paso

[Ir a: 09 - Ciclos Anidados →](./09_ciclos_anidados.md)

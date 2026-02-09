# 📖 01 - Introducción a las Listas

## ¿Qué es una Lista?

Una **lista** en Python es una colección ordenada y modificable de elementos. Es una de las estructuras de datos más versátiles y utilizadas en Python.

```python
# Una lista simple
frutas = ["manzana", "banana", "naranja"]
```

## 🔑 Características Clave

### 1. Ordenadas
Los elementos mantienen el orden en que fueron agregados.

```python
numeros = [1, 2, 3, 4, 5]
print(numeros[0])  # 1 (primer elemento)
print(numeros[-1]) # 5 (último elemento)
```

### 2. Modificables (Mutables)
Puedes cambiar, agregar o eliminar elementos después de crear la lista.

```python
colores = ["rojo", "verde", "azul"]
colores[0] = "amarillo"  # Cambiar elemento
colores.append("negro")   # Agregar elemento
```

### 3. Permiten Duplicados
Una lista puede contener valores repetidos.

```python
numeros = [1, 2, 2, 3, 3, 3]  # Válido
```

### 4. Pueden Contener Diferentes Tipos
Una lista puede tener números, strings, booleanos, incluso otras listas.

```python
mixta = [1, "hola", True, 3.14, [1, 2, 3]]
```

## 📝 Crear Listas

### Método 1: Usando corchetes []
```python
# Lista vacía
vacia = []

# Lista con elementos
numeros = [1, 2, 3, 4, 5]
nombres = ["Ana", "Juan", "Pedro"]
```

### Método 2: Usando list()
```python
# De un string
letras = list("Python")  # ['P', 'y', 't', 'h', 'o', 'n']

# De un rango
numeros = list(range(1, 6))  # [1, 2, 3, 4, 5]
```

### Método 3: List Comprehension
```python
# Lista de cuadrados
cuadrados = [x**2 for x in range(1, 6)]  # [1, 4, 9, 16, 25]
```

## 🎯 Acceder a Elementos

### Índices Positivos (desde el inicio)
```python
frutas = ["manzana", "banana", "naranja", "pera"]

print(frutas[0])   # "manzana" (primer elemento)
print(frutas[1])   # "banana"
print(frutas[3])   # "pera" (cuarto elemento)
```

### Índices Negativos (desde el final)
```python
print(frutas[-1])  # "pera" (último)
print(frutas[-2])  # "naranja" (penúltimo)
```

### Slicing (Rebanadas)
```python
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numeros[2:5])    # [2, 3, 4] (desde 2 hasta 5, sin incluir 5)
print(numeros[:3])     # [0, 1, 2] (desde el inicio hasta 3)
print(numeros[7:])     # [7, 8, 9] (desde 7 hasta el final)
print(numeros[::2])    # [0, 2, 4, 6, 8] (cada 2 elementos)
print(numeros[::-1])   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (invertida)
```

## 🔍 Operaciones Básicas

### Longitud
```python
frutas = ["manzana", "banana", "naranja"]
print(len(frutas))  # 3
```

### Verificar Existencia
```python
if "banana" in frutas:
    print("Sí tenemos bananas!")
```

### Concatenar Listas
```python
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
combinada = lista1 + lista2  # [1, 2, 3, 4, 5, 6]
```

### Repetir Listas
```python
ceros = [0] * 5  # [0, 0, 0, 0, 0]
```

## 💡 Ejemplos Prácticos

### Ejemplo 1: Lista de compras
```python
compras = ["leche", "pan", "huevos"]

# Agregar artículo
compras.append("café")

# Verificar si tenemos algo
if "pan" in compras:
    print("Tenemos pan")

# Ver total de artículos
print(f"Artículos en la lista: {len(compras)}")
```

### Ejemplo 2: Temperaturas de la semana
```python
temperaturas = [22, 24, 23, 25, 26, 24, 22]

# Temperatura máxima
max_temp = max(temperaturas)

# Temperatura mínima
min_temp = min(temperaturas)

# Promedio
promedio = sum(temperaturas) / len(temperaturas)

print(f"Máxima: {max_temp}°C")
print(f"Mínima: {min_temp}°C")
print(f"Promedio: {promedio:.1f}°C")
```

### Ejemplo 3: Lista de tareas
```python
tareas = ["Estudiar", "Hacer ejercicio", "Cocinar"]

print("Mis tareas de hoy:")
for i, tarea in enumerate(tareas, 1):
    print(f"{i}. {tarea}")
```

## 📊 Comparación con Otros Lenguajes

| Python | JavaScript | Java | C++ |
|--------|-----------|------|-----|
| `lista = [1, 2, 3]` | `let arr = [1, 2, 3]` | `ArrayList<Integer> list` | `vector<int> vec` |
| `lista.append(4)` | `arr.push(4)` | `list.add(4)` | `vec.push_back(4)` |
| `len(lista)` | `arr.length` | `list.size()` | `vec.size()` |

## ⚠️ Errores Comunes

### 1. Índice fuera de rango
```python
frutas = ["manzana", "banana"]
# print(frutas[5])  # Error: list index out of range
```

### 2. Modificar durante iteración
```python
# ❌ INCORRECTO
numeros = [1, 2, 3, 4, 5]
for num in numeros:
    if num % 2 == 0:
        numeros.remove(num)  # Puede causar problemas

# ✅ CORRECTO
numeros = [num for num in numeros if num % 2 != 0]
```

## 📝 Para Recordar

1. Las listas se crean con `[]`
2. Los índices empiezan en 0
3. Se pueden usar índices negativos (-1 es el último)
4. Las listas son mutables (se pueden modificar)
5. Pueden contener cualquier tipo de dato
6. Usa `len()` para obtener la longitud
7. Usa `in` para verificar si un elemento existe

## 🔜 Siguiente Paso

Ahora que entiendes qué son las listas y cómo crearlas, aprenderás los métodos más importantes para manipularlas.

[Ir a: 02 - Métodos de Listas →](./02_metodos_listas.md)

---

**💡 Consejo**: Practica creando diferentes tipos de listas y accediendo a sus elementos. La familiaridad con los índices es fundamental.


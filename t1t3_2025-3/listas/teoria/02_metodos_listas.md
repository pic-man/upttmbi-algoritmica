# 📖 02 - Métodos de Listas

## Métodos Principales de Listas en Python

Python proporciona muchos métodos integrados para trabajar con listas. Aquí están los más importantes.

## 📝 Métodos para Agregar Elementos

### `append()` - Agregar al final
```python
frutas = ["manzana", "banana"]
frutas.append("naranja")
print(frutas)  # ['manzana', 'banana', 'naranja']
```

### `insert()` - Insertar en posición específica
```python
frutas = ["manzana", "naranja"]
frutas.insert(1, "banana")  # Insertar en índice 1
print(frutas)  # ['manzana', 'banana', 'naranja']
```

### `extend()` - Agregar múltiples elementos
```python
frutas = ["manzana", "banana"]
frutas.extend(["naranja", "pera"])
print(frutas)  # ['manzana', 'banana', 'naranja', 'pera']
```

## 🗑️ Métodos para Eliminar Elementos

### `remove()` - Eliminar por valor
```python
frutas = ["manzana", "banana", "naranja"]
frutas.remove("banana")
print(frutas)  # ['manzana', 'naranja']
```

### `pop()` - Eliminar por índice y retornar
```python
frutas = ["manzana", "banana", "naranja"]
ultima = frutas.pop()      # Elimina y retorna el último
print(ultima)              # 'naranja'
print(frutas)              # ['manzana', 'banana']

primera = frutas.pop(0)    # Elimina y retorna el índice 0
print(primera)             # 'manzana'
```

### `clear()` - Vaciar la lista
```python
frutas = ["manzana", "banana"]
frutas.clear()
print(frutas)  # []
```

## 🔍 Métodos de Búsqueda

### `index()` - Encontrar índice de un elemento
```python
frutas = ["manzana", "banana", "naranja"]
posicion = frutas.index("banana")
print(posicion)  # 1
```

### `count()` - Contar ocurrencias
```python
numeros = [1, 2, 3, 2, 2, 4]
cantidad = numeros.count(2)
print(cantidad)  # 3
```

## 📊 Métodos de Ordenamiento

### `sort()` - Ordenar la lista (modifica original)
```python
numeros = [3, 1, 4, 1, 5]
numeros.sort()
print(numeros)  # [1, 1, 3, 4, 5]

# Orden descendente
numeros.sort(reverse=True)
print(numeros)  # [5, 4, 3, 1, 1]
```

### `reverse()` - Invertir la lista
```python
numeros = [1, 2, 3, 4, 5]
numeros.reverse()
print(numeros)  # [5, 4, 3, 2, 1]
```

### `sorted()` - Retorna lista ordenada (no modifica original)
```python
original = [3, 1, 4, 1, 5]
ordenada = sorted(original)
print(original)   # [3, 1, 4, 1, 5] (sin cambios)
print(ordenada)   # [1, 1, 3, 4, 5]
```

## 📋 Copiar Listas

### `copy()` - Copia superficial
```python
original = [1, 2, 3]
copia = original.copy()
copia.append(4)
print(original)  # [1, 2, 3] (no cambia)
print(copia)     # [1, 2, 3, 4]
```

## 📊 Tabla Resumen de Métodos

| Método | Descripción | Ejemplo | Retorna |
|--------|-------------|---------|---------|
| `append(x)` | Agrega x al final | `lista.append(5)` | None |
| `insert(i, x)` | Inserta x en posición i | `lista.insert(0, 5)` | None |
| `extend(iterable)` | Agrega elementos de iterable | `lista.extend([1,2])` | None |
| `remove(x)` | Elimina primera ocurrencia de x | `lista.remove(5)` | None |
| `pop(i)` | Elimina y retorna elemento en i | `x = lista.pop()` | Elemento |
| `clear()` | Vacía la lista | `lista.clear()` | None |
| `index(x)` | Índice de primera ocurrencia | `i = lista.index(5)` | int |
| `count(x)` | Cuenta ocurrencias de x | `n = lista.count(5)` | int |
| `sort()` | Ordena la lista | `lista.sort()` | None |
| `reverse()` | Invierte la lista | `lista.reverse()` | None |
| `copy()` | Copia la lista | `nueva = lista.copy()` | Lista |

## 💡 Ejemplos Prácticos Completos

### Ejemplo 1: Gestión de Tareas
```python
tareas = []

# Agregar tareas
tareas.append("Estudiar Python")
tareas.append("Hacer ejercicio")
tareas.insert(0, "Desayunar")  # Más importante, va primero

print("Tareas del día:")
for i, tarea in enumerate(tareas, 1):
    print(f"{i}. {tarea}")

# Completar tarea (eliminar)
tarea_completada = tareas.pop(0)
print(f"\n✅ Completada: {tarea_completada}")

print("\nTareas restantes:")
for tarea in tareas:
    print(f"- {tarea}")
```

### Ejemplo 2: Análisis de Calificaciones
```python
calificaciones = [85, 92, 78, 90, 88, 95, 82]

# Estadísticas
promedio = sum(calificaciones) / len(calificaciones)
maxima = max(calificaciones)
minima = min(calificaciones)

print(f"Promedio: {promedio:.2f}")
print(f"Máxima: {maxima}")
print(f"Mínima: {minima}")

# Ordenar para ver ranking
ranking = calificaciones.copy()
ranking.sort(reverse=True)
print(f"\nRanking: {ranking}")

# Contar cuántos aprobaron (>= 80)
aprobados = sum(1 for nota in calificaciones if nota >= 80)
print(f"Aprobados: {aprobados}/{len(calificaciones)}")
```

### Ejemplo 3: Inventario de Productos
```python
inventario = ["laptop", "mouse", "teclado"]

print("=== SISTEMA DE INVENTARIO ===")

# Agregar producto
nuevo_producto = "monitor"
inventario.append(nuevo_producto)
print(f"✅ Agregado: {nuevo_producto}")

# Verificar si existe
buscar = "mouse"
if buscar in inventario:
    posicion = inventario.index(buscar)
    print(f"📦 {buscar} está en posición {posicion}")

# Eliminar producto vendido
vendido = inventario.pop(1)
print(f"💰 Vendido: {vendido}")

# Ordenar alfabéticamente
inventario.sort()
print(f"\n📋 Inventario ordenado:")
for producto in inventario:
    print(f"  - {producto}")
```

## ⚠️ Errores Comunes

### 1. Confundir append() con extend()
```python
# ❌ INCORRECTO
lista = [1, 2, 3]
lista.append([4, 5])  # Agrega la lista completa como un elemento
print(lista)  # [1, 2, 3, [4, 5]]

# ✅ CORRECTO
lista = [1, 2, 3]
lista.extend([4, 5])  # Agrega cada elemento
print(lista)  # [1, 2, 3, 4, 5]
```

### 2. Usar remove() sin verificar
```python
# ❌ INCORRECTO
frutas = ["manzana", "banana"]
# frutas.remove("naranja")  # Error: ValueError

# ✅ CORRECTO
if "naranja" in frutas:
    frutas.remove("naranja")
else:
    print("Naranja no está en la lista")
```

### 3. Modificar lista durante iteración
```python
# ❌ INCORRECTO
numeros = [1, 2, 3, 4, 5]
for num in numeros:
    if num % 2 == 0:
        numeros.remove(num)  # Problemas

# ✅ CORRECTO
numeros = [num for num in numeros if num % 2 != 0]
```

## 🧪 Ejercicios de Práctica

### Ejercicio 1:
Crea una lista con 5 números, ordénala, y luego invirtela.

<details>
<summary>Ver solución</summary>

```python
numeros = [5, 2, 8, 1, 9]
numeros.sort()      # [1, 2, 5, 8, 9]
numeros.reverse()   # [9, 8, 5, 2, 1]
print(numeros)
```
</details>

### Ejercicio 2:
Cuenta cuántas veces aparece el número 3 en esta lista: `[1, 3, 5, 3, 7, 3, 9]`

<details>
<summary>Ver solución</summary>

```python
numeros = [1, 3, 5, 3, 7, 3, 9]
cantidad = numeros.count(3)
print(f"El 3 aparece {cantidad} veces")  # 3 veces
```
</details>

## 📝 Resumen

| Acción | Método | Modifica Original |
|--------|--------|-------------------|
| Agregar al final | `append()` | Sí |
| Agregar en posición | `insert()` | Sí |
| Agregar varios | `extend()` | Sí |
| Eliminar por valor | `remove()` | Sí |
| Eliminar por índice | `pop()` | Sí |
| Buscar posición | `index()` | No |
| Contar elementos | `count()` | No |
| Ordenar | `sort()` | Sí |
| Invertir | `reverse()` | Sí |
| Copiar | `copy()` | No (crea nueva) |

## 🔜 Siguiente Paso

Ahora que dominas los métodos básicos, aprenderás operaciones más avanzadas con listas.

[← Anterior: 01 - Introducción](./01_introduccion_listas.md) | [Siguiente: 03 - Operaciones con Listas →](./03_operaciones_listas.md)


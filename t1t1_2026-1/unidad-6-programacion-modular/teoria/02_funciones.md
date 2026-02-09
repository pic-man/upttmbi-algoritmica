# 📖 02 - Funciones

## ¿Qué es una Función?

Una **función** es un bloque de código reutilizable que realiza una tarea específica y puede retornar un valor.

## Sintaxis en Python

```python
def nombre_funcion(parametro1, parametro2):
    """Documentación de la función (docstring)."""
    # Cuerpo de la función
    resultado = parametro1 + parametro2
    return resultado
```

## Partes de una Función

```
def calcular_area(base, altura):    ← Definición y parámetros
    """Calcula el área."""          ← Docstring
    area = base * altura            ← Cuerpo
    return area                     ← Retorno
```

## Tipos de Funciones

### 1. Función sin parámetros ni retorno

```python
def saludar():
    print("¡Hola, mundo!")

saludar()  # Llamada
```

### 2. Función con parámetros

```python
def saludar_persona(nombre):
    print(f"¡Hola, {nombre}!")

saludar_persona("María")
```

### 3. Función con retorno

```python
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)  # resultado = 8
```

### 4. Función con parámetros por defecto

```python
def saludar(nombre, saludo="Hola"):
    return f"{saludo}, {nombre}!"

print(saludar("Juan"))           # "Hola, Juan!"
print(saludar("Ana", "Buenos días"))  # "Buenos días, Ana!"
```

### 5. Función con múltiples retornos

```python
def dividir(a, b):
    cociente = a // b
    residuo = a % b
    return cociente, residuo

c, r = dividir(17, 5)  # c=3, r=2
```

## Ejemplos Prácticos

### Calcular factorial

```python
def factorial(n):
    """Calcula el factorial de n."""
    if n < 0:
        return None
    if n <= 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

print(factorial(5))  # 120
```

### Verificar número primo

```python
def es_primo(n):
    """Verifica si n es primo."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(es_primo(7))   # True
print(es_primo(10))  # False
```

### Función con validación

```python
def calcular_promedio(notas):
    """Calcula el promedio de una lista de notas."""
    if not notas:
        return 0
    return sum(notas) / len(notas)

notas = [85, 90, 78, 92]
print(f"Promedio: {calcular_promedio(notas)}")
```

## Buenas Prácticas

1. **Nombres descriptivos**: `calcular_area()` no `ca()`
2. **Una función, una tarea**
3. **Documentar** con docstrings
4. **Validar** parámetros de entrada
5. **Funciones cortas** (máximo 20-30 líneas)

## 📝 Para Recordar

1. Las funciones se definen con `def`
2. Pueden tener **parámetros** y **retorno**
3. El `return` devuelve un valor
4. Sin `return`, la función devuelve `None`
5. Los **docstrings** documentan la función

## 🔜 Siguiente Paso

[Ir a: 04 - Ámbito de Variables →](./04_ambito_variables.md)

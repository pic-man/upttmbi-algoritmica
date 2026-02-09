# 📦 Variables y Tipos de Datos

## ¿Qué es una Variable?

Una **variable** es como una caja con un nombre donde guardamos información.

```
┌─────────────┐
│    edad     │  ← Nombre de la variable
├─────────────┤
│     25      │  ← Valor almacenado
└─────────────┘
```

En Python, creamos una variable así:

```python
edad = 25
nombre = "María"
precio = 19.99
```

## Reglas para Nombrar Variables

✅ **Permitido:**
- Letras minúsculas: `edad`, `nombre`, `total`
- Letras y números: `nota1`, `valor2`
- Guion bajo: `precio_total`, `nombre_completo`

❌ **No permitido:**
- Empezar con número: `1nota` ❌
- Espacios: `mi variable` ❌
- Caracteres especiales: `precio$`, `nota#` ❌
- Palabras reservadas: `print`, `if`, `for` ❌

💡 **Buenas prácticas:**
- Usar nombres descriptivos: `edad` en vez de `e`
- Usar minúsculas: `nombre` en vez de `Nombre`
- Separar palabras con guion bajo: `fecha_nacimiento`

## Tipos de Datos Básicos

En Python hay tres tipos de datos fundamentales:

### 1. Enteros (`int`)

Números sin decimales (positivos o negativos):

```python
edad = 25
temperatura = -5
cantidad = 100
```

### 2. Decimales (`float`)

Números con punto decimal:

```python
precio = 19.99
estatura = 1.75
promedio = 8.5
```

### 3. Texto (`str`)

Cadenas de caracteres entre comillas:

```python
nombre = "Juan"
mensaje = 'Hola mundo'
direccion = "Calle 123"
```

> 💡 Puedes usar comillas dobles `"texto"` o simples `'texto'`

## Tabla Resumen

| Tipo | Nombre en Python | Ejemplo | Uso |
|------|------------------|---------|-----|
| Entero | `int` | `25`, `-10`, `0` | Edades, cantidades |
| Decimal | `float` | `3.14`, `19.99` | Precios, promedios |
| Texto | `str` | `"Hola"`, `'Juan'` | Nombres, mensajes |

## Ver el Tipo de una Variable

Usa la función `type()` para saber el tipo:

```python
edad = 25
print(type(edad))      # <class 'int'>

precio = 19.99
print(type(precio))    # <class 'float'>

nombre = "Ana"
print(type(nombre))    # <class 'str'>
```

## Cambiar el Valor de una Variable

Las variables pueden cambiar su valor:

```python
puntos = 10
print(puntos)    # Muestra: 10

puntos = 15
print(puntos)    # Muestra: 15

puntos = puntos + 5
print(puntos)    # Muestra: 20
```

---

## 📝 Resumen

- Una **variable** almacena un valor con un nombre
- Tipos básicos: `int` (enteros), `float` (decimales), `str` (texto)
- Usa nombres descriptivos en minúsculas
- Las variables pueden cambiar de valor

---

**Anterior:** [01_introduccion.md](./01_introduccion.md) | **Siguiente:** [03_entrada_salida.md](./03_entrada_salida.md)

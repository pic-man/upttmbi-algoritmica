# 📖 01 - Introducción a las Cadenas de Caracteres

## ¿Qué es una Cadena?

Una **cadena de caracteres** (string) es una secuencia ordenada e inmutable de caracteres. En Python se representa escribiendo texto entre comillas simples (`'...'`) o dobles (`"..."`).

```python
mensaje = "Hola mundo"
omega = 'Python 3.12'
```

## 🔑 Características Clave

### 1. Ordenadas
Los caracteres mantienen el orden en que fueron escritos.

```python
texto = "python"
print(texto[0])   # 'p'
print(texto[-1])  # 'n'
```

### 2. Inmutables
Una vez creada, no puedes modificar la cadena directamente. Se generan nuevas cadenas al aplicar operaciones.

```python
nombre = "Ana"
# nombre[0] = "a"  # Error: TypeError
nombre = "a" + nombre[1:]  # Crear una nueva cadena
```

### 3. Pueden contener cualquier carácter
Incluyen letras, números, símbolos, saltos de línea y emojis.

```python
mensaje = "Clave: A2#9\nEmoji: 😊"
```

## 📝 Crear Cadenas

### Comillas simples o dobles
```python
saludo = "Hola"
otro = 'Adiós'
```

### Cadenas multilínea con triple comillas
```python
doc = """Python es divertido.
Trabaja con strings, listas y más."""
```

### Función `str()`
Convierte otros tipos de datos en cadenas.

```python
numero = 42
texto = str(numero)  # '42'
```

## 🎯 Acceder a Caracteres

### Índices positivos y negativos
```python
palabra = "algoritmo"
print(palabra[2])   # 'g'
print(palabra[-3])  # 't'
```

### Slicing (rebanadas)
```python
serie = "ABCDEFGHI"
print(serie[2:5])    # 'CDE'
print(serie[:4])     # 'ABCD'
print(serie[::2])    # 'ACEGI'
print(serie[::-1])   # 'IHGFEDCBA'
```

## 🔍 Operaciones Básicas

### Longitud
```python
mensaje = "Hola"
print(len(mensaje))  # 4
```

### Concatenación
```python
saludo = "Hola" + " " + "mundo"
```

### Repetición
```python
separador = "-" * 10  # '----------'
```

### Pertenencia
```python
texto = "python"
print("py" in texto)   # True
print("java" not in texto)  # True
```

## 🧱 Literales Especiales

| Secuencia | Significado |
|-----------|-------------|
| `\n` | Salto de línea |
| `\t` | Tabulación |
| `\"` | Comilla doble |
| `\\` | Barra invertida |

```python
ruta = "C:\\Users\\Carlos"
```

## 📊 Comparación con Otros Lenguajes

| Python | JavaScript | Java | C++ |
|--------|-----------|------|-----|
| `texto = "hola"` | `let texto = "hola";` | `String texto = "hola";` | `std::string texto = "hola";` |
| `len(texto)` | `texto.length` | `texto.length()` | `texto.size()` |
| `texto.upper()` | `texto.toUpperCase()` | `texto.toUpperCase()` | `std::toupper` (cada char) |

## ⚠️ Errores Comunes

### 1. Olvidar la inmutabilidad
```python
palabra = "hola"
# palabra[0] = 'H'  # Error
palabra = 'H' + palabra[1:]
```

### 2. Escapar caracteres de forma incorrecta
```python
# ❌ INCORRECTO
titulo = "El libro se llama "Python Básico""  # Error de sintaxis

# ✅ CORRECTO
titulo = "El libro se llama \"Python Básico\""
```

### 3. Confundir `'` con ```
Recuerda que las comillas simples y dobles deben abrir y cerrar correctamente.

## 📝 Para Recordar

1. Las cadenas son inmutables.
2. Usa índices y slicing para leer caracteres, no para modificarlos.
3. `len()` devuelve la cantidad de caracteres.
4. Concatenar y repetir crean nuevas cadenas.
5. Usa `\` para escapar caracteres especiales.

## 🔜 Siguiente Paso

En la siguiente lección aprenderás los métodos integrados más utilizados para transformar y analizar cadenas.

# 📖 02 - Métodos de Cadenas

## Métodos más usados en Python

Python ofrece una amplia colección de métodos para transformar, buscar y analizar cadenas. La mayoría retornan **nuevas** cadenas (recuerda: son inmutables).

## ✏️ Métodos de Transformación

### `upper()` y `lower()`
```python
texto = "Python"
print(texto.upper())  # 'PYTHON'
print(texto.lower())  # 'python'
```

### `title()` y `capitalize()`
```python
frase = "bienvenidos al curso"
print(frase.title())      # 'Bienvenidos Al Curso'
print(frase.capitalize()) # 'Bienvenidos al curso'
```

### `strip()`, `lstrip()`, `rstrip()`
Eliminan espacios (u otros caracteres) al inicio/fin.
```python
codigo = "   abc123   "
print(codigo.strip())   # 'abc123'
print(codigo.lstrip())  # 'abc123   '
print(codigo.rstrip())  # '   abc123'
```

## 🔍 Métodos de Búsqueda

### `find()` y `rfind()`
Retornan el índice de la primera/última coincidencia, o `-1` si no existe.
```python
mensaje = "analizando cadenas"
print(mensaje.find("an"))   # 0
print(mensaje.rfind("an"))  # 14
```

### `index()` y `rindex()`
Similares a `find()`, pero lanzan `ValueError` si no existe la subcadena.

### `count()`
Cuenta apariciones.
```python
texto = "banana"
print(texto.count("na"))  # 2
```

## 🧰 Métodos de División y Unión

### `split()`
Divide la cadena en una lista.
```python
campos = "Carlos;Bravo;Python"
print(campos.split(";"))  # ['Carlos', 'Bravo', 'Python']
```

### `splitlines()`
```python
parrafo = "Linea 1\nLinea 2\nLinea 3"
print(parrafo.splitlines())
```

### `join()`
Une elementos de un iterable en una sola cadena.
```python
items = ["2025", "03", "15"]
fecha = "-".join(items)
print(fecha)  # '2025-03-15'
```

## 🔁 Métodos de Reemplazo y Formateo

### `replace()`
```python
texto = "hola mundo"
print(texto.replace("mundo", "Python"))
```

### `format()` y f-strings
```python
nombre = "Ana"
print("Hola {}".format(nombre))
print(f"Hola {nombre}")
```

### `zfill()` y `rjust()`
```python
numero = "42"
print(numero.zfill(5))   # '00042'
print(numero.rjust(5, ' '))  # '   42'
```

## ✅ Métodos lógicos

### `startswith()` y `endswith()`
```python
archivo = "informe.pdf"
print(archivo.endswith(".pdf"))  # True
```

### Métodos `is...`
| Método | Verifica |
|--------|----------|
| `isalnum()` | Si todos los caracteres son alfanuméricos |
| `isalpha()` | Solo letras |
| `isdigit()` | Solo dígitos |
| `islower()` | Todo en minúsculas |
| `isupper()` | Todo en mayúsculas |

```python
codigo = "ABC123"
print(codigo.isalnum())  # True
print(codigo.isupper())  # True
```

## 🧪 Ejemplos Completos

### Normalizador de nombres propios
```python
entrada = "cARLOS bravo"
normalizado = " ".join(parte.capitalize() for parte in entrada.split())
print(normalizado)  # 'Carlos Bravo'
```

### Analizador de correos electrónicos
```python
correo = "estudiante@example.com"
usuario, dominio = correo.split("@")
print(f"Usuario: {usuario}")
print(f"Dominio: {dominio}")
```

### Contador de palabras clave
```python
texto = "Python es poderoso. Python es flexible."
clave = "python"
conteo = texto.lower().count(clave)
print(f"'{clave}' aparece {conteo} veces")
```

## 📋 Tabla Resumen

| Método | Descripción | Retorna |
|--------|-------------|---------|
| `upper()` | Convierte a mayúsculas | Cadena |
| `lower()` | Convierte a minúsculas | Cadena |
| `strip()` | Quita caracteres en extremos | Cadena |
| `find()` | Índice de subcadena o -1 | int |
| `split(sep)` | Divide según separador | Lista |
| `join(iterable)` | Une elementos | Cadena |
| `replace(viejo, nuevo)` | Reemplaza subcadena | Cadena |
| `startswith(prefijo)` | ¿Inicia con? | bool |
| `isdigit()` | ¿Solo dígitos? | bool |

## ⚠️ Errores Comunes

1. Olvidar que los métodos no modifican la cadena original.
2. Mezclar tipos al usar `join()` (debe recibir solo strings).
3. No controlar cuando `split()` produce listas vacías o con longitud distinta a la esperada.

## 📝 Resumen

- Usa métodos de transformación para preparar datos (mayúsculas, espacios, reemplazos).
- Métodos de búsqueda (`find`, `startswith`) son útiles para validaciones.
- `split`/`join` permiten pasar de texto a estructuras y viceversa.

## 🔜 Siguiente Paso

Avanzaremos hacia operaciones combinadas: validaciones, limpieza de datos y patrones comunes al trabajar con cadenas.

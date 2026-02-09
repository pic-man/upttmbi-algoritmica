# 📖 02 - Tipos de Datos

## ¿Qué son los Tipos de Datos?

Los **tipos de datos** definen la naturaleza de los valores que pueden almacenarse en una variable y las operaciones que pueden realizarse con ellos.

```
┌─────────────────────────────────────────────────────────────┐
│                    TIPOS DE DATOS                            │
├─────────────────┬─────────────────┬─────────────────────────┤
│   NUMÉRICOS     │  ALFANUMÉRICOS  │       LÓGICOS           │
│                 │                 │                         │
│ - Enteros       │ - Caracteres    │ - Booleanos             │
│ - Reales        │ - Cadenas       │   (True/False)          │
└─────────────────┴─────────────────┴─────────────────────────┘
```

## 1. Datos Numéricos

### Enteros (int)

Números sin parte decimal, positivos o negativos.

```python
# Ejemplos de enteros
edad = 25
temperatura = -5
cantidad = 0
poblacion = 7800000000

# Operaciones con enteros
suma = 10 + 5        # 15
resta = 10 - 5       # 5
multiplicacion = 10 * 5   # 50
division_entera = 10 // 3  # 3 (sin decimales)
modulo = 10 % 3      # 1 (residuo)
```

### Reales (float)

Números con parte decimal.

```python
# Ejemplos de reales
precio = 19.99
pi = 3.14159
altura = 1.75
porcentaje = 0.15

# Operaciones con reales
division = 10 / 3    # 3.3333...
area = pi * (5 ** 2) # 78.53975
```

### Tabla de Tipos Numéricos

| Tipo | Descripción | Rango (aprox.) | Ejemplo |
|------|-------------|----------------|---------|
| int | Entero | Ilimitado en Python | `42` |
| float | Real | ±1.8 × 10³⁰⁸ | `3.14` |

## 2. Datos Alfanuméricos

### Caracteres

Un solo símbolo (letra, número, especial).

```python
# En Python, caracteres y cadenas usan el mismo tipo (str)
letra = 'A'
digito = '7'
simbolo = '@'
espacio = ' '
```

### Cadenas (str)

Secuencia de caracteres.

```python
# Ejemplos de cadenas
nombre = "María García"
direccion = '123 Calle Principal'
vacio = ""
multilinea = """Esta es una
cadena de múltiples
líneas"""

# Operaciones con cadenas
concatenar = "Hola" + " " + "Mundo"  # "Hola Mundo"
repetir = "Ja" * 3                    # "JaJaJa"
longitud = len("Python")              # 6
mayusculas = "hola".upper()           # "HOLA"
```

### Acceso a Caracteres

```python
texto = "Python"
#        012345  (índices)

print(texto[0])   # 'P'
print(texto[2])   # 't'
print(texto[-1])  # 'n' (último)
print(texto[0:3]) # 'Pyt' (subcadena)
```

## 3. Datos Lógicos (Booleanos)

Solo pueden tener dos valores: `True` (verdadero) o `False` (falso).

```python
# Ejemplos de booleanos
es_mayor = True
tiene_permiso = False
activo = True

# Resultados de comparaciones (producen booleanos)
resultado1 = 5 > 3      # True
resultado2 = 10 == 20   # False
resultado3 = "a" < "b"  # True

# Operaciones lógicas
y_logico = True and False   # False
o_logico = True or False    # True
negacion = not True         # False
```

### Tabla de Verdad

```
AND (Y)              OR (O)              NOT (NO)
┌───┬───┬───────┐   ┌───┬───┬───────┐   ┌───┬───────┐
│ A │ B │ A and B│   │ A │ B │ A or B│   │ A │ not A │
├───┼───┼───────┤   ├───┼───┼───────┤   ├───┼───────┤
│ V │ V │   V   │   │ V │ V │   V   │   │ V │   F   │
│ V │ F │   F   │   │ V │ F │   V   │   │ F │   V   │
│ F │ V │   F   │   │ F │ V │   V   │   └───┴───────┘
│ F │ F │   F   │   │ F │ F │   F   │
└───┴───┴───────┘   └───┴───┴───────┘
```

## Conversión entre Tipos

Python permite convertir datos de un tipo a otro:

```python
# Conversiones
entero = int("42")       # Cadena a entero: 42
real = float("3.14")     # Cadena a real: 3.14
cadena = str(100)        # Entero a cadena: "100"
booleano = bool(1)       # Entero a booleano: True

# Ejemplos prácticos
edad_texto = input("Ingrese su edad: ")  # Siempre es string
edad_numero = int(edad_texto)            # Convertir a entero

precio = 19.99
precio_texto = f"${precio:.2f}"          # "$19.99"
```

### Reglas de Conversión

| De | A | Función | Ejemplo |
|----|---|---------|---------|
| str → int | Entero | `int("42")` | 42 |
| str → float | Real | `float("3.14")` | 3.14 |
| int → str | Cadena | `str(42)` | "42" |
| float → int | Entero | `int(3.9)` | 3 (trunca) |
| int → bool | Booleano | `bool(0)` | False |
| int → bool | Booleano | `bool(5)` | True |

## Verificar Tipo de Datos

```python
# Usar type() para conocer el tipo
valor = 42
print(type(valor))  # <class 'int'>

# Usar isinstance() para verificar
print(isinstance(42, int))      # True
print(isinstance(3.14, float))  # True
print(isinstance("hola", str))  # True
```

## Resumen de Tipos

```
┌─────────────────────────────────────────────────────────────┐
│                    TIPOS DE DATOS EN PYTHON                  │
├──────────┬──────────────────┬───────────────────────────────┤
│  Tipo    │  Palabra clave   │  Ejemplos                     │
├──────────┼──────────────────┼───────────────────────────────┤
│ Entero   │ int              │ 42, -7, 0, 1000               │
│ Real     │ float            │ 3.14, -0.5, 2.0               │
│ Cadena   │ str              │ "Hola", 'A', "123"            │
│ Booleano │ bool             │ True, False                   │
│ Nulo     │ NoneType         │ None                          │
└──────────┴──────────────────┴───────────────────────────────┘
```

## 📝 Para Recordar

1. **Numéricos**: enteros (int) y reales (float)
2. **Alfanuméricos**: caracteres y cadenas (str)
3. **Lógicos**: booleanos (bool) - True/False
4. Usar `type()` para conocer el tipo de un dato
5. Usar funciones de conversión para cambiar tipos

## ✅ Ejercicio Rápido

¿De qué tipo es cada valor?

```python
a = 42
b = "42"
c = 42.0
d = True
e = None
```

<details>
<summary>Ver respuesta</summary>

```python
a = 42      # int (entero)
b = "42"    # str (cadena)
c = 42.0    # float (real)
d = True    # bool (booleano)
e = None    # NoneType (nulo)
```
</details>

## 🔜 Siguiente Paso

Ahora aprenderás sobre los operadores.

[Ir a: 03 - Operadores →](./03_operadores.md)

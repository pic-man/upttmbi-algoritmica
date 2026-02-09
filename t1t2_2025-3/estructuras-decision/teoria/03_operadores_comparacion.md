# 📖 03 - Operadores de Comparación

## ¿Qué son los Operadores de Comparación?

Los **operadores de comparación** se usan para comparar dos valores. Siempre devuelven un valor booleano: `True` (verdadero) o `False` (falso).

## 📊 Tabla de Operadores

| Operador | Significado | Ejemplo | Resultado |
|----------|-------------|---------|-----------|
| `==` | Igual a | `5 == 5` | `True` |
| `!=` | Diferente de | `5 != 3` | `True` |
| `>` | Mayor que | `5 > 3` | `True` |
| `<` | Menor que | `3 < 5` | `True` |
| `>=` | Mayor o igual que | `5 >= 5` | `True` |
| `<=` | Menor o igual que | `3 <= 5` | `True` |

## 1️⃣ Igual a (`==`)

Compara si dos valores son exactamente iguales.

⚠️ **¡Cuidado!** No confundir con `=` (asignación)

```python
# = es asignación
edad = 18

# == es comparación
if edad == 18:
    print("Tienes exactamente 18 años")
```

### Ejemplos:
```python
print(5 == 5)      # True
print(5 == 3)      # False
print("hola" == "hola")  # True
print("Hola" == "hola")  # False (sensible a mayúsculas)
```

### Uso práctico:
```python
password_correcta = "12345"
password_ingresada = input("Ingresa tu contraseña: ")

if password_ingresada == password_correcta:
    print("Acceso concedido ✅")
else:
    print("Contraseña incorrecta ❌")
```

## 2️⃣ Diferente de (`!=`)

Compara si dos valores son diferentes.

```python
print(5 != 3)      # True (5 es diferente de 3)
print(5 != 5)      # False (5 no es diferente de 5)
```

### Uso práctico:
```python
opcion = input("Continuar? (s/n): ")

if opcion != "s":
    print("Programa terminado")
    exit()
```

## 3️⃣ Mayor que (`>`)

Verifica si el valor de la izquierda es mayor que el de la derecha.

```python
print(10 > 5)      # True
print(5 > 10)      # False
print(5 > 5)       # False (no es mayor, es igual)
```

### Uso práctico:
```python
precio = 100
limite = 50

if precio > limite:
    print("El precio excede tu límite")
```

## 4️⃣ Menor que (`<`)

Verifica si el valor de la izquierda es menor que el de la derecha.

```python
print(3 < 5)       # True
print(5 < 3)       # False
print(5 < 5)       # False
```

### Uso práctico:
```python
edad = 15

if edad < 18:
    print("Eres menor de edad")
```

## 5️⃣ Mayor o igual que (`>=`)

Verifica si el valor es mayor **O** igual.

```python
print(10 >= 5)     # True (mayor)
print(5 >= 5)      # True (igual)
print(3 >= 5)      # False
```

### Uso práctico:
```python
calificacion = 6

if calificacion >= 6:
    print("¡Aprobado! ✅")
```

## 6️⃣ Menor o igual que (`<=`)

Verifica si el valor es menor **O** igual.

```python
print(3 <= 5)      # True (menor)
print(5 <= 5)      # True (igual)
print(10 <= 5)     # False
```

### Uso práctico:
```python
intentos = 3
maximo_intentos = 3

if intentos <= maximo_intentos:
    print("Intento válido")
```

## 🎯 Comparaciones con Diferentes Tipos

### Números enteros y decimales:
```python
print(5 == 5.0)    # True (Python los considera iguales)
print(5 > 4.5)     # True
```

### Cadenas de texto (strings):
```python
print("abc" < "abd")   # True (orden alfabético)
print("A" < "a")       # True (mayúsculas van primero)
print("10" < "2")      # True (compara como texto, no como número)
```

⚠️ **Importante con strings**:
```python
# Comparando números como texto
print("10" < "2")      # True (porque "1" < "2" en texto)

# Para comparar números, conviértelos:
print(int("10") < int("2"))  # False (compara como números)
```

## 🔗 Encadenando Comparaciones

Python permite encadenar comparaciones (algo único):

```python
edad = 25

# Forma tradicional
if edad >= 18 and edad < 65:
    print("Adulto en edad laboral")

# Forma encadenada (más legible)
if 18 <= edad < 65:
    print("Adulto en edad laboral")
```

### Más ejemplos:
```python
x = 5

if 0 < x < 10:
    print("x está entre 0 y 10")

if 1 <= x <= 100:
    print("x está entre 1 y 100 (inclusive)")
```

## 💡 Ejemplos Prácticos Completos

### Ejemplo 1: Validar rango de edad
```python
edad = int(input("Ingresa tu edad: "))

if edad < 0:
    print("Edad no válida")
elif edad <= 12:
    print("Eres un niño")
elif edad <= 17:
    print("Eres un adolescente")
elif edad <= 64:
    print("Eres un adulto")
elif edad <= 120:
    print("Eres un adulto mayor")
else:
    print("Edad no válida")
```

### Ejemplo 2: Sistema de login
```python
usuario_correcto = "admin"
password_correcta = "1234"

usuario = input("Usuario: ")
password = input("Contraseña: ")

if usuario == usuario_correcto and password == password_correcta:
    print("✅ Acceso concedido")
else:
    print("❌ Credenciales incorrectas")
```

### Ejemplo 3: Calificación con validación
```python
nota = float(input("Ingresa tu nota (0-10): "))

if nota < 0 or nota > 10:
    print("Nota inválida")
elif nota >= 9:
    print("Excelente 🌟")
elif nota >= 7:
    print("Bien 👍")
elif nota >= 6:
    print("Aprobado ✅")
else:
    print("Reprobado ❌")
```

### Ejemplo 4: Descuento por cantidad
```python
cantidad = int(input("¿Cuántas unidades compras?: "))
precio_unitario = 100

if cantidad >= 100:
    descuento = 0.20  # 20%
elif cantidad >= 50:
    descuento = 0.15  # 15%
elif cantidad >= 10:
    descuento = 0.10  # 10%
else:
    descuento = 0

total = cantidad * precio_unitario
total_con_descuento = total - (total * descuento)

print(f"Total sin descuento: ${total}")
print(f"Descuento: {descuento * 100}%")
print(f"Total a pagar: ${total_con_descuento}")
```

## 🧪 Ejercicios de Práctica

### Ejercicio 1:
¿Qué imprime este código?
```python
x = 10
y = 20

print(x < y)
print(x == y)
print(x != y)
```

<details>
<summary>Ver respuesta</summary>

```
True
False
True
```
</details>

### Ejercicio 2:
¿Cuál es el error aquí?
```python
edad = 18

if edad = 18:
    print("Tienes 18 años")
```

<details>
<summary>Ver respuesta</summary>
Usa `=` (asignación) en lugar de `==` (comparación). Debería ser `if edad == 18:`
</details>

### Ejercicio 3:
¿Qué imprime?
```python
if 5 < 10 < 15:
    print("A")
else:
    print("B")
```

<details>
<summary>Ver respuesta</summary>
`A` - Porque 5 < 10 es True y 10 < 15 es True
</details>

## 📝 Errores Comunes

### ❌ Error 1: Confundir `=` con `==`
```python
# INCORRECTO
if x = 5:  # Error de sintaxis
    print("x es 5")

# CORRECTO
if x == 5:
    print("x es 5")
```

### ❌ Error 2: Comparar tipos incompatibles sin cuidado
```python
edad = "18"  # String

if edad >= 18:  # Error: no puedes comparar string con int
    print("Mayor de edad")

# CORRECTO
edad = int("18")  # Convertir a número
if edad >= 18:
    print("Mayor de edad")
```

### ❌ Error 3: Comparar flotantes directamente
```python
# Ten cuidado con decimales
if 0.1 + 0.2 == 0.3:  # Puede ser False debido a precisión flotante
    print("Son iguales")

# Mejor usar rangos
diferencia = abs((0.1 + 0.2) - 0.3)
if diferencia < 0.0001:
    print("Son aproximadamente iguales")
```

## 📝 Resumen

| Operador | Uso | Ejemplo |
|----------|-----|---------|
| `==` | Igualdad | `edad == 18` |
| `!=` | Desigualdad | `opcion != "s"` |
| `>` | Mayor | `precio > 100` |
| `<` | Menor | `edad < 18` |
| `>=` | Mayor o igual | `nota >= 6` |
| `<=` | Menor o igual | `temperatura <= 0` |

### Puntos clave:
1. Todos los operadores devuelven `True` o `False`
2. `==` compara valores, `=` asigna valores
3. Se pueden encadenar: `0 < x < 10`
4. Cuidado al comparar diferentes tipos de datos

## 🔜 Siguiente Paso

Ahora aprenderás a combinar múltiples condiciones con operadores lógicos.

[← Anterior: 02 - If, Else, Elif](./02_if_else_elif.md) | [Siguiente: 04 - Operadores Lógicos →](./04_operadores_logicos.md)


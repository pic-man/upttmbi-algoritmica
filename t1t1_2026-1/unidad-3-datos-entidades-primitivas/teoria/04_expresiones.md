# 📖 04 - Las Expresiones

## ¿Qué es una Expresión?

Una **expresión** es una combinación de valores, variables, operadores y llamadas a funciones que se evalúa para producir un resultado.

```
┌─────────────────────────────────────────────────────────────┐
│                       EXPRESIÓN                              │
│                                                             │
│    precio * cantidad + (precio * cantidad * IVA)            │
│      ↓        ↓              ↓                              │
│  variable  variable    sub-expresión                        │
│                                                             │
│           ──────────────────────────────────                │
│                    se evalúa a                              │
│                      un valor                               │
└─────────────────────────────────────────────────────────────┘
```

## Tipos de Expresiones

### 1. Expresiones Aritméticas

Producen un valor numérico.

```python
# Expresiones aritméticas simples
5 + 3                    # 8
10 * 2                   # 20

# Expresiones con variables
x = 5
y = 3
resultado = x + y * 2    # 11

# Expresiones complejas
area_circulo = 3.14159 * radio ** 2
promedio = (nota1 + nota2 + nota3) / 3
hipotenusa = (cateto1**2 + cateto2**2) ** 0.5
```

### 2. Expresiones Relacionales

Producen un valor booleano (True/False).

```python
# Comparaciones simples
5 > 3          # True
10 == 10       # True
"a" < "b"      # True

# Con variables
edad = 25
es_adulto = edad >= 18              # True
en_rango = 18 <= edad <= 65         # True (comparación encadenada)

# Expresiones complejas
nota = 75
asistencia = 85
cumple_requisitos = nota >= 60 and asistencia >= 80  # True
```

### 3. Expresiones Lógicas

Combinan valores booleanos.

```python
# Expresiones lógicas
True and False          # False
True or False           # True
not True               # False

# Con comparaciones
x = 10
(x > 5) and (x < 20)   # True
(x < 5) or (x > 8)     # True
not (x == 10)          # False
```

### 4. Expresiones de Cadena

Operaciones con texto.

```python
# Concatenación
"Hola" + " " + "Mundo"           # "Hola Mundo"

# Repetición
"=" * 20                          # "===================="

# Con variables
nombre = "Juan"
saludo = "Hola, " + nombre + "!"  # "Hola, Juan!"

# f-strings (expresiones dentro de cadenas)
edad = 25
mensaje = f"Tienes {edad} años"   # "Tienes 25 años"
calculo = f"El doble es {edad * 2}"  # "El doble es 50"
```

## Evaluación de Expresiones

### Reglas de Evaluación

1. Se evalúan primero los **paréntesis** (de adentro hacia afuera)
2. Se respeta la **precedencia** de operadores
3. Operadores de igual precedencia se evalúan de **izquierda a derecha** (excepto potencia)

### Ejemplo Paso a Paso

```python
expresion = 2 + 3 * 4 - 8 / 2

# Paso 1: Multiplicación (3 * 4 = 12)
# 2 + 12 - 8 / 2

# Paso 2: División (8 / 2 = 4.0)
# 2 + 12 - 4.0

# Paso 3: Suma (2 + 12 = 14)
# 14 - 4.0

# Paso 4: Resta (14 - 4.0 = 10.0)
# Resultado: 10.0
```

### Ejemplo con Paréntesis

```python
expresion = (2 + 3) * (4 - 8) / 2

# Paso 1: Paréntesis izquierdo (2 + 3 = 5)
# 5 * (4 - 8) / 2

# Paso 2: Paréntesis derecho (4 - 8 = -4)
# 5 * -4 / 2

# Paso 3: Multiplicación (5 * -4 = -20)
# -20 / 2

# Paso 4: División (-20 / 2 = -10.0)
# Resultado: -10.0
```

## Expresiones en Asignaciones

```python
# Asignación simple
x = 5

# Asignación con expresión
y = x + 10           # y = 15

# Actualización con expresión
x = x + 1            # x = 6 (incremento)
x += 1               # x = 7 (forma abreviada)

# Múltiples asignaciones
a = b = c = 0        # Todas valen 0

# Asignación múltiple
x, y = 10, 20        # x=10, y=20
x, y = y, x          # Intercambio: x=20, y=10
```

## Expresiones Condicionales (Operador Ternario)

Una forma compacta de escribir if-else:

```python
# Sintaxis: valor_si_true if condicion else valor_si_false

edad = 20
estado = "Mayor" if edad >= 18 else "Menor"
# estado = "Mayor"

# Equivalente a:
if edad >= 18:
    estado = "Mayor"
else:
    estado = "Menor"

# Más ejemplos
numero = 7
paridad = "Par" if numero % 2 == 0 else "Impar"  # "Impar"

nota = 75
resultado = "Aprobado" if nota >= 60 else "Reprobado"  # "Aprobado"
```

## Expresiones con Funciones

```python
# Funciones que retornan valores
import math

# Expresiones con funciones matemáticas
raiz = math.sqrt(16)              # 4.0
valor_absoluto = abs(-5)          # 5
maximo = max(3, 7, 2)             # 7
minimo = min(3, 7, 2)             # 2
redondeado = round(3.7)           # 4

# Combinando funciones
hipotenusa = math.sqrt(3**2 + 4**2)  # 5.0

# Funciones de conversión en expresiones
numero = int("42") + 8            # 50
texto = str(100) + " puntos"      # "100 puntos"
```

## Ejemplos Prácticos

### Cálculo de Precio Final

```python
precio_base = 100
cantidad = 5
descuento = 0.10
iva = 0.16

# Expresión para calcular total
subtotal = precio_base * cantidad
total_con_descuento = subtotal * (1 - descuento)
total_final = total_con_descuento * (1 + iva)

# O en una sola expresión
total = precio_base * cantidad * (1 - descuento) * (1 + iva)
```

### Fórmula Cuadrática

```python
import math

a, b, c = 1, -5, 6  # Coeficientes de ax² + bx + c = 0

discriminante = b**2 - 4*a*c
x1 = (-b + math.sqrt(discriminante)) / (2*a)
x2 = (-b - math.sqrt(discriminante)) / (2*a)

print(f"x1 = {x1}, x2 = {x2}")  # x1 = 3.0, x2 = 2.0
```

## 📝 Para Recordar

1. Una **expresión** combina valores, variables y operadores
2. Se evalúa siguiendo las reglas de **precedencia**
3. Los **paréntesis** alteran el orden de evaluación
4. Existen expresiones **aritméticas, relacionales, lógicas y de cadena**
5. El **operador ternario** permite expresiones condicionales compactas

## ✅ Ejercicio Rápido

Evalúa las siguientes expresiones:

```python
a = 2 + 3 * 4 / 2
b = (2 + 3) * 4 / 2
c = 10 > 5 and 3 < 2
d = "Hola" + str(2 + 3)
e = "Par" if 10 % 2 == 0 else "Impar"
```

<details>
<summary>Ver respuesta</summary>

```python
a = 2 + 3 * 4 / 2    # 2 + 6.0 = 8.0
b = (2 + 3) * 4 / 2  # 5 * 4 / 2 = 10.0
c = 10 > 5 and 3 < 2 # True and False = False
d = "Hola" + str(2 + 3)  # "Hola" + "5" = "Hola5"
e = "Par" if 10 % 2 == 0 else "Impar"  # "Par"
```
</details>

## 🔜 Siguiente Paso

Ahora aprenderás sobre los identificadores.

[Ir a: 05 - Identificadores →](./05_identificadores.md)

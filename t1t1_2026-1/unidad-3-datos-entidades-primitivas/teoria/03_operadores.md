# 📖 03 - Los Operadores

## ¿Qué son los Operadores?

Los **operadores** son símbolos que indican al programa realizar operaciones específicas sobre uno o más valores (operandos).

```
    operando    operador    operando
        ↓          ↓          ↓
       10         +          5       =  15
                                         ↑
                                     resultado
```

## Tipos de Operadores

```
┌─────────────────────────────────────────────────────────────┐
│                    TIPOS DE OPERADORES                       │
├─────────────┬─────────────┬─────────────┬───────────────────┤
│ ARITMÉTICOS │ RELACIONALES│   LÓGICOS   │   ASIGNACIÓN      │
│             │             │             │                   │
│ +  -  *  /  │ ==  !=  <   │ and  or     │ =  +=  -=  *=     │
│ //  %  **   │ >  <=  >=   │ not         │ /=  //=  %=       │
└─────────────┴─────────────┴─────────────┴───────────────────┘
```

## 1. Operadores Aritméticos

Realizan operaciones matemáticas.

| Operador | Nombre | Ejemplo | Resultado |
|----------|--------|---------|-----------|
| `+` | Suma | `5 + 3` | `8` |
| `-` | Resta | `5 - 3` | `2` |
| `*` | Multiplicación | `5 * 3` | `15` |
| `/` | División | `5 / 2` | `2.5` |
| `//` | División entera | `5 // 2` | `2` |
| `%` | Módulo (residuo) | `5 % 2` | `1` |
| `**` | Potencia | `5 ** 2` | `25` |

### Ejemplos en Python

```python
# Operaciones básicas
a = 10
b = 3

suma = a + b          # 13
resta = a - b         # 7
multiplicacion = a * b # 30
division = a / b      # 3.3333...
division_entera = a // b  # 3
residuo = a % b       # 1
potencia = a ** b     # 1000

# Uso práctico del módulo
numero = 17
es_par = numero % 2 == 0  # False (17 es impar)

# Raíz cuadrada usando potencia
import math
raiz = 16 ** 0.5      # 4.0
# o usar math.sqrt(16)
```

## 2. Operadores Relacionales (Comparación)

Comparan dos valores y devuelven un booleano.

| Operador | Nombre | Ejemplo | Resultado |
|----------|--------|---------|-----------|
| `==` | Igual a | `5 == 5` | `True` |
| `!=` | Diferente de | `5 != 3` | `True` |
| `>` | Mayor que | `5 > 3` | `True` |
| `<` | Menor que | `5 < 3` | `False` |
| `>=` | Mayor o igual | `5 >= 5` | `True` |
| `<=` | Menor o igual | `3 <= 5` | `True` |

### Ejemplos en Python

```python
x = 10
y = 5

print(x == y)   # False
print(x != y)   # True
print(x > y)    # True
print(x < y)    # False
print(x >= 10)  # True
print(y <= 5)   # True

# Comparación de cadenas (orden alfabético)
print("abc" < "abd")   # True
print("Ana" < "ana")   # True (mayúsculas antes)

# Uso en condiciones
edad = 20
if edad >= 18:
    print("Mayor de edad")
```

## 3. Operadores Lógicos

Combinan expresiones booleanas.

| Operador | Nombre | Descripción |
|----------|--------|-------------|
| `and` | Y lógico | True si AMBOS son True |
| `or` | O lógico | True si AL MENOS UNO es True |
| `not` | Negación | Invierte el valor |

### Tablas de Verdad

```
AND                    OR                     NOT
A     B     A and B    A     B     A or B     A     not A
True  True  True       True  True  True       True  False
True  False False      True  False True       False True
False True  False      False True  True
False False False      False False False
```

### Ejemplos en Python

```python
# Operador AND
tiene_edad = True
tiene_licencia = False
puede_conducir = tiene_edad and tiene_licencia  # False

# Operador OR
tiene_efectivo = False
tiene_tarjeta = True
puede_pagar = tiene_efectivo or tiene_tarjeta  # True

# Operador NOT
esta_lloviendo = True
salir_sin_paraguas = not esta_lloviendo  # False

# Combinaciones
edad = 25
es_estudiante = True
tiene_descuento = (edad < 30) and es_estudiante  # True

# Expresiones complejas
nota = 75
asistencia = 85
aprobado = (nota >= 60) and (asistencia >= 80)  # True
```

## 4. Operadores de Asignación

Asignan valores a variables.

| Operador | Ejemplo | Equivalente a |
|----------|---------|---------------|
| `=` | `x = 5` | `x = 5` |
| `+=` | `x += 3` | `x = x + 3` |
| `-=` | `x -= 3` | `x = x - 3` |
| `*=` | `x *= 3` | `x = x * 3` |
| `/=` | `x /= 3` | `x = x / 3` |
| `//=` | `x //= 3` | `x = x // 3` |
| `%=` | `x %= 3` | `x = x % 3` |
| `**=` | `x **= 3` | `x = x ** 3` |

### Ejemplos

```python
# Asignación simple
contador = 0

# Incremento
contador += 1  # contador = 1

# Acumulador
suma = 0
suma += 10  # suma = 10
suma += 20  # suma = 30

# Otros operadores
x = 10
x *= 2   # x = 20
x /= 4   # x = 5.0
```

## Precedencia de Operadores

Orden en que se evalúan los operadores (de mayor a menor prioridad):

```
1. ()           Paréntesis
2. **           Potencia
3. +x, -x       Positivo, Negativo unario
4. *, /, //, %  Multiplicación, División, Módulo
5. +, -         Suma, Resta
6. ==, !=, <, >, <=, >=  Comparación
7. not          Negación lógica
8. and          Y lógico
9. or           O lógico
10. =, +=, -=   Asignación
```

### Ejemplos de Precedencia

```python
# Sin paréntesis
resultado = 2 + 3 * 4      # 14 (primero * , luego +)

# Con paréntesis
resultado = (2 + 3) * 4    # 20 (primero + , luego *)

# Expresión compleja
resultado = 2 ** 3 + 4 * 5 - 6 / 2
# = 8 + 20 - 3.0
# = 25.0

# Lógicos
resultado = True or False and False
# and se evalúa primero: False and False = False
# luego: True or False = True
```

## 📝 Para Recordar

1. **Aritméticos**: +, -, *, /, //, %, **
2. **Relacionales**: ==, !=, <, >, <=, >=
3. **Lógicos**: and, or, not
4. **Asignación**: =, +=, -=, *=, etc.
5. Usar **paréntesis** para controlar la precedencia

## ✅ Ejercicio Rápido

¿Cuál es el resultado de cada expresión?

```python
a = 10 + 5 * 2
b = (10 + 5) * 2
c = 17 % 5
d = 2 ** 3 ** 2
e = True and False or True
```

<details>
<summary>Ver respuesta</summary>

```python
a = 10 + 5 * 2       # 20 (5*2=10, 10+10=20)
b = (10 + 5) * 2     # 30 (15*2=30)
c = 17 % 5           # 2 (17÷5=3, residuo=2)
d = 2 ** 3 ** 2      # 512 (3**2=9, 2**9=512) - derecha a izquierda
e = True and False or True  # True (False or True = True)
```
</details>

## 🔜 Siguiente Paso

Ahora aprenderás sobre las expresiones.

[Ir a: 04 - Expresiones →](./04_expresiones.md)

# ➕ Operaciones Aritméticas

## Operadores Básicos

Python puede realizar operaciones matemáticas como una calculadora.

| Operador | Operación | Ejemplo | Resultado |
|----------|-----------|---------|-----------|
| `+` | Suma | `5 + 3` | `8` |
| `-` | Resta | `10 - 4` | `6` |
| `*` | Multiplicación | `6 * 7` | `42` |
| `/` | División | `15 / 2` | `7.5` |
| `//` | División entera | `15 // 2` | `7` |
| `%` | Módulo (residuo) | `15 % 2` | `1` |
| `**` | Potencia | `2 ** 3` | `8` |

## Ejemplos de Cada Operación

### Suma y Resta

```python
a = 10
b = 3

suma = a + b        # 13
resta = a - b       # 7

print(f"{a} + {b} = {suma}")
print(f"{a} - {b} = {resta}")
```

### Multiplicación y División

```python
a = 20
b = 4

multiplicacion = a * b    # 80
division = a / b          # 5.0

print(f"{a} × {b} = {multiplicacion}")
print(f"{a} ÷ {b} = {division}")
```

### División Entera y Módulo

```python
a = 17
b = 5

division_entera = a // b  # 3 (solo la parte entera)
residuo = a % b           # 2 (lo que sobra)

print(f"{a} // {b} = {division_entera}")
print(f"{a} % {b} = {residuo}")
```

> 💡 El **módulo** (`%`) es útil para saber si un número es par o impar:
> - Si `numero % 2 == 0` → es **par**
> - Si `numero % 2 == 1` → es **impar**

### Potencia

```python
base = 2
exponente = 3

potencia = base ** exponente  # 2³ = 8

print(f"{base} elevado a {exponente} = {potencia}")
```

---

## Orden de las Operaciones

Python sigue las reglas matemáticas (PEMDAS):

1. **P**aréntesis `( )`
2. **E**xponentes `**`
3. **M**ultiplicación y **D**ivisión `* / // %`
4. **A**dición y **S**ustracción `+ -`

### Ejemplo

```python
resultado = 2 + 3 * 4      # 14 (primero 3*4, luego +2)
resultado = (2 + 3) * 4    # 20 (primero 2+3, luego *4)
```

---

## Operaciones con Variables

```python
# Pedir dos números
num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))

# Realizar operaciones
suma = num1 + num2
resta = num1 - num2
producto = num1 * num2
cociente = num1 / num2

# Mostrar resultados
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Producto: {producto}")
print(f"Cociente: {cociente}")
```

---

## Operadores de Asignación Compuesta

Forma abreviada de modificar una variable:

| Operador | Equivalente | Ejemplo |
|----------|-------------|---------|
| `+=` | `x = x + n` | `x += 5` |
| `-=` | `x = x - n` | `x -= 3` |
| `*=` | `x = x * n` | `x *= 2` |
| `/=` | `x = x / n` | `x /= 4` |

```python
contador = 10
contador += 5     # contador = 15
contador -= 3     # contador = 12
contador *= 2     # contador = 24
```

---

## Fórmulas Comunes

### Área de un rectángulo
```python
base = float(input("Base: "))
altura = float(input("Altura: "))
area = base * altura
print(f"Área: {area}")
```

### Promedio de tres números
```python
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
promedio = (n1 + n2 + n3) / 3
print(f"Promedio: {promedio}")
```

### Conversión de temperatura (°C a °F)
```python
celsius = float(input("Temperatura en °C: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")
```

---

## 📝 Resumen

- Operadores: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- División `/` da decimales, `//` da solo enteros
- `%` (módulo) da el residuo de la división
- Los paréntesis cambian el orden de las operaciones
- Operadores compuestos: `+=`, `-=`, `*=`, `/=`

---

**Anterior:** [03_entrada_salida.md](./03_entrada_salida.md)

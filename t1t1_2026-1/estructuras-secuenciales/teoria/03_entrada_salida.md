# 🔄 Entrada y Salida de Datos

## La Función `print()` - Mostrar Datos

`print()` muestra información en la pantalla (SALIDA).

### Sintaxis básica

```python
print("Hola mundo")
```

### Mostrar variables

```python
nombre = "Carlos"
print(nombre)           # Muestra: Carlos

edad = 20
print(edad)             # Muestra: 20
```

### Mostrar texto y variables juntos

**Opción 1: Separar con comas**
```python
nombre = "Ana"
edad = 22
print("Nombre:", nombre)          # Muestra: Nombre: Ana
print("Edad:", edad, "años")      # Muestra: Edad: 22 años
```

**Opción 2: f-strings (recomendado)**
```python
nombre = "Ana"
edad = 22
print(f"Nombre: {nombre}")        # Muestra: Nombre: Ana
print(f"Tienes {edad} años")      # Muestra: Tienes 22 años
```

> 💡 Las **f-strings** llevan una `f` antes de las comillas y las variables van entre `{llaves}`

---

## La Función `input()` - Recibir Datos

`input()` pide información al usuario (ENTRADA).

### Sintaxis básica

```python
nombre = input("¿Cómo te llamas? ")
print(f"Hola, {nombre}")
```

Cuando se ejecuta:
```
¿Cómo te llamas? María
Hola, María
```

### ⚠️ Importante: `input()` siempre devuelve texto

```python
edad = input("Tu edad: ")
print(type(edad))    # <class 'str'> ← ¡Es texto, no número!
```

### Convertir texto a número

Para hacer cálculos, debes convertir el texto a número:

| Conversión | Función | Ejemplo |
|------------|---------|---------|
| Texto → Entero | `int()` | `int("25")` → `25` |
| Texto → Decimal | `float()` | `float("3.14")` → `3.14` |
| Número → Texto | `str()` | `str(25)` → `"25"` |

### Ejemplo correcto

```python
# Pedir edad como número entero
edad = int(input("Tu edad: "))

# Ahora podemos hacer cálculos
edad_futura = edad + 10
print(f"En 10 años tendrás {edad_futura} años")
```

### Ejemplo con decimales

```python
# Pedir precio como número decimal
precio = float(input("Precio del producto: "))

# Calcular con descuento
descuento = precio * 0.10
precio_final = precio - descuento

print(f"Precio con descuento: {precio_final}")
```

---

## Patrón Completo: Entrada → Proceso → Salida

```python
# ENTRADA
numero = int(input("Ingresa un número: "))

# PROCESO
cuadrado = numero * numero

# SALIDA
print(f"El cuadrado de {numero} es {cuadrado}")
```

---

## 📝 Resumen

| Función | Uso | Ejemplo |
|---------|-----|---------|
| `print()` | Mostrar datos | `print("Hola")` |
| `input()` | Pedir datos | `input("Nombre: ")` |
| `int()` | Convertir a entero | `int(input("Edad: "))` |
| `float()` | Convertir a decimal | `float(input("Precio: "))` |

---

**Anterior:** [02_variables_tipos.md](./02_variables_tipos.md) | **Siguiente:** [04_operaciones.md](./04_operaciones.md)

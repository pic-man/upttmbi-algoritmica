# 📖 02 - Estructuras de Decisión

## ¿Qué son las Estructuras de Decisión?

Las **estructuras de decisión** permiten que el programa elija entre diferentes caminos de ejecución según se cumpla o no una condición.

## Tipos de Estructuras de Decisión

```
┌─────────────────────────────────────────────────────────────┐
│                ESTRUCTURAS DE DECISIÓN                       │
├─────────────┬─────────────┬─────────────┬───────────────────┤
│   SIMPLE    │    DOBLE    │  MÚLTIPLE   │    ANIDADA        │
│             │             │             │                   │
│  if         │ if-else     │ if-elif-else│ if dentro de if   │
└─────────────┴─────────────┴─────────────┴───────────────────┘
```

## 1. Condicional Simple (if)

Ejecuta un bloque de código **solo si** la condición es verdadera.

```python
# Sintaxis
if condicion:
    # instrucciones si es verdadero

# Ejemplo
edad = 20
if edad >= 18:
    print("Puede votar")
```

## 2. Condicional Doble (if-else)

Ejecuta un bloque si es verdadero, **otro bloque** si es falso.

```python
# Sintaxis
if condicion:
    # instrucciones si es verdadero
else:
    # instrucciones si es falso

# Ejemplo
nota = 55
if nota >= 60:
    print("Aprobado")
else:
    print("Reprobado")
```

## 3. Condicional Múltiple (if-elif-else)

Evalúa **múltiples condiciones** en secuencia.

```python
# Sintaxis
if condicion1:
    # si condicion1 es verdadera
elif condicion2:
    # si condicion2 es verdadera
elif condicion3:
    # si condicion3 es verdadera
else:
    # si ninguna es verdadera

# Ejemplo: Calificación por letra
nota = 85
if nota >= 90:
    letra = "A"
elif nota >= 80:
    letra = "B"
elif nota >= 70:
    letra = "C"
elif nota >= 60:
    letra = "D"
else:
    letra = "F"
print(f"Calificación: {letra}")
```

## 4. Condicionales Anidados

Un condicional **dentro de otro**.

```python
# Ejemplo: Clasificar triángulo
if lado1 == lado2 == lado3:
    print("Equilátero")
else:
    if lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print("Isósceles")
    else:
        print("Escaleno")
```

## 5. Estructura Selectiva (match-case)

Python 3.10+ incluye `match-case` para selección múltiple:

```python
# Ejemplo
opcion = 2

match opcion:
    case 1:
        print("Opción uno")
    case 2:
        print("Opción dos")
    case 3:
        print("Opción tres")
    case _:
        print("Opción no válida")
```

## Ejemplos Prácticos

### Determinar tipo de número

```python
numero = int(input("Ingrese un número: "))

if numero > 0:
    print("Positivo")
elif numero < 0:
    print("Negativo")
else:
    print("Cero")
```

### Calculadora de descuentos

```python
total_compra = float(input("Total de compra: $"))

if total_compra >= 1000:
    descuento = 0.20  # 20%
elif total_compra >= 500:
    descuento = 0.10  # 10%
elif total_compra >= 100:
    descuento = 0.05  # 5%
else:
    descuento = 0

monto_descuento = total_compra * descuento
total_pagar = total_compra - monto_descuento

print(f"Descuento: ${monto_descuento:.2f}")
print(f"Total a pagar: ${total_pagar:.2f}")
```

## 📝 Para Recordar

1. **Simple (if)**: una sola condición
2. **Doble (if-else)**: dos caminos posibles
3. **Múltiple (if-elif-else)**: varias condiciones
4. **Anidada**: condicionales dentro de otros
5. **Selectiva (match)**: selección por valor exacto

## 🔜 Siguiente Paso

[Ir a: 06 - Ciclo Mientras →](./06_ciclo_mientras.md)

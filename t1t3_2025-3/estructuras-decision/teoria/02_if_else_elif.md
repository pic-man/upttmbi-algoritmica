# 📖 02 - If, Else, Elif

## Sintaxis Completa de las Estructuras de Decisión

En Python, tenemos tres palabras clave para tomar decisiones:
- `if` - Si (condición inicial)
- `elif` - Sino si (condiciones adicionales)
- `else` - Sino (caso por defecto)

## 1️⃣ IF (Si)

La forma más básica de tomar una decisión.

### Sintaxis:
```python
if condicion:
    # código a ejecutar si la condición es verdadera
    instruccion1
    instruccion2
```

### Ejemplo:
```python
edad = 20

if edad >= 18:
    print("Eres mayor de edad")
    print("Puedes votar")
```

### Características:
- Si la condición es `True`, ejecuta el bloque indentado
- Si es `False`, **salta** el bloque y continúa
- Puede existir solo, sin `else` o `elif`

## 2️⃣ IF-ELSE (Si-Sino)

Cuando quieres ejecutar algo si la condición es falsa.

### Sintaxis:
```python
if condicion:
    # código si es verdadero
else:
    # código si es falso
```

### Ejemplo:
```python
edad = 15

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

**Resultado**: `Eres menor de edad`

### Diagrama de flujo:
```
       ┌──────────┐
       │ Condición│
       └────┬─────┘
            │
       ┌────┴────┐
       │         │
      Sí        No
       │         │
       ▼         ▼
   ┌──────┐ ┌──────┐
   │  IF  │ │ ELSE │
   └──────┘ └──────┘
```

## 3️⃣ IF-ELIF-ELSE (Si-Sino Si-Sino)

Para múltiples condiciones.

### Sintaxis:
```python
if condicion1:
    # código si condicion1 es verdadera
elif condicion2:
    # código si condicion2 es verdadera
elif condicion3:
    # código si condicion3 es verdadera
else:
    # código si ninguna es verdadera
```

### Ejemplo:
```python
nota = 7

if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Bien")
elif nota >= 6:
    print("Aprobado")
else:
    print("Reprobado")
```

**Resultado**: `Bien` (porque 7 >= 7 es la primera condición verdadera)

### Características importantes:

1. **Se evalúan en orden**: De arriba hacia abajo
2. **Solo se ejecuta UNO**: Cuando encuentra una condición verdadera, ejecuta ese bloque y termina
3. **else es opcional**: Puedes tener if-elif sin else
4. **elif ilimitados**: Puedes tener tantos elif como necesites

### Ejemplo con múltiples elif:

```python
dia = 3

if dia == 1:
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miércoles")
elif dia == 4:
    print("Jueves")
elif dia == 5:
    print("Viernes")
elif dia == 6:
    print("Sábado")
elif dia == 7:
    print("Domingo")
else:
    print("Día inválido")
```

**Resultado**: `Miércoles`

## 🔄 Comparación: IF múltiples vs IF-ELIF

### ❌ IF múltiples (INCORRECTO para opciones excluyentes):
```python
nota = 8

if nota >= 6:
    print("Aprobado")      # Se imprime
if nota >= 7:
    print("Bien")          # Se imprime
if nota >= 9:
    print("Excelente")     # NO se imprime
```
**Resultado**: 
```
Aprobado
Bien
```
⚠️ Se evalúan TODAS las condiciones

### ✅ IF-ELIF (CORRECTO):
```python
nota = 8

if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Bien")          # Se imprime SOLO esto
elif nota >= 6:
    print("Aprobado")
```
**Resultado**: 
```
Bien
```
✅ Se detiene en la primera condición verdadera

## 📊 Ejemplos Prácticos

### Ejemplo 1: Sistema de descuentos
```python
total = 100

if total >= 500:
    descuento = 0.20  # 20%
    print("Descuento: 20%")
elif total >= 200:
    descuento = 0.10  # 10%
    print("Descuento: 10%")
elif total >= 100:
    descuento = 0.05  # 5%
    print("Descuento: 5%")
else:
    descuento = 0
    print("Sin descuento")

precio_final = total - (total * descuento)
print(f"Total a pagar: ${precio_final}")
```

### Ejemplo 2: Clasificación de temperatura
```python
temperatura = 22

if temperatura >= 30:
    print("Hace mucho calor 🥵")
elif temperatura >= 20:
    print("Clima agradable 😊")
elif temperatura >= 10:
    print("Hace fresco 😐")
else:
    print("Hace frío 🥶")
```

### Ejemplo 3: Validación de edad
```python
edad = int(input("Ingresa tu edad: "))

if edad < 0:
    print("Edad no válida")
elif edad < 13:
    print("Eres un niño")
elif edad < 18:
    print("Eres un adolescente")
elif edad < 60:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")
```

## 🎯 Orden de las Condiciones

⚠️ **MUY IMPORTANTE**: El orden importa cuando las condiciones se solapan.

### ❌ Orden INCORRECTO:
```python
edad = 25

if edad >= 0:
    print("Edad válida")     # Siempre se ejecuta esto
elif edad >= 18:
    print("Mayor de edad")   # Nunca se alcanza
```

### ✅ Orden CORRECTO:
```python
edad = 25

if edad < 0:
    print("Edad inválida")
elif edad < 18:
    print("Menor de edad")
elif edad < 120:
    print("Mayor de edad")   # Se ejecuta esto
else:
    print("Edad inválida")
```

**Regla general**: Ordena de **más específico a más general**.

## 🧪 Ejercicios de Práctica

### Ejercicio 1:
¿Qué imprime este código?
```python
x = 10

if x > 15:
    print("A")
elif x > 5:
    print("B")
else:
    print("C")
```

<details>
<summary>Ver respuesta</summary>
`B` - Porque 10 > 5 es la primera condición verdadera.
</details>

### Ejercicio 2:
¿Qué está mal en este código?
```python
nota = 7

if nota >= 9:
    print("Excelente")
if nota >= 6:
    print("Aprobado")
```

<details>
<summary>Ver respuesta</summary>
Debería usar `elif` en lugar del segundo `if`, porque ahora imprime ambas cosas si nota es >= 9.
</details>

## 📝 Resumen

| Estructura | Uso | Cantidad |
|------------|-----|----------|
| `if` | Primera condición | Obligatorio (1) |
| `elif` | Condiciones adicionales | Opcional (0 o más) |
| `else` | Caso por defecto | Opcional (0 o 1) |

### Reglas de oro:
1. Siempre comienza con `if`
2. `elif` va después de `if` o de otro `elif`
3. `else` siempre va al final
4. Solo se ejecuta **un** bloque
5. El orden de las condiciones **importa**

## 🔜 Siguiente Paso

Ahora que dominas la sintaxis básica, aprenderás sobre los operadores de comparación.

[← Anterior: 01 - Introducción](./01_introduccion.md) | [Siguiente: 03 - Operadores de Comparación →](./03_operadores_comparacion.md)


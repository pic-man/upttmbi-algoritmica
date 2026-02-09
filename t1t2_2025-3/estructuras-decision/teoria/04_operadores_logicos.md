# 📖 04 - Operadores Lógicos

## ¿Qué son los Operadores Lógicos?

Los **operadores lógicos** permiten combinar múltiples condiciones. Son como conectores que unen varias preguntas en una sola.

En Python tenemos tres operadores lógicos:
- `and` (y)
- `or` (o)
- `not` (no)

## 1️⃣ AND (Y)

El operador `and` devuelve `True` solo si **AMBAS** condiciones son verdaderas.

### Tabla de verdad:
| Condición 1 | Condición 2 | Resultado |
|-------------|-------------|-----------|
| `True` | `True` | `True` ✅ |
| `True` | `False` | `False` ❌ |
| `False` | `True` | `False` ❌ |
| `False` | `False` | `False` ❌ |

### Sintaxis:
```python
if condicion1 and condicion2:
    # Se ejecuta solo si AMBAS son verdaderas
```

### Ejemplos básicos:
```python
print(True and True)     # True
print(True and False)    # False
print(False and False)   # False

print(5 > 3 and 10 > 8)  # True (ambas verdaderas)
print(5 > 3 and 10 < 8)  # False (una es falsa)
```

### Uso práctico:
```python
edad = 25
tiene_licencia = True

if edad >= 18 and tiene_licencia:
    print("Puedes conducir ✅")
else:
    print("No puedes conducir ❌")
```

### Ejemplo con números:
```python
nota = 8

if nota >= 6 and nota <= 10:
    print("Nota válida y aprobado")

# Forma más elegante (encadenada):
if 6 <= nota <= 10:
    print("Nota válida y aprobado")
```

## 2️⃣ OR (O)

El operador `or` devuelve `True` si **AL MENOS UNA** condición es verdadera.

### Tabla de verdad:
| Condición 1 | Condición 2 | Resultado |
|-------------|-------------|-----------|
| `True` | `True` | `True` ✅ |
| `True` | `False` | `True` ✅ |
| `False` | `True` | `True` ✅ |
| `False` | `False` | `False` ❌ |

### Sintaxis:
```python
if condicion1 or condicion2:
    # Se ejecuta si AL MENOS UNA es verdadera
```

### Ejemplos básicos:
```python
print(True or True)      # True
print(True or False)     # True
print(False or False)    # False

print(5 > 3 or 10 < 8)   # True (una es verdadera)
print(5 < 3 or 10 < 8)   # False (ambas falsas)
```

### Uso práctico:
```python
dia = "sábado"

if dia == "sábado" or dia == "domingo":
    print("Es fin de semana 🎉")
else:
    print("Es día laboral 💼")
```

### Ejemplo de validación:
```python
edad = -5

if edad < 0 or edad > 120:
    print("Edad no válida")
else:
    print("Edad válida")
```

## 3️⃣ NOT (NO)

El operador `not` invierte el valor booleano.

### Tabla de verdad:
| Condición | Resultado |
|-----------|-----------|
| `True` | `False` |
| `False` | `True` |

### Sintaxis:
```python
if not condicion:
    # Se ejecuta si la condición es FALSA
```

### Ejemplos básicos:
```python
print(not True)          # False
print(not False)         # True

print(not 5 > 3)         # False (porque 5 > 3 es True)
print(not 5 < 3)         # True (porque 5 < 3 es False)
```

### Uso práctico:
```python
es_admin = False

if not es_admin:
    print("No tienes permisos de administrador")
```

### Ejemplo con strings:
```python
respuesta = input("¿Deseas continuar? (s/n): ")

if not respuesta == "s":
    print("Programa terminado")
    exit()

# Forma equivalente (más común):
if respuesta != "s":
    print("Programa terminado")
    exit()
```

## 🔗 Combinando Operadores

Puedes combinar múltiples operadores lógicos en una sola condición.

### Ejemplo 1: AND y OR
```python
edad = 25
tiene_dinero = True
es_fin_de_semana = True

if (edad >= 18 and tiene_dinero) or es_fin_de_semana:
    print("Puedes salir a divertirte")
```

### Ejemplo 2: Validación compleja
```python
usuario = "admin"
password = "1234"
tiene_token = False

if (usuario == "admin" and password == "1234") or tiene_token:
    print("Acceso concedido")
else:
    print("Acceso denegado")
```

### Ejemplo 3: Validación de rango
```python
temperatura = 22

if temperatura > 0 and temperatura < 30:
    print("Temperatura agradable")
elif temperatura >= 30 or temperatura <= 0:
    print("Temperatura extrema")
```

## ⚙️ Orden de Evaluación (Precedencia)

Python evalúa los operadores en este orden:
1. `not` (primero)
2. `and` (segundo)
3. `or` (último)

### Ejemplo sin paréntesis:
```python
# not se evalúa primero, luego and, luego or
if True or False and not True:
    print("A")
else:
    print("B")

# Evaluación paso a paso:
# 1. not True = False
# 2. False and False = False
# 3. True or False = True
# Resultado: "A"
```

### Usa paréntesis para claridad:
```python
# Sin paréntesis (confuso)
if edad >= 18 and ciudad == "Madrid" or tiene_permiso:
    print("Puedes entrar")

# Con paréntesis (claro)
if (edad >= 18 and ciudad == "Madrid") or tiene_permiso:
    print("Puedes entrar")
```

## 💡 Ejemplos Prácticos Completos

### Ejemplo 1: Sistema de login completo
```python
usuario_correcto = "admin"
password_correcta = "1234"

usuario = input("Usuario: ")
password = input("Contraseña: ")

if usuario == usuario_correcto and password == password_correcta:
    print("✅ Acceso concedido")
elif usuario != usuario_correcto and password != password_correcta:
    print("❌ Usuario y contraseña incorrectos")
elif usuario != usuario_correcto:
    print("❌ Usuario incorrecto")
else:
    print("❌ Contraseña incorrecta")
```

### Ejemplo 2: Elegibilidad para préstamo
```python
edad = int(input("Edad: "))
ingreso_mensual = float(input("Ingreso mensual: "))
tiene_deudas = input("¿Tienes deudas? (s/n): ") == "s"

if edad >= 18 and edad <= 65 and ingreso_mensual >= 1000 and not tiene_deudas:
    print("✅ Eres elegible para el préstamo")
else:
    print("❌ No eres elegible")
    
    # Especificar por qué
    if edad < 18 or edad > 65:
        print("   - Edad fuera del rango permitido")
    if ingreso_mensual < 1000:
        print("   - Ingreso insuficiente")
    if tiene_deudas:
        print("   - Tienes deudas pendientes")
```

### Ejemplo 3: Clasificación de día
```python
dia = input("Ingresa el día: ").lower()

if dia == "sábado" or dia == "domingo":
    print("🎉 Fin de semana - Descansa")
elif dia == "lunes" or dia == "martes" or dia == "miércoles" or dia == "jueves" or dia == "viernes":
    print("💼 Día laboral - A trabajar")
else:
    print("❌ Día no válido")
```

### Ejemplo 4: Permiso para montaña rusa
```python
altura = float(input("Altura en cm: "))
edad = int(input("Edad: "))
va_con_adulto = input("¿Va con un adulto? (s/n): ") == "s"

# Puede subir si:
# - Tiene al menos 140cm, O
# - Tiene entre 120-140cm Y va con un adulto, Y tiene al menos 8 años

puede_subir = (
    altura >= 140 or
    (120 <= altura < 140 and va_con_adulto and edad >= 8)
)

if puede_subir:
    print("🎢 ¡Puedes subir a la montaña rusa!")
else:
    print("❌ No cumples los requisitos")
    if altura < 120:
        print("   - Altura mínima requerida: 120cm")
    elif altura < 140 and not va_con_adulto:
        print("   - Necesitas ir acompañado de un adulto")
    elif altura < 140 and edad < 8:
        print("   - Edad mínima: 8 años")
```

## 🧪 Ejercicios de Práctica

### Ejercicio 1:
¿Qué imprime este código?
```python
x = 5
y = 10

if x > 0 and y > 0:
    print("Ambos positivos")
```

<details>
<summary>Ver respuesta</summary>
`Ambos positivos` - Porque ambas condiciones son verdaderas.
</details>

### Ejercicio 2:
¿Qué imprime?
```python
edad = 16
tiene_permiso = True

if edad >= 18 or tiene_permiso:
    print("Puede entrar")
else:
    print("No puede entrar")
```

<details>
<summary>Ver respuesta</summary>
`Puede entrar` - Aunque edad < 18, tiene_permiso es True, y con `or` basta que una sea verdadera.
</details>

### Ejercicio 3:
¿Qué imprime?
```python
if not False:
    print("A")
else:
    print("B")
```

<details>
<summary>Ver respuesta</summary>
`A` - Porque `not False` es `True`.
</details>

## 📝 Errores Comunes

### ❌ Error 1: Repetir variables innecesariamente
```python
# INCORRECTO (redundante)
if x == 5 or x == 10 or x == 15:
    print("x es múltiplo de 5")

# MEJOR (más limpio)
if x in [5, 10, 15]:
    print("x es múltiplo de 5")

# O si es rango continuo:
if x % 5 == 0 and 5 <= x <= 15:
    print("x es múltiplo de 5 entre 5 y 15")
```

### ❌ Error 2: No usar paréntesis en expresiones complejas
```python
# CONFUSO
if edad >= 18 and ciudad == "Madrid" or tiene_permiso

# CLARO
if (edad >= 18 and ciudad == "Madrid") or tiene_permiso
```

### ❌ Error 3: Comparar con booleanos innecesariamente
```python
# INNECESARIO
if tiene_licencia == True:
    print("Tiene licencia")

# MEJOR
if tiene_licencia:
    print("Tiene licencia")

# Y para False:
if not tiene_licencia:
    print("No tiene licencia")
```

## 📝 Resumen

| Operador | Significado | ¿Cuándo es True? |
|----------|-------------|------------------|
| `and` | Y | Cuando TODAS las condiciones son True |
| `or` | O | Cuando AL MENOS UNA condición es True |
| `not` | NO | Invierte el valor booleano |

### Reglas de oro:
1. `and` requiere que **todo** sea verdadero
2. `or` requiere que **al menos uno** sea verdadero
3. `not` invierte el valor
4. Usa paréntesis para claridad
5. Orden de precedencia: `not` → `and` → `or`

## 🔜 Siguiente Paso

Ahora que dominas las condiciones y operadores, aprenderás las buenas prácticas para escribir código limpio.

[← Anterior: 03 - Operadores de Comparación](./03_operadores_comparacion.md) | [Siguiente: 05 - Buenas Prácticas →](./05_buenas_practicas.md)


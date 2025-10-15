# 📖 05 - Buenas Prácticas

## ¿Por qué Código Limpio?

Escribir código que funciona es solo el 50% del trabajo. El otro 50% es que sea **legible, mantenible y profesional**.

> "El código se lee mucho más de lo que se escribe" - Proverbio de programadores

## ✅ 1. Usa Nombres Descriptivos

### ❌ Malo:
```python
x = 18
if x >= 18:
    print("OK")
```

### ✅ Bueno:
```python
edad_minima = 18
edad_usuario = 20

if edad_usuario >= edad_minima:
    print("Puedes registrarte")
```

**Regla**: El código debe explicarse a sí mismo.

## ✅ 2. Evita Números Mágicos

Los "números mágicos" son valores sin contexto.

### ❌ Malo:
```python
if edad >= 18 and edad < 65:
    print("Edad laboral")
```

### ✅ Bueno:
```python
EDAD_MINIMA_LABORAL = 18
EDAD_MAXIMA_LABORAL = 65

if EDAD_MINIMA_LABORAL <= edad < EDAD_MAXIMA_LABORAL:
    print("Edad laboral")
```

**Regla**: Usa constantes con nombres descriptivos (en MAYÚSCULAS).

## ✅ 3. Mantén las Condiciones Simples

### ❌ Malo:
```python
if not (edad < 18 or edad > 120):
    print("Edad válida")
```

### ✅ Bueno:
```python
if 18 <= edad <= 120:
    print("Edad válida")
```

**Regla**: Busca la forma más directa y legible.

## ✅ 4. Evita Anidación Excesiva

### ❌ Malo:
```python
if edad >= 18:
    if tiene_licencia:
        if tiene_auto:
            if tiene_gasolina:
                print("Puedes conducir")
            else:
                print("Sin gasolina")
        else:
            print("Sin auto")
    else:
        print("Sin licencia")
else:
    print("Menor de edad")
```

### ✅ Bueno (Validación temprana):
```python
if edad < 18:
    print("Menor de edad")
    return

if not tiene_licencia:
    print("Sin licencia")
    return

if not tiene_auto:
    print("Sin auto")
    return

if not tiene_gasolina:
    print("Sin gasolina")
    return

print("Puedes conducir")
```

O mejor aún:

```python
puede_conducir = (
    edad >= 18 and
    tiene_licencia and
    tiene_auto and
    tiene_gasolina
)

if puede_conducir:
    print("Puedes conducir")
else:
    print("No cumples todos los requisitos")
```

**Regla**: Máximo 2-3 niveles de anidación. Si necesitas más, refactoriza.

## ✅ 5. Usa Comparaciones Positivas

### ❌ Malo:
```python
if not es_invalido:
    procesar()
```

### ✅ Bueno:
```python
if es_valido:
    procesar()
```

**Regla**: El cerebro humano procesa mejor las afirmaciones que las negaciones.

## ✅ 6. Agrupa Condiciones Relacionadas

### ❌ Malo:
```python
if edad >= 0 and edad <= 12:
    print("Niño")
if edad >= 13 and edad <= 17:
    print("Adolescente")
if edad >= 18 and edad <= 64:
    print("Adulto")
if edad >= 65:
    print("Adulto mayor")
```

### ✅ Bueno:
```python
if edad < 0:
    print("Edad inválida")
elif edad <= 12:
    print("Niño")
elif edad <= 17:
    print("Adolescente")
elif edad <= 64:
    print("Adulto")
else:
    print("Adulto mayor")
```

**Regla**: Usa `elif` cuando las condiciones son mutuamente excluyentes.

## ✅ 7. Comenta el "Por Qué", No el "Qué"

### ❌ Malo:
```python
# Si la edad es mayor o igual a 18
if edad >= 18:
    print("Mayor de edad")
```

### ✅ Bueno:
```python
# Verificamos la mayoría de edad según la ley venezolana
MAYORIA_DE_EDAD = 18
if edad >= MAYORIA_DE_EDAD:
    print("Mayor de edad")
```

O si el código es claro:
```python
# Sin comentario necesario (el código se explica solo)
MAYORIA_DE_EDAD = 18
if edad >= MAYORIA_DE_EDAD:
    print("Mayor de edad")
```

**Regla**: Comenta el propósito o la razón, no lo obvio.

## ✅ 8. Usa Espacios para Legibilidad

### ❌ Malo:
```python
if edad>=18and tiene_licencia==True or es_admin:
    print("Acceso concedido")
```

### ✅ Bueno:
```python
if edad >= 18 and tiene_licencia or es_admin:
    print("Acceso concedido")
```

**Regla**: Espacios alrededor de operadores (PEP 8).

## ✅ 9. Evita Comparaciones con True/False

### ❌ Malo:
```python
if tiene_permiso == True:
    print("Tiene permiso")

if es_admin == False:
    print("No es admin")
```

### ✅ Bueno:
```python
if tiene_permiso:
    print("Tiene permiso")

if not es_admin:
    print("No es admin")
```

**Regla**: Los booleanos ya son True o False.

## ✅ 10. Consistencia en el Estilo

### ❌ Malo (inconsistente):
```python
if edad>=18:
    print("Mayor")
    
if edad < 18:
print("Menor")

if(edad==18):
    print("Exacto")
```

### ✅ Bueno (consistente):
```python
if edad >= 18:
    print("Mayor")
    
if edad < 18:
    print("Menor")

if edad == 18:
    print("Exacto")
```

**Regla**: Mantén el mismo estilo en todo el código.

## 📊 Ejemplo: Antes y Después

### ❌ Código Malo:
```python
x=int(input("edad: "))
if x>=0:
    if x<18:
        print("menor")
    else:
        if x<65:
            print("adulto")
        else:
            if x<=120:
                print("adulto mayor")
            else:
                print("no valido")
else:
    print("no valido")
```

### ✅ Código Bueno:
```python
"""
Clasificador de edad según rangos etarios.
"""

# Constantes
EDAD_MINIMA_VALIDA = 0
EDAD_MAXIMA_VALIDA = 120
EDAD_ADULTO = 18
EDAD_ADULTO_MAYOR = 65

# Entrada
edad = int(input("Ingresa tu edad: "))

# Validación y clasificación
if edad < EDAD_MINIMA_VALIDA or edad > EDAD_MAXIMA_VALIDA:
    print("Edad no válida")
elif edad < EDAD_ADULTO:
    print("Menor de edad")
elif edad < EDAD_ADULTO_MAYOR:
    print("Adulto")
else:
    print("Adulto mayor")
```

## 🎨 Guía de Estilo PEP 8

Python tiene una guía oficial de estilo llamada PEP 8. Aquí los puntos clave:

### Indentación
```python
# 4 espacios por nivel
if condicion:
    hacer_algo()
    si_otra_condicion:
        hacer_otra_cosa()
```

### Longitud de línea
```python
# Máximo 79-88 caracteres por línea
# Si es muy largo, dividir:

if (edad >= 18 and 
    tiene_licencia and 
    tiene_auto):
    print("Puede conducir")
```

### Nombres de variables
```python
# Variables y funciones: snake_case
edad_usuario = 25
nombre_completo = "Juan"

# Constantes: MAYÚSCULAS
EDAD_MAXIMA = 120
PI = 3.14159

# Clases: PascalCase
class PersonaJoven:
    pass
```

### Espacios en blanco
```python
# ✅ Correcto
x = 5
if x == 5:
    print("Cinco")

# ❌ Incorrecto
x=5
if x==5:
    print("Cinco")
```

## 🧪 Ejercicio Práctico

Mejora este código aplicando las buenas prácticas:

```python
x=int(input("nota: "))
if x>=0 and x<=10:
    if x>=9:
        print("excelente")
    else:
        if x>=7:
            print("bien")
        else:
            if x>=6:
                print("aprobado")
            else:
                print("reprobado")
else:
    print("nota invalida")
```

<details>
<summary>Ver solución mejorada</summary>

```python
"""
Sistema de calificación de notas.
Rango válido: 0-10
"""

# Constantes
NOTA_MINIMA = 0
NOTA_MAXIMA = 10
NOTA_APROBADO = 6
NOTA_BIEN = 7
NOTA_EXCELENTE = 9

# Entrada
nota = float(input("Ingresa tu nota (0-10): "))

# Validación
if nota < NOTA_MINIMA or nota > NOTA_MAXIMA:
    print("❌ Nota inválida. Debe estar entre 0 y 10")
elif nota >= NOTA_EXCELENTE:
    print("🌟 Excelente")
elif nota >= NOTA_BIEN:
    print("👍 Bien")
elif nota >= NOTA_APROBADO:
    print("✅ Aprobado")
else:
    print("❌ Reprobado")
```
</details>

## 📝 Checklist de Código Limpio

Antes de entregar tu código, verifica:

- [ ] ¿Los nombres de variables son descriptivos?
- [ ] ¿Evité números mágicos?
- [ ] ¿Las condiciones son simples y legibles?
- [ ] ¿Hay máximo 2-3 niveles de anidación?
- [ ] ¿Usé `elif` en lugar de múltiples `if`?
- [ ] ¿Los comentarios explican el "por qué"?
- [ ] ¿Hay espacios alrededor de operadores?
- [ ] ¿Evité comparar con `True`/`False`?
- [ ] ¿El estilo es consistente?
- [ ] ¿El código es fácil de leer para otra persona?

## 🎯 Principios Fundamentales

### 1. KISS (Keep It Simple, Stupid)
> "Mantenlo simple"

```python
# Simple y directo
if 18 <= edad <= 65:
    print("Edad laboral")
```

### 2. DRY (Don't Repeat Yourself)
> "No te repitas"

```python
# ❌ Malo
if opcion == "1":
    print("Opción seleccionada: 1")
if opcion == "2":
    print("Opción seleccionada: 2")

# ✅ Bueno
print(f"Opción seleccionada: {opcion}")
```

### 3. YAGNI (You Aren't Gonna Need It)
> "No lo necesitas (aún)"

No agregues funcionalidad que "tal vez" necesites después. Mantenlo simple.

## 📚 Recursos Adicionales

- [PEP 8 - Guía de estilo oficial](https://pep8.org/)
- [Clean Code en Python](https://realpython.com/python-code-quality/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)

## 📝 Resumen

1. **Nombres descriptivos** - El código se documenta solo
2. **Sin números mágicos** - Usa constantes
3. **Condiciones simples** - Legibilidad primero
4. **Poca anidación** - Máximo 2-3 niveles
5. **Comparaciones positivas** - Más naturales
6. **elif sobre if múltiples** - Para opciones excluyentes
7. **Comenta el "por qué"** - No el "qué"
8. **Espacios consistentes** - PEP 8
9. **Sin comparar booleanos** - Ya son True/False
10. **Consistencia** - Mismo estilo siempre

---

¡Felicidades! Has completado la teoría de Estructuras de Decisión. 🎉

## 🔜 Siguiente Paso

Ahora practica con los ejemplos de código y luego resuelve los ejercicios.

[← Anterior: 04 - Operadores Lógicos](./04_operadores_logicos.md) | [Ir a Ejemplos →](./ejemplos/)


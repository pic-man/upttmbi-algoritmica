# 📖 01 - Introducción a las Estructuras de Decisión

## ¿Qué son las Estructuras de Decisión?

Las **estructuras de decisión** son instrucciones que permiten que un programa tome diferentes caminos según ciertas condiciones. Es como cuando tú decides qué hacer basándote en una situación:

> "Si tengo hambre, como. Si no, sigo trabajando."

En programación, estas decisiones se toman con las palabras clave: `if`, `elif` y `else`.

## 🤔 ¿Por qué las necesitamos?

Imagina que quieres crear un programa que determine si una persona puede votar. La regla es simple:

- Si tiene 18 años o más → Puede votar
- Si tiene menos de 18 → No puede votar

Sin estructuras de decisión, tu programa solo podría seguir una secuencia lineal. ¡No podría adaptarse a diferentes situaciones!

## 📊 Diagrama de Flujo

```
       ┌─────────────┐
       │   Inicio    │
       └──────┬──────┘
              │
              ▼
       ┌─────────────┐
       │ edad >= 18? │
       └──────┬──────┘
              │
         ┌────┴────┐
         │         │
        Sí        No
         │         │
         ▼         ▼
   ┌─────────┐ ┌─────────┐
   │ "Puedes │ │"No puedes│
   │  votar" │ │ votar"  │
   └────┬────┘ └────┬────┘
        │           │
        └─────┬─────┘
              ▼
       ┌─────────────┐
       │     Fin     │
       └─────────────┘
```

## 💻 Tu Primer Ejemplo

```python
edad = 20

if edad >= 18:
    print("Puedes votar")
else:
    print("No puedes votar")
```

### ¿Qué hace este código?

1. **Línea 1**: Define una variable `edad` con el valor 20
2. **Línea 3**: Evalúa si `edad >= 18` (¿es 20 mayor o igual a 18?)
3. Como es **verdadero**, ejecuta la línea 4
4. Imprime: `Puedes votar`

### Probemos con otro valor:

```python
edad = 15

if edad >= 18:
    print("Puedes votar")
else:
    print("No puedes votar")
```

Ahora, como 15 < 18, la condición es **falsa**, por lo que se ejecuta el bloque `else` y imprime: `No puedes votar`

## 🔑 Conceptos Clave

### 1. Condición

Es una expresión que se evalúa como **verdadera** (`True`) o **falsa** (`False`).

```python
edad >= 18  # Esta es una condición
```

### 2. Indentación

En Python, los bloques de código se definen por su **indentación** (espacios al inicio):

```python
if edad >= 18:
    print("Esto está dentro del if")
    print("Esto también")
print("Esto está fuera del if")
```

⚠️ **Importante**: Python usa **4 espacios** como estándar.

### 3. Booleanos

Las condiciones se evalúan como valores booleanos:
- `True` (Verdadero)
- `False` (Falso)

```python
print(20 >= 18)  # True
print(15 >= 18)  # False
```

## 🎯 Analogías del Mundo Real

### 1. Semáforo
```
Si la luz es verde → Avanza
Si la luz es amarilla → Precaución
Si la luz es roja → Detente
```

### 2. Acceso a una discoteca
```
Si edad >= 18 → Pasa
Si no → No puedes entrar
```

### 3. Calificación
```
Si nota >= 6 → Aprobado
Si no → Reprobado
```

## ✅ Ejercicio Rápido

Antes de continuar, intenta predecir qué imprimirá este código:

```python
temperatura = 30

if temperatura > 25:
    print("Hace calor")
else:
    print("Hace frío")
```

<details>
<summary>Ver respuesta</summary>

Imprimirá: `Hace calor`

Porque 30 > 25 es verdadero.
</details>

## 📝 Para Recordar

1. Las estructuras de decisión permiten que el programa elija qué hacer
2. `if` evalúa una condición
3. Si la condición es verdadera, ejecuta un bloque de código
4. Si es falsa, puede ejecutar otro bloque con `else`
5. La indentación es **fundamental** en Python

## 🔜 Siguiente Paso

Ahora que entiendes el concepto básico, aprenderás la sintaxis completa de `if`, `else` y `elif` en el siguiente archivo.

[Ir a: 02 - If, Else, Elif →](./02_if_else_elif.md)

---

**💡 Consejo**: Si algo no queda claro, relee esta sección. Los conceptos básicos son la base de todo lo demás.


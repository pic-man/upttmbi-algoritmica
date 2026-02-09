# 📖 06 - Las Variables

## ¿Qué es una Variable?

Una **variable** es un espacio en memoria que almacena un valor y puede cambiar durante la ejecución del programa.

```
┌─────────────────────────────────────────────────────────────┐
│                    MEMORIA                                   │
│  ┌─────────────┐                                            │
│  │   edad      │ ← identificador (nombre)                   │
│  │  ┌───────┐  │                                            │
│  │  │  25   │  │ ← valor almacenado                         │
│  │  └───────┘  │                                            │
│  │   int       │ ← tipo de dato                             │
│  └─────────────┘                                            │
└─────────────────────────────────────────────────────────────┘
```

## Declaración y Asignación

En Python, las variables se crean al asignarles un valor:

```python
# Declaración implícita y asignación
nombre = "Juan"       # Variable de tipo str
edad = 25             # Variable de tipo int
altura = 1.75         # Variable de tipo float
activo = True         # Variable de tipo bool

# Reasignación (el valor puede cambiar)
edad = 26             # Ahora edad vale 26
edad = edad + 1       # Ahora edad vale 27
```

## Clasificación de Variables

### Por su Contenido

```
┌─────────────────────────────────────────────────────────────┐
│            CLASIFICACIÓN POR CONTENIDO                       │
├─────────────────┬─────────────────┬─────────────────────────┤
│   NUMÉRICAS     │    LÓGICAS      │    ALFANUMÉRICAS        │
│                 │                 │                         │
│ Almacenan       │ Almacenan       │ Almacenan               │
│ números         │ True/False      │ texto                   │
│                 │                 │                         │
│ edad = 25       │ activo = True   │ nombre = "Juan"         │
│ precio = 19.99  │ valido = False  │ codigo = "A123"         │
└─────────────────┴─────────────────┴─────────────────────────┘
```

### Por su Uso

```
┌─────────────────────────────────────────────────────────────┐
│               CLASIFICACIÓN POR USO                          │
├─────────────────┬─────────────────┬─────────────────────────┤
│  DE TRABAJO     │   CONTADOR      │    ACUMULADOR           │
│                 │                 │                         │
│ Almacenan       │ Cuentan         │ Suman valores           │
│ resultados      │ repeticiones    │ progresivamente         │
│ intermedios     │                 │                         │
│                 │                 │                         │
│ temp = a        │ contador = 0    │ suma = 0                │
│ a = b           │ contador += 1   │ suma += valor           │
│ b = temp        │                 │                         │
└─────────────────┴─────────────────┴─────────────────────────┘
```

## 1. Variables de Trabajo

Almacenan valores temporales o resultados intermedios.

```python
# Intercambio de valores (usando variable de trabajo)
a = 5
b = 10

temp = a    # Variable de trabajo
a = b
b = temp

print(a, b)  # 10, 5

# Cálculos intermedios
precio = 100
descuento = precio * 0.15      # Variable de trabajo
precio_final = precio - descuento
```

## 2. Variables Contador

Cuentan el número de veces que ocurre algo.

### Características:
- Se **inicializan en cero** (generalmente)
- Se **incrementan en uno** (o valor fijo) en cada iteración

```python
# Contar números pares del 1 al 10
contador_pares = 0  # Inicialización

for numero in range(1, 11):
    if numero % 2 == 0:
        contador_pares += 1  # Incremento en 1

print(f"Hay {contador_pares} números pares")  # 5

# Contar intentos
intentos = 0
max_intentos = 3

while intentos < max_intentos:
    respuesta = input("Ingrese contraseña: ")
    intentos += 1
    if respuesta == "secreta":
        print("Acceso concedido")
        break
```

## 3. Variables Acumulador

Suman o acumulan valores progresivamente.

### Características:
- Se **inicializan en cero** (para sumas) o **uno** (para productos)
- Se les **suma o multiplica** un valor en cada iteración

```python
# Sumar números del 1 al 10
suma = 0  # Inicialización para suma

for numero in range(1, 11):
    suma += numero  # Acumular

print(f"La suma es: {suma}")  # 55

# Calcular promedio
notas = [85, 90, 78, 92, 88]
suma_notas = 0

for nota in notas:
    suma_notas += nota

promedio = suma_notas / len(notas)
print(f"Promedio: {promedio}")  # 86.6

# Calcular factorial (acumulador multiplicativo)
n = 5
factorial = 1  # Inicialización para producto

for i in range(1, n + 1):
    factorial *= i  # Acumular multiplicando

print(f"{n}! = {factorial}")  # 120
```

## Ejemplo Completo

```python
"""
Programa: Estadísticas de Calificaciones
Demuestra los tres tipos de variables por uso
"""

# Lista de calificaciones
calificaciones = [85, 92, 78, 65, 90, 55, 88, 72, 95, 60]

# Variables
suma_total = 0          # ACUMULADOR: para calcular promedio
contador_aprobados = 0  # CONTADOR: estudiantes aprobados
contador_reprobados = 0 # CONTADOR: estudiantes reprobados
nota_maxima = 0         # TRABAJO: almacenar máximo temporal
nota_minima = 100       # TRABAJO: almacenar mínimo temporal

# Procesar calificaciones
for nota in calificaciones:
    # Acumular para el promedio
    suma_total += nota
    
    # Contar aprobados/reprobados
    if nota >= 60:
        contador_aprobados += 1
    else:
        contador_reprobados += 1
    
    # Encontrar máximo y mínimo (variables de trabajo)
    if nota > nota_maxima:
        nota_maxima = nota
    if nota < nota_minima:
        nota_minima = nota

# Calcular promedio
promedio = suma_total / len(calificaciones)

# Mostrar resultados
print("=== ESTADÍSTICAS ===")
print(f"Total estudiantes: {len(calificaciones)}")
print(f"Aprobados: {contador_aprobados}")
print(f"Reprobados: {contador_reprobados}")
print(f"Nota máxima: {nota_maxima}")
print(f"Nota mínima: {nota_minima}")
print(f"Promedio: {promedio:.2f}")
```

## Alcance de Variables

```python
# Variable global
mensaje_global = "Hola"

def mi_funcion():
    # Variable local (solo existe dentro de la función)
    mensaje_local = "Mundo"
    print(mensaje_global)  # Puede acceder a global
    print(mensaje_local)   # Puede acceder a local

mi_funcion()
# print(mensaje_local)  # ERROR: no existe fuera de la función
```

## 📝 Para Recordar

1. Las **variables** almacenan valores que pueden cambiar
2. **Por contenido**: numéricas, lógicas, alfanuméricas
3. **Por uso**: trabajo, contador, acumulador
4. Los **contadores** se inicializan en 0 y se incrementan en 1
5. Los **acumuladores** suman (inicio 0) o multiplican (inicio 1)

## ✅ Ejercicio Rápido

Identifica el tipo de variable por uso:

```python
total = 0
for precio in [10, 20, 30]:
    total += precio

intentos = 0
while intentos < 3:
    intentos += 1

aux = x
x = y
y = aux
```

<details>
<summary>Ver respuesta</summary>

```python
# ACUMULADOR: suma valores progresivamente
total = 0
for precio in [10, 20, 30]:
    total += precio

# CONTADOR: cuenta repeticiones
intentos = 0
while intentos < 3:
    intentos += 1

# VARIABLE DE TRABAJO: almacena valor temporal para intercambio
aux = x
x = y
y = aux
```
</details>

## 🔜 Siguiente Paso

Ahora aprenderás sobre las constantes.

[Ir a: 07 - Constantes →](./07_constantes.md)

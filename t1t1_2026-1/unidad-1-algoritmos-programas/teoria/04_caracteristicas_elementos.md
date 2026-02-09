# 📖 04 - Características y Elementos para Construir un Algoritmo

## Características de un Buen Algoritmo

Para que un algoritmo sea válido y útil, debe cumplir con ciertas características fundamentales:

### 1. Precisión (Exactitud)

Cada paso debe estar **claramente definido**, sin ambigüedades ni confusiones.

❌ **Mal ejemplo** (ambiguo):
```
Agregar un poco de sal
```

✅ **Buen ejemplo** (preciso):
```
Agregar 5 gramos de sal
```

### 2. Definido (Determinístico)

Dado el mismo conjunto de entradas, el algoritmo siempre debe producir el **mismo resultado**.

```
Entrada: 5, 3
Proceso: Sumar
Salida: 8  ← Siempre será 8
```

### 3. Finito

El algoritmo debe **terminar** después de un número finito de pasos. No puede ejecutarse indefinidamente.

❌ **Mal ejemplo** (infinito):
```
1. Sumar 1 al contador
2. Ir al paso 1
```

✅ **Buen ejemplo** (finito):
```
1. Iniciar contador en 0
2. Mientras contador < 10:
   2.1. Sumar 1 al contador
3. Mostrar contador
```

### 4. Tiene Entrada

El algoritmo puede recibir **cero o más** datos de entrada que utiliza para realizar sus operaciones.

### 5. Tiene Salida

El algoritmo debe producir **al menos un resultado**. Si no produce salida, no resuelve ningún problema.

### 6. Efectividad

Cada paso debe ser **suficientemente básico** para poder ejecutarse en un tiempo finito.

❌ **Mal ejemplo** (no efectivo):
```
Calcular todos los números primos
```

✅ **Buen ejemplo** (efectivo):
```
Calcular los números primos del 1 al 100
```

## Resumen de Características

| Característica | Descripción | Pregunta de Verificación |
|----------------|-------------|--------------------------|
| Precisión | Pasos claros y exactos | ¿Cada paso es claro? |
| Definido | Mismo resultado siempre | ¿El resultado es predecible? |
| Finito | Tiene fin | ¿Termina eventualmente? |
| Entrada | Datos que recibe | ¿Qué datos necesita? |
| Salida | Resultados que produce | ¿Qué produce? |
| Efectividad | Pasos ejecutables | ¿Se puede hacer cada paso? |

## Elementos para Construir un Algoritmo

### 1. Variables

Espacios de memoria que almacenan datos que pueden cambiar durante la ejecución.

```python
edad = 25           # Variable numérica
nombre = "María"    # Variable de texto
activo = True       # Variable lógica
```

### 2. Constantes

Valores que no cambian durante la ejecución del algoritmo.

```python
PI = 3.14159
IVA = 0.16
DIAS_SEMANA = 7
```

### 3. Operadores

Símbolos que realizan operaciones sobre los datos.

#### Operadores Aritméticos
| Operador | Operación | Ejemplo |
|----------|-----------|---------|
| `+` | Suma | `5 + 3 = 8` |
| `-` | Resta | `5 - 3 = 2` |
| `*` | Multiplicación | `5 * 3 = 15` |
| `/` | División | `6 / 3 = 2` |
| `%` | Módulo (residuo) | `7 % 3 = 1` |

#### Operadores de Comparación
| Operador | Significado | Ejemplo |
|----------|-------------|---------|
| `==` | Igual a | `5 == 5` → True |
| `!=` | Diferente de | `5 != 3` → True |
| `>` | Mayor que | `5 > 3` → True |
| `<` | Menor que | `5 < 3` → False |
| `>=` | Mayor o igual | `5 >= 5` → True |
| `<=` | Menor o igual | `3 <= 5` → True |

#### Operadores Lógicos
| Operador | Significado | Ejemplo |
|----------|-------------|---------|
| `and` / `Y` | Y lógico | `True and False` → False |
| `or` / `O` | O lógico | `True or False` → True |
| `not` / `NO` | Negación | `not True` → False |

### 4. Expresiones

Combinación de variables, constantes y operadores que producen un valor.

```python
# Expresiones aritméticas
area = base * altura
promedio = (nota1 + nota2 + nota3) / 3

# Expresiones lógicas
es_mayor = edad >= 18
puede_entrar = tiene_boleto and es_mayor
```

### 5. Instrucciones

Son las órdenes que el algoritmo debe ejecutar:

- **Asignación**: Almacenar un valor en una variable
- **Entrada**: Leer datos
- **Salida**: Mostrar resultados
- **Decisión**: Elegir entre opciones
- **Repetición**: Ejecutar pasos múltiples veces

## Ejemplo: Aplicando los Elementos

**Problema**: Calcular el área de un círculo

```
ALGORITMO CalcularAreaCirculo
    CONSTANTES
        PI = 3.14159
    
    VARIABLES
        radio: REAL
        area: REAL
    
    INICIO
        // Entrada
        ESCRIBIR "Ingrese el radio del círculo:"
        LEER radio
        
        // Proceso (usando operadores y expresión)
        area ← PI * radio * radio
        
        // Salida
        ESCRIBIR "El área del círculo es:", area
    FIN
FIN ALGORITMO
```

```python
# Constante
PI = 3.14159

# Entrada
radio = float(input("Ingrese el radio del círculo: "))

# Proceso (expresión aritmética)
area = PI * radio * radio

# Salida
print(f"El área del círculo es: {area}")
```

## Diagrama de Elementos

```
┌─────────────────────────────────────────────────────────────┐
│                    ALGORITMO                                 │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  DATOS                                                │   │
│  │  ├── Variables (cambian)                              │   │
│  │  └── Constantes (no cambian)                          │   │
│  └──────────────────────────────────────────────────────┘   │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  OPERACIONES                                          │   │
│  │  ├── Operadores (+, -, *, /, ==, >, and, or...)      │   │
│  │  └── Expresiones (combinaciones)                      │   │
│  └──────────────────────────────────────────────────────┘   │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  INSTRUCCIONES                                        │   │
│  │  ├── Entrada (LEER)                                   │   │
│  │  ├── Salida (ESCRIBIR)                                │   │
│  │  ├── Asignación (←)                                   │   │
│  │  ├── Decisión (SI-ENTONCES-SINO)                      │   │
│  │  └── Repetición (MIENTRAS, PARA)                      │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

## 📝 Para Recordar

1. Un buen algoritmo debe ser: **preciso, definido, finito, efectivo**
2. Los **elementos básicos** son: variables, constantes, operadores, expresiones e instrucciones
3. Las **expresiones** combinan datos y operadores para producir valores
4. Las **instrucciones** son las acciones que ejecuta el algoritmo

## ✅ Ejercicio Rápido

¿Cuál de estos algoritmos cumple con todas las características?

**A)**
```
1. Leer un número
2. Multiplicar por algo
3. Mostrar resultado
```

**B)**
```
1. Leer un número N
2. Calcular cuadrado = N * N
3. Mostrar cuadrado
```

<details>
<summary>Ver respuesta</summary>

**B es correcto** porque:
- ✅ Es preciso (cada paso está bien definido)
- ✅ Es definido (siempre produce el mismo resultado para N)
- ✅ Es finito (tiene 3 pasos y termina)
- ✅ Tiene entrada (el número N)
- ✅ Tiene salida (el cuadrado)

**A tiene problemas** porque:
- ❌ "Multiplicar por algo" no es preciso
</details>

## 🔜 Siguiente Paso

Ahora aprenderás las diferentes formas de representar un algoritmo.

[Ir a: 05 - Formas de Representación →](./05_formas_representacion.md)

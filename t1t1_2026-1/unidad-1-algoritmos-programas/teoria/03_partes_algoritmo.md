# 📖 03 - Partes de un Algoritmo

## Las Tres Partes Fundamentales

Todo algoritmo se compone de tres partes esenciales:

```
┌─────────────────────────────────────────────────────────────┐
│                        ALGORITMO                             │
├─────────────────┬─────────────────┬─────────────────────────┤
│     ENTRADA     │     PROCESO     │         SALIDA          │
│                 │                 │                         │
│ Datos que       │ Operaciones y   │ Resultados que          │
│ recibe el       │ transformaciones│ produce el              │
│ algoritmo       │ de los datos    │ algoritmo               │
└─────────────────┴─────────────────┴─────────────────────────┘
```

## 1. ENTRADA (Input)

La **entrada** son los datos que el algoritmo necesita para funcionar. Estos datos pueden provenir de:

- El usuario (teclado)
- Un archivo
- Una base de datos
- Sensores
- Otros programas

### Características de la Entrada

- Define **qué datos** necesita el algoritmo
- Especifica el **tipo de dato** (número, texto, etc.)
- Puede haber **cero o más** entradas
- Debe estar claramente **definida**

### Ejemplo de Entradas

| Problema | Entradas |
|----------|----------|
| Calcular área de un círculo | Radio |
| Sumar dos números | Número 1, Número 2 |
| Calcular promedio de notas | Nota 1, Nota 2, Nota 3 |
| Saludar a una persona | Nombre de la persona |

## 2. PROCESO

El **proceso** es el conjunto de operaciones que transforman los datos de entrada en los resultados deseados.

### Tipos de Operaciones en el Proceso

1. **Operaciones aritméticas**: suma, resta, multiplicación, división
2. **Operaciones de comparación**: mayor que, menor que, igual a
3. **Operaciones lógicas**: Y, O, NO
4. **Asignaciones**: almacenar valores en variables
5. **Estructuras de control**: decisiones y repeticiones

### Ejemplo de Procesos

```
Problema: Calcular el precio final con descuento

PROCESO:
1. Calcular el monto del descuento
   descuento ← precio * (porcentaje / 100)
   
2. Calcular el precio final
   precio_final ← precio - descuento
```

## 3. SALIDA (Output)

La **salida** es el resultado que produce el algoritmo después de procesar los datos de entrada.

### Formas de Salida

- Pantalla (texto, gráficos)
- Archivos
- Impresora
- Base de datos
- Otros dispositivos

### Características de la Salida

- Representa la **solución** al problema
- Debe ser **clara** y **comprensible**
- Puede haber **una o más** salidas
- Debe **corresponder** con lo que se esperaba resolver

## Ejemplo Completo: Calcular Promedio

### Planteamiento del Problema

**Problema**: Calcular el promedio de tres calificaciones de un estudiante.

### Identificación de las Partes

```
┌─────────────────────────────────────────────────────────────┐
│               ALGORITMO: Calcular Promedio                  │
├─────────────────────────────────────────────────────────────┤
│ ENTRADA:                                                    │
│   - Calificación 1 (número)                                 │
│   - Calificación 2 (número)                                 │
│   - Calificación 3 (número)                                 │
├─────────────────────────────────────────────────────────────┤
│ PROCESO:                                                    │
│   1. Sumar las tres calificaciones                          │
│   2. Dividir la suma entre 3                                │
├─────────────────────────────────────────────────────────────┤
│ SALIDA:                                                     │
│   - Promedio de las calificaciones                          │
└─────────────────────────────────────────────────────────────┘
```

### Pseudocódigo

```
ALGORITMO CalcularPromedio
    INICIO
        // ENTRADA
        ESCRIBIR "Ingrese la primera calificación:"
        LEER cal1
        ESCRIBIR "Ingrese la segunda calificación:"
        LEER cal2
        ESCRIBIR "Ingrese la tercera calificación:"
        LEER cal3
        
        // PROCESO
        suma ← cal1 + cal2 + cal3
        promedio ← suma / 3
        
        // SALIDA
        ESCRIBIR "El promedio es:", promedio
    FIN
FIN ALGORITMO
```

### Código en Python

```python
# ENTRADA
cal1 = float(input("Ingrese la primera calificación: "))
cal2 = float(input("Ingrese la segunda calificación: "))
cal3 = float(input("Ingrese la tercera calificación: "))

# PROCESO
suma = cal1 + cal2 + cal3
promedio = suma / 3

# SALIDA
print(f"El promedio es: {promedio}")
```

## Diagrama de las Partes

```
        ┌─────────┐
        │ INICIO  │
        └────┬────┘
             │
             ▼
    ┌────────────────┐
    │    ENTRADA     │ ◄── Datos del usuario
    │  (Leer datos)  │
    └────────┬───────┘
             │
             ▼
    ┌────────────────┐
    │    PROCESO     │ ◄── Cálculos y operaciones
    │  (Calcular)    │
    └────────┬───────┘
             │
             ▼
    ┌────────────────┐
    │    SALIDA      │ ◄── Mostrar resultados
    │  (Mostrar)     │
    └────────┬───────┘
             │
             ▼
        ┌─────────┐
        │   FIN   │
        └─────────┘
```

## 📝 Para Recordar

| Parte | Pregunta Clave | Verbos Comunes |
|-------|----------------|----------------|
| ENTRADA | ¿Qué datos necesito? | Leer, Solicitar, Obtener |
| PROCESO | ¿Qué debo hacer con los datos? | Calcular, Comparar, Asignar |
| SALIDA | ¿Qué resultado debo mostrar? | Escribir, Mostrar, Imprimir |

## ✅ Ejercicio Rápido

Identifica las partes (Entrada, Proceso, Salida) del siguiente problema:

**"Convertir una temperatura de grados Celsius a Fahrenheit"**

<details>
<summary>Ver respuesta</summary>

**ENTRADA:**
- Temperatura en grados Celsius

**PROCESO:**
- Aplicar la fórmula: F = (C × 9/5) + 32

**SALIDA:**
- Temperatura en grados Fahrenheit

```python
# Entrada
celsius = float(input("Ingrese temperatura en Celsius: "))

# Proceso
fahrenheit = (celsius * 9/5) + 32

# Salida
print(f"{celsius}°C equivale a {fahrenheit}°F")
```
</details>

## 🔜 Siguiente Paso

Ahora aprenderás las características y elementos necesarios para construir un algoritmo.

[Ir a: 04 - Características y Elementos →](./04_caracteristicas_elementos.md)

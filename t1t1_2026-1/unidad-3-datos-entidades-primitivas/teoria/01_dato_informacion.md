# 📖 01 - Concepto y Diferencia entre Dato e Información

## ¿Qué es un Dato?

Un **dato** es una representación simbólica (numérica, alfabética, etc.) de un atributo o característica de una entidad. Por sí solo, un dato no tiene significado completo.

### Ejemplos de Datos

```
25
"Juan"
3.14159
True
"2025-01-25"
```

Por sí solos, estos valores no nos dicen mucho. ¿25 qué? ¿Años? ¿Kilogramos? ¿Grados?

## ¿Qué es Información?

La **información** es el resultado de procesar, organizar y dar contexto a los datos, convirtiéndolos en algo significativo y útil para la toma de decisiones.

### De Dato a Información

```
┌─────────────────┐         ┌─────────────────┐         ┌─────────────────┐
│      DATO       │  ────▶  │     PROCESO     │  ────▶  │   INFORMACIÓN   │
│       25        │         │   + contexto    │         │  "Edad: 25 años"│
└─────────────────┘         └─────────────────┘         └─────────────────┘
```

### Ejemplos Comparativos

| Dato | Contexto | Información |
|------|----------|-------------|
| 25 | Edad de una persona | "Juan tiene 25 años" |
| 36.5 | Temperatura corporal | "Temperatura normal: 36.5°C" |
| 1500 | Salario mensual | "Salario: $1,500 USD/mes" |
| "A" | Calificación de examen | "Aprobó con A (Excelente)" |

## Diferencias Clave

```
┌─────────────────────────────────────────────────────────────┐
│                    DATO vs INFORMACIÓN                       │
├──────────────────────────┬──────────────────────────────────┤
│          DATO            │          INFORMACIÓN             │
├──────────────────────────┼──────────────────────────────────┤
│ Valor sin procesar       │ Dato procesado y contextualizado │
│ Sin significado propio   │ Con significado y propósito      │
│ Materia prima            │ Producto terminado               │
│ No facilita decisiones   │ Facilita la toma de decisiones   │
│ Ejemplo: 98.6            │ Ejemplo: "Fiebre: 98.6°F"        │
└──────────────────────────┴──────────────────────────────────┘
```

## El Proceso de Transformación

```
   DATOS                    PROCESO                 INFORMACIÓN
┌─────────┐            ┌─────────────┐            ┌─────────────┐
│ 85      │            │             │            │ Promedio:   │
│ 90      │  ────────▶ │  Calcular   │ ────────▶  │ 87.5        │
│ 78      │            │  promedio   │            │ Estado:     │
│ 97      │            │  + evaluar  │            │ Aprobado    │
└─────────┘            └─────────────┘            └─────────────┘
  (notas)                                         (calificación final)
```

## Tipos de Datos en Programación

En programación, los datos se clasifican según el tipo de valor que pueden almacenar:

### Tipos Primitivos

| Tipo | Descripción | Ejemplo en Python |
|------|-------------|-------------------|
| **Entero** (int) | Números sin decimales | `42`, `-7`, `0` |
| **Real** (float) | Números con decimales | `3.14`, `-0.5` |
| **Carácter** (str) | Un solo carácter | `'A'`, `'5'`, `'@'` |
| **Cadena** (str) | Secuencia de caracteres | `"Hola mundo"` |
| **Booleano** (bool) | Verdadero o Falso | `True`, `False` |

### Ejemplo en Python

```python
# Datos de diferentes tipos
edad = 25                    # Entero (int)
altura = 1.75               # Real (float)
inicial = 'J'               # Carácter (str)
nombre = "Juan Pérez"       # Cadena (str)
es_estudiante = True        # Booleano (bool)

# Verificar tipos
print(type(edad))           # <class 'int'>
print(type(altura))         # <class 'float'>
print(type(nombre))         # <class 'str'>
print(type(es_estudiante))  # <class 'bool'>
```

## Importancia de los Datos

### En la Vida Cotidiana

```
Datos del supermercado:
- Leche: $2.50
- Pan: $1.20
- Huevos: $3.00

Información (después del proceso):
- Total de compra: $6.70
- IVA: $1.07
- Total a pagar: $7.77
```

### En Programación

```python
# Datos de entrada
horas_trabajadas = 40
tarifa_por_hora = 15.50

# Proceso
salario_bruto = horas_trabajadas * tarifa_por_hora
impuestos = salario_bruto * 0.15
salario_neto = salario_bruto - impuestos

# Información de salida
print(f"Salario bruto: ${salario_bruto:.2f}")
print(f"Impuestos: ${impuestos:.2f}")
print(f"Salario neto: ${salario_neto:.2f}")
```

## 📝 Para Recordar

1. Un **dato** es un valor sin contexto
2. La **información** es datos procesados con significado
3. Los datos son la **materia prima** de los programas
4. La información es el **resultado** del procesamiento
5. Los tipos de datos definen qué valores pueden almacenarse

## ✅ Ejercicio Rápido

Identifica qué es dato y qué es información:

1. `37.8`
2. "El paciente tiene fiebre: 37.8°C"
3. `"2025-01-25"`
4. "Fecha de nacimiento: 25 de enero de 2025"
5. `[85, 90, 78]`

<details>
<summary>Ver respuesta</summary>

1. **Dato** - Solo un número sin contexto
2. **Información** - Número con significado (temperatura + diagnóstico)
3. **Dato** - Cadena de texto sin contexto
4. **Información** - Fecha con significado claro
5. **Dato** - Lista de números sin explicar qué representan

</details>

## 🔜 Siguiente Paso

Ahora aprenderás sobre los tipos de datos en detalle.

[Ir a: 02 - Tipos de Datos →](./02_tipos_datos.md)

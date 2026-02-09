# 📖 02 - Forma de Trazabilizar un Algoritmo

## ¿Qué es la Trazabilidad?

La **trazabilidad** es la capacidad de seguir el recorrido de un algoritmo paso a paso, desde sus entradas hasta sus salidas, documentando cada transformación de datos.

```
┌─────────┐     ┌─────────┐     ┌─────────┐     ┌─────────┐
│ Entrada │ ──▶ │ Paso 1  │ ──▶ │ Paso 2  │ ──▶ │ Salida  │
│         │     │         │     │         │     │         │
│ datos   │     │ trans.  │     │ trans.  │     │ result. │
└─────────┘     └─────────┘     └─────────┘     └─────────┘
     ↓               ↓               ↓               ↓
  [registro]    [registro]      [registro]      [registro]
```

## Importancia de la Trazabilidad

1. **Depuración**: Encontrar dónde ocurren los errores
2. **Verificación**: Confirmar que el algoritmo funciona correctamente
3. **Documentación**: Explicar cómo funciona el algoritmo
4. **Auditoría**: Revisar el proceso en cualquier momento
5. **Aprendizaje**: Entender la lógica del algoritmo

## Métodos de Trazabilidad

### 1. Tabla de Traza Manual

Es el método clásico de seguimiento paso a paso.

```
ALGORITMO Factorial
    VARIABLES
        n, i, fact: ENTERO
    INICIO
        LEER n
        fact ← 1
        PARA i ← 1 HASTA n HACER
            fact ← fact * i
        FIN PARA
        ESCRIBIR fact
    FIN
FIN ALGORITMO
```

**Tabla de Traza** (n = 4):

| Iteración | i | fact | fact * i |
|-----------|---|------|----------|
| Inicio    | - | 1    | -        |
| 1         | 1 | 1    | 1 × 1 = 1 |
| 2         | 2 | 2    | 1 × 2 = 2 |
| 3         | 3 | 6    | 2 × 3 = 6 |
| 4         | 4 | 24   | 6 × 4 = 24 |

**Resultado**: 4! = 24 ✅

### 2. Comentarios de Traza en Código

```python
def factorial(n):
    print(f"INICIO: n = {n}")  # Traza
    
    fact = 1
    print(f"Inicialización: fact = {fact}")  # Traza
    
    for i in range(1, n + 1):
        fact_anterior = fact
        fact = fact * i
        print(f"Iteración {i}: {fact_anterior} × {i} = {fact}")  # Traza
    
    print(f"RESULTADO: {n}! = {fact}")  # Traza
    return fact

# Ejecutar
factorial(4)
```

**Salida**:
```
INICIO: n = 4
Inicialización: fact = 1
Iteración 1: 1 × 1 = 1
Iteración 2: 1 × 2 = 2
Iteración 3: 2 × 3 = 6
Iteración 4: 6 × 4 = 24
RESULTADO: 4! = 24
```

### 3. Logging Estructurado

```python
import logging

# Configurar el logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s - %(message)s'
)

def calcular_descuento(precio, porcentaje):
    logging.info(f"Entrada: precio={precio}, porcentaje={porcentaje}")
    
    descuento = precio * (porcentaje / 100)
    logging.debug(f"Cálculo descuento: {precio} × {porcentaje}/100 = {descuento}")
    
    precio_final = precio - descuento
    logging.debug(f"Cálculo final: {precio} - {descuento} = {precio_final}")
    
    logging.info(f"Salida: precio_final={precio_final}")
    return precio_final
```

## Elementos de una Traza Completa

### 1. Identificación del Algoritmo

```
┌──────────────────────────────────────┐
│ Algoritmo: CalcularPromedio          │
│ Versión: 1.0                         │
│ Fecha: 2025-01-25                    │
│ Autor: Estudiante                    │
└──────────────────────────────────────┘
```

### 2. Datos de Entrada

```
┌──────────────────────────────────────┐
│ ENTRADA                              │
│ nota1 = 8.5                          │
│ nota2 = 7.0                          │
│ nota3 = 9.5                          │
└──────────────────────────────────────┘
```

### 3. Registro de Pasos

```
┌──────────────────────────────────────┐
│ PROCESO                              │
│ Paso 1: suma = 8.5 + 7.0 + 9.5 = 25  │
│ Paso 2: promedio = 25 / 3 = 8.33     │
│ Paso 3: 8.33 >= 6 → Aprobado         │
└──────────────────────────────────────┘
```

### 4. Resultado Final

```
┌──────────────────────────────────────┐
│ SALIDA                               │
│ promedio = 8.33                      │
│ estado = "Aprobado"                  │
└──────────────────────────────────────┘
```

## Plantilla de Documento de Traza

```
═══════════════════════════════════════════════════════════
                    DOCUMENTO DE TRAZA
═══════════════════════════════════════════════════════════

INFORMACIÓN DEL ALGORITMO
─────────────────────────
Nombre: [Nombre del algoritmo]
Propósito: [Qué hace el algoritmo]
Fecha de traza: [Fecha]
Realizado por: [Nombre]

DATOS DE ENTRADA
─────────────────────────
Variable 1: [valor]
Variable 2: [valor]
...

TABLA DE TRAZA
─────────────────────────
| Paso | Instrucción | Var1 | Var2 | ... | Salida |
|------|-------------|------|------|-----|--------|
| 1    |             |      |      |     |        |
| 2    |             |      |      |     |        |
...

RESULTADO
─────────────────────────
Salida esperada: [valor]
Salida obtenida: [valor]
Estado: [ ] Correcto  [ ] Incorrecto

OBSERVACIONES
─────────────────────────
[Notas adicionales sobre la ejecución]

═══════════════════════════════════════════════════════════
```

## Herramientas para Trazabilidad

| Herramienta | Uso |
|-------------|-----|
| Papel y lápiz | Trazas manuales básicas |
| Hojas de cálculo | Tablas de traza organizadas |
| Depurador (debugger) | Seguimiento en tiempo real |
| Logging | Registro automático en código |
| Diagramas de secuencia | Visualización del flujo |

## 📝 Para Recordar

1. La **trazabilidad** permite seguir la ejecución paso a paso
2. Existen varios métodos: **manual, comentarios, logging**
3. Una traza completa incluye: **entrada, proceso, salida**
4. La trazabilidad ayuda a **depurar** y **documentar**
5. Siempre **documenta** tus trazas para referencia futura

## ✅ Ejercicio Rápido

Realiza la traza del siguiente algoritmo con n = 5:

```
ALGORITMO SumaPares
    VARIABLES
        n, i, suma: ENTERO
    INICIO
        LEER n
        suma ← 0
        PARA i ← 2 HASTA n PASO 2 HACER
            suma ← suma + i
        FIN PARA
        ESCRIBIR suma
    FIN
FIN ALGORITMO
```

<details>
<summary>Ver respuesta</summary>

| Paso | Instrucción | n | i | suma | Observación |
|------|-------------|---|---|------|-------------|
| 1 | LEER n | 5 | - | - | Entrada |
| 2 | suma ← 0 | 5 | - | 0 | Inicialización |
| 3 | i ← 2 | 5 | 2 | 0 | Inicio ciclo |
| 4 | suma ← suma + i | 5 | 2 | 2 | 0 + 2 = 2 |
| 5 | i ← 4 | 5 | 4 | 2 | Siguiente par |
| 6 | suma ← suma + i | 5 | 4 | 6 | 2 + 4 = 6 |
| 7 | i ← 6 | 5 | 6 | 6 | 6 > 5, sale del ciclo |
| 8 | ESCRIBIR suma | 5 | 6 | 6 | **Salida: 6** |

**Verificación**: 2 + 4 = 6 ✅
</details>

## 🔜 Siguiente Paso

Ahora aprenderás sobre las técnicas de documentación.

[Ir a: 03 - Documentación →](./03_documentacion.md)

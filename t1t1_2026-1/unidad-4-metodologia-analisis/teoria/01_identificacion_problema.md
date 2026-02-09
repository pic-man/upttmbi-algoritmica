# 📖 01 - Identificación del Problema

## ¿Qué es Identificar un Problema?

**Identificar el problema** es el primer y más importante paso en el desarrollo de algoritmos. Consiste en comprender claramente qué se necesita resolver.

> "Un problema bien definido está medio resuelto."

## Pasos para Identificar un Problema

```
┌─────────────────────────────────────────────────────────────┐
│                IDENTIFICACIÓN DEL PROBLEMA                   │
├─────────────────────────────────────────────────────────────┤
│  1. Leer y comprender el enunciado                          │
│  2. Identificar qué se pide (objetivo)                      │
│  3. Identificar los datos disponibles (entrada)             │
│  4. Identificar el resultado esperado (salida)              │
│  5. Identificar restricciones y condiciones                 │
└─────────────────────────────────────────────────────────────┘
```

## Metodología de Análisis

### 1. Comprender el Enunciado

Lee el problema varias veces hasta entenderlo completamente.

**Ejemplo de enunciado:**
> "Una tienda ofrece un descuento del 15% en compras mayores a $100. Calcular el monto a pagar por una compra."

### 2. Preguntas Clave

| Pregunta | Respuesta |
|----------|-----------|
| ¿Qué se pide calcular? | El monto a pagar |
| ¿Qué datos tengo? | Monto de la compra |
| ¿Hay condiciones? | Descuento si compra > $100 |
| ¿Cuál es el resultado? | Monto final a pagar |

### 3. Análisis Estructurado

```
PROBLEMA: Calcular monto a pagar con descuento

ENTRADA:
  - monto_compra (número real)

PROCESO:
  1. Si monto_compra > 100:
     - Calcular descuento = monto_compra × 0.15
     - monto_pagar = monto_compra - descuento
  2. Si no:
     - monto_pagar = monto_compra

SALIDA:
  - monto_pagar (número real)
```

## Ejemplo Completo

### Problema
> "Una empresa paga a sus empleados por hora. Si trabajan más de 40 horas, las horas extra se pagan al 150% de la tarifa normal. Calcular el salario semanal."

### Análisis

```
┌─────────────────────────────────────────────────────────────┐
│ ANÁLISIS DEL PROBLEMA                                        │
├─────────────────────────────────────────────────────────────┤
│ OBJETIVO:                                                    │
│   Calcular el salario semanal de un empleado                │
├─────────────────────────────────────────────────────────────┤
│ DATOS DE ENTRADA:                                            │
│   - Horas trabajadas (número entero)                        │
│   - Tarifa por hora (número real)                           │
├─────────────────────────────────────────────────────────────┤
│ CONDICIONES:                                                 │
│   - Horas normales: hasta 40 horas                          │
│   - Horas extra: más de 40 horas                            │
│   - Pago extra: 150% de tarifa normal                       │
├─────────────────────────────────────────────────────────────┤
│ SALIDA ESPERADA:                                             │
│   - Salario semanal total (número real)                     │
├─────────────────────────────────────────────────────────────┤
│ FÓRMULAS:                                                    │
│   Si horas ≤ 40:                                            │
│     salario = horas × tarifa                                │
│   Si horas > 40:                                            │
│     salario = (40 × tarifa) + ((horas-40) × tarifa × 1.5)   │
└─────────────────────────────────────────────────────────────┘
```

## Errores Comunes

| Error | Consecuencia | Solución |
|-------|--------------|----------|
| No leer completo | Ignorar condiciones | Leer varias veces |
| Asumir datos | Programa incompleto | Preguntar/verificar |
| Ignorar casos especiales | Errores en ejecución | Analizar límites |

## Plantilla de Análisis

```
═══════════════════════════════════════════════════════════
            ANÁLISIS DEL PROBLEMA
═══════════════════════════════════════════════════════════

ENUNCIADO:
[Copiar el problema aquí]

OBJETIVO:
[¿Qué debe hacer el programa?]

ENTRADA (Datos necesarios):
- [dato 1]: [tipo] - [descripción]
- [dato 2]: [tipo] - [descripción]

PROCESO (Operaciones):
1. [Paso 1]
2. [Paso 2]
3. [Paso 3]

SALIDA (Resultados):
- [resultado 1]: [tipo] - [descripción]

RESTRICCIONES/CONDICIONES:
- [condición 1]
- [condición 2]

CASOS DE PRUEBA:
- Entrada: [...] → Salida esperada: [...]
═══════════════════════════════════════════════════════════
```

## 📝 Para Recordar

1. **Leer** el problema varias veces
2. **Identificar** entrada, proceso y salida
3. **Detectar** condiciones y restricciones
4. **Verificar** con casos de prueba
5. **Documentar** el análisis antes de programar

## 🔜 Siguiente Paso

[Ir a: 02 - Datos de Entrada →](./02_datos_entrada.md)

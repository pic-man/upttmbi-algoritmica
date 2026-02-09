# 📖 03 - Identificación de los Datos de Salida

## ¿Qué son los Datos de Salida?

Los **datos de salida** son los resultados que produce el algoritmo después de procesar los datos de entrada. Representan la solución al problema planteado.

## Preguntas para Identificar Salidas

1. **¿Qué resultado se espera?**
2. **¿En qué formato debe presentarse?**
3. **¿Cuántos resultados hay?**
4. **¿Dónde se muestran los resultados?**

## Tipos de Salida

| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| **Valor calculado** | Resultado de operaciones | Promedio: 85.5 |
| **Mensaje** | Texto informativo | "Aprobado" |
| **Estado** | Condición resultante | True/False |
| **Lista** | Múltiples valores | [2, 4, 6, 8, 10] |

## Ejemplos de Identificación

### Ejemplo 1: Calculadora de promedio

```
SALIDAS IDENTIFICADAS:
┌─────────────────────────────────────────────┐
│ - promedio: número real                     │
│   Formato: 2 decimales                      │
│   Ejemplo: "El promedio es: 85.50"          │
│                                             │
│ - estado: texto                             │
│   Valores posibles: "Aprobado"/"Reprobado"  │
└─────────────────────────────────────────────┘
```

### Ejemplo 2: Calculadora de nómina

```
SALIDAS IDENTIFICADAS:
┌─────────────────────────────────────────────┐
│ - salario_normal: real (2 decimales)        │
│ - pago_extras: real (2 decimales)           │
│ - deducciones: real (2 decimales)           │
│ - salario_neto: real (2 decimales)          │
│                                             │
│ Formato de presentación:                    │
│   Salario normal:  $800.00                  │
│   Horas extra:     $150.00                  │
│   Deducciones:     -$95.00                  │
│   ─────────────────────────                 │
│   TOTAL A PAGAR:   $855.00                  │
└─────────────────────────────────────────────┘
```

## Formato de Salida

```python
# Ejemplos de formato de salida

# Números con decimales fijos
precio = 19.5
print(f"Precio: ${precio:.2f}")  # Precio: $19.50

# Alineación
print(f"{'Concepto':<20}{'Monto':>10}")
print(f"{'Subtotal':<20}{'$100.00':>10}")
print(f"{'IVA':<20}{'$16.00':>10}")

# Separadores
print("=" * 30)
print(f"{'TOTAL':<20}{'$116.00':>10}")
```

## Documentación de Salidas

```
┌─────────────────────────────────────────────────────────────┐
│ ESPECIFICACIÓN DE SALIDA                                     │
├──────────────┬──────────┬───────────────────────────────────┤
│ Variable     │   Tipo   │ Descripción                       │
├──────────────┼──────────┼───────────────────────────────────┤
│ promedio     │ float    │ Promedio de notas (2 decimales)   │
│ estado       │ str      │ "Aprobado" o "Reprobado"          │
│ mensaje      │ str      │ Mensaje descriptivo del resultado │
└──────────────┴──────────┴───────────────────────────────────┘
```

## 📝 Para Recordar

1. Identificar **qué resultados** se necesitan
2. Definir el **formato** de presentación
3. Considerar **mensajes** adicionales
4. Especificar **precisión** en números
5. Diseñar una **presentación clara**

## 🔜 Siguiente Paso

[Ir a: 04 - Operaciones y Cálculos →](./04_operaciones_calculos.md)

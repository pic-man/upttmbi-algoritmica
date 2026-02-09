# 📖 04 - Descripción de las Operaciones y Cálculos

## ¿Qué son las Operaciones?

Las **operaciones** son las transformaciones y cálculos que se aplican a los datos de entrada para obtener los resultados deseados.

## Tipos de Operaciones

```
┌─────────────────────────────────────────────────────────────┐
│                    TIPOS DE OPERACIONES                      │
├───────────────┬───────────────┬─────────────────────────────┤
│  ARITMÉTICAS  │    LÓGICAS    │      COMPARACIÓN            │
│               │               │                             │
│ +, -, *, /    │ AND, OR, NOT  │ ==, !=, <, >, <=, >=        │
│ %, //, **     │               │                             │
└───────────────┴───────────────┴─────────────────────────────┘
```

## Identificación de Operaciones

### Paso 1: Analizar qué cálculos se necesitan

**Problema:** Calcular el precio final de un producto con descuento e IVA.

```
Cálculos necesarios:
1. Calcular monto de descuento
2. Calcular precio con descuento
3. Calcular IVA
4. Calcular precio final
```

### Paso 2: Definir las fórmulas

```
FÓRMULAS:
─────────
descuento = precio × (porcentaje_descuento / 100)
precio_con_descuento = precio - descuento
iva = precio_con_descuento × tasa_iva
precio_final = precio_con_descuento + iva
```

### Paso 3: Identificar operaciones lógicas

```
CONDICIONES:
────────────
- Si precio > 1000: aplicar descuento adicional
- Si cliente_vip: no cobrar envío
```

## Ejemplo Completo

### Problema: Sistema de nómina

```
┌─────────────────────────────────────────────────────────────┐
│ OPERACIONES Y CÁLCULOS                                       │
├─────────────────────────────────────────────────────────────┤
│ ENTRADA:                                                     │
│   - horas_trabajadas                                        │
│   - tarifa_hora                                             │
│   - porcentaje_deducciones                                  │
├─────────────────────────────────────────────────────────────┤
│ CÁLCULOS:                                                    │
│                                                             │
│ 1. Calcular pago normal:                                    │
│    SI horas ≤ 40:                                           │
│       pago_normal = horas × tarifa                          │
│    SI NO:                                                   │
│       pago_normal = 40 × tarifa                             │
│                                                             │
│ 2. Calcular pago de horas extra:                            │
│    SI horas > 40:                                           │
│       horas_extra = horas - 40                              │
│       pago_extra = horas_extra × tarifa × 1.5               │
│    SI NO:                                                   │
│       pago_extra = 0                                        │
│                                                             │
│ 3. Calcular salario bruto:                                  │
│    salario_bruto = pago_normal + pago_extra                 │
│                                                             │
│ 4. Calcular deducciones:                                    │
│    deducciones = salario_bruto × (porcentaje / 100)         │
│                                                             │
│ 5. Calcular salario neto:                                   │
│    salario_neto = salario_bruto - deducciones               │
├─────────────────────────────────────────────────────────────┤
│ SALIDA:                                                      │
│   - salario_bruto, deducciones, salario_neto                │
└─────────────────────────────────────────────────────────────┘
```

## Pseudocódigo de las Operaciones

```
ALGORITMO CalcularNomina
    // Cálculo de pago normal
    SI horas_trabajadas <= 40 ENTONCES
        pago_normal ← horas_trabajadas * tarifa_hora
        pago_extra ← 0
    SINO
        pago_normal ← 40 * tarifa_hora
        horas_extra ← horas_trabajadas - 40
        pago_extra ← horas_extra * tarifa_hora * 1.5
    FIN SI
    
    // Cálculo de totales
    salario_bruto ← pago_normal + pago_extra
    deducciones ← salario_bruto * (porcentaje_deducciones / 100)
    salario_neto ← salario_bruto - deducciones
FIN ALGORITMO
```

## 📝 Para Recordar

1. Identificar **todas las operaciones** necesarias
2. Definir **fórmulas** claramente
3. Considerar **condiciones** que afectan los cálculos
4. Ordenar operaciones **lógicamente**
5. Verificar con **casos de prueba**

## 🔜 Siguiente Paso

[Ir a: 05 - Descripción de Procesos →](./05_descripcion_procesos.md)

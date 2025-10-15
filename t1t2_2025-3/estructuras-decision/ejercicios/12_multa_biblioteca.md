# 📚 Ejercicio 12: Multa de Biblioteca

## Dificultad: ⭐⭐ Intermedio

## 📝 Descripción

Crea un programa que calcule la multa por retraso en la devolución de un libro de biblioteca.

## 🎯 Objetivo

Practicar rangos numéricos con cálculos.

## 📋 Especificaciones

El programa debe:

1. Solicitar los días de retraso
2. Calcular la multa según:
   - **0 días**: Sin multa
   - **1 a 5 días**: $5 por día
   - **6 a 10 días**: $10 por día
   - **Más de 10 días**: $15 por día
3. Mostrar el total de la multa

## 💻 Ejemplo de Ejecución

### Ejemplo 1:
```
=== SISTEMA DE MULTAS - BIBLIOTECA ===

¿Cuántos días de retraso tiene el libro? 3

--- RESUMEN ---
Días de retraso: 3
Tarifa: $5 por día
Multa total: $15

Gracias por devolver el libro
```

### Ejemplo 2:
```
=== SISTEMA DE MULTAS - BIBLIOTECA ===

¿Cuántos días de retraso tiene el libro? 8

--- RESUMEN ---
Días de retraso: 8
Tarifa: $10 por día
Multa total: $80

Por favor, paga la multa en recepción
```

### Ejemplo 3:
```
=== SISTEMA DE MULTAS - BIBLIOTECA ===

¿Cuántos días de retraso tiene el libro? 15

--- RESUMEN ---
Días de retraso: 15
Tarifa: $15 por día
Multa total: $225

⚠️ AVISO: Retraso excesivo
La multa es muy alta. Considera renovar tus préstamos a tiempo.
```

### Ejemplo 4:
```
=== SISTEMA DE MULTAS - BIBLIOTECA ===

¿Cuántos días de retraso tiene el libro? 0

✅ ¡Libro devuelto a tiempo!
Sin multa
Gracias por ser un usuario responsable
```

## 🧪 Casos de Prueba

Prueba tu programa con estos valores:

| Días | Tarifa | Multa Total |
|------|--------|-------------|
| 0 | - | $0 |
| 1 | $5 | $5 |
| 5 | $5 | $25 |
| 6 | $10 | $60 |
| 10 | $10 | $100 |
| 11 | $15 | $165 |
| 20 | $15 | $300 |

## 💡 Pistas

1. Estructura de rangos:
   ```python
   if dias == 0:
       multa = 0
   elif dias <= 5:
       multa = dias * 5
   elif dias <= 10:
       multa = dias * 10
   else:
       multa = dias * 15
   ```

2. Para calcular: `multa = dias * tarifa_por_dia`

3. Guarda la tarifa en una variable para mostrarla después

## ⚠️ Errores Comunes

- ❌ No incluir el caso de 0 días (sin multa)
- ❌ Confundir los límites (¿5 días es $5 o $10?)
- ❌ No multiplicar por los días
- ❌ No validar días negativos

## 🎓 Conceptos Practicados

- Rangos numéricos
- Multiplicación de tarifas
- `if-elif-else` con cálculos
- Validación de entrada

## 📊 Tabla de Tarifas

| Rango de Días | Tarifa por Día | Ejemplo (3 días) |
|---------------|----------------|------------------|
| 0 | $0 | $0 |
| 1-5 | $5 | $15 |
| 6-10 | $10 | - |
| 11+ | $15 | - |

## 🚀 Desafíos Extra (Opcional)

1. **Validación**:
   - No aceptar días negativos
   - Advertir si los días son muy altos (> 30)

2. **Descuento por pronto pago**:
   - Si paga hoy: 10% descuento
   - Si paga en 3 días: sin descuento
   - Si paga después: multa adicional

3. **Múltiples libros**:
   - Permite calcular multa de varios libros
   - Suma el total
   - Aplica descuento por pago de múltiples multas

4. **Sistema de membresía**:
   - Básica: tarifas normales
   - Premium: 50% descuento en multas
   - VIP: sin multas por retrasos < 7 días

5. **Historial**:
   - Guarda retrasos anteriores
   - Si es reincidente: multa x2

---

**Tiempo estimado**: 15-20 minutos  
**Archivo de solución**: `ejercicio_12.py`


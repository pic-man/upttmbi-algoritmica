# 🎵 Ejercicio 17: Streaming de Música

## Dificultad: ⭐⭐ Intermedio

## 📝 Descripción

Crea un programa que pida el plan de suscripción a un servicio de streaming de música y muestre sus características y precio.

## 🎯 Objetivo

Practicar comparación de strings con información detallada de planes.

## 📋 Especificaciones

El programa debe:

1. Solicitar el tipo de plan
2. Mostrar información según:
   - **Gratuito**: "Música con anuncios"
   - **Básico**: "Música sin anuncios - $59/mes"
   - **Premium**: "Música sin anuncios + descargas - $99/mes"
   - **Otro**: "Plan no válido"

## 💻 Ejemplo de Ejecución

### Ejemplo 1:
```
=== PLANES DE STREAMING ===

Planes disponibles: gratuito, básico, premium

Elige tu plan: gratuito

🎵 PLAN GRATUITO

Características:
✓ Catálogo completo de música
✓ Calidad estándar (128 kbps)
✗ Anuncios cada 3 canciones
✗ Sin descargas offline
✗ Saltos de canción limitados

Precio: GRATIS
```

### Ejemplo 2:
```
=== PLANES DE STREAMING ===

Planes disponibles: gratuito, básico, premium

Elige tu plan: premium

🎵 PLAN PREMIUM

Características:
✓ Catálogo completo de música
✓ Calidad alta (320 kbps)
✓ Sin anuncios
✓ Descargas ilimitadas offline
✓ Saltos de canción ilimitados
✓ Podcasts exclusivos
✓ Modo offline

Precio: $99/mes
Ahorro anual: $198 (si pagas por año)
```

### Ejemplo 3:
```
=== PLANES DE STREAMING ===

Planes disponibles: gratuito, básico, premium

Elige tu plan: familiar

❌ Plan no válido
Por favor, elige entre: gratuito, básico o premium
```

## 🧪 Casos de Prueba

Prueba tu programa con estos valores:

| Entrada | Resultado |
|---------|-----------|
| gratuito | Música con anuncios |
| Gratuito | Música con anuncios |
| básico | Sin anuncios - $59/mes |
| basico | Sin anuncios - $59/mes |
| premium | Sin anuncios + descargas - $99/mes |
| familiar | Plan no válido |
| estudiante | Plan no válido |

## 💡 Pistas

1. Normaliza la entrada:
   ```python
   plan = input("Plan: ").lower()
   ```

2. Considera variaciones de acentos:
   ```python
   if plan == "basico" or plan == "básico":
       # plan básico
   ```

3. Muestra información estructurada para mejor UX

## 📊 Comparación de Planes

| Característica | Gratuito | Básico | Premium |
|----------------|----------|--------|---------|
| Precio | $0 | $59 | $99 |
| Anuncios | Sí | No | No |
| Calidad | 128 kbps | 192 kbps | 320 kbps |
| Descargas | No | No | Sí |
| Saltos | 6/hora | Ilimitados | Ilimitados |
| Dispositivos | 1 | 1 | 5 |

## ⚠️ Errores Comunes

- ❌ No normalizar a minúsculas
- ❌ No considerar acentos
- ❌ No validar planes incorrectos
- ❌ No mostrar los planes disponibles

## 🎓 Conceptos Practicados

- Comparación de strings
- Normalización de texto
- Múltiples condiciones con `or`
- Presentación de información estructurada

## 🚀 Desafíos Extra (Opcional)

1. **Más planes**:
   - Estudiante: $45/mes (requiere correo .edu)
   - Familiar: $149/mes (hasta 6 usuarios)
   - Duo: $129/mes (2 cuentas)

2. **Recomendador**:
   - Pregunta cuántas personas usarán el servicio
   - Pregunta si necesita descargas offline
   - Pregunta presupuesto máximo
   - Recomienda el mejor plan

3. **Calculadora de ahorro**:
   ```
   Plan Premium: $99/mes
   
   Opciones de pago:
   - Mensual: $99/mes = $1,188/año
   - Trimestral: $270 = $1,080/año (ahorro $108)
   - Anual: $990/año (ahorro $198)
   
   Recomendación: Plan anual (16.7% descuento)
   ```

4. **Comparador interactivo**:
   - Permite seleccionar 2 planes
   - Muestra diferencias lado a lado
   - Calcula cuánto ahorra/gasta extra

5. **Trial gratuito**:
   - Ofrece 30 días gratis en planes de pago
   - Calcula cuándo expira
   - Muestra cuánto cuesta después del trial

6. **Upgrade/Downgrade**:
   - Pregunta plan actual
   - Calcula diferencia de precio
   - Muestra qué gana/pierde

---

**Tiempo estimado**: 15-20 minutos  
**Archivo de solución**: `ejercicio_17.py`


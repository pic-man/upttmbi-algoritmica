# 💳 Ejercicio 15: Tipo de Tarjeta

## Dificultad: ⭐⭐ Intermedio

## 📝 Descripción

Crea un programa que pida el tipo de tarjeta de crédito y muestre los beneficios asociados.

## 🎯 Objetivo

Practicar comparación de strings con múltiples opciones y mostrar información estructurada.

## 📋 Especificaciones

El programa debe:

1. Solicitar el tipo de tarjeta
2. Mostrar beneficios según:
   - **Básica**: "1% de cashback"
   - **Oro**: "2% de cashback + seguro de viaje"
   - **Platino**: "3% de cashback + seguro + salas VIP"
   - **Otra**: "Tipo de tarjeta no válido"

## 💻 Ejemplo de Ejecución

### Ejemplo 1:
```
=== BENEFICIOS DE TARJETA DE CRÉDITO ===

Tipos disponibles: básica, oro, platino

Ingresa tu tipo de tarjeta: oro

💳 TARJETA ORO

Beneficios:
✓ 2% de cashback en todas tus compras
✓ Seguro de viaje incluido
✓ Sin comisión en retiros internacionales
✓ Protección de compras

Anualidad: $500
```

### Ejemplo 2:
```
=== BENEFICIOS DE TARJETA DE CRÉDITO ===

Tipos disponibles: básica, oro, platino

Ingresa tu tipo de tarjeta: platino

💳 TARJETA PLATINO

Beneficios:
✓ 3% de cashback en todas tus compras
✓ Seguro de viaje internacional premium
✓ Acceso a salas VIP en aeropuertos
✓ Protección de compras extendida
✓ Concierge 24/7
✓ Millas dobles en aerolíneas

Anualidad: $1,200
```

### Ejemplo 3:
```
=== BENEFICIOS DE TARJETA DE CRÉDITO ===

Tipos disponibles: básica, oro, platino

Ingresa tu tipo de tarjeta: plata

❌ Tipo de tarjeta no válido
Por favor, elige entre: básica, oro o platino
```

## 🧪 Casos de Prueba

Prueba tu programa con estos valores:

| Entrada | Resultado |
|---------|-----------|
| básica | 1% cashback |
| basica | 1% cashback |
| BASICA | 1% cashback |
| oro | 2% + seguro |
| Oro | 2% + seguro |
| platino | 3% + seguro + VIP |
| plata | No válido |
| negra | No válido |

## 💡 Pistas

1. Usa `.lower()` para normalizar:
   ```python
   tipo = input("Tipo de tarjeta: ").lower()
   ```

2. Considera variaciones: "básica", "basica" (sin acento)

3. Estructura:
   ```python
   if tipo == "basica" or tipo == "básica":
       # básica
   elif tipo == "oro":
       # oro
   elif tipo == "platino":
       # platino
   else:
       # no válido
   ```

## 📊 Comparación de Tarjetas

| Característica | Básica | Oro | Platino |
|----------------|--------|-----|---------|
| Cashback | 1% | 2% | 3% |
| Seguro viaje | ❌ | ✅ | ✅ Premium |
| Salas VIP | ❌ | ❌ | ✅ |
| Anualidad | $0 | $500 | $1,200 |
| Límite crédito | $10K | $50K | $100K |

## ⚠️ Errores Comunes

- ❌ No normalizar a minúsculas
- ❌ No considerar acentos (básica vs basica)
- ❌ No validar opciones incorrectas
- ❌ No mostrar las opciones disponibles

## 🎓 Conceptos Practicados

- Comparación de strings
- `.lower()` para normalización
- `if-elif-else` con strings
- Múltiples condiciones con `or`
- Validación de entrada

## 💎 Tarjetas del Mundo Real

**Ejemplos de clasificación**:
- **Visa/Mastercard**: Clásica, Oro, Platinum, Infinite
- **American Express**: Verde, Oro, Platino, Centurion (Negra)
- **Diners Club**: Clásica, Internacional, Élite

## 🚀 Desafíos Extra (Opcional)

1. **Más tipos de tarjeta**:
   - Negra/Infinite: Beneficios ilimitados
   - Estudiantil: Beneficios para estudiantes

2. **Comparador**:
   - Muestra todas las tarjetas en una tabla
   - Permite comparar 2 tarjetas lado a lado

3. **Requisitos**:
   - Pregunta ingresos mensuales
   - Recomienda qué tarjeta aplica según ingresos:
     - Básica: > $500
     - Oro: > $1,500
     - Platino: > $5,000

4. **Calculadora de beneficios**:
   ```
   Gasto mensual: $2,000
   
   Con Básica: $20 de cashback/mes = $240/año
   Con Oro: $40 de cashback/mes = $480/año (anualidad $500)
   Con Platino: $60 de cashback/mes = $720/año (anualidad $1,200)
   
   Recomendación: Tarjeta Básica (mejor relación)
   ```

5. **Sistema de puntos**:
   - Convierte cashback a puntos
   - Muestra opciones de canje

6. **Categorías especiales**:
   - Restaurantes: cashback diferente
   - Gasolina: cashback diferente
   - Supermercados: cashback diferente
   - Pregunta categoría de compra

---

**Tiempo estimado**: 15-20 minutos  
**Archivo de solución**: `ejercicio_15.py`


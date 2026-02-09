# 🍕 Ejercicio 11: Tamaño de Pizza

## Dificultad: ⭐ Básico

## 📝 Descripción

Crea un programa que pida el tamaño de una pizza y muestre su precio.

## 🎯 Objetivo

Practicar comparaciones con strings y múltiples opciones.

## 📋 Especificaciones

El programa debe:

1. Solicitar el tamaño de la pizza
2. Mostrar el precio según:
   - **Chica**: $80
   - **Mediana**: $120
   - **Grande**: $150
   - **Otro tamaño**: "No disponible"

## 💻 Ejemplo de Ejecución

### Ejemplo 1:
```
Tamaños disponibles: chica, mediana, grande

Ingresa el tamaño de pizza: mediana
Pizza mediana: $120
```

### Ejemplo 2:
```
Tamaños disponibles: chica, mediana, grande

Ingresa el tamaño de pizza: grande
Pizza grande: $150
```

### Ejemplo 3:
```
Tamaños disponibles: chica, mediana, grande

Ingresa el tamaño de pizza: familiar
Lo sentimos, ese tamaño no está disponible
```

## 🧪 Casos de Prueba

Prueba tu programa con estos valores:

| Entrada | Salida |
|---------|--------|
| chica | $80 |
| Chica | $80 |
| CHICA | $80 |
| mediana | $120 |
| grande | $150 |
| familiar | No disponible |
| extra | No disponible |

## 💡 Pistas

1. Usa `.lower()` para normalizar la entrada:
   ```python
   tamano = input("Tamaño: ").lower()
   ```
2. Esto hace que "Chica", "CHICA" y "chica" funcionen igual
3. Estructura con `if-elif-else`

## ⚠️ Errores Comunes

- ❌ No considerar mayúsculas/minúsculas
- ❌ No mostrar los tamaños disponibles
- ❌ No validar entradas incorrectas

## 🎓 Conceptos Practicados

- Comparación de strings
- `.lower()` para normalizar texto
- `if-elif-else` múltiple
- Validación de opciones

## 🚀 Desafíos Extra (Opcional)

1. **Ingredientes extras**:
   - Pregunta si quiere ingredientes extra
   - Cada ingrediente cuesta $20
   
2. **Cantidad**:
   - Pregunta cuántas pizzas quiere
   - Calcula el total
   - Agrega descuento por cantidad:
     - 2-3 pizzas: 10% descuento
     - 4+ pizzas: 15% descuento

3. **Menú completo**:
   ```
   === PIZZERÍA LA DELICIA ===
   
   TAMAÑOS Y PRECIOS:
   - Chica (6 rebanadas): $80
   - Mediana (8 rebanadas): $120
   - Grande (10 rebanadas): $150
   
   INGREDIENTES EXTRA ($20 c/u):
   - Pepperoni
   - Champiñones
   - Pimientos
   - Extra queso
   ```

4. **Calcular mejor opción**:
   - Muestra precio por rebanada
   - Sugiere mejor relación precio/cantidad

---

**Tiempo estimado**: 10-15 minutos  
**Archivo de solución**: `ejercicio_11.py`


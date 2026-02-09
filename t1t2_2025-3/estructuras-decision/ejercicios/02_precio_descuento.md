# 💰 Ejercicio 2: Precio con Descuento Simple

## Dificultad: ⭐ Básico

## 📝 Descripción

Crea un programa que pida el precio de un producto y aplique un descuento según la cantidad. Muestra el precio final.

## 🎯 Objetivo

Practicar condicionales simples con operaciones matemáticas.

## 📋 Especificaciones

El programa debe:

1. Solicitar el precio del producto al usuario
2. Aplicar descuento según estas reglas:
   - **Si el precio es mayor a $50**: aplica 10% de descuento
   - **Si es menor o igual a $50**: sin descuento
3. Mostrar el precio final

## 💻 Ejemplo de Ejecución

### Ejemplo 1:
```
Ingresa el precio del producto: $100
Precio original: $100.00
Descuento aplicado: 10%
Precio final: $90.00
```

### Ejemplo 2:
```
Ingresa el precio del producto: $30
Precio original: $30.00
Sin descuento aplicado
Precio final: $30.00
```

### Ejemplo 3:
```
Ingresa el precio del producto: $50
Precio original: $50.00
Sin descuento aplicado
Precio final: $50.00
```

## 🧪 Casos de Prueba

Prueba tu programa con estos valores:

| Entrada | Descuento | Precio Final |
|---------|-----------|--------------|
| $10 | 0% | $10.00 |
| $50 | 0% | $50.00 |
| $51 | 10% | $45.90 |
| $100 | 10% | $90.00 |
| $200 | 10% | $180.00 |

## 💡 Pistas

1. El descuento del 10% se calcula: `precio * 0.10`
2. El precio final es: `precio - descuento`
3. También puedes calcularlo directo: `precio * 0.90` (90% del precio)
4. Usa `.2f` para mostrar 2 decimales: `f"{precio:.2f}"`

## 📐 Fórmulas

```
Si precio > 50:
    descuento = precio * 0.10
    precio_final = precio - descuento
    # O directamente: precio_final = precio * 0.90
Sino:
    precio_final = precio
```

## ⚠️ Errores Comunes

- ❌ Olvidar el caso cuando precio = 50 (debe ser sin descuento)
- ❌ No mostrar el precio con formato adecuado (2 decimales)
- ❌ Calcular mal el descuento (restar en lugar de multiplicar)

## 🎓 Conceptos Practicados

- `if-else` simple
- Operaciones matemáticas
- Porcentajes
- Formato de números con decimales

## 🚀 Desafíos Extra (Opcional)

1. Agrega más niveles de descuento:
   - Más de $100: 15%
   - Más de $200: 20%
2. Muestra cuánto dinero se ahorró
3. Valida que el precio no sea negativo

---

**Tiempo estimado**: 10-15 minutos  
**Archivo de solución**: `ejercicio_02.py`


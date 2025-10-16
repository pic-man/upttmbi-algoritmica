# 🏪 Ejercicio 19: Supermercado Inteligente

## Dificultad: ⭐⭐⭐ Avanzado

## 📝 Descripción

Crea un sistema de carrito de compras donde puedas agregar productos (pueden repetirse), calcular cantidades, eliminar uno a uno, y calcular total agrupando por producto.

## 🎯 Objetivo

Sistema completo de carrito con conteo y cálculo de precios.

## 💻 Datos Iniciales

```python
carrito = []
precios = {"manzana": 2, "pan": 1.5, "leche": 3, "huevos": 4}
```

## 📋 Funciones a Implementar

```python
def agregar_producto(carrito, producto):
    """Agrega un producto al carrito"""
    pass

def eliminar_producto(carrito, producto):
    """Elimina UNA unidad del producto"""
    pass

def contar_productos(carrito):
    """Retorna dict con cantidades de cada producto"""
    pass

def calcular_total(carrito, precios):
    """Calcula el total a pagar"""
    pass

def mostrar_ticket(carrito, precios):
    """Muestra ticket de compra detallado"""
    pass
```

## 💻 Ejemplo de Ejecución

```
=== SUPERMERCADO ===

Agregando productos...
✓ manzana
✓ pan
✓ manzana
✓ leche
✓ manzana

🛒 CARRITO:
- manzana x3
- pan x1
- leche x1

💰 TICKET:
━━━━━━━━━━━━━━━━━━━━━━━━
SUPERMERCADO PYTHON
━━━━━━━━━━━━━━━━━━━━━━━━

manzana   x3    $2.00   $6.00
pan       x1    $1.50   $1.50
leche     x1    $3.00   $3.00

━━━━━━━━━━━━━━━━━━━━━━━━
SUBTOTAL:          $10.50
IVA (16%):          $1.68
━━━━━━━━━━━━━━━━━━━━━━━━
TOTAL:             $12.18
━━━━━━━━━━━━━━━━━━━━━━━━

¡Gracias por su compra!
```

## 💡 Pistas

1. `count()` para cantidades
2. `set()` para productos únicos
3. Usa diccionarios para agrupar

---

**Tiempo estimado**: 50-60 minutos  
**Archivo de solución**: `ejercicio_19.py`


# 📖 01 - Introducción a los Estándares de Calidad

## ¿Qué son los Estándares de Calidad?

Los **estándares de calidad** en el desarrollo de software son un conjunto de normas, prácticas y convenciones que aseguran que los algoritmos y programas sean:

- **Correctos**: Producen los resultados esperados
- **Legibles**: Fáciles de entender por otros
- **Mantenibles**: Fáciles de modificar y actualizar
- **Eficientes**: Usan recursos de manera óptima
- **Documentados**: Tienen información clara sobre su funcionamiento

## ¿Por Qué Son Importantes?

```
┌─────────────────────────────────────────────────────────────┐
│                  SIN ESTÁNDARES                             │
│  ┌─────────┐     ┌─────────┐     ┌─────────┐               │
│  │ Código  │ ──▶ │  Bugs   │ ──▶ │ Caos    │               │
│  │ confuso │     │ ocultos │     │ total   │               │
│  └─────────┘     └─────────┘     └─────────┘               │
├─────────────────────────────────────────────────────────────┤
│                  CON ESTÁNDARES                             │
│  ┌─────────┐     ┌─────────┐     ┌─────────┐               │
│  │ Código  │ ──▶ │ Fácil   │ ──▶ │ Éxito   │               │
│  │ limpio  │     │mantener │     │ total   │               │
│  └─────────┘     └─────────┘     └─────────┘               │
└─────────────────────────────────────────────────────────────┘
```

## Principios Básicos de Calidad

### 1. Claridad

El código debe ser fácil de leer y entender.

❌ **Mal ejemplo**:
```python
x=a+b*c/d-e
if x>0:y=1
else:y=0
```

✅ **Buen ejemplo**:
```python
# Calcular el resultado de la operación
resultado = valor_base + (cantidad * precio / dias) - descuento

# Determinar si es positivo
if resultado > 0:
    es_positivo = True
else:
    es_positivo = False
```

### 2. Consistencia

Usar el mismo estilo en todo el código.

- Mismo formato de nombres
- Misma indentación
- Mismo estilo de comentarios

### 3. Simplicidad

El código debe ser lo más simple posible.

> "La perfección se alcanza, no cuando no hay nada más que añadir, sino cuando no hay nada más que quitar." - Antoine de Saint-Exupéry

### 4. Modularidad

Dividir el código en partes pequeñas y manejables.

```python
# En lugar de un código largo y complejo:
def procesar_pedido(cliente, productos, direccion):
    # Validar datos
    if not validar_cliente(cliente):
        return "Error: Cliente inválido"
    
    # Calcular total
    total = calcular_total(productos)
    
    # Procesar pago
    if procesar_pago(cliente, total):
        # Enviar pedido
        enviar_pedido(direccion, productos)
        return "Pedido procesado"
    
    return "Error en el pago"
```

## Beneficios de Aplicar Estándares

| Beneficio | Descripción |
|-----------|-------------|
| **Menos errores** | Código más predecible y verificable |
| **Mantenimiento fácil** | Cambios rápidos y seguros |
| **Trabajo en equipo** | Todos entienden el código |
| **Reutilización** | Código puede usarse en otros proyectos |
| **Documentación** | El código se auto-documenta |

## Estándares Comunes

### Nomenclatura de Variables

| Tipo | Convención | Ejemplo |
|------|------------|---------|
| Variables | snake_case | `precio_total` |
| Constantes | MAYUSCULAS | `IVA_PORCENTAJE` |
| Funciones | snake_case | `calcular_promedio()` |
| Clases | PascalCase | `CalculadoraImpuestos` |

### Estructura del Código

```python
# 1. Imports (al inicio)
import math

# 2. Constantes
PI = 3.14159
RADIO_DEFAULT = 1.0

# 3. Funciones
def calcular_area(radio):
    """Calcula el área de un círculo."""
    return PI * radio ** 2

# 4. Código principal
if __name__ == "__main__":
    area = calcular_area(5)
    print(f"Área: {area}")
```

## El Ciclo de Calidad

```
       ┌─────────────┐
       │   Diseñar   │
       └──────┬──────┘
              │
              ▼
       ┌─────────────┐
       │  Codificar  │
       └──────┬──────┘
              │
              ▼
       ┌─────────────┐
       │   Probar    │ ◄──┐
       └──────┬──────┘    │
              │           │
              ▼           │
       ┌─────────────┐    │
       │  Revisar    │────┘
       └──────┬──────┘
              │
              ▼
       ┌─────────────┐
       │  Mejorar    │
       └─────────────┘
```

## 📝 Para Recordar

1. Los estándares aseguran **calidad** en el software
2. El código debe ser **claro, consistente y simple**
3. La **modularidad** facilita el mantenimiento
4. Seguir estándares mejora el **trabajo en equipo**
5. La calidad es un **proceso continuo**

## ✅ Ejercicio Rápido

Identifica los problemas de calidad en este código:

```python
def f(a,b,c):
    x=a*b
    y=x-c
    if y>0:return True
    else:return False
```

<details>
<summary>Ver respuesta</summary>

Problemas identificados:

1. ❌ Nombre de función no descriptivo (`f`)
2. ❌ Nombres de parámetros no descriptivos (`a`, `b`, `c`)
3. ❌ Falta espaciado alrededor de operadores
4. ❌ Sin comentarios ni docstring
5. ❌ Falta indentación después de if/else
6. ❌ Variables temporales con nombres poco claros

Versión mejorada:

```python
def es_ganancia_positiva(precio, cantidad, costos):
    """
    Determina si hay ganancia positiva.
    
    Args:
        precio: Precio unitario del producto
        cantidad: Cantidad vendida
        costos: Costos totales
    
    Returns:
        True si hay ganancia, False si no
    """
    ingresos = precio * cantidad
    ganancia = ingresos - costos
    
    return ganancia > 0
```
</details>

## 🔜 Siguiente Paso

Ahora aprenderás sobre la trazabilidad de algoritmos.

[Ir a: 02 - Trazabilidad →](./02_trazabilidad.md)

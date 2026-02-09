# 📖 05 - Técnicas de Escritura de Algoritmos y Programas

## Principios de Código Limpio

El **código limpio** es código que es fácil de leer, entender y mantener.

> "Cualquier tonto puede escribir código que una computadora entienda. Los buenos programadores escriben código que los humanos pueden entender." - Martin Fowler

## 1. Nomenclatura Clara

### Nombres de Variables

```python
# ❌ MAL: Nombres crípticos
x = 100
y = 0.16
z = x * y

# ✅ BIEN: Nombres descriptivos
precio_base = 100
tasa_impuesto = 0.16
impuesto = precio_base * tasa_impuesto
```

### Convenciones de Nombres en Python

| Tipo | Convención | Ejemplo |
|------|------------|---------|
| Variables | snake_case | `precio_total` |
| Constantes | SCREAMING_SNAKE_CASE | `IVA_PORCENTAJE` |
| Funciones | snake_case | `calcular_promedio()` |
| Clases | PascalCase | `CalculadoraImpuestos` |
| Privados | _prefijo | `_valor_interno` |

### Reglas para Buenos Nombres

1. **Usar nombres pronunciables**
   ```python
   # ❌ MAL
   fnclclprmd = 10
   
   # ✅ BIEN
   fecha_nacimiento = "1990-05-15"
   ```

2. **Evitar abreviaturas confusas**
   ```python
   # ❌ MAL
   calc_prom_est()
   
   # ✅ BIEN
   calcular_promedio_estudiante()
   ```

3. **Usar nombres que revelen intención**
   ```python
   # ❌ MAL
   d = 30  # ¿Qué es d?
   
   # ✅ BIEN
   dias_del_mes = 30
   ```

## 2. Estructura del Código

### Organización de un Archivo

```python
#!/usr/bin/env python3
"""
Descripción breve del módulo.

Descripción más detallada si es necesario.
"""

# 1. Imports de la biblioteca estándar
import os
import sys

# 2. Imports de terceros
import numpy as np

# 3. Imports locales
from mi_modulo import mi_funcion

# 4. Constantes
VALOR_MAXIMO = 100
MENSAJE_ERROR = "Ocurrió un error"

# 5. Funciones auxiliares
def funcion_auxiliar():
    pass

# 6. Funciones principales
def funcion_principal():
    pass

# 7. Código principal
if __name__ == "__main__":
    funcion_principal()
```

### Indentación Consistente

```python
# ✅ BIEN: Indentación de 4 espacios
def calcular_precio(cantidad, precio_unitario):
    subtotal = cantidad * precio_unitario
    if subtotal > 100:
        descuento = subtotal * 0.1
        total = subtotal - descuento
    else:
        total = subtotal
    return total

# ❌ MAL: Indentación inconsistente
def calcular_precio(cantidad, precio_unitario):
  subtotal = cantidad * precio_unitario
  if subtotal > 100:
      descuento = subtotal * 0.1
      total = subtotal - descuento
  else:
   total = subtotal
  return total
```

## 3. Funciones Bien Diseñadas

### Una Función, Una Tarea

```python
# ❌ MAL: Función que hace demasiado
def procesar_pedido(cliente, productos, direccion):
    # Validar cliente
    # Calcular totales
    # Procesar pago
    # Enviar email
    # Actualizar inventario
    pass

# ✅ BIEN: Funciones separadas
def validar_cliente(cliente):
    pass

def calcular_total(productos):
    pass

def procesar_pago(cliente, total):
    pass

def enviar_confirmacion(cliente, pedido):
    pass

def actualizar_inventario(productos):
    pass

def procesar_pedido(cliente, productos, direccion):
    if not validar_cliente(cliente):
        return None
    
    total = calcular_total(productos)
    
    if procesar_pago(cliente, total):
        actualizar_inventario(productos)
        enviar_confirmacion(cliente, productos)
        return True
    
    return False
```

### Funciones Cortas

```python
# ✅ BIEN: Función corta y clara
def es_mayor_de_edad(edad):
    """Verifica si una persona es mayor de edad."""
    return edad >= 18


def calcular_descuento(precio, porcentaje):
    """Calcula el monto del descuento."""
    return precio * (porcentaje / 100)
```

## 4. Manejo de Errores

### Validación de Entrada

```python
def dividir(dividendo, divisor):
    """
    Divide dos números de forma segura.
    
    Args:
        dividendo: El número a dividir
        divisor: El número por el cual dividir
    
    Returns:
        El resultado de la división
    
    Raises:
        ValueError: Si el divisor es cero
    """
    if divisor == 0:
        raise ValueError("El divisor no puede ser cero")
    
    return dividendo / divisor
```

### Mensajes de Error Claros

```python
# ❌ MAL: Mensaje vago
raise Exception("Error")

# ✅ BIEN: Mensaje específico
raise ValueError(f"La edad debe ser positiva, se recibió: {edad}")
```

## 5. Espaciado y Formato

### Espacios Alrededor de Operadores

```python
# ❌ MAL
resultado=a+b*c

# ✅ BIEN
resultado = a + b * c
```

### Líneas en Blanco

```python
# ✅ BIEN: Separación lógica
def calcular_subtotal(productos):
    """Calcula el subtotal de los productos."""
    total = 0
    for producto in productos:
        total += producto['precio'] * producto['cantidad']
    return total


def aplicar_impuesto(subtotal, tasa):
    """Aplica el impuesto al subtotal."""
    return subtotal * (1 + tasa)


def calcular_total(productos, tasa_impuesto):
    """Calcula el total final con impuestos."""
    subtotal = calcular_subtotal(productos)
    total = aplicar_impuesto(subtotal, tasa_impuesto)
    return total
```

## 6. Evitar Código Duplicado (DRY)

### Don't Repeat Yourself

```python
# ❌ MAL: Código duplicado
def calcular_area_cuadrado(lado):
    return lado * lado

def calcular_area_rectangulo(base, altura):
    return base * altura

def mostrar_area_cuadrado(lado):
    area = lado * lado
    print(f"El área es: {area}")

def mostrar_area_rectangulo(base, altura):
    area = base * altura
    print(f"El área es: {area}")


# ✅ BIEN: Sin duplicación
def calcular_area_rectangulo(base, altura):
    """Calcula el área de un rectángulo."""
    return base * altura

def calcular_area_cuadrado(lado):
    """Calcula el área de un cuadrado."""
    return calcular_area_rectangulo(lado, lado)

def mostrar_area(forma, area):
    """Muestra el área calculada."""
    print(f"El área del {forma} es: {area}")
```

## 7. Guía de Estilo PEP 8

Python tiene una guía de estilo oficial llamada **PEP 8**:

| Regla | Descripción |
|-------|-------------|
| Indentación | 4 espacios |
| Longitud de línea | Máximo 79 caracteres |
| Imports | Uno por línea |
| Espacios | Después de comas, alrededor de operadores |
| Nombres | snake_case para funciones y variables |
| Comentarios | Completos y actualizados |

## 📝 Para Recordar

1. Usa **nombres descriptivos** para variables y funciones
2. Mantén las funciones **pequeñas y enfocadas**
3. **Evita la duplicación** de código
4. Usa **espaciado consistente**
5. Sigue las **convenciones** del lenguaje (PEP 8)
6. **Comenta** el por qué, no el qué

## ✅ Ejercicio Rápido

Mejora el siguiente código aplicando las técnicas aprendidas:

```python
def f(l,d):
    t=0
    for i in l:t=t+i
    t=t-(t*d/100)
    return t
```

<details>
<summary>Ver respuesta</summary>

```python
def calcular_total_con_descuento(lista_precios, porcentaje_descuento):
    """
    Calcula el total de una lista de precios aplicando un descuento.
    
    Args:
        lista_precios (list): Lista de precios
        porcentaje_descuento (float): Porcentaje de descuento a aplicar
    
    Returns:
        float: Total con el descuento aplicado
    """
    # Calcular la suma de todos los precios
    subtotal = sum(lista_precios)
    
    # Calcular el monto del descuento
    descuento = subtotal * (porcentaje_descuento / 100)
    
    # Calcular y retornar el total final
    total = subtotal - descuento
    
    return total
```
</details>

## 🔜 Siguiente Paso

Ahora aprenderás sobre las pruebas de algoritmos y programas.

[Ir a: 06 - Pruebas de Algoritmos →](./06_pruebas_algoritmos.md)

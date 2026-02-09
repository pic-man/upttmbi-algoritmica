# 📖 07 - Las Constantes

## ¿Qué es una Constante?

Una **constante** es un valor que no cambia durante la ejecución del programa. Representa valores fijos que se usan repetidamente.

```
┌─────────────────────────────────────────────────────────────┐
│               VARIABLE vs CONSTANTE                          │
├────────────────────────────┬────────────────────────────────┤
│         VARIABLE           │          CONSTANTE             │
├────────────────────────────┼────────────────────────────────┤
│ Puede cambiar de valor     │ Valor fijo, no cambia          │
│ contador = contador + 1    │ PI = 3.14159                   │
│                            │                                │
│ edad = 25                  │ IVA = 0.16                     │
│ edad = 26  ✓               │ IVA = 0.18  ✗ (no debería)     │
└────────────────────────────┴────────────────────────────────┘
```

## Constantes en Python

Python **no tiene constantes reales** a nivel de lenguaje. Por convención, usamos nombres en MAYÚSCULAS para indicar que un valor no debe modificarse.

```python
# Constantes por convención (MAYÚSCULAS)
PI = 3.14159
GRAVEDAD = 9.81
IVA = 0.16
DIAS_SEMANA = 7
HORAS_DIA = 24
MESES_AÑO = 12

# Constantes de texto
MENSAJE_BIENVENIDA = "Bienvenido al sistema"
MENSAJE_ERROR = "Ha ocurrido un error"
RUTA_ARCHIVOS = "/datos/archivos/"
```

## ¿Cuándo Usar Constantes?

### 1. Valores Matemáticos

```python
PI = 3.14159265359
E = 2.71828
RAIZ_2 = 1.41421

# Uso
circunferencia = 2 * PI * radio
area = PI * radio ** 2
```

### 2. Valores de Configuración

```python
# Configuración del sistema
MAXIMO_INTENTOS = 3
TIEMPO_ESPERA = 30
TAMAÑO_PAGINA = 10
LONGITUD_MINIMA_PASSWORD = 8

# Uso
if intentos >= MAXIMO_INTENTOS:
    print("Cuenta bloqueada")
```

### 3. Valores de Negocio

```python
# Tasas e impuestos
IVA = 0.16
ISR = 0.30
COMISION_BANCARIA = 0.025

# Límites
SALARIO_MINIMO = 207.44
EDAD_MINIMA_VOTACION = 18
EDAD_JUBILACION = 65

# Uso
impuesto = precio * IVA
es_mayor = edad >= EDAD_MINIMA_VOTACION
```

### 4. Mensajes del Sistema

```python
# Mensajes
MSG_BIENVENIDA = "Bienvenido al sistema"
MSG_DESPEDIDA = "Gracias por usar el sistema"
MSG_ERROR_CONEXION = "Error: No se pudo conectar"
MSG_EXITO = "Operación realizada con éxito"

# Uso
print(MSG_BIENVENIDA)
```

## Ventajas de Usar Constantes

### 1. Código Más Legible

```python
# ❌ Sin constantes (¿qué significa 0.16?)
total = precio * 1.16

# ✅ Con constantes (claro y descriptivo)
IVA = 0.16
total = precio * (1 + IVA)
```

### 2. Fácil Mantenimiento

```python
# Si cambia el IVA, solo se modifica en un lugar
IVA = 0.16  # Cambiar a 0.18 si es necesario

# Se usa en múltiples lugares
total1 = precio1 * (1 + IVA)
total2 = precio2 * (1 + IVA)
total3 = precio3 * (1 + IVA)
```

### 3. Evita Errores

```python
# ❌ Propenso a errores (escribir mal el número)
area1 = 3.14159 * r1 ** 2
area2 = 3.14158 * r2 ** 2  # Error tipográfico

# ✅ Más seguro
PI = 3.14159
area1 = PI * r1 ** 2
area2 = PI * r2 ** 2  # Mismo valor garantizado
```

## Módulo de Constantes

Para proyectos grandes, es común crear un archivo de constantes:

```python
# archivo: constantes.py
"""Constantes del sistema"""

# Matemáticas
PI = 3.14159265359
E = 2.71828182845

# Configuración
MAX_INTENTOS_LOGIN = 3
TIEMPO_SESION_MINUTOS = 30
ITEMS_POR_PAGINA = 20

# Impuestos
IVA = 0.16
ISR_EMPLEADOS = 0.25

# Mensajes
MSG_BIENVENIDA = "Bienvenido"
MSG_ERROR = "Error"
MSG_EXITO = "Éxito"
```

```python
# archivo: main.py
from constantes import PI, IVA, MAX_INTENTOS_LOGIN

area = PI * radio ** 2
total = subtotal * (1 + IVA)
```

## Constantes Enumeradas

Para conjuntos de valores relacionados:

```python
from enum import Enum

class DiaSemana(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7

class Estado(Enum):
    ACTIVO = "activo"
    INACTIVO = "inactivo"
    PENDIENTE = "pendiente"

# Uso
hoy = DiaSemana.LUNES
print(hoy.value)  # 1

usuario_estado = Estado.ACTIVO
```

## Ejemplo Completo

```python
"""
Sistema de Facturación
Demuestra el uso de constantes
"""

# ============================================
# CONSTANTES
# ============================================

# Impuestos
IVA = 0.16
RETENCION_ISR = 0.10

# Descuentos
DESCUENTO_MAYOREO = 0.15      # 15% para compras mayoreo
CANTIDAD_MAYOREO = 10         # Mínimo para mayoreo
DESCUENTO_PRONTO_PAGO = 0.05  # 5% por pago anticipado

# Límites
MINIMO_FACTURA = 100.0
MAXIMO_DESCUENTO = 0.30       # Máximo 30% de descuento

# Mensajes
MSG_FACTURA_MINIMA = f"El mínimo de facturación es ${MINIMO_FACTURA}"

# ============================================
# FUNCIONES
# ============================================

def calcular_factura(precio_unitario, cantidad, pago_anticipado=False):
    """Calcula el total de una factura."""
    
    # Subtotal
    subtotal = precio_unitario * cantidad
    
    # Verificar mínimo
    if subtotal < MINIMO_FACTURA:
        print(MSG_FACTURA_MINIMA)
        return None
    
    # Aplicar descuento por mayoreo
    descuento = 0
    if cantidad >= CANTIDAD_MAYOREO:
        descuento = subtotal * DESCUENTO_MAYOREO
        print(f"Descuento mayoreo ({DESCUENTO_MAYOREO*100}%): -${descuento:.2f}")
    
    # Aplicar descuento por pronto pago
    if pago_anticipado:
        descuento_pp = subtotal * DESCUENTO_PRONTO_PAGO
        descuento += descuento_pp
        print(f"Descuento pronto pago ({DESCUENTO_PRONTO_PAGO*100}%): -${descuento_pp:.2f}")
    
    # Calcular totales
    subtotal_con_descuento = subtotal - descuento
    iva = subtotal_con_descuento * IVA
    total = subtotal_con_descuento + iva
    
    return {
        'subtotal': subtotal,
        'descuento': descuento,
        'iva': iva,
        'total': total
    }


# ============================================
# PROGRAMA PRINCIPAL
# ============================================

if __name__ == "__main__":
    resultado = calcular_factura(50, 12, pago_anticipado=True)
    
    if resultado:
        print(f"\nSubtotal: ${resultado['subtotal']:.2f}")
        print(f"Descuento: -${resultado['descuento']:.2f}")
        print(f"IVA ({IVA*100}%): +${resultado['iva']:.2f}")
        print(f"TOTAL: ${resultado['total']:.2f}")
```

## 📝 Para Recordar

1. Las **constantes** son valores que no deben cambiar
2. En Python se usan **MAYÚSCULAS** por convención
3. Mejoran la **legibilidad** y **mantenimiento** del código
4. Evitan **errores** por valores mágicos repetidos
5. Se pueden agrupar en un **módulo de constantes**

## ✅ Ejercicio Rápido

¿Cuáles de estos valores deberían ser constantes?

```python
contador = 0
pi = 3.14159
nombre_usuario = "Juan"
iva = 0.16
edad = 25
dias_febrero = 28
maximo_intentos = 3
```

<details>
<summary>Ver respuesta</summary>

```python
# VARIABLES (cambian durante la ejecución)
contador = 0           # Contador, cambia en cada iteración
nombre_usuario = "Juan" # Puede cambiar según el usuario
edad = 25              # Puede cambiar

# CONSTANTES (valores fijos)
PI = 3.14159          # Valor matemático fijo
IVA = 0.16            # Tasa fija (por período)
DIAS_FEBRERO = 28     # Valor fijo (en años no bisiestos)
MAXIMO_INTENTOS = 3   # Configuración fija del sistema
```
</details>

---

¡Felicidades! Has completado la teoría de la Unidad 3. Ahora puedes pasar a los ejercicios.

[Ir a: Ejercicios →](../ejercicios/README.md)

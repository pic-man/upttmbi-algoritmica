# 📖 01 - Introducción a la Programación Modular

## ¿Qué es la Programación Modular?

La **programación modular** es un paradigma que consiste en dividir un programa grande en partes más pequeñas llamadas **módulos** o **funciones**.

```
┌─────────────────────────────────────────────────────────────┐
│                    PROGRAMA PRINCIPAL                        │
├─────────────────┬─────────────────┬─────────────────────────┤
│    Módulo 1     │    Módulo 2     │        Módulo 3         │
│   (Función A)   │   (Función B)   │       (Función C)       │
│                 │                 │                         │
│ Tarea específica│ Tarea específica│   Tarea específica      │
└─────────────────┴─────────────────┴─────────────────────────┘
```

## Ventajas de la Modularidad

| Ventaja | Descripción |
|---------|-------------|
| **Organización** | Código dividido en partes lógicas |
| **Reutilización** | Funciones usables en múltiples lugares |
| **Mantenimiento** | Más fácil encontrar y corregir errores |
| **Legibilidad** | Código más fácil de entender |
| **Trabajo en equipo** | Cada persona puede trabajar en un módulo |
| **Pruebas** | Se pueden probar módulos individualmente |

## Principio "Divide y Vencerás"

```
     PROBLEMA GRANDE
           │
     ┌─────┴─────┐
     │   Dividir │
     └─────┬─────┘
           │
    ┌──────┼──────┐
    ▼      ▼      ▼
┌──────┐┌──────┐┌──────┐
│Parte1││Parte2││Parte3│
└──┬───┘└──┬───┘└──┬───┘
   │       │       │
   ▼       ▼       ▼
Resolver Resolver Resolver
   │       │       │
   └───────┼───────┘
           │
     ┌─────┴─────┐
     │  Combinar │
     └─────┬─────┘
           │
           ▼
      SOLUCIÓN
```

## Ejemplo: Sin modularidad vs Con modularidad

### ❌ Sin modularidad (código repetido)

```python
# Calcular área de círculo 1
radio1 = 5
area1 = 3.14159 * radio1 ** 2
print(f"Área 1: {area1}")

# Calcular área de círculo 2
radio2 = 8
area2 = 3.14159 * radio2 ** 2
print(f"Área 2: {area2}")

# Calcular área de círculo 3
radio3 = 3
area3 = 3.14159 * radio3 ** 2
print(f"Área 3: {area3}")
```

### ✅ Con modularidad (función reutilizable)

```python
def calcular_area_circulo(radio):
    """Calcula el área de un círculo dado su radio."""
    PI = 3.14159
    return PI * radio ** 2

# Usar la función múltiples veces
print(f"Área 1: {calcular_area_circulo(5)}")
print(f"Área 2: {calcular_area_circulo(8)}")
print(f"Área 3: {calcular_area_circulo(3)}")
```

## Conceptos Clave

### Función
Un bloque de código que realiza una tarea específica y puede retornar un valor.

### Procedimiento
Similar a una función pero **no retorna** un valor (solo ejecuta acciones).

### Módulo
Un archivo que contiene funciones y variables relacionadas.

### Parámetros
Valores que se pasan a una función para que trabaje con ellos.

### Valor de retorno
El resultado que una función devuelve al código que la llamó.

## Estructura de un Programa Modular

```python
# ============================================
# DEFINICIÓN DE FUNCIONES
# ============================================

def funcion_auxiliar_1():
    """Descripción de la función."""
    pass

def funcion_auxiliar_2():
    """Descripción de la función."""
    pass

def funcion_principal():
    """Función principal del programa."""
    funcion_auxiliar_1()
    funcion_auxiliar_2()

# ============================================
# PROGRAMA PRINCIPAL
# ============================================

if __name__ == "__main__":
    funcion_principal()
```

## 📝 Para Recordar

1. **Dividir** el programa en funciones pequeñas
2. Cada función debe hacer **una sola cosa**
3. Las funciones permiten **reutilizar** código
4. El código modular es más **fácil de mantener**
5. Las funciones deben tener **nombres descriptivos**

## 🔜 Siguiente Paso

[Ir a: 02 - Funciones →](./02_funciones.md)

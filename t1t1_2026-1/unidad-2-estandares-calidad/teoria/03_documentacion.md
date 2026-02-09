# 📖 03 - Formas y Técnicas de Documentar Algoritmos y Programas

## ¿Qué es la Documentación?

La **documentación** es el conjunto de descripciones, explicaciones y especificaciones que acompañan a un algoritmo o programa para facilitar su comprensión, uso y mantenimiento.

> "El código que escribes hoy será leído por alguien mañana, posiblemente tú mismo."

## Tipos de Documentación

```
┌─────────────────────────────────────────────────────────────┐
│                    DOCUMENTACIÓN                             │
├─────────────────┬─────────────────┬─────────────────────────┤
│    INTERNA      │    EXTERNA      │      TÉCNICA            │
│                 │                 │                         │
│ Comentarios en  │ Manuales de     │ Especificaciones        │
│ el código       │ usuario         │ del sistema             │
└─────────────────┴─────────────────┴─────────────────────────┘
```

## Documentación Interna (Comentarios)

### Tipos de Comentarios en Python

```python
# Comentario de una línea
# Explica qué hace la siguiente instrucción

"""
Comentario de múltiples líneas
También llamado docstring cuando está
al inicio de una función o clase
"""

'''
También se pueden usar
comillas simples triples
'''
```

### Comentarios de Encabezado

```python
"""
Nombre del Programa: Calculadora de Nómina
Autor: Juan Pérez
Fecha: 2025-01-25
Versión: 1.0

Descripción:
Este programa calcula el salario neto de un empleado
considerando deducciones de impuestos y seguro social.

Entradas:
- Salario bruto mensual
- Horas extras trabajadas

Salidas:
- Desglose de deducciones
- Salario neto a pagar
"""
```

### Comentarios de Función (Docstrings)

```python
def calcular_impuesto(salario, porcentaje):
    """
    Calcula el impuesto sobre un salario.
    
    Args:
        salario (float): El salario bruto del empleado
        porcentaje (float): El porcentaje de impuesto (0-100)
    
    Returns:
        float: El monto del impuesto a pagar
    
    Raises:
        ValueError: Si el porcentaje no está entre 0 y 100
    
    Example:
        >>> calcular_impuesto(1000, 15)
        150.0
    """
    if not 0 <= porcentaje <= 100:
        raise ValueError("El porcentaje debe estar entre 0 y 100")
    
    return salario * (porcentaje / 100)
```

### Comentarios de Sección

```python
# ============================================
# CONFIGURACIÓN INICIAL
# ============================================

IVA = 0.16
DESCUENTO_MAXIMO = 0.30

# ============================================
# FUNCIONES DE CÁLCULO
# ============================================

def calcular_subtotal(productos):
    # ... código ...
    pass

def aplicar_descuento(total, porcentaje):
    # ... código ...
    pass

# ============================================
# PROGRAMA PRINCIPAL
# ============================================

if __name__ == "__main__":
    # Inicio del programa
    pass
```

### Comentarios de Línea

```python
# Calcular el área del círculo usando la fórmula A = πr²
area = PI * radio ** 2  # ** es el operador de potencia en Python

# Verificar si el usuario es mayor de edad (18+ años)
if edad >= 18:
    puede_votar = True  # Cumple el requisito de edad
```

## Buenas Prácticas de Comentarios

### ✅ Qué Comentar

1. **El propósito** del código (por qué, no qué)
2. **Decisiones de diseño** importantes
3. **Casos especiales** o excepciones
4. **Algoritmos complejos**
5. **Referencias** a documentación externa

### ❌ Qué NO Comentar

```python
# MAL: Comentarios obvios
x = x + 1  # Incrementar x en 1
nombre = input("Nombre: ")  # Pedir el nombre

# BIEN: Comentarios útiles
# Compensar el índice base-0 para mostrar posición real al usuario
posicion_mostrada = indice + 1
```

## Documentación Externa

### Estructura de un Documento de Especificación

```
1. TÍTULO DEL DOCUMENTO
   
2. INFORMACIÓN GENERAL
   - Nombre del programa
   - Versión
   - Fecha
   - Autor(es)

3. DESCRIPCIÓN GENERAL
   - Propósito
   - Alcance
   - Requisitos

4. ESPECIFICACIONES TÉCNICAS
   - Entradas
   - Salidas
   - Procesos

5. INSTRUCCIONES DE USO
   - Instalación
   - Ejecución
   - Ejemplos

6. HISTORIAL DE CAMBIOS
   - Versiones anteriores
   - Modificaciones realizadas
```

## Ejemplo de Documentación Completa

### Código Documentado

```python
"""
Sistema de Gestión de Calificaciones
====================================

Autor: María García
Fecha: 2025-01-25
Versión: 2.1

Descripción:
    Sistema para registrar y calcular calificaciones de estudiantes.
    Permite ingresar notas y determinar si el estudiante aprobó.

Uso:
    python calificaciones.py
"""

# ============================================
# CONSTANTES DEL SISTEMA
# ============================================

NOTA_MINIMA_APROBACION = 6.0  # Nota mínima para aprobar
NOTA_MAXIMA = 10.0            # Nota máxima posible
NOTA_MINIMA = 0.0             # Nota mínima posible

# ============================================
# FUNCIONES
# ============================================

def validar_nota(nota):
    """
    Valida que una nota esté en el rango permitido.
    
    Args:
        nota (float): La nota a validar
    
    Returns:
        bool: True si la nota es válida, False si no
    """
    return NOTA_MINIMA <= nota <= NOTA_MAXIMA


def calcular_promedio(notas):
    """
    Calcula el promedio de una lista de notas.
    
    Args:
        notas (list): Lista de notas numéricas
    
    Returns:
        float: El promedio de las notas
    
    Raises:
        ValueError: Si la lista está vacía
    """
    if not notas:
        raise ValueError("La lista de notas no puede estar vacía")
    
    return sum(notas) / len(notas)


def determinar_estado(promedio):
    """
    Determina si un estudiante aprobó según su promedio.
    
    Args:
        promedio (float): El promedio del estudiante
    
    Returns:
        str: "Aprobado" o "Reprobado"
    """
    if promedio >= NOTA_MINIMA_APROBACION:
        return "Aprobado"
    else:
        return "Reprobado"


# ============================================
# PROGRAMA PRINCIPAL
# ============================================

if __name__ == "__main__":
    print("=== Sistema de Calificaciones ===\n")
    
    # Solicitar cantidad de notas
    cantidad = int(input("¿Cuántas notas desea ingresar? "))
    
    # Recolectar notas
    notas = []
    for i in range(cantidad):
        nota = float(input(f"Ingrese la nota {i + 1}: "))
        if validar_nota(nota):
            notas.append(nota)
        else:
            print(f"Nota inválida: {nota}")
    
    # Calcular y mostrar resultados
    if notas:
        promedio = calcular_promedio(notas)
        estado = determinar_estado(promedio)
        
        print(f"\nPromedio: {promedio:.2f}")
        print(f"Estado: {estado}")
```

## 📝 Para Recordar

1. La documentación es **esencial** para el mantenimiento
2. Usa **comentarios internos** para explicar el código
3. Usa **documentación externa** para usuarios y equipos
4. Comenta el **por qué**, no el **qué**
5. Mantén la documentación **actualizada**

## ✅ Ejercicio Rápido

Documenta el siguiente código:

```python
def f(l):
    if len(l) == 0:
        return 0
    return sum(l) / len(l)
```

<details>
<summary>Ver respuesta</summary>

```python
def calcular_promedio(lista_numeros):
    """
    Calcula el promedio de una lista de números.
    
    Args:
        lista_numeros (list): Lista de valores numéricos
    
    Returns:
        float: El promedio de los números, o 0 si la lista está vacía
    
    Example:
        >>> calcular_promedio([10, 20, 30])
        20.0
        >>> calcular_promedio([])
        0
    """
    # Verificar si la lista está vacía para evitar división por cero
    if len(lista_numeros) == 0:
        return 0
    
    # Calcular y retornar el promedio
    return sum(lista_numeros) / len(lista_numeros)
```
</details>

## 🔜 Siguiente Paso

Ahora aprenderás sobre los manuales del sistema.

[Ir a: 04 - Manuales del Sistema →](./04_manuales_sistema.md)

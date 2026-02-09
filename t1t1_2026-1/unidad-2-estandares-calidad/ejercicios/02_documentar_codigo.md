# 📝 Ejercicio 02: Documentar Código

## Nivel: ⭐ Básico

## 📝 Descripción

El siguiente código Python funciona correctamente pero **carece de documentación**. Tu tarea es agregar toda la documentación necesaria siguiendo los estándares de calidad.

## 🎯 Objetivo

Practicar las técnicas de documentación interna: encabezados, docstrings y comentarios.

## 📋 Código a Documentar

```python
def f(t, h):
    if t < -10:
        return "Extremadamente frío"
    elif t < 0:
        return "Muy frío"
    elif t < 10:
        return "Frío"
    elif t < 20:
        if h > 80:
            return "Templado húmedo"
        return "Templado"
    elif t < 30:
        if h > 70:
            return "Caluroso húmedo"
        return "Caluroso"
    else:
        return "Muy caluroso"

def main():
    temp = float(input("Temperatura: "))
    hum = float(input("Humedad: "))
    r = f(temp, hum)
    print(f"Clima: {r}")

if __name__ == "__main__":
    main()
```

## 📝 Requisitos de Documentación

### 1. Encabezado del Archivo
- Nombre del programa
- Autor
- Fecha
- Descripción
- Instrucciones de uso

### 2. Documentación de Funciones (Docstrings)
- Descripción de qué hace
- Parámetros (Args)
- Valor de retorno (Returns)
- Ejemplos de uso

### 3. Comentarios de Línea
- Explicar decisiones de diseño
- Aclarar lógica compleja

### 4. Mejoras Adicionales
- Renombrar variables con nombres descriptivos
- Agregar constantes si es necesario
- Organizar el código en secciones

## 📤 Formato de Entrega

Entrega el archivo Python completamente documentado como `ejercicio_02.py`

## ✅ Criterios de Evaluación

| Criterio | Puntos |
|----------|--------|
| Encabezado completo | 20 |
| Docstrings correctos | 30 |
| Comentarios útiles | 20 |
| Nombres descriptivos | 15 |
| Organización del código | 15 |

## 💡 Ejemplo de Docstring

```python
def calcular_area(base, altura):
    """
    Calcula el área de un rectángulo.
    
    Args:
        base (float): La base del rectángulo
        altura (float): La altura del rectángulo
    
    Returns:
        float: El área calculada (base × altura)
    
    Example:
        >>> calcular_area(5, 3)
        15.0
    """
    return base * altura
```

# 🎂 Ejercicio 1: Edad Válida

## Dificultad: ⭐ Básico

## 📝 Descripción

Crea un programa que pida la edad de una persona y verifique si es válida, además de determinar si es menor o mayor de edad.

## 🎯 Objetivo

Practicar el uso de `if-elif-else` con múltiples condiciones.

## 📋 Especificaciones

El programa debe:

1. Solicitar la edad al usuario
2. Validar y clasificar la edad según estos criterios:
   - **Menor a 0**: "Edad no válida"
   - **Entre 0 y 17**: "Eres menor de edad"
   - **Entre 18 y 120**: "Eres mayor de edad"
   - **Mayor a 120**: "Edad no válida"

## 💻 Ejemplo de Ejecución

### Ejemplo 1:
```
Ingresa tu edad: 25
Eres mayor de edad
```

### Ejemplo 2:
```
Ingresa tu edad: 15
Eres menor de edad
```

### Ejemplo 3:
```
Ingresa tu edad: -5
Edad no válida
```

### Ejemplo 4:
```
Ingresa tu edad: 150
Edad no válida
```

## 🧪 Casos de Prueba

Prueba tu programa con estos valores:

| Entrada | Salida Esperada |
|---------|----------------|
| -1 | Edad no válida |
| 0 | Eres menor de edad |
| 17 | Eres menor de edad |
| 18 | Eres mayor de edad |
| 25 | Eres mayor de edad |
| 120 | Eres mayor de edad |
| 121 | Edad no válida |

## 💡 Pistas

1. Usa `int(input())` para leer la edad
2. Piensa en el orden de las condiciones
3. Los rangos pueden expresarse de dos formas:
   - `edad >= 0 and edad <= 17`
   - `0 <= edad <= 17` (más elegante en Python)

## ⚠️ Errores Comunes

- ❌ No validar edades negativas
- ❌ No validar edades muy altas (>120)
- ❌ Confundir los límites (¿17 es menor o 18 es menor?)

## 🎓 Conceptos Practicados

- `if-elif-else`
- Comparaciones con `<`, `<=`, `>=`, `>`
- Rangos numéricos
- Validación de entrada

## 🚀 Desafíos Extra (Opcional)

1. Agrega categorías más detalladas (niño, adolescente, adulto, adulto mayor)
2. Maneja el caso donde el usuario ingrese texto en lugar de un número
3. Agrega emojis a cada mensaje

---

**Tiempo estimado**: 10-15 minutos  
**Archivo de solución**: `ejercicio_01.py`


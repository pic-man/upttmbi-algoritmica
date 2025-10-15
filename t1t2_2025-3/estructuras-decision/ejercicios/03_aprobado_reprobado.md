# 🎓 Ejercicio 3: Aprobado o Reprobado

## Dificultad: ⭐ Básico

## 📝 Descripción

Crea un programa que pida una calificación (0-10) y determine si el estudiante aprobó o reprobó.

## 🎯 Objetivo

Practicar condicionales simples con validación de rangos.

## 📋 Especificaciones

El programa debe:

1. Solicitar una calificación entre 0 y 10
2. Determinar el resultado según estos criterios:
   - **Mayor o igual a 6**: "Aprobado ✅"
   - **Menor a 6**: "Reprobado ❌"

## 💻 Ejemplo de Ejecución

### Ejemplo 1:
```
Ingresa tu calificación (0-10): 8
¡Aprobado! ✅
Tu calificación es: 8
```

### Ejemplo 2:
```
Ingresa tu calificación (0-10): 5
Reprobado ❌
Tu calificación es: 5
```

### Ejemplo 3:
```
Ingresa tu calificación (0-10): 6
¡Aprobado! ✅
Tu calificación es: 6
```

## 🧪 Casos de Prueba

Prueba tu programa con estos valores:

| Entrada | Resultado |
|---------|-----------|
| 0 | Reprobado ❌ |
| 5 | Reprobado ❌ |
| 5.9 | Reprobado ❌ |
| 6 | Aprobado ✅ |
| 7 | Aprobado ✅ |
| 10 | Aprobado ✅ |

## 💡 Pistas

1. Usa `float(input())` para aceptar decimales (ej: 5.5)
2. La condición de aprobado es `calificacion >= 6`
3. No necesitas `elif`, solo `if-else`

## ⚠️ Errores Comunes

- ❌ Confundir >= con > (6 debe aprobar)
- ❌ No aceptar calificaciones decimales
- ❌ No validar que la nota esté entre 0 y 10

## 🎓 Conceptos Practicados

- `if-else` simple
- Comparaciones con `>=` y `<`
- Lectura de números decimales

## 🚀 Desafíos Extra (Opcional)

1. Agrega validación: la nota debe estar entre 0 y 10
2. Agrega más categorías:
   - 9-10: Excelente
   - 7-8.9: Bien
   - 6-6.9: Suficiente
   - 0-5.9: Reprobado
3. Muestra un mensaje motivacional según la nota

---

**Tiempo estimado**: 5-10 minutos  
**Archivo de solución**: `ejercicio_03.py`


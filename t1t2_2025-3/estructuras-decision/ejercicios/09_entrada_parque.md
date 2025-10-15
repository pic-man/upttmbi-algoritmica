# 🎟️ Ejercicio 9: Entrada al Parque

## Dificultad: ⭐ Básico

## 📝 Descripción

Crea un programa que pida la estatura en centímetros y determine si la persona puede subir a una atracción del parque.

## 🎯 Objetivo

Practicar condicionales simples con comparaciones numéricas.

## 📋 Especificaciones

El programa debe:

1. Solicitar la estatura en centímetros
2. Determinar según:
   - **Menor a 120 cm**: "No puedes subir a la atracción"
   - **120 cm o más**: "Puedes subir a la atracción 🎢"

## 💻 Ejemplo de Ejecución

### Ejemplo 1:
```
Ingresa tu estatura en cm: 125
¡Puedes subir a la atracción! 🎢
Tu estatura: 125 cm
```

### Ejemplo 2:
```
Ingresa tu estatura en cm: 110
Lo sentimos, no puedes subir a la atracción
Estatura mínima requerida: 120 cm
Tu estatura: 110 cm
Te faltan: 10 cm
```

### Ejemplo 3:
```
Ingresa tu estatura en cm: 120
¡Puedes subir a la atracción! 🎢
Tu estatura: 120 cm (estatura mínima)
```

## 🧪 Casos de Prueba

Prueba tu programa con estos valores:

| Entrada | Resultado |
|---------|-----------|
| 100 | No puedes subir |
| 119 | No puedes subir |
| 120 | Puedes subir 🎢 |
| 150 | Puedes subir 🎢 |
| 200 | Puedes subir 🎢 |

## 💡 Pistas

1. Usa `int(input())` o `float(input())` según prefieras
2. La condición es muy simple: `estatura >= 120`
3. Es un buen ejercicio para practicar `if-else` básico

## ⚠️ Errores Comunes

- ❌ Confundir >= con > (120 debe permitir subir)
- ❌ No validar estaturas negativas o muy grandes
- ❌ No mostrar mensajes claros al usuario

## 🎓 Conceptos Practicados

- `if-else` simple
- Comparación con `>=`
- Validación de requisitos mínimos

## 🚀 Desafíos Extra (Opcional)

1. Muestra cuántos cm le faltan para subir (si no puede)
2. Agrega diferentes atracciones con diferentes requisitos:
   - Montaña rusa: 120 cm
   - Rueda de la fortuna: 100 cm
   - Casa del terror: 140 cm
3. Considera la edad además de la estatura:
   - Menores de 12 años necesitan adulto
   - Adultos de cualquier estatura pueden subir
4. Calcula el precio del boleto según la edad:
   - Niños (< 12): $5
   - Adultos: $10
   - Mayores (> 65): $7

---

**Tiempo estimado**: 5-10 minutos  
**Archivo de solución**: `ejercicio_09.py`


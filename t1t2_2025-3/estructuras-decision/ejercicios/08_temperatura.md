# 🌡️ Ejercicio 8: Fiebre o No

## Dificultad: ⭐ Básico

## 📝 Descripción

Crea un programa que pida la temperatura corporal en grados Celsius y determine si la persona tiene fiebre, hipotermia o temperatura normal.

## 🎯 Objetivo

Practicar rangos numéricos con valores médicos.

## 📋 Especificaciones

El programa debe:

1. Solicitar la temperatura corporal en °C
2. Clasificar según:
   - **Menor a 36**: "Hipotermia 🥶"
   - **36 a 37.5**: "Temperatura normal 😊"
   - **Mayor a 37.5**: "Tienes fiebre 🤒"

## 💻 Ejemplo de Ejecución

### Ejemplo 1:
```
Ingresa tu temperatura corporal (°C): 36.5
Temperatura normal 😊
Tu temperatura es: 36.5°C
```

### Ejemplo 2:
```
Ingresa tu temperatura corporal (°C): 38.2
¡Tienes fiebre! 🤒
Tu temperatura es: 38.2°C
Recomendación: Consulta a un médico
```

### Ejemplo 3:
```
Ingresa tu temperatura corporal (°C): 35.5
¡Hipotermia! 🥶
Tu temperatura es: 35.5°C
Recomendación: Busca atención médica inmediata
```

## 🧪 Casos de Prueba

Prueba tu programa con estos valores:

| Entrada | Clasificación |
|---------|---------------|
| 35.0 | Hipotermia 🥶 |
| 35.9 | Hipotermia 🥶 |
| 36.0 | Normal 😊 |
| 36.5 | Normal 😊 |
| 37.0 | Normal 😊 |
| 37.5 | Normal 😊 |
| 37.6 | Fiebre 🤒 |
| 38.5 | Fiebre 🤒 |
| 40.0 | Fiebre 🤒 |

## 💡 Pistas

1. Usa `float(input())` para aceptar decimales
2. La temperatura normal incluye 36 y 37.5 como límites
3. Estructura sugerida:
   ```python
   if temperatura < 36:
       # hipotermia
   elif temperatura <= 37.5:
       # normal
   else:
       # fiebre
   ```

## 📊 Información Adicional

Rangos de temperatura corporal:
- **< 35°C**: Hipotermia severa
- **35-36°C**: Hipotermia leve
- **36-37.5°C**: Temperatura normal
- **37.5-38°C**: Febrícula (fiebre leve)
- **38-40°C**: Fiebre moderada
- **> 40°C**: Fiebre alta (peligrosa)

## ⚠️ Errores Comunes

- ❌ No usar `float` (las temperaturas tienen decimales)
- ❌ Confundir los límites (¿37.5 es normal o fiebre?)
- ❌ No validar temperaturas imposibles (< 30 o > 45)

## 🎓 Conceptos Practicados

- Rangos numéricos con decimales
- Comparaciones con `<`, `<=`, `>`
- Números flotantes (`float`)
- Aplicación práctica en salud

## 🚀 Desafíos Extra (Opcional)

1. Agrega más categorías de fiebre:
   - 37.5-38: Febrícula
   - 38-40: Fiebre moderada
   - > 40: Fiebre alta
2. Valida que la temperatura esté en rango razonable (30-45°C)
3. Permite convertir de Fahrenheit a Celsius
4. Agrega recomendaciones según la temperatura:
   - Normal: "Todo está bien"
   - Febrícula: "Descansa y toma líquidos"
   - Fiebre alta: "Consulta a un médico urgente"

---

**Tiempo estimado**: 10-15 minutos  
**Archivo de solución**: `ejercicio_08.py`


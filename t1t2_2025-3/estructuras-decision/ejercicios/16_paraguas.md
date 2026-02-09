# 🌧️ Ejercicio 16: Necesitas Paraguas

## Dificultad: ⭐ Básico

## 📝 Descripción

Crea un programa que pida el porcentaje de probabilidad de lluvia (0-100) y determine si necesitas llevar paraguas.

## 🎯 Objetivo

Practicar rangos de porcentaje con recomendaciones.

## 📋 Especificaciones

El programa debe:

1. Solicitar el porcentaje de probabilidad de lluvia (0-100)
2. Recomendar según:
   - **Menor a 30%**: "No necesitas paraguas ☀️"
   - **30% a 70%**: "Lleva paraguas por si acaso ⛅"
   - **Mayor a 70%**: "Definitivamente lleva paraguas ☔"

## 💻 Ejemplo de Ejecución

### Ejemplo 1:
```
=== ASISTENTE DE CLIMA ===

¿Cuál es la probabilidad de lluvia? (%): 15

☀️ No necesitas paraguas
Probabilidad de lluvia: 15%
Disfruta del buen clima!
```

### Ejemplo 2:
```
=== ASISTENTE DE CLIMA ===

¿Cuál es la probabilidad de lluvia? (%): 50

⛅ Lleva paraguas por si acaso
Probabilidad de lluvia: 50%
Mejor prevenir que mojarse!
```

### Ejemplo 3:
```
=== ASISTENTE DE CLIMA ===

¿Cuál es la probabilidad de lluvia? (%): 85

☔ Definitivamente lleva paraguas
Probabilidad de lluvia: 85%
¡Muy probable que llueva! No olvides tu paraguas.
```

## 🧪 Casos de Prueba

Prueba tu programa con estos valores:

| Probabilidad | Recomendación |
|--------------|---------------|
| 0% | No necesitas ☀️ |
| 29% | No necesitas ☀️ |
| 30% | Por si acaso ⛅ |
| 50% | Por si acaso ⛅ |
| 70% | Por si acaso ⛅ |
| 71% | Definitivamente ☔ |
| 100% | Definitivamente ☔ |

## 💡 Pistas

1. Usa `int(input())` o `float(input())`
2. Estructura de rangos:
   ```python
   if probabilidad < 30:
       # no necesitas
   elif probabilidad <= 70:
       # por si acaso
   else:
       # definitivamente
   ```

3. Los límites clave son 30% y 70%

## ⚠️ Errores Comunes

- ❌ No validar que esté entre 0-100
- ❌ Confundir los límites (¿30% necesita o no?)
- ❌ No considerar valores decimales (45.5%)

## 🎓 Conceptos Practicados

- Rangos de porcentaje
- `if-elif-else` con 3 opciones
- Validación de rangos (0-100)
- Aplicación práctica

## 🌦️ Escala de Probabilidad

| % | Descripción | Recomendación |
|---|-------------|---------------|
| 0-10% | Muy improbable | Ni lo pienses |
| 10-30% | Poco probable | No necesario |
| 30-50% | Posible | Lleva por si acaso |
| 50-70% | Probable | Mejor llevarlo |
| 70-90% | Muy probable | Definitivamente |
| 90-100% | Casi seguro | ¡Imprescindible! |

## 🚀 Desafíos Extra (Opcional)

1. **Validación estricta**:
   - No aceptar valores fuera de 0-100
   - Muestra mensaje de error específico

2. **Más detalles climáticos**:
   - Pregunta la temperatura
   - Pregunta si hay viento
   - Recomienda además: abrigo, sombrero, etc.

3. **Niveles más detallados**:
   ```
   0-20%: Definitivamente no
   20-40%: Probablemente no, pero llévalo en el carro
   40-60%: Llévalo en la mochila
   60-80%: Llévalo en la mano
   80-100%: Úsalo desde que sales de casa
   ```

4. **Forecast completo**:
   ```
   Probabilidad: 65%
   
   Hora  | Prob | Recomendación
   ------|------|---------------
   08:00 | 30%  | No necesario
   12:00 | 50%  | Lleva por si acaso
   16:00 | 80%  | Definitivamente
   20:00 | 40%  | Puede guardarlo
   ```

5. **Alternativas**:
   - Si no tienes paraguas: recomendar impermeable
   - Calcular si vale la pena comprar uno
   - Sugerir esperar a que pase la lluvia

6. **Histórico**:
   - Compara con mismo día del año pasado
   - Precisión de pronósticos anteriores

---

**Tiempo estimado**: 10-15 minutos  
**Archivo de solución**: `ejercicio_16.py`


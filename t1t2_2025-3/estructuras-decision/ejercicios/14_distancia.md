# 🚶 Ejercicio 14: Distancia a Recorrer

## Dificultad: ⭐⭐ Intermedio

## 📝 Descripción

Crea un programa que pida la distancia en kilómetros y sugiera el medio de transporte más apropiado.

## 🎯 Objetivo

Practicar rangos numéricos con recomendaciones prácticas.

## 📋 Especificaciones

El programa debe:

1. Solicitar la distancia en kilómetros
2. Sugerir transporte según:
   - **Menor a 1 km**: "Ve caminando 🚶"
   - **1 a 5 km**: "Ve en bicicleta 🚲"
   - **5 a 20 km**: "Ve en auto 🚗"
   - **Más de 20 km**: "Ve en transporte público 🚌"

## 💻 Ejemplo de Ejecución

### Ejemplo 1:
```
=== RECOMENDADOR DE TRANSPORTE ===

¿Cuál es la distancia a recorrer? (km): 0.5

🚶 RECOMENDACIÓN: Ve caminando
Distancia: 0.5 km
Tiempo estimado: 6 minutos
Calorías quemadas: ~35 cal
Ventajas: Gratis, saludable, eco-friendly
```

### Ejemplo 2:
```
=== RECOMENDADOR DE TRANSPORTE ===

¿Cuál es la distancia a recorrer? (km): 3

🚲 RECOMENDACIÓN: Ve en bicicleta
Distancia: 3.0 km
Tiempo estimado: 12 minutos
Calorías quemadas: ~150 cal
Ventajas: Rápido, económico, saludable
```

### Ejemplo 3:
```
=== RECOMENDADOR DE TRANSPORTE ===

¿Cuál es la distancia a recorrer? (km): 15

🚗 RECOMENDACIÓN: Ve en auto
Distancia: 15.0 km
Tiempo estimado: 20 minutos (tráfico moderado)
Costo estimado: $45 (gasolina)
Ventajas: Cómodo, rápido, privado
```

### Ejemplo 4:
```
=== RECOMENDADOR DE TRANSPORTE ===

¿Cuál es la distancia a recorrer? (km): 35

🚌 RECOMENDACIÓN: Ve en transporte público
Distancia: 35.0 km
Tiempo estimado: 50 minutos
Costo estimado: $15 (pasaje)
Ventajas: Económico, relajante, eco-friendly
```

## 🧪 Casos de Prueba

Prueba tu programa con estos valores:

| Distancia | Recomendación |
|-----------|---------------|
| 0.3 | Caminando 🚶 |
| 0.9 | Caminando 🚶 |
| 1.0 | Bicicleta 🚲 |
| 3.0 | Bicicleta 🚲 |
| 5.0 | Bicicleta 🚲 |
| 5.1 | Auto 🚗 |
| 15.0 | Auto 🚗 |
| 20.0 | Auto 🚗 |
| 20.1 | Transporte público 🚌 |
| 50.0 | Transporte público 🚌 |

## 💡 Pistas

1. Usa `float(input())` para aceptar decimales
2. Estructura de rangos:
   ```python
   if distancia < 1:
       # caminando
   elif distancia <= 5:
       # bicicleta
   elif distancia <= 20:
       # auto
   else:
       # transporte público
   ```

3. Los límites clave son: 1, 5 y 20 km

## 📊 Tabla Comparativa

| Transporte | Distancia | Tiempo | Costo | Calorías |
|------------|-----------|--------|-------|----------|
| 🚶 Caminando | < 1 km | 12 min/km | Gratis | ~70 cal/km |
| 🚲 Bicicleta | 1-5 km | 4 min/km | Gratis | ~50 cal/km |
| 🚗 Auto | 5-20 km | 1.5 min/km | $3/km | 0 |
| 🚌 Bus | > 20 km | 2 min/km | $0.50/km | 0 |

## ⚠️ Errores Comunes

- ❌ No validar distancias negativas
- ❌ Confundir los límites (¿1 km es caminar o bicicleta?)
- ❌ No considerar el caso de 0 km
- ❌ No usar `float` para decimales

## 🎓 Conceptos Practicados

- Rangos numéricos con `float`
- `if-elif-else` con 4 opciones
- Aplicación práctica de decisiones
- Estimaciones y cálculos

## 🚀 Desafíos Extra (Opcional)

1. **Múltiples opciones**:
   - Muestra 2-3 alternativas en lugar de solo 1
   - Compara ventajas/desventajas

2. **Factores adicionales**:
   - Pregunta si llueve (no recomendar bicicleta)
   - Hora del día (tráfico en hora pico)
   - Presupuesto disponible
   - Condición física (¿puede caminar/pedalear?)

3. **Cálculos detallados**:
   ```python
   # Caminando: 5 km/h
   # Bicicleta: 15 km/h
   # Auto: 40 km/h (promedio con tráfico)
   # Bus: 30 km/h (con paradas)
   ```

4. **Comparación ambiental**:
   - Huella de carbono de cada opción
   - Recomienda opción más eco-friendly

5. **Combinación de transportes**:
   - Caminar 0.5km + Bus 15km + Caminar 0.3km
   - Optimiza tiempo y costo

6. **Mapa ASCII**:
   ```
   [Casa] --0.5km-- [Paradero] --15km-- [Metro] --0.3km-- [Destino]
   ```

---

**Tiempo estimado**: 15-20 minutos  
**Archivo de solución**: `ejercicio_14.py`


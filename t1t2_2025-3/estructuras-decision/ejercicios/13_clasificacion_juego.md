# 🎮 Ejercicio 13: Clasificación de Videojuego

## Dificultad: ⭐⭐ Intermedio

## 📝 Descripción

Crea un programa que pida la edad del jugador y recomiende la clasificación apropiada de videojuegos según el sistema ESRB.

## 🎯 Objetivo

Practicar rangos de edad con recomendaciones específicas.

## 📋 Especificaciones

El programa debe:

1. Solicitar la edad del jugador
2. Recomendar clasificación según:
   - **Menor a 7 años**: "Clasificación E (Everyone)"
   - **7 a 12 años**: "Clasificación E10+ (Everyone 10+)"
   - **13 a 17 años**: "Clasificación T (Teen)"
   - **18 años o más**: "Clasificación M (Mature)"

## 💻 Ejemplo de Ejecución

### Ejemplo 1:
```
=== CLASIFICACIÓN DE VIDEOJUEGOS ===

Ingresa tu edad: 5

Tu clasificación recomendada:
📗 CLASIFICACIÓN E (Everyone)

Descripción: Contenido apto para todas las edades
Ejemplos de juegos:
- Mario Kart
- Minecraft
- Animal Crossing
```

### Ejemplo 2:
```
=== CLASIFICACIÓN DE VIDEOJUEGOS ===

Ingresa tu edad: 15

Tu clasificación recomendada:
📙 CLASIFICACIÓN T (Teen)

Descripción: Contenido apto para mayores de 13 años
Puede contener: violencia leve, lenguaje moderado
Ejemplos de juegos:
- Fortnite
- Rocket League
- Splatoon
```

### Ejemplo 3:
```
=== CLASIFICACIÓN DE VIDEOJUEGOS ===

Ingresa tu edad: 20

Tu clasificación recomendada:
📕 CLASIFICACIÓN M (Mature)

Descripción: Contenido apto solo para adultos (18+)
Puede contener: violencia intensa, lenguaje fuerte, contenido adulto
Ejemplos de juegos:
- Grand Theft Auto V
- Call of Duty
- The Last of Us
```

## 🧪 Casos de Prueba

Prueba tu programa con estos valores:

| Edad | Clasificación |
|------|---------------|
| 3 | E (Everyone) |
| 6 | E (Everyone) |
| 7 | E10+ (Everyone 10+) |
| 10 | E10+ (Everyone 10+) |
| 12 | E10+ (Everyone 10+) |
| 13 | T (Teen) |
| 17 | T (Teen) |
| 18 | M (Mature) |
| 25 | M (Mature) |

## 💡 Pistas

1. Estructura de rangos:
   ```python
   if edad < 7:
       # E
   elif edad <= 12:
       # E10+
   elif edad <= 17:
       # T
   else:
       # M
   ```

2. Los límites importantes son: 7, 13, y 18

## 📊 Sistema de Clasificación ESRB

| Símbolo | Nombre | Edad | Contenido |
|---------|--------|------|-----------|
| E | Everyone | Todas | Contenido mínimo |
| E10+ | Everyone 10+ | 10+ | Violencia/lenguaje leve |
| T | Teen | 13+ | Violencia/lenguaje moderado |
| M | Mature | 18+ | Violencia/contenido intenso |
| AO | Adults Only | 18+ | Contenido extremo |

## ⚠️ Errores Comunes

- ❌ Confundir los límites de edad
- ❌ No considerar el límite exacto (¿7 es E o E10+?)
- ❌ No validar edades negativas o muy altas

## 🎓 Conceptos Practicados

- Rangos de edad
- `if-elif-else` con 4 opciones
- Sistemas de clasificación
- Validación de entrada

## 🎮 Información Extra

**¿Qué es ESRB?**
Entertainment Software Rating Board - organización que clasifica videojuegos según su contenido.

**Otras clasificaciones**:
- **EC (Early Childhood)**: Para preescolar
- **E (Everyone)**: Para todos
- **E10+ (Everyone 10+)**: Para mayores de 10
- **T (Teen)**: Para adolescentes (13+)
- **M (Mature)**: Para adultos (17+)
- **AO (Adults Only)**: Solo adultos (18+)

## 🚀 Desafíos Extra (Opcional)

1. **Clasificación detallada**:
   - Agrega EC (Early Childhood) para < 3 años
   - Agrega AO (Adults Only) para juegos extremos

2. **Descriptores de contenido**:
   - Pregunta qué tipo de juego busca (acción, aventura, etc.)
   - Recomienda juegos específicos de esa categoría

3. **Control parental**:
   - Para menores, pide permiso de un adulto
   - Muestra advertencia sobre contenido

4. **Comparador de regiones**:
   - ESRB (América)
   - PEGI (Europa)
   - CERO (Japón)
   - Muestra equivalencias

5. **Base de datos**:
   ```python
   juegos = {
       "E": ["Mario Kart", "Minecraft", "Animal Crossing"],
       "E10+": ["Sonic", "Pokemon", "Splatoon"],
       "T": ["Fortnite", "Rocket League", "Halo"],
       "M": ["GTA V", "Call of Duty", "The Last of Us"]
   }
   ```

---

**Tiempo estimado**: 15-20 minutos  
**Archivo de solución**: `ejercicio_13.py`


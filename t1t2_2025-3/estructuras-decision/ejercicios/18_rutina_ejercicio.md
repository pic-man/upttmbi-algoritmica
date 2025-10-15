# 🏋️ Ejercicio 18: Rutina de Ejercicio

## Dificultad: ⭐ Básico

## 📝 Descripción

Crea un programa que pida el nivel de condición física y recomiende una rutina de ejercicio apropiada.

## 🎯 Objetivo

Practicar comparación de strings con recomendaciones personalizadas.

## 📋 Especificaciones

El programa debe:

1. Solicitar el nivel de condición física
2. Recomendar rutina según:
   - **Principiante**: "20 minutos de cardio ligero"
   - **Intermedio**: "30 minutos de cardio + pesas"
   - **Avanzado**: "60 minutos de entrenamiento intenso"
   - **Otro**: "Nivel no válido"

## 💻 Ejemplo de Ejecución

### Ejemplo 1:
```
=== GENERADOR DE RUTINA DE EJERCICIO ===

Niveles disponibles: principiante, intermedio, avanzado

¿Cuál es tu nivel? principiante

🏃 RUTINA PARA PRINCIPIANTE

Duración: 20 minutos
Intensidad: Ligera

Tu rutina de hoy:
1. Calentamiento (5 min)
   - Caminata suave
   - Estiramientos básicos

2. Cardio (10 min)
   - Caminata rápida
   - O bicicleta suave

3. Enfriamiento (5 min)
   - Caminata lenta
   - Estiramientos

💡 Consejo: Mantén este ritmo por 2-3 semanas antes de aumentar intensidad
```

### Ejemplo 2:
```
=== GENERADOR DE RUTINA DE EJERCICIO ===

Niveles disponibles: principiante, intermedio, avanzado

¿Cuál es tu nivel? avanzado

🏋️ RUTINA PARA AVANZADO

Duración: 60 minutos
Intensidad: Alta

Tu rutina de hoy:
1. Calentamiento (10 min)
   - Trote ligero
   - Movilidad articular
   - Estiramientos dinámicos

2. Cardio HIIT (20 min)
   - 8 intervalos de 2 min
   - 1 min intenso + 1 min recuperación

3. Entrenamiento de fuerza (25 min)
   - Sentadillas: 4x12
   - Press de banca: 4x10
   - Peso muerto: 4x8
   - Dominadas: 4x8

4. Enfriamiento (5 min)
   - Trote suave
   - Estiramientos profundos

💡 Consejo: Mantén buena hidratación y descansa 48h entre sesiones intensas
```

## 🧪 Casos de Prueba

Prueba tu programa con estos valores:

| Entrada | Rutina |
|---------|--------|
| principiante | 20 min cardio ligero |
| Principiante | 20 min cardio ligero |
| intermedio | 30 min cardio + pesas |
| avanzado | 60 min intenso |
| experto | Nivel no válido |
| novato | Nivel no válido |

## 💡 Pistas

1. Normaliza la entrada:
   ```python
   nivel = input("Nivel: ").lower()
   ```

2. Estructura simple con `if-elif-else`

3. Puedes agregar más detalles para cada nivel

## 📊 Guía de Niveles

| Nivel | Duración | Intensidad | Frecuencia |
|-------|----------|------------|------------|
| Principiante | 20-30 min | Baja-Media | 3x/semana |
| Intermedio | 30-45 min | Media-Alta | 4x/semana |
| Avanzado | 45-90 min | Alta | 5-6x/semana |

## ⚠️ Errores Comunes

- ❌ No normalizar a minúsculas
- ❌ No validar niveles incorrectos
- ❌ No mostrar los niveles disponibles
- ❌ Recomendar rutinas muy difíciles para principiantes

## 🎓 Conceptos Practicados

- Comparación de strings
- Normalización con `.lower()`
- `if-elif-else` con strings
- Recomendaciones personalizadas

## 💪 Información de Fitness

**Principiante**:
- Nuevo en ejercicio o más de 6 meses sin entrenar
- Enfoque en formar el hábito
- Técnica sobre intensidad

**Intermedio**:
- 3-12 meses entrenando regularmente
- Puede hacer rutinas completas
- Conoce técnicas básicas

**Avanzado**:
- Más de 1 año entrenando
- Conocimiento profundo de técnicas
- Puede manejar alta intensidad

## 🚀 Desafíos Extra (Opcional)

1. **Objetivos específicos**:
   - Pregunta objetivo: perder peso, ganar músculo, resistencia
   - Adapta la rutina según objetivo

2. **Días de entrenamiento**:
   - Genera rutina diferente para cada día de la semana
   - Lunes: piernas, Martes: pecho, etc.

3. **Limitaciones físicas**:
   - Pregunta si tiene lesiones
   - Adapta ejercicios (sin rodillas, sin espalda, etc.)

4. **Equipo disponible**:
   - Casa (sin equipo)
   - Casa (con pesas)
   - Gimnasio completo

5. **Progresión**:
   ```
   Semana 1-2: Principiante básico
   Semana 3-4: Principiante intermedio
   Semana 5-6: Transición a intermedio
   ```

6. **Calculadora de calorías**:
   - Estima calorías quemadas por sesión
   - Según peso, edad, intensidad

7. **Plan completo**:
   ```
   Lunes: Fuerza superior
   Martes: Cardio
   Miércoles: Descanso
   Jueves: Fuerza inferior
   Viernes: HIIT
   Sábado: Yoga/Flexibilidad
   Domingo: Descanso
   ```

---

**Tiempo estimado**: 10-15 minutos  
**Archivo de solución**: `ejercicio_18.py`


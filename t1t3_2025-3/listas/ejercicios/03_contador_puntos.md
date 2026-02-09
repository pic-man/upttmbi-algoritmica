# 🎯 Ejercicio 3: Contador de Puntos

## Dificultad: ⭐ Básico

## 📝 Descripción

Tienes una lista de puntuaciones de un videojuego. Descubre cuántas veces obtuviste 100 puntos y en qué ronda fue la primera vez.

## 🎯 Objetivo

Practicar los métodos `count()` e `index()`.

## 📋 Especificaciones

1. Usar la lista de puntuaciones dada
2. Contar cuántas veces aparece 100
3. Encontrar en qué posición (ronda) fue la primera vez
4. Mostrar resultados

## 💻 Lista Inicial

```python
puntuaciones = [50, 100, 75, 100, 90, 100, 85, 100]
```

## 💻 Ejemplo de Ejecución

```
=== ANÁLISIS DE PUNTUACIONES ===

Puntuaciones: [50, 100, 75, 100, 90, 100, 85, 100]

🎯 Puntaje perfecto (100 puntos):
   - Conseguido: 4 veces
   - Primera vez: Ronda 2 (índice 1)

📊 Estadísticas adicionales:
   - Total de rondas: 8
   - Puntaje máximo: 100
   - Puntaje mínimo: 50
   - Promedio: 81.25
```

## 🧪 Casos de Prueba

Verifica:
- [ ] Cuenta correctamente las veces que aparece 100
- [ ] Encuentra el índice correcto de la primera aparición
- [ ] Maneja el caso si el valor no existe

## 💡 Pistas

1. `count(100)` cuenta las ocurrencias
2. `index(100)` encuentra la primera posición
3. Los índices empiezan en 0, pero las rondas en 1

## 🚀 Desafíos Extra

1. Encuentra todas las posiciones donde aparece 100
2. Calcula el porcentaje de rondas perfectas
3. Muestra un gráfico ASCII de las puntuaciones

---

**Tiempo estimado**: 10 minutos  
**Archivo de solución**: `ejercicio_03.py`


# 🏆 Ejercicio 6: Ranking de Jugadores

## Dificultad: ⭐⭐ Intermedio

## 📝 Descripción

Tienes una lista de puntajes desordenados. Crea un ranking de mayor a menor y muestra los 3 primeros lugares (medallistas de oro, plata y bronce).

## 🎯 Objetivo

Practicar `sort()` y slicing `[:]`.

## 📋 Especificaciones

1. Usar la lista de puntajes dada
2. Ordenar de mayor a menor
3. Mostrar el top 3 (podio)
4. Manejar empates correctamente

## 💻 Lista Inicial

```python
puntajes = [450, 890, 320, 670, 1200, 550, 890]
```

## 💻 Ejemplo de Ejecución

```
=== RANKING DE JUGADORES ===

Puntajes originales: [450, 890, 320, 670, 1200, 550, 890]

Ordenando de mayor a menor...

🏆 PODIO 🏆

🥇 MEDALLA DE ORO
   Puntaje: 1200

🥈 MEDALLA DE PLATA
   Puntaje: 890

🥉 MEDALLA DE BRONCE
   Puntaje: 890

⚠️ ¡Empate en plata! Dos jugadores con 890 puntos

📊 RANKING COMPLETO:
1º - 1200 puntos 🏆
2º - 890 puntos 🥈
3º - 890 puntos 🥈
4º - 670 puntos
5º - 550 puntos
6º - 450 puntos
7º - 320 puntos

Total de participantes: 7
Puntaje promedio: 710.0
```

## 🧪 Casos de Prueba

Verifica:
- [ ] Ordena correctamente de mayor a menor
- [ ] Muestra los 3 primeros
- [ ] Detecta empates
- [ ] El ranking completo es correcto

## 💡 Pistas

1. `sort(reverse=True)` ordena descendente
2. `lista[:3]` obtiene los primeros 3 elementos
3. Usa `set()` para detectar duplicados/empates

## 🚀 Desafíos Extra

1. Agrega nombres de jugadores (usa diccionarios o tuplas)
2. Calcula percentiles (top 10%, top 25%, etc.)
3. Muestra gráfico de barras ASCII
4. Detecta el salto de puntaje más grande

---

**Tiempo estimado**: 15-20 minutos  
**Archivo de solución**: `ejercicio_06.py`


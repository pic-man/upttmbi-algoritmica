# 🎲 Ejercicio 21: Juego de Batalla por Turnos

## Dificultad: ⭐⭐⭐ Avanzado (BONUS)

## 📝 Descripción

Crea un sistema de batalla donde dos listas representan equipos de personajes que atacan por turnos. El personaje que sobrevive vuelve al final, el que muere es eliminado.

## 🎯 Objetivo

Sistema de juego completo con lógica de batalla y gestión de listas.

## 💻 Configuración Inicial

```python
import random

equipo_a = ["Guerrero", "Mago", "Arquero"]
equipo_b = ["Orco", "Goblin", "Troll"]

# Cada personaje tiene 100 HP
# Daño aleatorio: 20-50 puntos
```

## 📋 Sistema a Implementar

El juego debe:
1. Mostrar estado de ambos equipos
2. Primer personaje de cada equipo ataca
3. Calcular daño aleatorio (20-50)
4. Si sobrevive → vuelve al final de su equipo
5. Si muere → es eliminado
6. Termina cuando un equipo se queda sin personajes

## 💻 Ejemplo de Ejecución

```
=== BATALLA POR TURNOS ===

EQUIPO A: [Guerrero(100), Mago(100), Arquero(100)]
EQUIPO B: [Orco(100), Goblin(100), Troll(100)]

━━━━━━━━━━━━━━━━━━━━━━
RONDA 1
━━━━━━━━━━━━━━━━━━━━━━

⚔️ Guerrero (100 HP) ataca a Orco (100 HP)
💥 Daño: 35
❤️ Orco ahora tiene: 65 HP
✓ Orco sobrevive y vuelve al final

⚔️ Orco (65 HP) ataca a Guerrero (100 HP)
💥 Daño: 42
❤️ Guerrero ahora tiene: 58 HP
✓ Guerrero sobrevive y vuelve al final

EQUIPO A: [Mago(100), Arquero(100), Guerrero(58)]
EQUIPO B: [Goblin(100), Troll(100), Orco(65)]

━━━━━━━━━━━━━━━━━━━━━━
RONDA 2
━━━━━━━━━━━━━━━━━━━━━━

⚔️ Mago (100 HP) ataca a Goblin (100 HP)
💥 Daño: 48
❤️ Goblin ahora tiene: 52 HP

⚔️ Goblin (52 HP) ataca a Mago (100 HP)
💥 Daño: 50
❤️ Mago ahora tiene: 50 HP

[... continúa hasta que un equipo pierda ...]

━━━━━━━━━━━━━━━━━━━━━━
FIN DE LA BATALLA
━━━━━━━━━━━━━━━━━━━━━━

🏆 ¡EQUIPO A GANA!

Sobrevivientes:
- Guerrero (12 HP)
- Arquero (34 HP)

Rondas totales: 8
```

## 💡 Pistas

1. Usa diccionarios para HP: `{"Guerrero": 100}`
2. `pop(0)` para sacar el primero de cada equipo
3. `append()` al final si sobrevive
4. `random.randint(20, 50)` para daño
5. Bucle `while len(equipo_a) > 0 and len(equipo_b) > 0`

## 🚀 Desafíos Extra

1. Habilidades especiales de cada personaje
2. Probabilidad de crítico (daño x2)
3. Sistema de defensa/esquive
4. Objetos curativos
5. Múltiples rondas (best of 3)

---

**Tiempo estimado**: 90+ minutos  
**Archivo de solución**: `ejercicio_21.py`

---

## 🎉 ¡FELICIDADES!

Si completaste este ejercicio, has dominado las listas en Python. Este es el ejercicio más complejo y combina todo lo aprendido.

**Habilidades adquiridas:**
- ✅ Manipulación avanzada de listas
- ✅ Lógica de juego
- ✅ Gestión de estado
- ✅ Bucles complejos
- ✅ Estructuras de datos combinadas

¡Estás listo para proyectos más grandes! 🚀


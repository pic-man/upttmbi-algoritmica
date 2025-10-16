# 🎲 Ejercicio 9: Juego de Dados

## Dificultad: ⭐⭐ Intermedio

## 📝 Descripción

Simula 20 lanzamientos de dados (números del 1-6). Muestra cuántas veces salió cada número.

## 🎯 Objetivo

Practicar `count()` con números aleatorios.

## 💻 Código Inicial

```python
import random
lanzamientos = [random.randint(1, 6) for _ in range(20)]
```

## 💻 Ejemplo de Ejecución

```
=== JUEGO DE DADOS ===

🎲 20 lanzamientos: [3, 5, 2, 6, 1, 5, 3, 4, 5, 2, 6, 1, 3, 5, 4, 2, 6, 5, 1, 3]

FRECUENCIA DE CADA NÚMERO:

⚀ 1: ███ (3 veces - 15%)
⚁ 2: ███ (3 veces - 15%)
⚂ 3: ████ (4 veces - 20%)
⚃ 4: ██ (2 veces - 10%)
⚄ 5: █████ (5 veces - 25%)
⚅ 6: ███ (3 veces - 15%)

Número más común: 5 (5 veces)
Número menos común: 4 (2 veces)
```

## 💡 Pistas

1. Usa `count()` para cada número del 1 al 6
2. Calcula porcentajes
3. Crea barras con `"█" * cantidad`

---

**Tiempo estimado**: 20 minutos  
**Archivo de solución**: `ejercicio_09.py`


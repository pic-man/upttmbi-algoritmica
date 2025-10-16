# 🎰 Ejercicio 14: Máquina Tragamonedas

## Dificultad: ⭐⭐ Intermedio

## 📝 Descripción

Crea una función que genere 3 símbolos aleatorios. Determina si ganaste: 3 iguales = Jackpot, 2 iguales = Premio menor, todos diferentes = Sin premio.

## 🎯 Objetivo

Practicar `random.choice()` y `count()`.

## 💻 Código Inicial

```python
import random
simbolos_posibles = ["🍒", "🍋", "🔔", "💎", "7️⃣"]
```

## 💻 Ejemplo de Ejecución

```
=== MÁQUINA TRAGAMONEDAS ===

🎰 Girando...

[ 🍒 ] [ 🍒 ] [ 💎 ]

Analizando resultado...

🎁 PREMIO MENOR!
Tienes 2 símbolos iguales (🍒)
Premio: $50

Presiona Enter para jugar de nuevo...

🎰 Girando...

[ 💎 ] [ 💎 ] [ 💎 ]

¡¡¡JACKPOT!!! 💰💰💰
¡3 símbolos iguales!
Premio: $1000
```

## 💡 Pistas

1. Usa `random.choice()` 3 veces
2. Cuenta cada símbolo con `count()`
3. Si alguno tiene count == 3 → Jackpot
4. Si alguno tiene count == 2 → Premio menor
5. Si no → Sin premio

---

**Tiempo estimado**: 20-25 minutos  
**Archivo de solución**: `ejercicio_14.py`


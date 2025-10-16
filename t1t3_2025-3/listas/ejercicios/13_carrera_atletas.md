# 🏃 Ejercicio 13: Carrera de Atletas

## Dificultad: ⭐⭐ Intermedio

## 📝 Descripción

Simula una carrera donde los atletas pueden adelantarse. Modifica el orden según: Bruno adelanta 2 posiciones, Diana adelanta 1 posición.

## 🎯 Objetivo

Practicar `pop()` e `insert()` para reordenar.

## 💻 Lista Inicial

```python
atletas = ["Ana", "Bruno", "Carlos", "Diana", "Elena"]
```

## 💻 Ejemplo de Ejecución

```
=== CARRERA DE ATLETAS ===

Orden inicial:
1º - Ana
2º - Bruno
3º - Carlos
4º - Diana
5º - Elena

⚡ Bruno adelanta 2 posiciones!
   De posición 2 a posición 0

Orden temporal:
1º - Bruno
2º - Ana
3º - Carlos
4º - Diana
5º - Elena

⚡ Diana adelanta 1 posición!
   De posición 4 a posición 3

ORDEN FINAL:
1º - Bruno
2º - Ana
3º - Diana
4º - Carlos
5º - Elena

🏆 Podio:
🥇 Bruno
🥈 Ana
🥉 Diana
```

## 💡 Pistas

1. Usa `index()` para encontrar posición actual
2. Usa `pop(index)` para sacar al atleta
3. Usa `insert(nueva_pos, atleta)` para moverlo
4. Adelantar 2 = restar 2 al índice

---

**Tiempo estimado**: 20 minutos  
**Archivo de solución**: `ejercicio_13.py`


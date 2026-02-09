# 🌙 Ejercicio 6: Turno de Trabajo

## Dificultad: ⭐⭐ Intermedio

## 📝 Descripción

Crea un programa que pida una hora (0-23) y determine el turno de trabajo correspondiente.

## 🎯 Objetivo

Practicar rangos numéricos con horarios.

## 📋 Especificaciones

El programa debe:

1. Solicitar una hora en formato 24 horas (0-23)
2. Determinar el turno según:
   - **6 a 13** (6:00 - 13:59): "Turno matutino ☀️"
   - **14 a 21** (14:00 - 21:59): "Turno vespertino 🌆"
   - **22 a 5** (22:00 - 5:59): "Turno nocturno 🌙"

## 💻 Ejemplo de Ejecución

### Ejemplo 1:
```
Ingresa la hora (0-23): 8
Turno matutino ☀️
```

### Ejemplo 2:
```
Ingresa la hora (0-23): 15
Turno vespertino 🌆
```

### Ejemplo 3:
```
Ingresa la hora (0-23): 23
Turno nocturno 🌙
```

### Ejemplo 4:
```
Ingresa la hora (0-23): 3
Turno nocturno 🌙
```

## 🧪 Casos de Prueba

Prueba tu programa con estos valores:

| Entrada | Turno |
|---------|-------|
| 6 | Matutino ☀️ |
| 13 | Matutino ☀️ |
| 14 | Vespertino 🌆 |
| 21 | Vespertino 🌆 |
| 22 | Nocturno 🌙 |
| 23 | Nocturno 🌙 |
| 0 | Nocturno 🌙 |
| 5 | Nocturno 🌙 |

## 💡 Pistas

1. Ten cuidado con el turno nocturno: abarca de 22 a 23 y de 0 a 5
2. Una opción es:
   ```python
   if 6 <= hora <= 13:
       # matutino
   elif 14 <= hora <= 21:
       # vespertino
   else:
       # nocturno
   ```
3. Otra opción para nocturno:
   ```python
   if (hora >= 22 and hora <= 23) or (hora >= 0 and hora <= 5):
       # nocturno
   ```

## ⚠️ Errores Comunes

- ❌ Olvidar que el turno nocturno va de 22-23 y 0-5 (no es continuo)
- ❌ No validar que la hora esté entre 0-23
- ❌ Confundir los límites (¿13 es matutino o vespertino?)

## 🎓 Conceptos Practicados

- Rangos numéricos con `<=` y `>=`
- Rangos no continuos (turno nocturno)
- Operador `or` para combinar condiciones

## 🚀 Desafíos Extra (Opcional)

1. Agrega validación: hora debe estar entre 0-23
2. Permite ingresar la hora en formato HH:MM (ej: 14:30)
3. Agrega información adicional:
   - Matutino: "Hora de entrada: 6:00"
   - Vespertino: "Hora de entrada: 14:00"
   - Nocturno: "Hora de entrada: 22:00"
4. Calcula cuántas horas faltan para terminar el turno

---

**Tiempo estimado**: 15-20 minutos  
**Archivo de solución**: `ejercicio_06.py`


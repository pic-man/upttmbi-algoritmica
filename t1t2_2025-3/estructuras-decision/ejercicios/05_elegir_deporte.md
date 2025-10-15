# 🏀 Ejercicio 5: Elegir Deporte

## Dificultad: ⭐ Básico

## 📝 Descripción

Crea un programa que pida un número del 1 al 3 y muestre el deporte correspondiente.

## 🎯 Objetivo

Practicar `if-elif-else` con múltiples opciones y validación.

## 📋 Especificaciones

El programa debe:

1. Solicitar un número del 1 al 3
2. Mostrar el deporte según:
   - **1**: "Fútbol ⚽"
   - **2**: "Basquetbol 🏀"
   - **3**: "Natación 🏊"
   - **Otro**: "Opción no válida"

## 💻 Ejemplo de Ejecución

### Ejemplo 1:
```
Elige un deporte:
1. Fútbol ⚽
2. Basquetbol 🏀
3. Natación 🏊

Ingresa tu opción (1-3): 1
Has elegido: Fútbol ⚽
```

### Ejemplo 2:
```
Elige un deporte:
1. Fútbol ⚽
2. Basquetbol 🏀
3. Natación 🏊

Ingresa tu opción (1-3): 2
Has elegido: Basquetbol 🏀
```

### Ejemplo 3:
```
Elige un deporte:
1. Fútbol ⚽
2. Basquetbol 🏀
3. Natación 🏊

Ingresa tu opción (1-3): 5
Opción no válida
```

## 🧪 Casos de Prueba

Prueba tu programa con estos valores:

| Entrada | Salida |
|---------|--------|
| 1 | Fútbol ⚽ |
| 2 | Basquetbol 🏀 |
| 3 | Natación 🏊 |
| 0 | Opción no válida |
| 4 | Opción no válida |
| -1 | Opción no válida |

## 💡 Pistas

1. Usa `int(input())` para leer el número
2. Estructura sugerida:
   ```python
   if opcion == 1:
       # Fútbol
   elif opcion == 2:
       # Basquetbol
   elif opcion == 3:
       # Natación
   else:
       # No válida
   ```
3. Muestra el menú antes de pedir la opción (mejor experiencia de usuario)

## ⚠️ Errores Comunes

- ❌ No validar opciones fuera del rango 1-3
- ❌ Usar `if` múltiples en lugar de `elif`
- ❌ No mostrar el menú de opciones

## 🎓 Conceptos Practicados

- `if-elif-else` con múltiples opciones
- Comparación con `==`
- Validación de entrada
- Menús interactivos

## 🚀 Desafíos Extra (Opcional)

1. Agrega más deportes (5-10 opciones)
2. Después de elegir, muestra información adicional del deporte:
   - Número de jugadores
   - Tipo (individual/equipo)
   - Equipo necesario
3. Permite elegir por nombre en lugar de número
4. Crea un programa que permita elegir múltiples deportes

---

**Tiempo estimado**: 10-15 minutos  
**Archivo de solución**: `ejercicio_05.py`


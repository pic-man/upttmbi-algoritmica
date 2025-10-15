# 🎨 Ejercicio 19: Mezcla de Colores Primarios

## Dificultad: ⭐⭐⭐ Avanzado

## 📝 Descripción

Crea un programa que pida dos colores primarios (rojo, azul, amarillo) y muestre el color resultante de su mezcla.

## 🎯 Objetivo

Practicar múltiples combinaciones con operador `and` y validaciones complejas.

## 📋 Especificaciones

El programa debe:

1. Solicitar dos colores primarios
2. Mostrar el resultado según:
   - **Rojo + Azul**: "Morado 💜"
   - **Rojo + Amarillo**: "Naranja 🧡"
   - **Azul + Amarillo**: "Verde 💚"
   - **Mismo color dos veces**: "No se puede mezclar el mismo color"
   - **Colores no primarios**: "Usa solo colores primarios (rojo, azul, amarillo)"

## 💻 Ejemplo de Ejecución

### Ejemplo 1:
```
=== MEZCLADOR DE COLORES ===

Colores primarios: rojo, azul, amarillo

Primer color: rojo
Segundo color: azul

🎨 RESULTADO: Morado 💜

Mezcla: Rojo + Azul = Morado
Tipo: Color secundario
Uso común: realeza, creatividad, misterio
```

### Ejemplo 2:
```
=== MEZCLADOR DE COLORES ===

Colores primarios: rojo, azul, amarillo

Primer color: amarillo
Segundo color: rojo

🎨 RESULTADO: Naranja 🧡

Mezcla: Amarillo + Rojo = Naranja
Tipo: Color secundario
Uso común: energía, entusiasmo, calidez
```

### Ejemplo 3:
```
=== MEZCLADOR DE COLORES ===

Colores primarios: rojo, azul, amarillo

Primer color: rojo
Segundo color: rojo

❌ Error: No se puede mezclar el mismo color
Por favor, elige dos colores diferentes
```

### Ejemplo 4:
```
=== MEZCLADOR DE COLORES ===

Colores primarios: rojo, azul, amarillo

Primer color: verde
Segundo color: rojo

❌ Error: Usa solo colores primarios
Verde no es un color primario
Colores válidos: rojo, azul, amarillo
```

## 🧪 Casos de Prueba

Prueba tu programa con estos valores:

| Color 1 | Color 2 | Resultado |
|---------|---------|-----------|
| rojo | azul | Morado 💜 |
| azul | rojo | Morado 💜 |
| rojo | amarillo | Naranja 🧡 |
| amarillo | rojo | Naranja 🧡 |
| azul | amarillo | Verde 💚 |
| amarillo | azul | Verde 💚 |
| rojo | rojo | Error: mismo color |
| verde | rojo | Error: no primario |
| rojo | verde | Error: no primario |

## 💡 Pistas

1. Normaliza ambos colores:
   ```python
   color1 = input("Color 1: ").lower()
   color2 = input("Color 2: ").lower()
   ```

2. Validaciones importantes:
   - Ambos deben ser colores primarios
   - No pueden ser el mismo color

3. Para las mezclas, el orden no importa:
   ```python
   if (color1 == "rojo" and color2 == "azul") or (color1 == "azul" and color2 == "rojo"):
       print("Morado")
   ```

4. Estructura sugerida:
   ```python
   # 1. Validar que ambos sean primarios
   # 2. Validar que no sean iguales
   # 3. Determinar la mezcla
   ```

## 🎨 Teoría del Color

### Colores Primarios:
- **Rojo** 🔴
- **Azul** 🔵
- **Amarillo** 🟡

### Colores Secundarios (mezclas):
- Rojo + Azul = **Morado** 💜
- Rojo + Amarillo = **Naranja** 🧡
- Azul + Amarillo = **Verde** 💚

### Colores Terciarios (primario + secundario):
- Rojo + Naranja = Rojo-Naranja
- Azul + Verde = Azul-Verde
- etc.

## ⚠️ Errores Comunes

- ❌ No considerar ambos órdenes (rojo+azul vs azul+rojo)
- ❌ No validar colores no primarios
- ❌ No validar mismo color dos veces
- ❌ Ser sensible a mayúsculas
- ❌ Código repetitivo para cada combinación

## 🎓 Conceptos Practicados

- Operador `and` múltiple
- Operador `or` para diferentes órdenes
- Validaciones en cascada
- Comparación de strings múltiples
- Lógica combinatoria

## 🔍 Ejemplo de Validación Completa

```python
COLORES_PRIMARIOS = ["rojo", "azul", "amarillo"]

# Normalizar
color1 = input("Color 1: ").lower()
color2 = input("Color 2: ").lower()

# Validar que sean primarios
if color1 not in COLORES_PRIMARIOS:
    print(f"{color1} no es primario")
elif color2 not in COLORES_PRIMARIOS:
    print(f"{color2} no es primario")
elif color1 == color2:
    print("No puedes mezclar el mismo color")
else:
    # Determinar mezcla
    if (color1 == "rojo" and color2 == "azul") or (color1 == "azul" and color2 == "rojo"):
        print("Morado 💜")
    # ... etc
```

## 🚀 Desafíos Extra (Opcional)

1. **Colores secundarios**:
   - Permite también mezclar secundarios
   - Verde + Naranja = ¿?
   - Morado + Verde = ¿?

2. **Proporciones**:
   - Pregunta la proporción de cada color
   - 75% rojo + 25% azul = Morado rojizo
   - 25% rojo + 75% azul = Morado azulado

3. **Código hexadecimal**:
   - Muestra el código hex aproximado
   - Morado: #800080
   - Naranja: #FFA500
   - Verde: #008000

4. **Simulador visual**:
   ```
   [ROJO] + [AZUL] = [MORADO]
    🔴      🔵        💜
   ```

5. **Mezclas múltiples**:
   - Permite mezclar 3 colores
   - Rojo + Azul + Amarillo = ¿?
   - Calcula resultado paso a paso

6. **Tintes y sombras**:
   - Agregar blanco = tinte (más claro)
   - Agregar negro = sombra (más oscuro)
   - Morado + blanco = Lavanda
   - Morado + negro = Púrpura oscuro

7. **Paleta de colores**:
   - Genera paleta armónica
   - Complementarios
   - Análogos
   - Tríada

8. **Quiz inverso**:
   - Dice el color resultante
   - Usuario debe adivinar la mezcla
   - "¿Qué colores hacen Naranja?"

---

**Tiempo estimado**: 20-30 minutos  
**Archivo de solución**: `ejercicio_19.py`

**Nota**: Este es uno de los ejercicios más complejos porque requiere:
- Validación de múltiples condiciones
- Considerar el orden de las entradas
- Manejo de varios casos especiales
- Lógica combinatoria


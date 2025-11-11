# 🧠 Ejercicio 16: Conversión a Binario

## Dificultad: ⭐⭐⭐ Avanzado

## 📝 Descripción

Desarrolla un programa que convierta un número entero positivo a su representación en binario usando divisiones sucesivas entre 2.

## 🎯 Objetivo

Practicar ciclos `while` con divisiones enteras, manejo de restos y construcción de cadenas.

## 📋 Especificaciones

El programa debe:

1. Solicitar un número entero positivo `n`.
2. Validar que `n` sea mayor o igual que 0.
3. Repetir divisiones entre 2, almacenando los residuos.
4. Construir la representación binaria en orden correcto.
5. Mostrar un caso especial para `n = 0` (binario `0`).

## 💻 Ejemplo de Ejecución

### Ejemplo 1:
```
Ingresa un número entero: 13
Binario: 1101
```

### Ejemplo 2:
```
Ingresa un número entero: 0
Binario: 0
```

### Ejemplo 3:
```
Ingresa un número entero: -5
Entrada no válida. Debes ingresar un entero mayor o igual a 0.
```

## 🧪 Casos de Prueba

| Entrada | Salida Esperada |
|---------|----------------|
| 1 | 1 |
| 2 | 10 |
| 7 | 111 |
| 13 | 1101 |
| 0 | 0 |

## 💡 Pistas

1. Usa una lista para guardar los residuos y luego inviértela.
2. Emplea la división entera `//` y el módulo `%`.
3. El ciclo termina cuando el número se reduce a 0.
4. Para invertir la lista, puedes usar `lista[::-1]` o `reversed`.

## ⚠️ Errores Comunes

- ❌ Escribir los bits en orden inverso (del último al primero).
- ❌ No manejar el caso especial cuando el número original es 0.
- ❌ Usar división normal y recibir números flotantes.

## 🎓 Conceptos Practicados

- Ciclo `while`
- División entera y módulo
- Construcción de cadenas a partir de listas

## 🚀 Desafíos Extra (Opcional)

1. Convierte también a representación octal y hexadecimal.
2. Permite convertir un número binario a decimal.
3. Acepta números binarios como entrada y valida que solo contengan 0 y 1.

---

**Tiempo estimado**: 20-25 minutos  
**Archivo de solución**: `ejercicio_16.py`


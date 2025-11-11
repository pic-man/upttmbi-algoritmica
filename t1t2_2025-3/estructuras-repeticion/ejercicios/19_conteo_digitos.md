# 🔢 Ejercicio 19: Conteo de Dígitos

## Dificultad: ⭐⭐ Intermedio

## 📝 Descripción

Escribe un programa que cuente cuántos dígitos tiene un número entero, sin convertirlo a cadena.

## 🎯 Objetivo

Practicar el uso de ciclos `while` con divisiones enteras y condiciones de parada.

## 📋 Especificaciones

El programa debe:

1. Solicitar un número entero (positivo o negativo).
2. Validar que no sea cero para el conteo especial.
3. Usar divisiones sucesivas entre 10 para contar cuántas cifras tiene.
4. Mostrar 1 como cantidad de dígitos si el número es 0.

## 💻 Ejemplo de Ejecución

### Ejemplo 1:
```
Ingresa un número entero: 12345
Cantidad de dígitos: 5
```

### Ejemplo 2:
```
Ingresa un número entero: -987
Cantidad de dígitos: 3
```

### Ejemplo 3:
```
Ingresa un número entero: 0
Cantidad de dígitos: 1
```

## 🧪 Casos de Prueba

| Entrada | Salida Esperada |
|---------|----------------|
| 0 | 1 |
| 7 | 1 |
| 42 | 2 |
| -1050 | 4 |
| 1234567890 | 10 |

## 💡 Pistas

1. Usa el valor absoluto del número con `abs()` para ignorar el signo.
2. Repite el ciclo mientras el número sea mayor que 0.
3. En cada iteración divide el número entre 10 usando `//`.

## ⚠️ Errores Comunes

- ❌ Convertir el número a string y contar caracteres (no se permite).
- ❌ Olvidar manejar campos negativos correctamente.
- ❌ Dividir con `/` en lugar de `//` y obtener flotantes.

## 🎓 Conceptos Practicados

- Ciclo `while`
- División entera
- Manejo de números negativos

## 🚀 Desafíos Extra (Opcional)

1. Calcula la suma de los dígitos además de contarlos.
2. Determina cuántos dígitos pares e impares tiene.
3. Identifica si el número es capicúa usando la lógica de los dígitos.

---

**Tiempo estimado**: 10-15 minutos  
**Archivo de solución**: `ejercicio_19.py`


# 🔢 Ejercicio 4: Número Positivo, Negativo o Cero

## Dificultad: ⭐ Básico

## 📝 Descripción

Crea un programa que pida un número y determine si es positivo, negativo o cero.

## 🎯 Objetivo

Practicar `if-elif-else` con tres opciones.

## 📋 Especificaciones

El programa debe:

1. Solicitar un número al usuario
2. Clasificar el número según:
   - **Mayor a 0**: "El número es positivo"
   - **Menor a 0**: "El número es negativo"
   - **Igual a 0**: "El número es cero"

## 💻 Ejemplo de Ejecución

### Ejemplo 1:
```
Ingresa un número: 15
El número 15 es positivo
```

### Ejemplo 2:
```
Ingresa un número: -8
El número -8 es negativo
```

### Ejemplo 3:
```
Ingresa un número: 0
El número es cero
```

## 🧪 Casos de Prueba

Prueba tu programa con estos valores:

| Entrada | Resultado |
|---------|-----------|
| 10 | Positivo |
| 0.5 | Positivo |
| 0 | Cero |
| -5 | Negativo |
| -0.1 | Negativo |

## 💡 Pistas

1. Usa `float(input())` para aceptar decimales
2. Puedes estructurarlo así:
   ```python
   if numero > 0:
       # positivo
   elif numero < 0:
       # negativo
   else:
       # cero
   ```
3. También puedes empezar verificando si es cero

## ⚠️ Errores Comunes

- ❌ Olvidar el caso del cero
- ❌ Usar solo `if` en lugar de `elif`
- ❌ No considerar números decimales

## 🎓 Conceptos Practicados

- `if-elif-else`
- Comparaciones con `>`, `<` y `==`
- Números positivos, negativos y cero

## 🚀 Desafíos Extra (Opcional)

1. Agrega información adicional:
   - Si es positivo: ¿Es par o impar?
   - Si es negativo: muestra su valor absoluto
2. Clasifica en más categorías:
   - Positivo pequeño (0-10)
   - Positivo grande (>10)
   - Negativo pequeño (-10-0)
   - Negativo grande (<-10)
3. Dibuja una representación visual:
   ```
   -5: ←←←←← |
   5:  | →→→→→
   ```

---

**Tiempo estimado**: 5-10 minutos  
**Archivo de solución**: `ejercicio_04.py`


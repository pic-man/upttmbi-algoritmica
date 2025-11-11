# ✖️ Ejercicio 4: Tabla de Multiplicar

## Dificultad: ⭐ Básico

## 📝 Descripción

Crea un programa que muestre la tabla de multiplicar de un número entero entre 1 y 10.

## 🎯 Objetivo

Refuerza el uso del ciclo `for` con rangos y operaciones simples.

## 📋 Especificaciones

El programa debe:

1. Solicitar un número entero `n` entre 1 y 10.
2. Validar que el número esté en ese rango.
3. Imprimir la tabla de multiplicar del 1 al 10 para el número `n`.
4. Mostrar un mensaje de error si el número no es válido.

## 💻 Ejemplo de Ejecución

### Ejemplo 1:
```
Ingresa un número entre 1 y 10: 4
4 x 1 = 4
4 x 2 = 8
...
4 x 10 = 40
```

### Ejemplo 2:
```
Ingresa un número entre 1 y 10: 10
10 x 1 = 10
10 x 2 = 20
...
10 x 10 = 100
```

### Ejemplo 3:
```
Ingresa un número entre 1 y 10: 15
Entrada no válida. Debes ingresar un número entero de 1 a 10.
```

## 🧪 Casos de Prueba

| Entrada | Salida Esperada |
|---------|----------------|
| 1 | Tabla del 1 |
| 5 | Tabla del 5 |
| 10 | Tabla del 10 |
| 0 | Mensaje de error |
| 11 | Mensaje de error |

## 💡 Pistas

1. Usa `range(1, 11)` para obtener los multiplicadores.
2. Puedes formatear cada línea con f-strings: `f"{n} x {i} = {n * i}"`.
3. Considera agregar un título antes de la tabla para mayor claridad.

## ⚠️ Errores Comunes

- ❌ Omitir la validación de rango y permitir números fuera de 1-10.
- ❌ Incluir el 0 en la tabla cuando no se solicita.
- ❌ Imprimir resultados sin formato claro.

## 🎓 Conceptos Practicados

- Ciclo `for`
- Uso de `range`
- Formato de salida

## 🚀 Desafíos Extra (Opcional)

1. Permite generar la tabla hasta un límite elegido por el usuario.
2. Muestra todas las tablas del 1 al 10 en formato de bloque.
3. Agrega un modo para mostrar la tabla en orden descendente.

---

**Tiempo estimado**: 5-10 minutos  
**Archivo de solución**: `ejercicio_04.py`


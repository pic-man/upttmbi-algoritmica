# ⭐ Ejercicio 15: Patrón de Asteriscos

## Dificultad: ⭐ Básico

## 📝 Descripción

Escribe un programa que dibuje un triángulo rectángulo formado por asteriscos según la altura indicada por el usuario.

## 🎯 Objetivo

Practicar ciclos `for` y la construcción de cadenas repetidas.

## 📋 Especificaciones

El programa debe:

1. Solicitar un entero positivo `altura`.
2. Validar que la altura sea al menos 1.
3. Imprimir líneas de asteriscos desde 1 hasta `altura`.
4. Cada línea debe contener la cantidad de asteriscos correspondiente a su número de fila.

## 💻 Ejemplo de Ejecución

### Ejemplo 1:
```
Ingresa la altura del triángulo: 4
*
**
***
****
```

### Ejemplo 2:
```
Ingresa la altura del triángulo: 1
*
```

### Ejemplo 3:
```
Ingresa la altura del triángulo: 0
Entrada no válida. Usa un entero positivo.
```

## 🧪 Casos de Prueba

| Altura | Salida Esperada |
|--------|-----------------|
| 3 | *, **, *** |
| 5 | 5 líneas con 1-5 asteriscos |
| 1 | * |
| 0 | Mensaje de error |
| -2 | Mensaje de error |

## 💡 Pistas

1. Usa `range(1, altura + 1)` para controlar la cantidad de filas.
2. Multiplica la cadena `"*"` por el número de fila para obtener la cantidad adecuada.
3. Asegúrate de agregar un salto de línea después de cada fila.

## ⚠️ Errores Comunes

- ❌ Usar el mismo número de asteriscos en todas las filas.
- ❌ No validar la altura y permitir valores negativos.
- ❌ Agregar espacios extra sin querer.

## 🎓 Conceptos Practicados

- Ciclo `for`
- Construcción de patrones
- Multiplicación de cadenas

## 🚀 Desafíos Extra (Opcional)

1. Dibuja un triángulo invertido (de mayor a menor).
2. Crea un triángulo isósceles centrado.
3. Permite elegir el carácter que se usará para el patrón.

---

**Tiempo estimado**: 5-10 minutos  
**Archivo de solución**: `ejercicio_15.py`


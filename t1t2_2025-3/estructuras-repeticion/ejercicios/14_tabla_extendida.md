# 🔢 Ejercicio 14: Tabla de Multiplicar Extendida

## Dificultad: ⭐⭐ Intermedio

## 📝 Descripción

Genera una tabla de multiplicar completa entre dos rangos definidos por el usuario, mostrando todas las combinaciones posibles.

## 🎯 Objetivo

Practicar ciclos `for` anidados y formateo de salida tabular.

## 📋 Especificaciones

El programa debe:

1. Solicitar dos números enteros: un límite inicial y un límite final (entre 1 y 10).
2. Validar que el límite inicial sea menor o igual que el final.
3. Para cada número dentro del rango, imprimir su tabla de multiplicar del 1 al 10.
4. Separar claramente las tablas generadas.

## 💻 Ejemplo de Ejecución

### Ejemplo 1:
```
Ingresa el número inicial: 3
Ingresa el número final: 5

Tabla del 3
3 x 1 = 3
...
3 x 10 = 30

Tabla del 4
4 x 1 = 4
...
4 x 10 = 40

Tabla del 5
5 x 1 = 5
...
5 x 10 = 50
```

### Ejemplo 2:
```
Ingresa el número inicial: 7
Ingresa el número final: 7

Tabla del 7
7 x 1 = 7
...
7 x 10 = 70
```

### Ejemplo 3:
```
Ingresa el número inicial: 8
Ingresa el número final: 3
Rangos inválidos. El número inicial debe ser menor o igual que el final.
```

## 🧪 Casos de Prueba

| Rango | Salida Esperada |
|-------|-----------------|
| 2 a 4 | Tablas del 2, 3 y 4 |
| 5 a 5 | Tabla del 5 |
| 1 a 3 | Tablas del 1, 2 y 3 |
| 9 a 7 | Mensaje de error |
| 0 a 3 | Mensaje de error si no está en 1-10 |

## 💡 Pistas

1. Usa un `for` externo para recorrer cada número base y otro interno para multiplicar del 1 al 10.
2. Aprovecha `range(inicio, fin + 1)` para incluir ambos límites.
3. Agrega saltos de línea o separadores para diferenciar cada tabla.

## ⚠️ Errores Comunes

- ❌ No validar el rango y generar resultados inconsistente.
- ❌ Olvidar reiniciar el multiplicador en cada ciclo externo.
- ❌ Imprimir las tablas sin formato y dificultar la lectura.

## 🎓 Conceptos Practicados

- Ciclos `for` anidados
- Rango con límites variables
- Formateo con f-strings

## 🚀 Desafíos Extra (Opcional)

1. Permite elegir el límite superior de los multiplicadores (no solo hasta 10).
2. Muestra las tablas en formato de matriz (una sola tabla grande).
3. Exporta la tabla completa a un archivo de texto.

---

**Tiempo estimado**: 15-20 minutos  
**Archivo de solución**: `ejercicio_14.py`


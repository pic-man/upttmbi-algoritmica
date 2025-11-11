# 📋 Ejercicio 20: Menú Interactivo

## Dificultad: ⭐⭐⭐ Avanzado

## 📝 Descripción

Diseña un programa con un menú interactivo que permita realizar diferentes acciones hasta que el usuario elija la opción de salir.

## 🎯 Objetivo

Practicar ciclos `while` en combinación con menús, validación de opciones y modularidad del código.

## 📋 Especificaciones

El programa debe:

1. Mostrar un menú similar al siguiente:
   ```
   1) Opción A
   2) Opción B
   3) Opción C
   4) Salir
   ```
2. Solicitar al usuario la opción deseada.
3. Ejecutar la acción correspondiente (puedes definir funciones simples como contar, sumar, mostrar mensajes, etc.).
4. Repetir el menú tras cada acción hasta que el usuario seleccione salir.
5. Validar entradas inválidas y mostrar un mensaje de error.

## 💻 Ejemplo de Ejecución

### Ejemplo 1:
```
--- Menú Principal ---
1) Mostrar saludo
2) Calcular cuadrado de un número
3) Mostrar contador de visitas
4) Salir
Selecciona una opción: 1
Hola, bienvenido al menú interactivo.

Selecciona una opción: 3
Has consultado el menú 2 veces.

Selecciona una opción: 4
Saliendo... ¡Hasta luego!
```

### Ejemplo 2:
```
Selecciona una opción: 5
Opción no válida. Inténtalo de nuevo.
```

### Ejemplo 3:
```
Selecciona una opción: 2
Ingresa un número: 7
7 al cuadrado es 49.
```

## 🧪 Casos de Prueba

| Secuencia | Resultado esperado |
|-----------|--------------------|
| 1, 4 | Muestra saludo y luego sale |
| 2 (n=5), 4 | Calcula 25 y luego sale |
| 5, 4 | Mensaje de error y luego salida |
| 3, 3, 4 | Muestra contador incrementado y sale |
| 4 | Sale inmediatamente |

## 💡 Pistas

1. Usa un `while True` y rompe el ciclo cuando la opción sea 4 (o la que definas como salir).
2. Crea funciones o bloques separados para cada opción.
3. Lleva un contador de cuántas veces se ha mostrado el menú si quieres estadísticas.
4. Maneja excepciones si decides aceptar entradas no numéricas.

## ⚠️ Errores Comunes

- ❌ No mostrar el menú nuevamente tras cada acción.
- ❌ Olvidar validar opciones inválidas.
- ❌ No actualizar variables globales en las distintas opciones.

## 🎓 Conceptos Practicados

- Ciclo `while` infinito con control de salida
- Validación de entradas
- Modularidad y organización del código

## 🚀 Desafíos Extra (Opcional)

1. Implementa un submenú dentro de una de las opciones.
2. Permite que el usuario personalice las opciones antes de iniciar el menú.
3. Guarda las acciones realizadas en una lista y muéstralas al salir.

---

**Tiempo estimado**: 20-25 minutos  
**Archivo de solución**: `ejercicio_20.py`


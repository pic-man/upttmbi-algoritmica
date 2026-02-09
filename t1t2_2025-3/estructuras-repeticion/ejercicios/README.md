# 🔁 Ejercicios - Estructuras de Repetición

## 20 Ejercicios Prácticos

A continuación encontrarás una colección de 20 ejercicios para dominar los ciclos `for` y `while` en Python.

## 📊 Lista de Ejercicios

| # | Nombre | Dificultad | Conceptos |
|---|--------|------------|-----------|
| 01 | [Contador Ascendente](01_contador_ascendente.md) | ⭐ Básico | while, incremento |
| 02 | [Contador Descendente](02_contador_descendente.md) | ⭐ Básico | while, decremento |
| 03 | [Suma de Números](03_suma_numeros.md) | ⭐ Básico | for, acumuladores |
| 04 | [Tabla de Multiplicar](04_tabla_multiplicar.md) | ⭐ Básico | for, rangos |
| 05 | [Promedio hasta Cero](05_promedio_hasta_cero.md) | ⭐⭐ Intermedio | while, sentinelas |
| 06 | [Factorial Iterativo](06_factorial_iterativo.md) | ⭐⭐ Intermedio | while, acumuladores |
| 07 | [Serie Fibonacci](07_serie_fibonacci.md) | ⭐⭐ Intermedio | while, actualización múltiple |
| 08 | [Contar Vocales](08_contar_vocales.md) | ⭐ Básico | for, strings |
| 09 | [Suma de Pares](09_suma_pares.md) | ⭐ Básico | for, condiciones |
| 10 | [Potencia por Multiplicación](10_potencia_multiplicacion.md) | ⭐⭐ Intermedio | while, multiplicación repetida |
| 11 | [Mayor y Menor](11_mayor_menor.md) | ⭐⭐ Intermedio | while, comparación |
| 12 | [Intentos de Contraseña](12_intentos_contrasena.md) | ⭐⭐ Intermedio | while, contadores |
| 13 | [Juego de Adivinanza](13_juego_adivinanza.md) | ⭐⭐ Intermedio | while, retroalimentación |
| 14 | [Tabla de Multiplicar Extendida](14_tabla_extendida.md) | ⭐⭐ Intermedio | for anidado |
| 15 | [Patrón de Asteriscos](15_patron_asteriscos.md) | ⭐ Básico | for, strings |
| 16 | [Conversión a Binario](16_conversion_binario.md) | ⭐⭐⭐ Avanzado | while, divisiones sucesivas |
| 17 | [Simulación de Cajero](17_cajero_automatico.md) | ⭐⭐⭐ Avanzado | while, menús |
| 18 | [Registro de Ventas Diarias](18_registro_ventas.md) | ⭐⭐ Intermedio | for, acumuladores |
| 19 | [Conteo de Dígitos](19_conteo_digitos.md) | ⭐⭐ Intermedio | while, divisiones enteras |
| 20 | [Menú Interactivo](20_menu_interactivo.md) | ⭐⭐⭐ Avanzado | while, menús, validación |

## 🎯 Por Nivel de Dificultad

### ⭐ Básico (7 ejercicios)
Ideales para comprender la sintaxis de los bucles y patrones repetitivos simples.

**Ejercicios**: 1, 2, 3, 4, 8, 9, 15

### ⭐⭐ Intermedio (10 ejercicios)
Presentan entradas dinámicas, condiciones adicionales y requieren mayor planificación.

**Ejercicios**: 5, 6, 7, 10, 11, 12, 13, 14, 18, 19

### ⭐⭐⭐ Avanzado (3 ejercicios)
Integran ciclos con lógica de control compleja y múltiples caminos posibles.

**Ejercicios**: 16, 17, 20

## 🚀 Cómo Empezar

### Paso 1: Elige un ejercicio
Selecciona un archivo `.md` del listado según tu nivel o interés.

### Paso 2: Lee el enunciado
Revisa las especificaciones y ejemplos para tener claro el objetivo.

### Paso 3: Copia la plantilla
```bash
cp plantilla_solucion.py ../soluciones/tu-usuario-github/ejercicio_XX.py
```

### Paso 4: Resuelve el ejercicio
Implementa tu solución en el archivo copiado siguiendo la plantilla.

### Paso 5: Prueba tu código
```bash
python ejercicio_XX.py
```

### Paso 6: Entrega
Haz commit y push cuando todos los casos de prueba funcionen.

## 📋 Plantilla de Solución

Utiliza esta estructura para cada ejercicio:

```python
"""
Ejercicio XX: Nombre del Ejercicio
Estudiante: Tu Nombre Completo
GitHub: @tu-usuario
Fecha: YYYY-MM-DD

Descripción:
Breve descripción de qué hace el programa

Ejemplo de uso:
Entrada: [valor de ejemplo]
Salida: [resultado esperado]
"""

# ============================================
# TU CÓDIGO COMIENZA AQUÍ
# ============================================

# Solicitar datos al usuario


# Procesar con ciclos de repetición


# Mostrar resultados


# ============================================
# FIN DEL CÓDIGO
# ============================================
```

## 💡 Consejos

1. **Esquematiza el algoritmo** antes de programar.
2. **Define qué ciclo usarás** (`for` o `while`) y por qué.
3. **Controla las condiciones de salida** para evitar ciclos infinitos.
4. **Usa acumuladores y contadores** cuando debas sumar o contar.
5. **Prueba con valores extremos** para asegurarte de que tu solución es robusta.
6. **Refactoriza** si notas código repetido o poco claro.

## 🧪 Casos de Prueba

Para validar tus soluciones considera:
- Valores mínimos y máximos del rango solicitado.
- Entradas inválidas o fuera de rango (cuando aplique).
- Datos que provoquen el fin del ciclo (sentinela).
- Ejemplos con resultados conocidos para verificar cálculos.

## 📈 Progreso Recomendado

### Semana 1
- Ejercicios 1-5 (ciclos básicos y acumuladores simples).

### Semana 2
- Ejercicios 6-10 (ciclos con cálculos y condiciones compuestas).

### Semana 3
- Ejercicios 11-15 (validación de entradas y ciclos anidados).

### Semana 4
- Ejercicios 16-20 (simulaciones completas y lógica avanzada).

## ✅ Criterios de Evaluación

1. **Funcionalidad** (40%): el programa cumple todas las especificaciones.
2. **Correctitud** (25%): maneja casos límite y entradas inválidas.
3. **Claridad** (20%): código legible, nombres descriptivos y comentarios útiles.
4. **Pruebas** (15%): incluye ejemplos y valida diferentes escenarios.

## 🆘 ¿Necesitas ayuda?

1. Repasa la teoría de ciclos y estructuras de control.
2. Haz diagramas de flujo para visualizar el proceso.
3. Pregunta a tus compañeros o en el canal del curso.
4. Crea un Issue con el formato: `[T1T3][Estructuras-Repeticion] Duda ejercicio XX`.

---

¡Disfruta resolviendo estos retos y fortalece tu lógica! 🚀


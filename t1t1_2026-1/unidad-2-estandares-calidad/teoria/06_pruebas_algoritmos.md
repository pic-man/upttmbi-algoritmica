# 📖 06 - Técnicas de Escritura y Pruebas de Algoritmos

## ¿Qué son las Pruebas?

Las **pruebas** son el proceso de verificar que un algoritmo o programa funciona correctamente, produciendo los resultados esperados para diferentes entradas.

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   ENTRADA   │ ──▶ │  PROGRAMA   │ ──▶ │   SALIDA    │
│  de prueba  │     │             │     │  obtenida   │
└─────────────┘     └─────────────┘     └─────────────┘
                                              │
                                              ▼
                                        ┌─────────────┐
                                        │ ¿Es igual a │
                                        │ lo esperado?│
                                        └─────────────┘
                                         /          \
                                       Sí            No
                                       ✅            ❌
```

## Tipos de Pruebas

### 1. Pruebas Manuales

Ejecutar el programa con diferentes datos y verificar visualmente.

```
Caso de prueba #1:
- Entrada: 5, 3
- Salida esperada: 8
- Salida obtenida: 8
- Resultado: ✅ PASÓ
```

### 2. Pruebas de Traza

Ejecutar el algoritmo paso a paso en papel (corrida en frío).

### 3. Pruebas Automatizadas

Usar código para verificar automáticamente los resultados.

```python
def sumar(a, b):
    return a + b

# Prueba automatizada
def test_sumar():
    assert sumar(5, 3) == 8, "Error: 5 + 3 debería ser 8"
    assert sumar(0, 0) == 0, "Error: 0 + 0 debería ser 0"
    assert sumar(-1, 1) == 0, "Error: -1 + 1 debería ser 0"
    print("✅ Todas las pruebas pasaron")

test_sumar()
```

## Casos de Prueba

### Tipos de Casos

| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| **Normal** | Valores típicos | edad = 25 |
| **Límite** | Valores en los bordes | edad = 18, edad = 0 |
| **Inválido** | Valores incorrectos | edad = -5, edad = "abc" |
| **Especial** | Casos particulares | lista vacía, división por cero |

### Diseño de Casos de Prueba

```
ALGORITMO: Determinar si es mayor de edad (>= 18)

┌─────────────────────────────────────────────────────────────┐
│                    CASOS DE PRUEBA                           │
├──────┬─────────────┬──────────────────┬─────────────────────┤
│ Caso │   Entrada   │  Salida Esperada │       Tipo          │
├──────┼─────────────┼──────────────────┼─────────────────────┤
│  1   │  edad = 25  │  "Mayor de edad" │  Normal             │
│  2   │  edad = 10  │  "Menor de edad" │  Normal             │
│  3   │  edad = 18  │  "Mayor de edad" │  Límite (exacto)    │
│  4   │  edad = 17  │  "Menor de edad" │  Límite (inferior)  │
│  5   │  edad = 0   │  "Menor de edad" │  Límite (mínimo)    │
│  6   │  edad = -5  │  Error/Inválido  │  Inválido           │
│  7   │  edad = 150 │  "Mayor de edad" │  Extremo            │
└──────┴─────────────┴──────────────────┴─────────────────────┘
```

## Proceso de Pruebas

### 1. Planificación

```
1. Identificar qué probar
2. Definir casos de prueba
3. Determinar datos de entrada
4. Calcular salidas esperadas
```

### 2. Ejecución

```
1. Ejecutar el programa con cada caso
2. Registrar la salida obtenida
3. Comparar con la salida esperada
4. Documentar resultados
```

### 3. Análisis

```
1. Identificar casos fallidos
2. Analizar la causa del error
3. Corregir el algoritmo
4. Volver a probar
```

## Ejemplo Completo de Pruebas

### Algoritmo a Probar

```python
def calcular_calificacion(nota):
    """
    Convierte una nota numérica a letra.
    
    A: 90-100
    B: 80-89
    C: 70-79
    D: 60-69
    F: 0-59
    """
    if nota < 0 or nota > 100:
        return "Inválido"
    elif nota >= 90:
        return "A"
    elif nota >= 80:
        return "B"
    elif nota >= 70:
        return "C"
    elif nota >= 60:
        return "D"
    else:
        return "F"
```

### Plan de Pruebas

```python
# Casos de prueba
casos_prueba = [
    # (entrada, salida_esperada, descripción)
    (95, "A", "Nota alta - A"),
    (90, "A", "Límite inferior A"),
    (89, "B", "Límite superior B"),
    (85, "B", "Nota media - B"),
    (80, "B", "Límite inferior B"),
    (75, "C", "Nota media - C"),
    (70, "C", "Límite inferior C"),
    (65, "D", "Nota media - D"),
    (60, "D", "Límite inferior D"),
    (59, "F", "Límite superior F"),
    (50, "F", "Nota baja - F"),
    (0, "F", "Nota mínima"),
    (100, "A", "Nota máxima"),
    (-1, "Inválido", "Nota negativa"),
    (101, "Inválido", "Nota mayor a 100"),
]

# Ejecutar pruebas
print("=" * 50)
print("REPORTE DE PRUEBAS")
print("=" * 50)

pasaron = 0
fallaron = 0

for nota, esperado, descripcion in casos_prueba:
    resultado = calcular_calificacion(nota)
    estado = "✅ PASÓ" if resultado == esperado else "❌ FALLÓ"
    
    if resultado == esperado:
        pasaron += 1
    else:
        fallaron += 1
    
    print(f"{estado} | Nota: {nota:3} | Esperado: {esperado} | Obtenido: {resultado} | {descripcion}")

print("=" * 50)
print(f"Resumen: {pasaron} pasaron, {fallaron} fallaron")
print(f"Tasa de éxito: {pasaron/(pasaron+fallaron)*100:.1f}%")
```

## Documentación de Pruebas

### Plantilla de Reporte

```
═══════════════════════════════════════════════════════════
                    REPORTE DE PRUEBAS
═══════════════════════════════════════════════════════════

INFORMACIÓN
───────────
Programa: [Nombre del programa]
Versión: [Número de versión]
Fecha: [Fecha de prueba]
Probador: [Nombre]

RESUMEN
───────────
Total de casos: XX
Casos exitosos: XX
Casos fallidos: XX
Tasa de éxito: XX%

CASOS DE PRUEBA DETALLADOS
───────────
[Tabla con todos los casos]

OBSERVACIONES
───────────
[Notas sobre los resultados]

CONCLUSIÓN
───────────
[ ] Aprobado para producción
[ ] Requiere correcciones
═══════════════════════════════════════════════════════════
```

## Errores Comunes y Cómo Evitarlos

| Error | Ejemplo | Solución |
|-------|---------|----------|
| No probar límites | Solo probar edad=25 | Probar edad=18, 17, 0 |
| Ignorar casos inválidos | No probar edad=-5 | Incluir validaciones |
| Pocas pruebas | Solo 1-2 casos | Mínimo 5-10 casos variados |
| No documentar | Pruebas sin registro | Usar plantillas de reporte |

## 📝 Para Recordar

1. Las pruebas **verifican** que el programa funciona
2. Usar **diferentes tipos** de casos de prueba
3. Siempre probar **casos límite**
4. **Documentar** todos los resultados
5. Las pruebas **automatizadas** ahorran tiempo
6. Un programa **sin probar** es un programa **con errores**

## ✅ Ejercicio Rápido

Diseña 5 casos de prueba para el siguiente algoritmo:

```python
def es_bisiesto(año):
    """Determina si un año es bisiesto."""
    if año % 400 == 0:
        return True
    if año % 100 == 0:
        return False
    if año % 4 == 0:
        return True
    return False
```

<details>
<summary>Ver respuesta</summary>

| Caso | Entrada | Esperado | Tipo |
|------|---------|----------|------|
| 1 | 2024 | True | Normal (divisible por 4) |
| 2 | 2023 | False | Normal (no divisible por 4) |
| 3 | 2000 | True | Especial (divisible por 400) |
| 4 | 1900 | False | Especial (divisible por 100 pero no 400) |
| 5 | 2100 | False | Límite futuro |

```python
casos = [
    (2024, True, "Divisible por 4"),
    (2023, False, "No divisible por 4"),
    (2000, True, "Divisible por 400"),
    (1900, False, "Divisible por 100, no por 400"),
    (2100, False, "Divisible por 100, no por 400 - futuro"),
]

for año, esperado, descripcion in casos:
    resultado = es_bisiesto(año)
    estado = "✅" if resultado == esperado else "❌"
    print(f"{estado} Año {año}: {resultado} ({descripcion})")
```
</details>

---

¡Felicidades! Has completado la teoría de la Unidad 2. Ahora puedes pasar a los ejercicios.

[Ir a: Ejercicios →](../ejercicios/README.md)

# 🔬 Ejercicio 05: Revisión de Calidad

## Nivel: ⭐⭐⭐ Avanzado

## 📝 Descripción

Realiza una **auditoría de calidad completa** del siguiente código, identificando problemas y proponiendo mejoras.

## 🎯 Objetivo

Aplicar todos los estándares de calidad aprendidos para evaluar y mejorar código existente.

## 📋 Código a Evaluar

```python
def p(l):
    s=0
    c=0
    for x in l:
        if x>0:
            s=s+x
            c=c+1
    if c>0:
        return s/c
    return 0

def m(l):
    if len(l)==0:return None
    m=l[0]
    for x in l:
        if x>m:m=x
    return m

def n(l):
    if len(l)==0:return None
    m=l[0]
    for x in l:
        if x<m:m=x
    return m

def r(l):
    return m(l)-n(l)

def main():
    d=[23,45,-12,67,89,-5,34,0,56,78]
    print("Promedio positivos:",p(d))
    print("Maximo:",m(d))
    print("Minimo:",n(d))
    print("Rango:",r(d))

main()
```

## 📝 Tareas a Realizar

### Parte 1: Identificación de Problemas (30 puntos)

Completa la siguiente tabla:

| # | Línea | Problema | Categoría | Severidad |
|---|-------|----------|-----------|-----------|
| 1 | | | | |
| 2 | | | | |
| ... | | | | |

**Categorías**: Nomenclatura, Documentación, Estructura, Legibilidad, Eficiencia
**Severidad**: Alta, Media, Baja

### Parte 2: Código Corregido (40 puntos)

Reescribe el código aplicando todos los estándares de calidad:

1. Encabezado del archivo
2. Nombres descriptivos
3. Docstrings completos
4. Comentarios explicativos
5. Estructura organizada
6. Manejo de errores

### Parte 3: Plan de Pruebas (20 puntos)

Diseña 10 casos de prueba para verificar las funciones corregidas.

### Parte 4: Reporte de Auditoría (10 puntos)

Genera un reporte ejecutivo con:

```
═══════════════════════════════════════════════════════════
                REPORTE DE AUDITORÍA DE CALIDAD
═══════════════════════════════════════════════════════════

RESUMEN EJECUTIVO
─────────────────
Código evaluado: [nombre]
Fecha: [fecha]
Auditor: [tu nombre]

Problemas encontrados: [número]
  - Alta severidad: [número]
  - Media severidad: [número]
  - Baja severidad: [número]

PRINCIPALES HALLAZGOS
─────────────────────
1. [Problema más crítico]
2. [Segundo problema]
3. [Tercer problema]

RECOMENDACIONES
───────────────
1. [Recomendación principal]
2. [Segunda recomendación]

CONCLUSIÓN
──────────
[Evaluación general del código y si cumple estándares]

═══════════════════════════════════════════════════════════
```

## 📤 Formato de Entrega

1. Tabla de problemas identificados
2. Código corregido (`ejercicio_05_corregido.py`)
3. Archivo de pruebas (`ejercicio_05_pruebas.py`)
4. Reporte de auditoría

## ✅ Criterios de Evaluación

| Parte | Puntos |
|-------|--------|
| Identificación de problemas | 30 |
| Código corregido | 40 |
| Plan de pruebas | 20 |
| Reporte de auditoría | 10 |

## 💡 Guía de Análisis

Busca problemas en estas áreas:

1. **Nomenclatura**
   - ¿Los nombres revelan intención?
   - ¿Siguen convenciones?

2. **Documentación**
   - ¿Hay docstrings?
   - ¿Los comentarios son útiles?

3. **Estructura**
   - ¿El código está organizado?
   - ¿Hay separación lógica?

4. **Legibilidad**
   - ¿Es fácil de leer?
   - ¿Hay espaciado adecuado?

5. **Robustez**
   - ¿Maneja casos especiales?
   - ¿Valida las entradas?

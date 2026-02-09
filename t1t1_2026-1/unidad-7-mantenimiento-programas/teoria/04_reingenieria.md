# 📖 04 - Reingeniería de Programas

## ¿Qué es la Reingeniería?

La **reingeniería** es el proceso de examinar, analizar y reconstruir un sistema de software existente para mejorarlo sin cambiar su funcionalidad.

```
┌─────────────────────────────────────────────────────────────┐
│                    REINGENIERÍA                              │
│                                                             │
│   Sistema       ──────▶   Sistema                           │
│   Antiguo                 Mejorado                          │
│                                                             │
│   - Difícil de mantener   - Fácil de mantener              │
│   - Código confuso        - Código limpio                  │
│   - Sin documentación     - Bien documentado               │
│   - Tecnología obsoleta   - Tecnología actual              │
│                                                             │
│        (Misma funcionalidad, mejor estructura)              │
└─────────────────────────────────────────────────────────────┘
```

## Proceso de Reingeniería

```
1. INGENIERÍA INVERSA
   Entender el sistema actual
         ↓
2. ANÁLISIS
   Identificar problemas y oportunidades
         ↓
3. REESTRUCTURACIÓN
   Mejorar la estructura del código
         ↓
4. INGENIERÍA DIRECTA
   Reconstruir con mejoras
         ↓
5. VALIDACIÓN
   Verificar que funciona igual
```

## Actividades de Reingeniería

### 1. Ingeniería Inversa

Entender cómo funciona el sistema actual.

```
Código fuente → Análisis → Documentación
                         → Diagramas
                         → Especificaciones
```

### 2. Reestructuración de Código

```python
# ANTES: Código confuso
def f(l):
    s=0
    for x in l:
        if x>0:s+=x
    return s/len(l)if len(l)>0 else 0

# DESPUÉS: Código reestructurado
def calcular_promedio_positivos(numeros):
    """Calcula el promedio de los números positivos."""
    if not numeros:
        return 0
    
    positivos = [n for n in numeros if n > 0]
    
    if not positivos:
        return 0
    
    return sum(positivos) / len(positivos)
```

### 3. Migración de Datos

Actualizar formatos de datos obsoletos.

### 4. Modernización de Interfaces

Actualizar la interfaz de usuario a tecnologías actuales.

## Refactorización

La **refactorización** es mejorar el código sin cambiar su comportamiento.

### Técnicas Comunes

| Técnica | Descripción |
|---------|-------------|
| **Renombrar** | Mejores nombres para variables/funciones |
| **Extraer función** | Separar código en funciones más pequeñas |
| **Eliminar duplicados** | Consolidar código repetido |
| **Simplificar condiciones** | Reducir complejidad de if/else |

### Ejemplo de Refactorización

```python
# ANTES
def procesar(datos):
    # Validar
    if datos is None:
        return None
    if len(datos) == 0:
        return None
    
    # Calcular suma
    total = 0
    for d in datos:
        total = total + d
    
    # Calcular promedio
    promedio = total / len(datos)
    
    # Clasificar
    if promedio >= 90:
        resultado = "A"
    elif promedio >= 80:
        resultado = "B"
    elif promedio >= 70:
        resultado = "C"
    else:
        resultado = "F"
    
    return resultado

# DESPUÉS (refactorizado)
def validar_datos(datos):
    """Valida que los datos no estén vacíos."""
    return datos is not None and len(datos) > 0

def calcular_promedio(datos):
    """Calcula el promedio de una lista."""
    return sum(datos) / len(datos)

def obtener_calificacion(promedio):
    """Convierte un promedio numérico a letra."""
    if promedio >= 90: return "A"
    if promedio >= 80: return "B"
    if promedio >= 70: return "C"
    return "F"

def procesar(datos):
    """Procesa datos y retorna calificación."""
    if not validar_datos(datos):
        return None
    
    promedio = calcular_promedio(datos)
    return obtener_calificacion(promedio)
```

## Cuándo Aplicar Reingeniería

| Indicador | Acción |
|-----------|--------|
| Muchos errores | Refactorizar áreas problemáticas |
| Difícil de modificar | Mejorar estructura |
| Código duplicado | Consolidar y reutilizar |
| Sin documentación | Documentar y simplificar |
| Tecnología obsoleta | Migrar a nuevas tecnologías |

## 📝 Para Recordar

1. La reingeniería **mejora sin cambiar funcionalidad**
2. Incluye **ingeniería inversa** (entender) y **directa** (reconstruir)
3. La **refactorización** es una forma de reingeniería
4. Siempre **probar** después de cada cambio
5. **Documentar** los cambios realizados

---

¡Felicidades! Has completado la teoría de la Unidad 7.

[Ir a: Ejercicios →](../ejercicios/README.md)

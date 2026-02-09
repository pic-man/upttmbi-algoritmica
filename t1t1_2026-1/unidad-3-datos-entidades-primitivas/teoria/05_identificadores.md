# 📖 05 - Los Identificadores

## ¿Qué es un Identificador?

Un **identificador** es el nombre que se le asigna a los elementos de un programa: variables, constantes, funciones, clases, etc.

```python
# Ejemplos de identificadores
edad = 25              # 'edad' es un identificador
nombre = "Juan"        # 'nombre' es un identificador
PI = 3.14159           # 'PI' es un identificador

def calcular_area():   # 'calcular_area' es un identificador
    pass

class Estudiante:      # 'Estudiante' es un identificador
    pass
```

## Reglas de Escritura

### Reglas Obligatorias (Sintaxis)

1. **Debe comenzar** con una letra (a-z, A-Z) o guion bajo (_)
2. **Puede contener** letras, números y guiones bajos
3. **No puede contener** espacios ni caracteres especiales
4. **No puede ser** una palabra reservada del lenguaje
5. **Distingue** mayúsculas de minúsculas (case-sensitive)

```python
# ✅ Identificadores VÁLIDOS
edad
_privado
nombre_completo
contador1
miVariable
CONSTANTE

# ❌ Identificadores INVÁLIDOS
1numero         # No puede empezar con número
mi-variable     # No puede contener guion
mi variable     # No puede contener espacios
for             # Es palabra reservada
precio$         # No puede contener $
```

### Palabras Reservadas en Python

No se pueden usar como identificadores:

```
False    await    else      import    pass
None     break    except    in        raise
True     class    finally   is        return
and      continue for       lambda    try
as       def      from      nonlocal  while
assert   del      global    not       with
async    elif     if        or        yield
```

## Convenciones de Nomenclatura

### Estilos de Escritura

| Estilo | Descripción | Ejemplo |
|--------|-------------|---------|
| snake_case | Palabras separadas por _ | `nombre_completo` |
| camelCase | Primera palabra minúscula | `nombreCompleto` |
| PascalCase | Cada palabra capitalizada | `NombreCompleto` |
| SCREAMING_SNAKE | Todo mayúsculas con _ | `NOMBRE_COMPLETO` |

### Convenciones en Python (PEP 8)

```python
# Variables y funciones: snake_case
nombre_usuario = "Juan"
def calcular_promedio():
    pass

# Constantes: SCREAMING_SNAKE_CASE
PI = 3.14159
MAXIMO_INTENTOS = 3
TASA_IVA = 0.16

# Clases: PascalCase
class CuentaBancaria:
    pass

# Variables privadas: _prefijo
_contador_interno = 0

# Variables "muy privadas": __doble_prefijo
__secreto = "oculto"

# Variables especiales: __dunder__
__version__ = "1.0"
```

## Buenas Prácticas

### 1. Nombres Descriptivos

```python
# ❌ MAL: Nombres crípticos
x = 100
y = 0.16
z = x * y

# ✅ BIEN: Nombres descriptivos
precio = 100
tasa_impuesto = 0.16
impuesto = precio * tasa_impuesto
```

### 2. Nombres que Revelen Intención

```python
# ❌ MAL: No queda claro qué representa
d = 30

# ✅ BIEN: Se entiende claramente
dias_del_mes = 30
```

### 3. Evitar Abreviaturas Confusas

```python
# ❌ MAL: Abreviaturas difíciles de entender
clcprmd()
fch_nac = "2000-01-01"

# ✅ BIEN: Nombres completos o abreviaturas conocidas
calcular_promedio()
fecha_nacimiento = "2000-01-01"
num_estudiantes = 30  # 'num' es aceptable
```

### 4. Consistencia

```python
# ❌ MAL: Inconsistente
nombre_usuario = "Juan"
edadUsuario = 25
CorreoElectronico = "juan@email.com"

# ✅ BIEN: Consistente (todo snake_case)
nombre_usuario = "Juan"
edad_usuario = 25
correo_electronico = "juan@email.com"
```

### 5. Longitud Apropiada

```python
# ❌ MAL: Demasiado corto
n = "Juan"
e = 25

# ❌ MAL: Demasiado largo
nombre_completo_del_usuario_registrado = "Juan"
edad_en_años_del_usuario_actual = 25

# ✅ BIEN: Longitud equilibrada
nombre_usuario = "Juan"
edad = 25
```

## Ejemplos por Contexto

### Variables de Contador

```python
# Contadores típicos
contador = 0
indice = 0
i = 0        # Aceptable en ciclos cortos

for i in range(10):
    contador += 1
```

### Variables de Acumulador

```python
# Acumuladores
suma_total = 0
promedio_acumulado = 0.0
total_ventas = 0
```

### Booleanos

```python
# Nombres que indican condición (usar es_, tiene_, puede_, etc.)
es_valido = True
tiene_permiso = False
puede_continuar = True
esta_activo = True
hay_errores = False
```

### Colecciones

```python
# Usar plurales para listas/conjuntos
estudiantes = ["Ana", "Luis", "María"]
numeros_primos = [2, 3, 5, 7, 11]
productos_seleccionados = []

# Diccionarios: usar nombres que indiquen la relación
precio_por_producto = {"manzana": 1.50, "naranja": 2.00}
estudiante_por_id = {1: "Ana", 2: "Luis"}
```

## 📝 Para Recordar

1. Los identificadores **nombran** elementos del programa
2. Deben seguir **reglas sintácticas** del lenguaje
3. Seguir las **convenciones** mejora la legibilidad
4. Usar nombres **descriptivos** y **consistentes**
5. En Python: snake_case para variables, PascalCase para clases

## ✅ Ejercicio Rápido

¿Cuáles de estos identificadores son válidos en Python?

```python
1. nombre_completo
2. 2do_lugar
3. _privado
4. mi-variable
5. class
6. numeroDeEstudiantes
7. MAXIMO_VALOR
8. for
```

<details>
<summary>Ver respuesta</summary>

1. `nombre_completo` ✅ Válido
2. `2do_lugar` ❌ Inválido (empieza con número)
3. `_privado` ✅ Válido
4. `mi-variable` ❌ Inválido (contiene guion)
5. `class` ❌ Inválido (palabra reservada)
6. `numeroDeEstudiantes` ✅ Válido (aunque no sigue PEP 8)
7. `MAXIMO_VALOR` ✅ Válido
8. `for` ❌ Inválido (palabra reservada)
</details>

## 🔜 Siguiente Paso

Ahora aprenderás sobre las variables.

[Ir a: 06 - Variables →](./06_variables.md)

# 📖 02 - Identificación de los Datos de Entrada

## ¿Qué son los Datos de Entrada?

Los **datos de entrada** son la información que el algoritmo necesita recibir para poder realizar su trabajo. Sin datos de entrada, el programa no tiene con qué trabajar.

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   ENTRADA   │ ──▶ │   PROCESO   │ ──▶ │   SALIDA    │
│             │     │             │     │             │
│ Datos que   │     │ Operaciones │     │ Resultados  │
│ recibimos   │     │             │     │             │
└─────────────┘     └─────────────┘     └─────────────┘
```

## Características de los Datos de Entrada

| Característica | Descripción |
|----------------|-------------|
| **Tipo** | Numérico, texto, booleano |
| **Origen** | Usuario, archivo, sensor, otro programa |
| **Validez** | Debe cumplir ciertas condiciones |
| **Cantidad** | Pueden ser uno o múltiples datos |

## Preguntas para Identificar Entradas

1. **¿Qué datos necesito para resolver el problema?**
2. **¿De qué tipo es cada dato?**
3. **¿De dónde provienen los datos?**
4. **¿Hay restricciones sobre los valores?**

## Ejemplos de Identificación

### Ejemplo 1: Calcular área de un círculo

```
Problema: Calcular el área de un círculo

Análisis de entrada:
┌─────────────────────────────────────────────┐
│ DATOS DE ENTRADA                            │
├─────────────────────────────────────────────┤
│ - radio: número real, positivo              │
│   Origen: usuario                           │
│   Restricción: radio > 0                    │
└─────────────────────────────────────────────┘
```

### Ejemplo 2: Calcular salario

```
Problema: Calcular salario con horas extra

Análisis de entrada:
┌─────────────────────────────────────────────┐
│ DATOS DE ENTRADA                            │
├─────────────────────────────────────────────┤
│ - horas_trabajadas: entero, positivo        │
│   Restricción: horas >= 0                   │
│                                             │
│ - tarifa_hora: real, positivo               │
│   Restricción: tarifa > 0                   │
└─────────────────────────────────────────────┘
```

### Ejemplo 3: Sistema de notas

```
Problema: Calcular promedio y determinar aprobación

Análisis de entrada:
┌─────────────────────────────────────────────┐
│ DATOS DE ENTRADA                            │
├─────────────────────────────────────────────┤
│ - nota1: real, entre 0 y 10                 │
│ - nota2: real, entre 0 y 10                 │
│ - nota3: real, entre 0 y 10                 │
│                                             │
│ Restricción: 0 ≤ nota ≤ 10                  │
└─────────────────────────────────────────────┘
```

## Validación de Entradas

Es importante validar que los datos de entrada sean correctos:

```python
# Ejemplo de validación de entrada
def obtener_edad():
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            if edad < 0 or edad > 150:
                print("Error: La edad debe estar entre 0 y 150")
            else:
                return edad
        except ValueError:
            print("Error: Debe ingresar un número entero")
```

## Documentación de Entradas

```
┌─────────────────────────────────────────────────────────────┐
│ ESPECIFICACIÓN DE ENTRADA                                    │
├──────────┬──────────┬──────────┬────────────────────────────┤
│ Variable │   Tipo   │ Rango    │ Descripción                │
├──────────┼──────────┼──────────┼────────────────────────────┤
│ edad     │ int      │ 0-150    │ Edad del usuario en años   │
│ nombre   │ str      │ 1-100    │ Nombre completo            │
│ salario  │ float    │ > 0      │ Salario mensual en USD     │
└──────────┴──────────┴──────────┴────────────────────────────┘
```

## 📝 Para Recordar

1. Identificar **todos** los datos necesarios
2. Definir el **tipo** de cada dato
3. Establecer **restricciones** y rangos válidos
4. Considerar la **validación** de entradas
5. **Documentar** cada entrada claramente

## 🔜 Siguiente Paso

[Ir a: 03 - Datos de Salida →](./03_datos_salida.md)

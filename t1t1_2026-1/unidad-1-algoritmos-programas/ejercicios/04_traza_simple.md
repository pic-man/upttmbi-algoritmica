# 🔍 Ejercicio 04: Traza Simple

## Nivel: ⭐ Básico

## 📝 Descripción

Realiza la **traza** (corrida en frío) del siguiente algoritmo con los datos de prueba proporcionados.

## 🎯 Objetivo

Practicar la ejecución manual de algoritmos paso a paso, registrando los valores de las variables.

## 📋 Algoritmo a Trazar

```
ALGORITMO CalcularDescuento
    VARIABLES
        precio, descuento, precio_final: REAL
        porcentaje: ENTERO
    
    INICIO
        LEER precio
        LEER porcentaje
        
        descuento ← precio * (porcentaje / 100)
        precio_final ← precio - descuento
        
        ESCRIBIR "Descuento aplicado:", descuento
        ESCRIBIR "Precio final:", precio_final
    FIN
FIN ALGORITMO
```

## 📥 Datos de Prueba

**Caso 1:**
- precio = 100
- porcentaje = 20

**Caso 2:**
- precio = 250
- porcentaje = 15

## 📝 Formato de la Tabla de Traza

Completa la siguiente tabla para cada caso:

```
| Paso | Instrucción | precio | porcentaje | descuento | precio_final | Salida |
|------|-------------|--------|------------|-----------|--------------|--------|
| 1    |             |        |            |           |              |        |
| 2    |             |        |            |           |              |        |
| ...  |             |        |            |           |              |        |
```

## 💡 Ejemplo de Cómo Llenar

| Paso | Instrucción | precio | porcentaje | descuento | precio_final | Salida |
|------|-------------|--------|------------|-----------|--------------|--------|
| 1    | LEER precio | 100 | - | - | - | - |
| 2    | LEER porcentaje | 100 | 20 | - | - | - |
| ... | ... | ... | ... | ... | ... | ... |

## ✅ Criterios de Evaluación

| Criterio | Puntos |
|----------|--------|
| Tabla correctamente estructurada | 20 |
| Pasos en orden correcto | 20 |
| Valores de variables correctos | 30 |
| Salidas correctas | 20 |
| Ambos casos resueltos | 10 |

## 🔍 Respuestas Esperadas

Después de completar la traza, verifica:

**Caso 1** (precio=100, porcentaje=20):
- ¿Cuál es el descuento? ____
- ¿Cuál es el precio final? ____

**Caso 2** (precio=250, porcentaje=15):
- ¿Cuál es el descuento? ____
- ¿Cuál es el precio final? ____

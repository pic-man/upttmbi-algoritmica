# 📘 Introducción a la Algorítmica

## ¿Qué es un Algoritmo?

Un **algoritmo** es una secuencia de pasos ordenados y finitos para resolver un problema.

### Ejemplo de la vida cotidiana: Preparar café

```
1. Tomar la taza
2. Agregar café instantáneo
3. Calentar agua
4. Verter el agua caliente en la taza
5. Revolver
6. Servir
```

Este es un algoritmo porque:
- ✅ Tiene pasos **ordenados** (uno después de otro)
- ✅ Es **finito** (tiene un fin)
- ✅ Resuelve un **problema** (preparar café)

## ¿Qué es un Programa?

Un **programa** es un algoritmo escrito en un lenguaje que la computadora puede entender y ejecutar.

```
ALGORITMO (idea) → PROGRAMA (código) → COMPUTADORA (ejecuta)
```

## Las Tres Partes de Todo Programa

Todo programa, sin importar qué tan complejo sea, tiene tres partes fundamentales:

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   ENTRADA   │ →   │   PROCESO   │ →   │   SALIDA    │
│             │     │             │     │             │
│ Datos que   │     │ Cálculos y  │     │ Resultados  │
│ ingresa el  │     │ operaciones │     │ que se      │
│ usuario     │     │             │     │ muestran    │
└─────────────┘     └─────────────┘     └─────────────┘
```

### Ejemplo: Calcular el doble de un número

| Parte | Descripción | En Python |
|-------|-------------|-----------|
| ENTRADA | El usuario ingresa un número | `numero = int(input("Número: "))` |
| PROCESO | Calculamos el doble | `doble = numero * 2` |
| SALIDA | Mostramos el resultado | `print(doble)` |

## ¿Qué es Python?

**Python** es un lenguaje de programación:
- 🐍 Fácil de aprender
- 📖 Código legible (parece inglés)
- 🆓 Gratuito
- 🌍 Usado en todo el mundo

## Tu Primer Programa

El programa más simple en Python:

```python
print("¡Hola, mundo!")
```

Este programa:
1. **ENTRADA**: No tiene (no pide datos)
2. **PROCESO**: No tiene (no hace cálculos)
3. **SALIDA**: Muestra el texto "¡Hola, mundo!"

---

## 📝 Resumen

- Un **algoritmo** es una secuencia de pasos para resolver un problema
- Un **programa** es un algoritmo escrito en código
- Todo programa tiene: **ENTRADA → PROCESO → SALIDA**
- **Python** es el lenguaje que usaremos para programar

---

**Siguiente tema:** [02_variables_tipos.md](./02_variables_tipos.md)

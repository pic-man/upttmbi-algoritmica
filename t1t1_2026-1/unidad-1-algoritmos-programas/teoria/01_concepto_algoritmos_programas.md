# 📖 01 - Concepto de Algoritmos y Programas

## ¿Qué es un Algoritmo?

Un **algoritmo** es un conjunto ordenado y finito de pasos o instrucciones que permiten resolver un problema o realizar una tarea específica.

> "Un algoritmo es como una receta de cocina: una serie de pasos claros que, si se siguen correctamente, llevan a un resultado esperado."

### Características de un Algoritmo

1. **Preciso**: Cada paso debe estar claramente definido
2. **Definido**: Si se sigue dos veces, produce el mismo resultado
3. **Finito**: Debe terminar en algún momento
4. **Tiene entrada**: Puede recibir datos de entrada
5. **Tiene salida**: Produce al menos un resultado

### Ejemplos de Algoritmos en la Vida Diaria

#### Algoritmo para Preparar Café ☕

```
1. Inicio
2. Llenar la cafetera con agua
3. Colocar el filtro
4. Agregar café molido al filtro
5. Encender la cafetera
6. Esperar a que termine de filtrar
7. Servir el café en una taza
8. Fin
```

#### Algoritmo para Cruzar la Calle 🚶

```
1. Inicio
2. Acercarse a la esquina
3. Mirar a la izquierda
4. Mirar a la derecha
5. Si hay vehículos cerca:
   5.1. Esperar a que pasen
   5.2. Volver al paso 3
6. Si no hay vehículos:
   6.1. Cruzar la calle
7. Fin
```

## ¿Qué es un Programa?

Un **programa** es la traducción de un algoritmo a un lenguaje de programación específico que puede ser ejecutado por una computadora.

### Diferencias entre Algoritmo y Programa

| Aspecto | Algoritmo | Programa |
|---------|-----------|----------|
| Lenguaje | Natural, pseudocódigo o diagrama | Lenguaje de programación |
| Ejecución | No ejecutable directamente | Ejecutable por computadora |
| Dependencia | Independiente del lenguaje | Dependiente del lenguaje |
| Abstracción | Alto nivel de abstracción | Nivel técnico específico |

### Ejemplo: Del Algoritmo al Programa

**Algoritmo** (en lenguaje natural):
```
1. Pedir dos números al usuario
2. Sumar los dos números
3. Mostrar el resultado
```

**Programa** (en Python):
```python
# Solicitar dos números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Calcular la suma
suma = numero1 + numero2

# Mostrar el resultado
print(f"La suma es: {suma}")
```

## Relación entre Algoritmo y Programa

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│    PROBLEMA     │ ──▶ │    ALGORITMO    │ ──▶ │    PROGRAMA     │
│                 │     │                 │     │                 │
│ (Qué resolver)  │     │ (Cómo resolver) │     │ (Implementación)│
└─────────────────┘     └─────────────────┘     └─────────────────┘
```

## Importancia de los Algoritmos

1. **Pensar antes de programar**: Diseñar el algoritmo ayuda a entender el problema
2. **Independencia del lenguaje**: Un buen algoritmo puede implementarse en cualquier lenguaje
3. **Facilita la comunicación**: Permite explicar la solución a otros
4. **Reduce errores**: Detecta problemas lógicos antes de programar
5. **Mejora la eficiencia**: Permite optimizar la solución

## 📝 Para Recordar

- Un **algoritmo** es la solución lógica a un problema
- Un **programa** es la implementación de un algoritmo en código
- Primero se diseña el algoritmo, luego se programa
- Los algoritmos son independientes del lenguaje de programación

## ✅ Ejercicio Rápido

¿Cuál de los siguientes es un algoritmo válido para calcular el área de un rectángulo?

A)
```
1. Calcular área
2. Mostrar resultado
```

B)
```
1. Obtener la base del rectángulo
2. Obtener la altura del rectángulo
3. Multiplicar base por altura
4. Mostrar el resultado
```

<details>
<summary>Ver respuesta</summary>

La respuesta correcta es **B**.

El algoritmo A no es válido porque:
- No especifica cómo calcular el área
- No indica qué datos necesita
- Es demasiado vago

El algoritmo B es válido porque:
- Indica claramente los datos necesarios (base y altura)
- Especifica la operación (multiplicar)
- Es preciso y completo
</details>

## 🔜 Siguiente Paso

Ahora que entiendes qué son los algoritmos y programas, aprenderás sobre los lenguajes algorítmicos y de programación.

[Ir a: 02 - Lenguaje Algorítmico y de Programación →](./02_lenguaje_algoritmico.md)

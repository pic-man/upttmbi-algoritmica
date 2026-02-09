# 📖 02 - Lenguaje Algorítmico y de Programación

## ¿Qué es un Lenguaje Algorítmico?

El **lenguaje algorítmico** es una forma de expresar algoritmos utilizando palabras y estructuras que permiten describir la solución de un problema de manera clara y precisa, sin depender de un lenguaje de programación específico.

### Tipos de Lenguaje Algorítmico

1. **Lenguaje Natural**: Usa el idioma cotidiano
2. **Pseudocódigo**: Mezcla de lenguaje natural con estructuras de programación
3. **Diagramas de Flujo**: Representación gráfica

## Lenguaje Natural

Es la forma más simple de expresar un algoritmo, usando el idioma que hablamos normalmente.

### Ejemplo: Determinar si un número es par

```
1. Inicio
2. Solicitar un número al usuario
3. Dividir el número entre 2
4. Si el residuo es cero, entonces el número es par
5. Si el residuo no es cero, entonces el número es impar
6. Mostrar el resultado
7. Fin
```

### Ventajas y Desventajas

| Ventajas | Desventajas |
|----------|-------------|
| Fácil de entender | Puede ser ambiguo |
| No requiere conocimientos técnicos | Difícil de traducir directamente a código |
| Rápido de escribir | Puede tener múltiples interpretaciones |

## Pseudocódigo

El **pseudocódigo** es una representación de un algoritmo que utiliza palabras clave similares a las de los lenguajes de programación, pero en español o el idioma del programador.

### Palabras Clave Comunes

| Palabra | Significado |
|---------|-------------|
| `INICIO` / `FIN` | Delimitan el algoritmo |
| `LEER` / `ESCRIBIR` | Entrada/salida de datos |
| `SI... ENTONCES... SINO` | Estructura de decisión |
| `MIENTRAS... HACER` | Ciclo mientras |
| `PARA... HASTA... HACER` | Ciclo para |
| `REPETIR... HASTA` | Ciclo repetir |

### Ejemplo: Calcular el promedio de 3 números

```
ALGORITMO CalcularPromedio
    INICIO
        VARIABLES
            num1, num2, num3, suma, promedio: REAL
        
        ESCRIBIR "Ingrese el primer número:"
        LEER num1
        
        ESCRIBIR "Ingrese el segundo número:"
        LEER num2
        
        ESCRIBIR "Ingrese el tercer número:"
        LEER num3
        
        suma ← num1 + num2 + num3
        promedio ← suma / 3
        
        ESCRIBIR "El promedio es:", promedio
    FIN
FIN ALGORITMO
```

### Símbolos Comunes en Pseudocódigo

| Símbolo | Significado |
|---------|-------------|
| `←` o `=` | Asignación |
| `+`, `-`, `*`, `/` | Operaciones aritméticas |
| `=`, `<>`, `<`, `>`, `<=`, `>=` | Comparaciones |
| `Y`, `O`, `NO` | Operadores lógicos |

## ¿Qué es un Lenguaje de Programación?

Un **lenguaje de programación** es un conjunto de reglas sintácticas y semánticas que permiten escribir instrucciones que una computadora puede interpretar y ejecutar.

### Niveles de Lenguajes de Programación

```
┌─────────────────────────────────────────────┐
│           ALTO NIVEL                        │
│  Python, JavaScript, Java, C#               │
│  (Más cercano al lenguaje humano)           │
├─────────────────────────────────────────────┤
│           NIVEL MEDIO                       │
│  C, C++                                     │
│  (Balance entre abstracción y control)      │
├─────────────────────────────────────────────┤
│           BAJO NIVEL                        │
│  Ensamblador                                │
│  (Cercano al lenguaje máquina)              │
├─────────────────────────────────────────────┤
│           LENGUAJE MÁQUINA                  │
│  Binario (0s y 1s)                          │
│  (Lo que entiende la computadora)           │
└─────────────────────────────────────────────┘
```

### Comparación: Pseudocódigo vs Python

**Pseudocódigo:**
```
SI edad >= 18 ENTONCES
    ESCRIBIR "Es mayor de edad"
SINO
    ESCRIBIR "Es menor de edad"
FIN SI
```

**Python:**
```python
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")
```

## Proceso de Desarrollo

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   Problema   │ ──▶ │  Algoritmo   │ ──▶ │   Código     │
│              │     │ (Pseudocódigo│     │   (Python)   │
│              │     │  o diagrama) │     │              │
└──────────────┘     └──────────────┘     └──────────────┘
                            │
                            ▼
                     ┌──────────────┐
                     │   Pruebas    │
                     │              │
                     └──────────────┘
```

## 📝 Para Recordar

- El **lenguaje algorítmico** permite expresar soluciones sin depender de un lenguaje específico
- El **pseudocódigo** es un puente entre el pensamiento humano y el código
- Los **lenguajes de programación** son herramientas para implementar algoritmos
- Siempre es recomendable diseñar el algoritmo antes de programar

## ✅ Ejercicio Rápido

Convierte el siguiente pseudocódigo a Python:

```
ALGORITMO CalcularAreaTriangulo
    INICIO
        ESCRIBIR "Ingrese la base:"
        LEER base
        ESCRIBIR "Ingrese la altura:"
        LEER altura
        area ← (base * altura) / 2
        ESCRIBIR "El área es:", area
    FIN
FIN ALGORITMO
```

<details>
<summary>Ver respuesta</summary>

```python
# Algoritmo para calcular el área de un triángulo

# Entrada de datos
base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))

# Proceso
area = (base * altura) / 2

# Salida
print(f"El área es: {area}")
```
</details>

## 🔜 Siguiente Paso

Ahora aprenderás sobre las partes que componen un algoritmo.

[Ir a: 03 - Partes de un Algoritmo →](./03_partes_algoritmo.md)

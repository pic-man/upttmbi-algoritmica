# 📖 05 - Formas de Representar un Algoritmo

## Tres Formas Principales

Los algoritmos pueden representarse de diferentes maneras, cada una con sus ventajas:

```
┌─────────────────────────────────────────────────────────────┐
│           FORMAS DE REPRESENTAR ALGORITMOS                   │
├───────────────────┬───────────────────┬─────────────────────┤
│  LENGUAJE NATURAL │   PSEUDOCÓDIGO    │ DIAGRAMA DE FLUJO   │
│                   │                   │                     │
│  Texto en español │  Texto            │  Símbolos           │
│  o tu idioma      │  estructurado     │  gráficos           │
└───────────────────┴───────────────────┴─────────────────────┘
```

## 1. Lenguaje Natural

Es la descripción del algoritmo usando el idioma cotidiano (español, inglés, etc.).

### Ejemplo: Determinar si un estudiante aprobó

```
1. Inicio
2. Solicitar la calificación del estudiante
3. Si la calificación es mayor o igual a 6, entonces
   el estudiante está aprobado
4. Si la calificación es menor a 6, entonces
   el estudiante está reprobado
5. Mostrar si aprobó o reprobó
6. Fin
```

### Ventajas y Desventajas

| Ventajas | Desventajas |
|----------|-------------|
| ✅ Fácil de escribir | ❌ Puede ser ambiguo |
| ✅ No requiere conocimientos técnicos | ❌ Difícil de convertir a código |
| ✅ Cualquiera puede entenderlo | ❌ Puede ser muy extenso |

## 2. Pseudocódigo

Es una representación estructurada que usa palabras clave similares a las de programación.

### Estructura Básica

```
ALGORITMO NombreDelAlgoritmo
    VARIABLES
        // Declaración de variables
    CONSTANTES
        // Declaración de constantes
    INICIO
        // Instrucciones del algoritmo
    FIN
FIN ALGORITMO
```

### Palabras Clave del Pseudocódigo

| Español | Función |
|---------|---------|
| `ALGORITMO` | Inicio de la definición |
| `INICIO` / `FIN` | Delimitan el cuerpo |
| `VARIABLES` | Sección de declaración |
| `LEER` | Entrada de datos |
| `ESCRIBIR` | Salida de datos |
| `SI... ENTONCES... SINO... FIN SI` | Decisión |
| `MIENTRAS... HACER... FIN MIENTRAS` | Ciclo |
| `PARA... HASTA... HACER... FIN PARA` | Ciclo con contador |
| `←` | Asignación |

### Ejemplo: Calcular el mayor de dos números

```
ALGORITMO MayorDeDos
    VARIABLES
        num1, num2, mayor: ENTERO
    
    INICIO
        ESCRIBIR "Ingrese el primer número:"
        LEER num1
        
        ESCRIBIR "Ingrese el segundo número:"
        LEER num2
        
        SI num1 > num2 ENTONCES
            mayor ← num1
        SINO
            mayor ← num2
        FIN SI
        
        ESCRIBIR "El mayor es:", mayor
    FIN
FIN ALGORITMO
```

### Ventajas y Desventajas

| Ventajas | Desventajas |
|----------|-------------|
| ✅ Estructura clara | ❌ Requiere aprender la sintaxis |
| ✅ Fácil de convertir a código | ❌ No es estándar universal |
| ✅ Independiente del lenguaje | ❌ Puede variar entre autores |

## 3. Diagrama de Flujo

Es una representación **gráfica** del algoritmo usando símbolos estandarizados.

### Símbolos Básicos

```
┌─────────────────────────────────────────────────────────────┐
│                   SÍMBOLOS DE DIAGRAMA DE FLUJO             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│     ┌─────────┐                                             │
│     │  INICIO │    INICIO / FIN                             │
│     │   FIN   │    (Óvalo o rectángulo redondeado)          │
│     └─────────┘                                             │
│                                                             │
│     ┌─────────┐                                             │
│     │         │    PROCESO                                  │
│     │         │    (Rectángulo)                             │
│     └─────────┘    Operaciones, cálculos, asignaciones      │
│                                                             │
│     ╱╲                                                      │
│    ╱  ╲            DECISIÓN                                 │
│   ╱    ╲           (Rombo)                                  │
│   ╲    ╱           Condiciones SI/NO                        │
│    ╲  ╱                                                     │
│     ╲╱                                                      │
│                                                             │
│     ┌──────────┐                                            │
│    ╱            ╲  ENTRADA/SALIDA                           │
│   ╱              ╲ (Paralelogramo)                          │
│   ╲              ╱ Leer datos, mostrar resultados           │
│    ╲            ╱                                           │
│     └──────────┘                                            │
│                                                             │
│         │                                                   │
│         │          LÍNEA DE FLUJO                           │
│         ▼          (Flecha)                                 │
│                    Indica la secuencia                      │
│                                                             │
│        ○           CONECTOR                                 │
│                    (Círculo)                                │
│                    Une partes del diagrama                  │
└─────────────────────────────────────────────────────────────┘
```

### Ejemplo: Calcular el mayor de dos números

```
        ┌─────────┐
        │ INICIO  │
        └────┬────┘
             │
             ▼
    ┌────────────────┐
   ╱                  ╲
  ╱  Leer num1, num2   ╲
  ╲                    ╱
   ╲                  ╱
    └───────┬────────┘
            │
            ▼
       ╱╲
      ╱  ╲
     ╱    ╲
    ╱ num1 ╲
   ╱   >    ╲
  ╱  num2?   ╲
  ╲          ╱
   ╲        ╱
    ╲      ╱
     ╲    ╱
      ╲  ╱
       ╲╱
    Sí │      │ No
       │      │
       ▼      ▼
┌──────────┐ ┌──────────┐
│ mayor ←  │ │ mayor ←  │
│   num1   │ │   num2   │
└────┬─────┘ └────┬─────┘
     │            │
     └──────┬─────┘
            │
            ▼
    ┌────────────────┐
   ╱                  ╲
  ╱  Escribir mayor    ╲
  ╲                    ╱
   ╲                  ╱
    └───────┬────────┘
            │
            ▼
        ┌─────────┐
        │   FIN   │
        └─────────┘
```

### Ventajas y Desventajas

| Ventajas | Desventajas |
|----------|-------------|
| ✅ Visual y fácil de seguir | ❌ Puede ser grande y complejo |
| ✅ Identifica flujo claramente | ❌ Requiere herramientas para dibujar |
| ✅ Estándar internacional | ❌ Difícil de modificar |

## Comparación de las Tres Formas

### Problema: Calcular el área de un rectángulo

**Lenguaje Natural:**
```
1. Inicio
2. Pedir la base del rectángulo
3. Pedir la altura del rectángulo
4. Multiplicar la base por la altura para obtener el área
5. Mostrar el área calculada
6. Fin
```

**Pseudocódigo:**
```
ALGORITMO AreaRectangulo
    VARIABLES
        base, altura, area: REAL
    INICIO
        ESCRIBIR "Ingrese la base:"
        LEER base
        ESCRIBIR "Ingrese la altura:"
        LEER altura
        area ← base * altura
        ESCRIBIR "El área es:", area
    FIN
FIN ALGORITMO
```

**Diagrama de Flujo:**
```
    ┌─────────┐
    │ INICIO  │
    └────┬────┘
         │
         ▼
   ╱────────────╲
  ╱ Leer base    ╲
  ╲              ╱
   ╲────────────╱
         │
         ▼
   ╱────────────╲
  ╱ Leer altura  ╲
  ╲              ╱
   ╲────────────╱
         │
         ▼
  ┌──────────────┐
  │ area ←       │
  │ base*altura  │
  └──────┬───────┘
         │
         ▼
   ╱────────────╲
  ╱ Escribir     ╲
  ╲ area         ╱
   ╲────────────╱
         │
         ▼
    ┌─────────┐
    │   FIN   │
    └─────────┘
```

## ¿Cuándo Usar Cada Forma?

| Situación | Forma Recomendada |
|-----------|-------------------|
| Explicar a alguien no técnico | Lenguaje Natural |
| Documentar formalmente | Pseudocódigo |
| Presentaciones visuales | Diagrama de Flujo |
| Preparar para programar | Pseudocódigo |
| Analizar la lógica | Diagrama de Flujo |

## 📝 Para Recordar

1. Existen tres formas principales: **Natural, Pseudocódigo, Diagrama**
2. El **lenguaje natural** es el más simple pero puede ser ambiguo
3. El **pseudocódigo** es estructurado y fácil de convertir a código
4. El **diagrama de flujo** es visual y muestra el flujo claramente
5. Puedes usar **más de una forma** para el mismo algoritmo

## ✅ Ejercicio Rápido

Representa el siguiente algoritmo en las tres formas:

**"Determinar si un número es positivo, negativo o cero"**

<details>
<summary>Ver respuesta</summary>

**Lenguaje Natural:**
```
1. Inicio
2. Pedir un número al usuario
3. Si el número es mayor que cero, es positivo
4. Si el número es menor que cero, es negativo
5. Si el número es igual a cero, es cero
6. Mostrar el resultado
7. Fin
```

**Pseudocódigo:**
```
ALGORITMO TipoNumero
    VARIABLES
        numero: REAL
    INICIO
        ESCRIBIR "Ingrese un número:"
        LEER numero
        
        SI numero > 0 ENTONCES
            ESCRIBIR "El número es positivo"
        SINO SI numero < 0 ENTONCES
            ESCRIBIR "El número es negativo"
        SINO
            ESCRIBIR "El número es cero"
        FIN SI
    FIN
FIN ALGORITMO
```
</details>

## 🔜 Siguiente Paso

Ahora aprenderás sobre la traza de un algoritmo (corrida en frío).

[Ir a: 06 - Traza de un Algoritmo →](./06_traza_algoritmo.md)

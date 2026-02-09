# 📖 06 - Traza de un Algoritmo (Corrida en Frío)

## ¿Qué es una Traza?

La **traza** o **corrida en frío** es la ejecución manual paso a paso de un algoritmo, registrando los valores de las variables en cada momento. Es como "ser la computadora" y ejecutar el algoritmo con papel y lápiz.

> "La traza es una herramienta fundamental para verificar que un algoritmo funciona correctamente antes de programarlo."

## ¿Para Qué Sirve?

1. **Verificar la lógica** del algoritmo
2. **Detectar errores** antes de programar
3. **Entender el comportamiento** del algoritmo
4. **Depurar problemas** cuando algo no funciona
5. **Aprender** cómo fluyen los datos

## Cómo Hacer una Traza

### Pasos para Realizar una Traza

1. **Crear una tabla** con columnas para cada variable
2. **Agregar columna de salida** (lo que se muestra)
3. **Seguir cada instrucción** en orden
4. **Actualizar los valores** cuando cambien
5. **Registrar las salidas** cuando ocurran

### Formato de la Tabla de Traza

| Paso | Instrucción | var1 | var2 | var3 | Salida |
|------|-------------|------|------|------|--------|
| 1    | ...         | ...  | ...  | ...  | ...    |
| 2    | ...         | ...  | ...  | ...  | ...    |

## Ejemplo 1: Suma de Dos Números

### Algoritmo

```
ALGORITMO SumarDosNumeros
    VARIABLES
        a, b, suma: ENTERO
    INICIO
        LEER a
        LEER b
        suma ← a + b
        ESCRIBIR suma
    FIN
FIN ALGORITMO
```

### Datos de Prueba
- a = 5
- b = 3

### Tabla de Traza

| Paso | Instrucción | a | b | suma | Salida |
|------|-------------|---|---|------|--------|
| 1    | LEER a | 5 | - | - | - |
| 2    | LEER b | 5 | 3 | - | - |
| 3    | suma ← a + b | 5 | 3 | 8 | - |
| 4    | ESCRIBIR suma | 5 | 3 | 8 | **8** |

### Resultado
El algoritmo produce la salida **8**, que es correcto (5 + 3 = 8).

## Ejemplo 2: Con Estructura de Decisión

### Algoritmo

```
ALGORITMO MayorDeDos
    VARIABLES
        num1, num2, mayor: ENTERO
    INICIO
        LEER num1
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

### Datos de Prueba
- num1 = 7
- num2 = 12

### Tabla de Traza

| Paso | Instrucción | num1 | num2 | mayor | Condición | Salida |
|------|-------------|------|------|-------|-----------|--------|
| 1    | LEER num1 | 7 | - | - | - | - |
| 2    | LEER num2 | 7 | 12 | - | - | - |
| 3    | SI num1 > num2 | 7 | 12 | - | 7 > 12 = **FALSO** | - |
| 4    | mayor ← num2 | 7 | 12 | 12 | - | - |
| 5    | ESCRIBIR mayor | 7 | 12 | 12 | - | **El mayor es: 12** |

### Resultado
El algoritmo produce **12**, que es correcto.

## Ejemplo 3: Con Ciclo (Bucle)

### Algoritmo

```
ALGORITMO SumarHastaN
    VARIABLES
        n, i, suma: ENTERO
    INICIO
        LEER n
        suma ← 0
        i ← 1
        MIENTRAS i <= n HACER
            suma ← suma + i
            i ← i + 1
        FIN MIENTRAS
        ESCRIBIR "La suma es:", suma
    FIN
FIN ALGORITMO
```

### Datos de Prueba
- n = 4

### Tabla de Traza

| Paso | Instrucción | n | i | suma | Condición | Salida |
|------|-------------|---|---|------|-----------|--------|
| 1    | LEER n | 4 | - | - | - | - |
| 2    | suma ← 0 | 4 | - | 0 | - | - |
| 3    | i ← 1 | 4 | 1 | 0 | - | - |
| 4    | MIENTRAS i <= n | 4 | 1 | 0 | 1 <= 4 = **V** | - |
| 5    | suma ← suma + i | 4 | 1 | 1 | - | - |
| 6    | i ← i + 1 | 4 | 2 | 1 | - | - |
| 7    | MIENTRAS i <= n | 4 | 2 | 1 | 2 <= 4 = **V** | - |
| 8    | suma ← suma + i | 4 | 2 | 3 | - | - |
| 9    | i ← i + 1 | 4 | 3 | 3 | - | - |
| 10   | MIENTRAS i <= n | 4 | 3 | 3 | 3 <= 4 = **V** | - |
| 11   | suma ← suma + i | 4 | 3 | 6 | - | - |
| 12   | i ← i + 1 | 4 | 4 | 6 | - | - |
| 13   | MIENTRAS i <= n | 4 | 4 | 6 | 4 <= 4 = **V** | - |
| 14   | suma ← suma + i | 4 | 4 | 10 | - | - |
| 15   | i ← i + 1 | 4 | 5 | 10 | - | - |
| 16   | MIENTRAS i <= n | 4 | 5 | 10 | 5 <= 4 = **F** | - |
| 17   | ESCRIBIR suma | 4 | 5 | 10 | - | **La suma es: 10** |

### Verificación
Suma de 1 a 4: 1 + 2 + 3 + 4 = 10 ✅

## Errores Comunes que Detecta la Traza

### 1. Error de Inicialización

```
// Error: suma no inicializada
LEER n
i ← 1
MIENTRAS i <= n HACER
    suma ← suma + i    // ¿Cuál es el valor inicial de suma?
    i ← i + 1
FIN MIENTRAS
```

### 2. Ciclo Infinito

```
// Error: i nunca cambia
MIENTRAS i <= n HACER
    suma ← suma + i
    // Falta: i ← i + 1
FIN MIENTRAS
```

### 3. Condición Incorrecta

```
// Error: nunca entra al ciclo si i empieza en 1
i ← 1
MIENTRAS i < 1 HACER    // Debería ser i <= n
    ...
FIN MIENTRAS
```

## Plantilla de Tabla de Traza

```
┌──────┬─────────────────────┬──────┬──────┬──────┬───────────┬────────┐
│ Paso │     Instrucción     │ var1 │ var2 │ var3 │ Condición │ Salida │
├──────┼─────────────────────┼──────┼──────┼──────┼───────────┼────────┤
│  1   │                     │      │      │      │           │        │
├──────┼─────────────────────┼──────┼──────┼──────┼───────────┼────────┤
│  2   │                     │      │      │      │           │        │
├──────┼─────────────────────┼──────┼──────┼──────┼───────────┼────────┤
│  3   │                     │      │      │      │           │        │
└──────┴─────────────────────┴──────┴──────┴──────┴───────────┴────────┘
```

## Consejos para Hacer Trazas

1. **Usa lápiz** - Podrás borrar y corregir
2. **Sé ordenado** - Sigue cada paso sistemáticamente
3. **No asumas nada** - Ejecuta exactamente lo que dice el algoritmo
4. **Prueba varios casos** - Especialmente casos límite
5. **Verifica el resultado** - Compara con lo esperado

## Casos de Prueba Recomendados

| Tipo de Caso | Descripción | Ejemplo |
|--------------|-------------|---------|
| Normal | Valores típicos | n = 5 |
| Límite inferior | Valor mínimo | n = 0, n = 1 |
| Límite superior | Valor grande | n = 100 |
| Negativo | Valores negativos | n = -5 |
| Especial | Casos particulares | División por cero |

## 📝 Para Recordar

1. La **traza** es ejecutar el algoritmo manualmente
2. Usar una **tabla** para registrar valores de variables
3. Seguir las instrucciones **en orden**
4. Probar con **diferentes datos** de entrada
5. Es fundamental para **detectar errores**

## ✅ Ejercicio Práctico

Realiza la traza del siguiente algoritmo con n = 3:

```
ALGORITMO Factorial
    VARIABLES
        n, i, fact: ENTERO
    INICIO
        LEER n
        fact ← 1
        i ← 1
        MIENTRAS i <= n HACER
            fact ← fact * i
            i ← i + 1
        FIN MIENTRAS
        ESCRIBIR "Factorial:", fact
    FIN
FIN ALGORITMO
```

<details>
<summary>Ver respuesta</summary>

| Paso | Instrucción | n | i | fact | Condición | Salida |
|------|-------------|---|---|------|-----------|--------|
| 1    | LEER n | 3 | - | - | - | - |
| 2    | fact ← 1 | 3 | - | 1 | - | - |
| 3    | i ← 1 | 3 | 1 | 1 | - | - |
| 4    | MIENTRAS i <= n | 3 | 1 | 1 | 1 <= 3 = V | - |
| 5    | fact ← fact * i | 3 | 1 | 1 | - | - |
| 6    | i ← i + 1 | 3 | 2 | 1 | - | - |
| 7    | MIENTRAS i <= n | 3 | 2 | 1 | 2 <= 3 = V | - |
| 8    | fact ← fact * i | 3 | 2 | 2 | - | - |
| 9    | i ← i + 1 | 3 | 3 | 2 | - | - |
| 10   | MIENTRAS i <= n | 3 | 3 | 2 | 3 <= 3 = V | - |
| 11   | fact ← fact * i | 3 | 3 | 6 | - | - |
| 12   | i ← i + 1 | 3 | 4 | 6 | - | - |
| 13   | MIENTRAS i <= n | 3 | 4 | 6 | 4 <= 3 = F | - |
| 14   | ESCRIBIR fact | 3 | 4 | 6 | - | **Factorial: 6** |

**Verificación**: 3! = 3 × 2 × 1 = 6 ✅
</details>

---

¡Felicidades! Has completado la teoría de la Unidad 1. Ahora puedes pasar a los ejercicios prácticos.

[Ir a: Ejercicios →](../ejercicios/README.md)

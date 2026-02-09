# 🔍 Ejercicio 01: Traza de Algoritmo

## Nivel: ⭐ Básico

## 📝 Descripción

Realiza la **traza completa** del siguiente algoritmo, documentando cada paso según los estándares de calidad aprendidos.

## 🎯 Objetivo

Practicar la trazabilidad de algoritmos siguiendo un formato estándar de documentación.

## 📋 Algoritmo a Trazar

```
ALGORITMO CalcularSerie
    VARIABLES
        n, i, termino, suma: ENTERO
    INICIO
        LEER n
        suma ← 0
        termino ← 1
        
        PARA i ← 1 HASTA n HACER
            suma ← suma + termino
            termino ← termino * 2
        FIN PARA
        
        ESCRIBIR "La suma es:", suma
    FIN
FIN ALGORITMO
```

## 📥 Datos de Prueba

Realiza la traza para **n = 4**

## 📝 Formato de Entrega

Utiliza la siguiente plantilla de documento de traza:

```
═══════════════════════════════════════════════════════════
                    DOCUMENTO DE TRAZA
═══════════════════════════════════════════════════════════

INFORMACIÓN DEL ALGORITMO
─────────────────────────
Nombre: CalcularSerie
Propósito: [Describe qué calcula el algoritmo]
Fecha de traza: [Tu fecha]
Realizado por: [Tu nombre]

DATOS DE ENTRADA
─────────────────────────
n = 4

TABLA DE TRAZA
─────────────────────────
| Paso | Instrucción | n | i | termino | suma | Condición |
|------|-------------|---|---|---------|------|-----------|
| 1    |             |   |   |         |      |           |
| ...  |             |   |   |         |      |           |

RESULTADO
─────────────────────────
Salida esperada: [Calcula manualmente]
Salida obtenida: [Resultado de la traza]
Estado: [ ] Correcto  [ ] Incorrecto

ANÁLISIS
─────────────────────────
[Explica qué serie calcula este algoritmo]
[Identifica el patrón matemático]

═══════════════════════════════════════════════════════════
```

## ✅ Criterios de Evaluación

| Criterio | Puntos |
|----------|--------|
| Formato del documento completo | 20 |
| Tabla de traza correcta | 40 |
| Resultado correcto | 20 |
| Análisis del algoritmo | 20 |

## 💡 Pista

Observa qué valores toma `termino` en cada iteración: 1, 2, 4, 8...
¿Qué serie matemática representa?

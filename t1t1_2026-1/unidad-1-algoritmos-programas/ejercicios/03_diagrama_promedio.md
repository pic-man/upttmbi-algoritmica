# 📊 Ejercicio 03: Diagrama de Flujo - Promedio

## Nivel: ⭐ Básico

## 📝 Descripción

Diseña un **diagrama de flujo** que calcule el promedio de tres calificaciones y determine si el estudiante aprobó (promedio >= 6) o reprobó.

## 🎯 Objetivo

Practicar la representación gráfica de algoritmos usando los símbolos estándar de diagramas de flujo.

## 📋 Requisitos

1. Usar los símbolos correctos:
   - Óvalo: Inicio/Fin
   - Paralelogramo: Entrada/Salida
   - Rectángulo: Proceso
   - Rombo: Decisión
2. Las flechas deben indicar el flujo
3. Incluir la decisión de aprobado/reprobado

## 📥 Entrada

- Tres calificaciones (números del 0 al 10)

## 📤 Salida

- El promedio calculado
- Mensaje: "Aprobado" o "Reprobado"

## 💡 Símbolos a Usar

```
    ┌─────────┐
    │ INICIO  │     Inicio/Fin (Óvalo)
    └─────────┘

   ╱──────────╲
  ╱   LEER     ╲    Entrada/Salida (Paralelogramo)
  ╲            ╱
   ╲──────────╱

  ┌────────────┐
  │  PROCESO   │    Proceso (Rectángulo)
  └────────────┘

       ╱╲
      ╱  ╲
     ╱    ╲          Decisión (Rombo)
    ╱  ??  ╲
    ╲      ╱
     ╲    ╱
      ╲  ╱
       ╲╱
```

## 📝 Estructura Esperada

```
     INICIO
        ↓
    Leer cal1, cal2, cal3
        ↓
    promedio = (cal1+cal2+cal3)/3
        ↓
    ¿promedio >= 6?
     ↙      ↘
   Sí        No
    ↓         ↓
 "Aprobado" "Reprobado"
     ↘      ↙
        ↓
    Mostrar promedio y resultado
        ↓
       FIN
```

## ✅ Criterios de Evaluación

| Criterio | Puntos |
|----------|--------|
| Símbolos correctos | 25 |
| Flujo claro y ordenado | 25 |
| Decisión bien implementada | 25 |
| Inicio y fin presentes | 15 |
| Etiquetas legibles | 10 |

## 🛠️ Herramientas Sugeridas

- Papel y lápiz (para práctica)
- Draw.io (online, gratuito)
- Lucidchart
- Microsoft Visio
- PowerPoint/Google Slides

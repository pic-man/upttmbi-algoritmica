# 📊 Ejercicio 15: Análisis de Ventas

## Dificultad: ⭐⭐ Intermedio

## 📝 Descripción

Tienes ventas mensuales del año. Encuentra qué mes tuvo las ventas más altas, cuál fue su posición, y calcula el promedio anual.

## 🎯 Objetivo

Practicar `max()`, `index()` y `sum()`.

## 💻 Listas Iniciales

```python
ventas = [1200, 1500, 980, 2100, 1800, 1650, 2300, 1900, 1750, 2000, 2200, 2500]
meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
```

## 💻 Ejemplo de Ejecución

```
=== ANÁLISIS DE VENTAS ANUALES ===

📊 VENTAS POR MES:
Ene: $1,200
Feb: $1,500
Mar: $980
Abr: $2,100
May: $1,800
Jun: $1,650
Jul: $2,300
Ago: $1,900
Sep: $1,750
Oct: $2,000
Nov: $2,200
Dic: $2,500

📈 ANÁLISIS:

Mejor mes: Diciembre
Ventas más altas: $2,500
Posición en el año: Mes #12

Peor mes: Marzo
Ventas más bajas: $980

📊 Promedio anual: $1,823.33

Meses sobre el promedio: 7
Meses bajo el promedio: 5

Total anual: $21,880
```

## 💡 Pistas

1. `max(ventas)` para mayor venta
2. `ventas.index(max(ventas))` para posición
3. `sum(ventas) / len(ventas)` para promedio
4. Usa f-strings para formato: `f"${venta:,}"`

---

**Tiempo estimado**: 20-25 minutos  
**Archivo de solución**: `ejercicio_15.py`


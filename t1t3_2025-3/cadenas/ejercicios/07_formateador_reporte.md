# 📊 Ejercicio 7: Formateador de Reportes

## Dificultad: ⭐⭐ Intermedio

## 📝 Descripción

Genera un reporte tabular a partir de datos de ventas utilizando f-strings y métodos de alineación (`ljust`, `rjust`, `center`).

## 🎯 Objetivo

Practicar el formateo de cadenas con alineaciones y plantillas multilinea.

## 📋 Especificaciones

1. Usa la lista `ventas` con tuplas `(producto, unidades, precio_unitario)`.
2. Calcula el total por producto y el total general.
3. Construye un reporte alineado con encabezados.
4. Usa separadores como `-` repetidos.

## 💻 Datos Iniciales

```python
ventas = [
    ("Teclado", 12, 25.5),
    ("Mouse", 20, 15.0),
    ("Monitor", 5, 210.99),
]
```

## 💻 Ejemplo de Ejecución

```
=========== REPORTE DE VENTAS ===========
Producto           Unidades   P.Unit    Total
----------------------------------------------
Teclado            12         25.50     306.00
Mouse              20         15.00     300.00
Monitor            5          210.99    1054.95
----------------------------------------------
TOTAL GENERAL                              1660.95
```

## 🧪 Casos de Prueba

- [ ] Alineas correctamente las columnas.
- [ ] Calcula los totales con dos decimales.
- [ ] El separador se adapta al ancho total.
- [ ] No pierdes precisión al formatear.

## 💡 Pistas

1. Usa `f"{texto:<15}"` para justificar a la izquierda.
2. Multiplica strings: `"-" * 46`.
3. `format(total, ".2f")` o `f"{total:.2f}"` asegura dos decimales.

## ⚠️ Errores Comunes

- ❌ No convertir números a float antes de multiplicar.
- ❌ Alineaciones inconsistentes por diferentes anchos.
- ❌ No recalcular el total general correctamente.

## 🎓 Conceptos Practicados

- f-strings avanzados
- Operaciones aritméticas con strings formateados
- Diseño de plantillas de texto

## 🚀 Desafíos Extra (Opcional)

1. Ajusta el ancho de cada columna dinámicamente según el dato más largo.
2. Añade una columna con el porcentaje del total respecto al general.
3. Exporta el reporte a un archivo `.txt`.

---

**Tiempo estimado**: 18 minutos  
**Archivo de solución**: `ejercicio_07.py`  
**Métodos a usar**: f-strings, `ljust()`, `rjust()`

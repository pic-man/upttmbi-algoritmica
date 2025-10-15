# 🍎 Ejercicio 7: Contador de Frutas

## Dificultad: ⭐ Básico

## 📝 Descripción

Crea un programa que pida el nombre de una fruta y muestre su precio por kilogramo.

## 🎯 Objetivo

Practicar comparaciones con cadenas de texto (strings).

## 📋 Especificaciones

El programa debe:

1. Solicitar el nombre de una fruta
2. Mostrar el precio según:
   - **Manzana**: $15 por kg
   - **Naranja**: $12 por kg
   - **Plátano**: $10 por kg
   - **Otra fruta**: "No disponible"

## 💻 Ejemplo de Ejecución

### Ejemplo 1:
```
¿Qué fruta deseas?
Frutas disponibles: manzana, naranja, plátano

Ingresa el nombre de la fruta: manzana
Manzana: $15 por kg
```

### Ejemplo 2:
```
¿Qué fruta deseas?
Frutas disponibles: manzana, naranja, plátano

Ingresa el nombre de la fruta: naranja
Naranja: $12 por kg
```

### Ejemplo 3:
```
¿Qué fruta deseas?
Frutas disponibles: manzana, naranja, plátano

Ingresa el nombre de la fruta: uva
Lo sentimos, uva no está disponible
```

## 🧪 Casos de Prueba

Prueba tu programa con estos valores:

| Entrada | Salida |
|---------|--------|
| manzana | $15 por kg |
| Manzana | $15 por kg |
| MANZANA | $15 por kg |
| naranja | $12 por kg |
| plátano | $10 por kg |
| platano | $10 por kg |
| uva | No disponible |
| "" (vacío) | No disponible |

## 💡 Pistas

1. Usa `.lower()` para convertir a minúsculas:
   ```python
   fruta = input("Fruta: ").lower()
   ```
2. Esto permite que "Manzana", "MANZANA" y "manzana" funcionen igual
3. Para el plátano, considera ambas formas: "plátano" y "platano"

## ⚠️ Errores Comunes

- ❌ No considerar mayúsculas/minúsculas
- ❌ No manejar acentos (plátano vs platano)
- ❌ No validar entrada vacía

## 🎓 Conceptos Practicados

- Comparación de strings con `==`
- Método `.lower()` para normalizar texto
- `if-elif-else` con strings
- Manejo de acentos opcionales

## 🚀 Desafíos Extra (Opcional)

1. Agrega más frutas (5-10 opciones)
2. Permite al usuario comprar cantidad:
   - Pide: "¿Cuántos kg?"
   - Calcula el total
3. Muestra todos los precios en una tabla
4. Permite comprar múltiples frutas
5. Agrega descuentos por cantidad:
   - Más de 5 kg: 10% descuento
   - Más de 10 kg: 15% descuento

---

**Tiempo estimado**: 10-15 minutos  
**Archivo de solución**: `ejercicio_07.py`


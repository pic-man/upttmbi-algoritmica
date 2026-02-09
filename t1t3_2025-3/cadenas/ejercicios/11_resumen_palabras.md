# 🧮 Ejercicio 11: Resumen de Palabras

## Dificultad: ⭐⭐ Intermedio

## 📝 Descripción

Genera un resumen estadístico de un texto corto: cantidad total de palabras, palabras únicas y la más frecuente.

## 🎯 Objetivo

Practicar normalización, separación en palabras y conteo usando diccionarios o `count()`.

## 📋 Especificaciones

1. Recibir el texto `texto_raw`.
2. Convertir a minúsculas y eliminar signos básicos de puntuación (`.,;:!?`).
3. Dividir en palabras por espacios.
4. Calcular:
   - Total de palabras
   - Número de palabras únicas
   - Palabra con mayor frecuencia
5. Mostrar el resumen y un top 3 de palabras más usadas.

## 💻 Datos Iniciales

```python
texto_raw = "Python es poderoso y Python es divertido cuando practicas"
```

## 💻 Ejemplo de Ejecución

```
=== RESUMEN DE PALABRAS ===
Texto limpio: python es poderoso y python es divertido cuando practicas
Total de palabras: 9
Palabras únicas: 7
Top 3:
1. python (2)
2. es (2)
3. poderoso (1)
```

## 🧪 Casos de Prueba

- [ ] Quita correctamente la puntuación.
- [ ] Suma coincidentemente total y únicas.
- [ ] Resuelve empates en el top 3 de forma consistente.
- [ ] Maneja textos con una sola palabra.

## 💡 Pistas

1. Usa `texto.replace(",", "")` iterativamente o `translate()`.
2. `split()` produce una lista; conviértela en `set` para contar únicas.
3. Un diccionario puede almacenar frecuencias.

## ⚠️ Errores Comunes

- ❌ Contar palabras vacías por dobles espacios.
- ❌ Ignorar mayúsculas y considerar "Python" y "python" diferentes.
- ❌ No controlar listas vacías.

## 🎓 Conceptos Practicados

- Limpieza de texto
- Diccionarios de frecuencias
- Ordenamiento por valor

## 🚀 Desafíos Extra (Opcional)

1. Ignora palabras de una lista de stopwords (`el`, `la`, `de`).
2. Exporta el resumen a JSON.
3. Calcula la longitud promedio de las palabras.

---

**Tiempo estimado**: 15 minutos  
**Archivo de solución**: `ejercicio_11.py`  
**Métodos a usar**: `lower()`, `replace()`, `split()`, `set()`, `sorted()`

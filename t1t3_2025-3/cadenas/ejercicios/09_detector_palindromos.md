# 🔁 Ejercicio 9: Detector de Palíndromos

## Dificultad: ⭐⭐ Intermedio

## 📝 Descripción

Determina si una frase es un palíndromo ignorando espacios, signos y diferencias entre mayúsculas/minúsculas.

## 🎯 Objetivo

Practicar limpieza de cadenas, `replace()`, `lower()` y comparación con `[::-1]`.

## 📋 Especificaciones

1. Recibir la frase `frase_raw`.
2. Eliminar espacios y signos de puntuación (`.,;:!?¡¿"'`).
3. Convertir a minúsculas.
4. Comparar la cadena limpia con su versión invertida.
5. Mostrar un mensaje indicando si es palíndromo.

## 💻 Datos Iniciales

```python
frase_raw = "Anita lava la tina"
```

## 💻 Ejemplo de Ejecución

```
=== DETECTOR DE PALÍNDROMOS ===
Frase original: Anita lava la tina
Frase limpia: anitalavalatina
¿Es palíndromo? Sí
```

## 🧪 Casos de Prueba

- [ ] Detecta correctamente palíndromos clásicos.
- [ ] Rechaza frases que no lo son.
- [ ] Funciona con acentos (puedes removerlos o considerarlos).
- [ ] Controla frases vacías o muy cortas.

## 💡 Pistas

1. Usa un bucle o varias llamadas a `replace()` para limpiar.
2. `str.maketrans()` con `translate()` puede simplificar la limpieza.
3. `frase[::-1]` devuelve la cadena invertida.

## ⚠️ Errores Comunes

- ❌ No eliminar todos los signos, causando falsas negativas.
- ❌ Considerar acentos como caracteres distintos.
- ❌ Olvidar manejar mayúsculas/minúsculas.

## 🎓 Conceptos Practicados

- Normalización y limpieza
- Slicing inverso
- Lógica condicional

## 🚀 Desafíos Extra (Opcional)

1. Implementa una función que devuelva `True/False` y úsala en un programa.
2. Muestra los caracteres que causan que no sea palíndromo.
3. Acepta frases con números y considera solo los dígitos.

---

**Tiempo estimado**: 12 minutos  
**Archivo de solución**: `ejercicio_09.py`  
**Métodos a usar**: `lower()`, `replace()`, slicing

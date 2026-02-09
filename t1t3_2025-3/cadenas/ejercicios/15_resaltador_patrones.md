# 🔦 Ejercicio 15: Resaltador de Patrones

## Dificultad: ⭐⭐⭐ Avanzado

## 📝 Descripción

Dado un texto y una lista de patrones, resalta cada coincidencia envolviéndola en corchetes `[[...]]` sin afectar las coincidencias solapadas.

## 🎯 Objetivo

Practicar búsquedas múltiples, orden de reemplazos y manejo de offsets.

## 📋 Especificaciones

1. Texto base:
   ```python
   texto = "En 2025 Python lidera en IA, y PyCon 2025 será imperdible."
   patrones = ["Python", "PyCon", "2025", "IA"]
   ```
2. Encuentra todas las coincidencias (sin distinción de mayúsculas).
3. Resalta cada una con `[[coincidencia]]` en la cadena original.
4. Evita resaltar parcialmente coincidencias ya marcadas.
5. Muestra el texto resultante y un conteo por patrón.

## 💻 Ejemplo de Ejecución

```
=== RESALTADOR ===
Texto original: En 2025 Python lidera en IA, y PyCon 2025 será imperdible.
Texto resaltado: En [[2025]] [[Python]] lidera en [[IA]], y [[PyCon]] [[2025]] será imperdible.
Conteo:
- Python: 1
- PyCon: 1
- 2025: 2
- IA: 1
```

## 🧪 Casos de Prueba

- [ ] Respeta coincidencias independientes (no resalta "Py" dentro de "Python").
- [ ] Maneja patrones con distinta longitud.
- [ ] Funciona aunque el patrón aparezca al inicio o final.
- [ ] Acepta patrones repetidos en la lista sin duplicar el resaltado.

## 💡 Pistas

1. Ordena los patrones por longitud descendente para evitar solapamientos.
2. Usa índices para recorrer el texto y construir la nueva cadena.
3. `lower()` ayuda a comparar sin importar mayúsculas.

## ⚠️ Errores Comunes

- ❌ Reemplazar directamente con `replace()` y romper el conteo.
- ❌ No ajustar el índice tras insertar `[[ ]]`.
- ❌ Ignorar posiciones ya resaltadas.

## 🎓 Conceptos Practicados

- Manejo de offsets
- Construcción incremental de cadenas
- Lógica de coincidencias múltiples

## 🚀 Desafíos Extra (Opcional)

1. Permite resaltar con códigos de color ANSI.
2. Exporta el resultado a HTML usando `<mark>`.
3. Acepta expresiones regulares como patrones.

---

**Tiempo estimado**: 22 minutos  
**Archivo de solución**: `ejercicio_15.py`  
**Métodos a usar**: `lower()`, slicing, ciclos `while`

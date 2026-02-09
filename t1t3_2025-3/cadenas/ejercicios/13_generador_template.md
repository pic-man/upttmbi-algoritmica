# 🧾 Ejercicio 13: Generador de Plantillas

## Dificultad: ⭐⭐ Intermedio

## 📝 Descripción

Construye un pequeño motor de plantillas que reemplace marcadores en un texto (`{{nombre}}`, `{{fecha}}`) por valores proporcionados en un diccionario.

## 🎯 Objetivo

Practicar `replace()`, formateo con diccionarios y validaciones.

## 📋 Especificaciones

1. Cadena base:
   ```python
   plantilla = """
   Hola {{nombre}},
   Tu cita está programada para el {{fecha}} a las {{hora}}.
   Atentamente,
   {{empresa}}
   """
   ```
2. Diccionario datos:
   ```python
   datos = {
       "nombre": "Ana",
       "fecha": "12/03/2025",
       "hora": "10:30",
       "empresa": "Clínica Central"
   }
   ```
3. Reemplaza todos los marcadores y valida que no falte ninguno.
4. Si falta un valor, muestra un mensaje indicando cuál.

## 💻 Ejemplo de Ejecución

```
=== GENERADOR DE PLANTILLAS ===
Hola Ana,
Tu cita está programada para el 12/03/2025 a las 10:30.
Atentamente,
Clínica Central
```

## 🧪 Casos de Prueba

- [ ] Reemplaza todos los marcadores correctamente.
- [ ] Detecta marcadores no definidos en `datos`.
- [ ] Permite plantillas con marcadores repetidos.
- [ ] Maneja diccionarios con valores vacíos.

## 💡 Pistas

1. Recorre las llaves del diccionario y usa `replace()`.
2. Usa `set` para identificar marcadores únicos.
3. `str.format_map()` puede ser opcional si decides explorarlo.

## ⚠️ Errores Comunes

- ❌ Reemplazar `{nombre}` en lugar de `{{nombre}}`.
- ❌ No escapar correctamente las llaves si usas `format()`.
- ❌ Mutar la cadena base sin conservar una copia.

## 🎓 Conceptos Practicados

- Formateo de texto personalizado
- Uso de diccionarios
- Validaciones

## 🚀 Desafíos Extra (Opcional)

1. Permite valores por defecto (`{{campo|valor_default}}`).
2. Acepta plantillas desde archivo y genera un reporte en otro archivo.
3. Implementa soporte para bucles simples (`{{for item}} ... {{endfor}}`).

---

**Tiempo estimado**: 14 minutos  
**Archivo de solución**: `ejercicio_13.py`  
**Métodos a usar**: `replace()`, `split()`, `set()`

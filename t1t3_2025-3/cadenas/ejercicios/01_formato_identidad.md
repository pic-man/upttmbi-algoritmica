# 🪪 Ejercicio 1: Formato de Identidad

## Dificultad: ⭐ Básico

## 📝 Descripción

Recibes el nombre completo y el número de documento de una persona con mayúsculas/minúsculas desordenadas y espacios extra. Debes limpiar la entrada y generar un identificador estandarizado.

## 🎯 Objetivo

Practicar normalización con `strip()`, `split()`, `join()`, `upper()` y `lower()`.

## 📋 Especificaciones

El programa debe:

1. Recibir (o usar variables base) `nombre_raw` y `documento_raw`.
2. Quitar espacios al inicio y final.
3. Capitalizar cada palabra del nombre.
4. Eliminar guiones del documento y dejarlo en mayúsculas.
5. Mostrar un identificador en formato `NOMBRE APELLIDO - DOC: XXXXXXXX`.

## 💻 Datos Iniciales

```python
nombre_raw = "  aNa carLos  bravo  "
documento_raw = "  ab-1234-cd  "
```

## 💻 Ejemplo de Ejecución

```
=== NORMALIZADOR DE IDENTIDAD ===
Nombre original: '  aNa carLos  bravo  '
Documento original: '  ab-1234-cd  '

Nombre limpio: Ana Carlos Bravo
Documento limpio: AB1234CD
ID generado: ANA CARLOS BRAVO - DOC: AB1234CD
```

## 🧪 Casos de Prueba

- [ ] Elimina espacios sobrantes.
- [ ] Respeta la capitalización (cada palabra con inicial mayúscula).
- [ ] El documento final no tiene guiones ni espacios.
- [ ] El identificador está en mayúsculas.

## 💡 Pistas

1. Usa `strip()` para limpiar extremos.
2. `split()` sin argumentos divide por cualquier espacio.
3. `" ".join(...)` permite reconstruir el nombre normalizado.
4. `replace('-', '')` elimina guiones.

## ⚠️ Errores Comunes

- ❌ No convertir a mayúsculas antes de generar el identificador.
- ❌ Usar índices incorrectos al reconstruir el nombre.
- ❌ Olvidar que `strip()` no modifica la cadena original; debes reasignar.

## 🎓 Conceptos Practicados

- Normalización de texto
- Métodos básicos de cadenas
- Concatenación y formateo

## 🚀 Desafíos Extra (Opcional)

1. Solicita los datos desde `input()`.
2. Valida que el documento tenga exactamente 8 caracteres tras limpiar.
3. Genera un código interno con las iniciales y los 4 últimos caracteres del documento.

---

**Tiempo estimado**: 10 minutos  
**Archivo de solución**: `ejercicio_01.py`  
**Métodos a usar**: `strip()`, `split()`, `join()`, `upper()`, `replace()`

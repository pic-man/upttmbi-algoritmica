# 🔎 Ejercicio 6: Búsqueda de Coincidencias

## Dificultad: ⭐⭐ Intermedio

## 📝 Descripción

Escribe un programa que recorra un texto y reporte las posiciones en las que aparece una palabra clave.

## 🎯 Objetivo

Practicar `find()` con desplazamientos, slicing y acumulación de resultados.

## 📋 Especificaciones

1. Recibir el texto `texto` y la palabra `clave`.
2. Buscar todas las posiciones donde aparece la clave (permitir superposiciones).
3. Guardar las posiciones en una lista.
4. Mostrar el total y las posiciones encontradas.

## 💻 Datos Iniciales

```python
texto = "banana bandana"
clave = "ana"
```

## 💻 Ejemplo de Ejecución

```
=== BUSCADOR DE COINCIDENCIAS ===
Texto: banana bandana
Clave: ana

Coincidencias encontradas: 3
Índices: [1, 3, 11]
```

## 🧪 Casos de Prueba

- [ ] Maneja textos donde la clave no aparece.
- [ ] Funciona con claves de un solo carácter.
- [ ] Detecta coincidencias superpuestas (ej: "ana" en "banana").
- [ ] Lista de índices en orden ascendente.

## 💡 Pistas

1. Usa un ciclo `while` con `texto.find(clave, inicio)`.
2. Actualiza `inicio` con `pos + 1` para permitir superposición.
3. Si `find` devuelve `-1`, termina el bucle.

## ⚠️ Errores Comunes

- ❌ No reiniciar correctamente la búsqueda después de cada coincidencia.
- ❌ Olvidar manejar el caso `pos == -1`.
- ❌ No controlar claves vacías (puedes descartar este caso con una validación temprana).

## 🎓 Conceptos Practicados

- `find()` con desplazamiento
- Listas y acumulación
- Bucles `while`

## 🚀 Desafíos Extra (Opcional)

1. Muestra un extracto de texto alrededor de cada coincidencia.
2. Resalta la clave reemplazándola por `[...]` en el texto.
3. Crea una función reutilizable `buscar_coincidencias(texto, clave)`.

---

**Tiempo estimado**: 12 minutos  
**Archivo de solución**: `ejercicio_06.py`  
**Métodos a usar**: `find()`, `while`

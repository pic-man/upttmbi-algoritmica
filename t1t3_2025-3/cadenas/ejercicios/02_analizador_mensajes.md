# 💬 Ejercicio 2: Analizador de Mensajes

## Dificultad: ⭐ Básico

## 📝 Descripción

Tienes un mensaje recibido desde una API. Debes detectar si contiene palabras prohibidas y contabilizar cuántas veces aparece una palabra clave.

## 🎯 Objetivo

Aplicar `lower()`, `in`, `count()` y reportar resultados.

## 📋 Especificaciones

1. Convierte el mensaje a minúsculas para comparar.
2. Revisa si contiene alguna palabra de la lista `prohibidas`.
3. Cuenta cuántas veces aparece la palabra `"urgente"`.
4. Muestra un resumen con banderas booleanas.

## 💻 Datos Iniciales

```python
mensaje = "URGENTE: Reunión URGENTE mañana. Llevar informe urgente."
prohibidas = ["spam", "publicidad", "virus"]
```

## 💻 Ejemplo de Ejecución

```
=== ANALIZADOR ===
Mensaje original: URGENTE: Reunión URGENTE mañana. Llevar informe urgente.
Palabras prohibidas detectadas: No
Conteo 'urgente': 3
Requiere atención inmediata: Sí
```

## 🧪 Casos de Prueba

- [ ] Convierte correctamente a minúsculas antes de buscar.
- [ ] Detecta si existe alguna palabra prohibida.
- [ ] Cuenta las apariciones de "urgente".
- [ ] El resumen final usa Sí/No o True/False de forma consistente.

## 💡 Pistas

1. Usa un bucle para checar todas las palabras prohibidas.
2. `any()` puede ayudarte a evaluar una colección booleana.
3. Considera quitar signos de puntuación con `replace()` si lo crees necesario.

## ⚠️ Errores Comunes

- ❌ Buscar palabras sin normalizar el texto.
- ❌ Contar con `count()` sin convertir a minúsculas cuando el mensaje está en mayúsculas.
- ❌ No restablecer la versión original al mostrar el mensaje.

## 🎓 Conceptos Practicados

- Normalización
- Búsqueda en cadenas
- Resúmenes booleanos

## 🚀 Desafíos Extra (Opcional)

1. Reemplaza palabras prohibidas por `***` antes de mostrar.
2. Calcula el porcentaje de palabras clave respecto al total.
3. Permite ingresar la palabra clave a buscar desde teclado.

---

**Tiempo estimado**: 10 minutos  
**Archivo de solución**: `ejercicio_02.py`  
**Métodos a usar**: `lower()`, `count()`, `replace()`

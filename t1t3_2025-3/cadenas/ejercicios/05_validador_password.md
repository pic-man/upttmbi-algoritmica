# 🔐 Ejercicio 5: Validador de Contraseñas

## Dificultad: ⭐⭐ Intermedio

## 📝 Descripción

Crea un validador que determine si una contraseña cumple requisitos mínimos: longitud, mayúsculas, minúsculas, dígitos y símbolos.

## 🎯 Objetivo

Utilizar métodos `any()`, iteraciones y comprobaciones `isupper()`, `islower()`, `isdigit()`.

## 📋 Especificaciones

1. Recibir la contraseña `password`.
2. Verificar:
   - Longitud mínima de 8 caracteres.
   - Contiene al menos una mayúscula.
   - Contiene al menos una minúscula.
   - Contiene al menos un dígito.
   - Contiene al menos un símbolo de `!@#$%^&*`.
3. Mostrar un reporte por requisito y una conclusión final.

## 💻 Datos Iniciales

```python
password = "Py3!2025"
```

## 💻 Ejemplo de Ejecución

```
=== VALIDADOR DE CONTRASEÑAS ===
Contraseña analizada: Py3!2025

- Longitud mínima (8): ✅
- Contiene mayúscula: ✅
- Contiene minúscula: ✅
- Contiene dígito: ✅
- Contiene símbolo (!@#$%^&*): ✅

Resultado final: CONTRASEÑA SEGURA
```

## 🧪 Casos de Prueba

- [ ] Rechaza contraseñas sin símbolos.
- [ ] Funciona con contraseñas de longitud variable.
- [ ] No falla con símbolos no considerados.
- [ ] Mensajes claros en el reporte.

## 💡 Pistas

1. Usa `any(char.isupper() for char in password)`.
2. Define un conjunto `simbolos = set("!@#$%^&*")`.
3. Maneja el caso de contraseña vacía.

## ⚠️ Errores Comunes

- ❌ Olvidar verificar la longitud primero.
- ❌ Usar `if char in simbolos` sin convertir a conjunto (aunque funciona, es más lento).
- ❌ No normalizar el mensaje final (mostrar "INSEGURA" si falta algo).

## 🎓 Conceptos Practicados

- Funciones `any()` y `all()`
- Iteración sobre cadenas
- Validaciones condicionales

## 🚀 Desafíos Extra (Opcional)

1. Clasifica la fortaleza (débil, media, fuerte) según la cantidad de criterios cumplidos.
2. Muestra sugerencias personalizadas para cada fallo.
3. Genera un reporte en formato JSON.

---

**Tiempo estimado**: 15 minutos  
**Archivo de solución**: `ejercicio_05.py`  
**Métodos a usar**: `isupper()`, `islower()`, `isdigit()`, iteración

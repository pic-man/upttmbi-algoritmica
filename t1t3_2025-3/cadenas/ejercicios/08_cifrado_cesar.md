# 🔐 Ejercicio 8: Cifrado César

## Dificultad: ⭐⭐⭐ Avanzado

## 📝 Descripción

Implementa un cifrado César básico que desplace letras un número fijo de posiciones en el alfabeto.

## 🎯 Objetivo

Trabajar con operaciones sobre caracteres, `ord()`, `chr()` y manejo de minúsculas/mayúsculas.

## 📋 Especificaciones

1. Recibir `mensaje` y `desplazamiento` (entero positivo o negativo).
2. El desplazamiento solo afecta letras del alfabeto latino.
3. Mantén las letras con su misma mayúscula/minúscula.
4. No modifiques números ni símbolos.
5. Devuelve el mensaje cifrado y descifrado.

## 💻 Datos Iniciales

```python
mensaje = "Hola Mundo 2025!"
desplazamiento = 3
```

## 💻 Ejemplo de Ejecución

```
=== CIFRADO CÉSAR ===
Mensaje original: Hola Mundo 2025!
Desplazamiento: 3

Mensaje cifrado: Krod Pxqgr 2025!
Mensaje descifrado: Hola Mundo 2025!
```

## 🧪 Casos de Prueba

- [ ] Funciona con desplazamientos negativos.
- [ ] Mantiene caracteres no alfabéticos igual.
- [ ] Cicla correctamente el alfabeto (de Z pasa a A).
- [ ] El descifrado revierte el proceso.

## 💡 Pistas

1. `ord('a')` devuelve 97; úsalo como base.
2. Usa `% 26` para envolver el alfabeto.
3. Convierte la letra a 0-25, suma desplazamiento, vuelve a convertir.

## ⚠️ Errores Comunes

- ❌ Olvidar normalizar el desplazamiento (`desplazamiento % 26`).
- ❌ Mezclar índices de mayúsculas y minúsculas.
- ❌ No manejar correctamente letras con tilde (puedes omitirlas para este ejercicio).

## 🎓 Conceptos Practicados

- Transformación de caracteres
- Modularidad
- Bucles y concatenación de strings

## 🚀 Desafíos Extra (Opcional)

1. Permite elegir el alfabeto (incluyendo `ñ`).
2. Acepta claves como palabras y genera desplazamientos variables.
3. Implementa una función `descifrar()` y otra `cifrar()` reutilizables.

---

**Tiempo estimado**: 20 minutos  
**Archivo de solución**: `ejercicio_08.py`  
**Métodos a usar**: `ord()`, `chr()`, concatenación

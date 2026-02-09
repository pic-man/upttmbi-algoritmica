# 💬 Ejercicio 14: Tokenizador de Chat

## Dificultad: ⭐⭐⭐ Avanzado

## 📝 Descripción

Simula el conteo de tokens de un sistema de chat, donde cada mensaje se descompone en palabras y símbolos especiales (emojis, menciones, hashtags).

## 🎯 Objetivo

Aplicar análisis caracter a caracter, construyendo tokens personalizados.

## 📋 Especificaciones

1. Lista de mensajes:
   ```python
   mensajes = [
       "@ana ¡Hola! ¿List@ para el #reto?",
       "Sí 😊, tengo listo el resumen en https://ejemplo.com",
       "Perfecto, nos vemos a las 18:00"
   ]
   ```
2. Divide cada mensaje en tokens:
   - Palabras alfanuméricas
   - Emojis individuales
   - Menciones (`@usuario`)
   - Hashtags (`#tema`)
   - URLs completas
   - Otros símbolos puntuales
3. Calcula el total de tokens por mensaje y global.
4. Muestra un resumen con el top de tokens más frecuentes.

## 💻 Ejemplo de Ejecución

```
=== TOKENIZADOR ===
Mensaje 1 tokens (8): ['@ana', '¡', 'Hola', '!', '¿', 'List', '@', 'para', ...]
...
Total de tokens: 32
Top 5: [('para', 2), ('@ana', 1), ...]
```

## 🧪 Casos de Prueba

- [ ] Detecta y conserva URLs completas.
- [ ] Separa emojis sin perderlos.
- [ ] No mezcla hashtags con palabras adyacentes.
- [ ] Maneja mensajes con múltiples espacios.

## 💡 Pistas

1. Recorre cada caracter y clasifícalo; usa un buffer para palabras.
2. Un conjunto de emojis básicos puede definirse manualmente.
3. Para URLs, detecta el prefijo `http` y consume hasta el próximo espacio.

## ⚠️ Errores Comunes

- ❌ Cortar la URL por `:` o `/`.
- ❌ Unir menciones con signos de puntuación.
- ❌ Ignorar los signos de interrogación inversos (`¿`, `¡`).

## 🎓 Conceptos Practicados

- Autómatas simples
- Clasificación de caracteres
- Conteo de frecuencia

## 🚀 Desafíos Extra (Opcional)

1. Integra expresiones regulares para simplificar el tokenizador.
2. Calcula el costo en tokens según reglas de modelos (ej. 4 caracteres = 1 token).
3. Distingue entre emojis de un solo codepoint y compuestos.

---

**Tiempo estimado**: 25 minutos  
**Archivo de solución**: `ejercicio_14.py`  
**Métodos/Módulos sugeridos**: `re`, estructuras de control

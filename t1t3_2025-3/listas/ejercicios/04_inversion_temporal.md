# 🔄 Ejercicio 4: Inversión Temporal

## Dificultad: ⭐ Básico

## 📝 Descripción

Tienes una lista de eventos en orden cronológico. Muestra los eventos del más reciente al más antiguo. Luego crea una copia de esa lista para una línea temporal alternativa.

## 🎯 Objetivo

Practicar `reverse()` y `copy()`.

## 📋 Especificaciones

1. Usar la lista de eventos dada
2. Mostrar el orden original
3. Invertir la lista
4. Crear una copia de la lista invertida
5. Demostrar que son listas independientes

## 💻 Lista Inicial

```python
eventos = ["Nacimiento", "Escuela", "Universidad", "Trabajo", "Jubilación"]
```

## 💻 Ejemplo de Ejecución

```
=== MÁQUINA DEL TIEMPO ===

📅 Línea temporal original:
1. Nacimiento
2. Escuela
3. Universidad
4. Trabajo
5. Jubilación

🔄 Invirtiendo el tiempo...

⏪ Línea temporal invertida (del futuro al pasado):
1. Jubilación
2. Trabajo
3. Universidad
4. Escuela
5. Nacimiento

📋 Creando línea temporal alternativa...

✅ Líneas temporales:
   - Original (invertida): ['Jubilación', 'Trabajo', 'Universidad', 'Escuela', 'Nacimiento']
   - Alternativa (copia): ['Jubilación', 'Trabajo', 'Universidad', 'Escuela', 'Nacimiento']

Modificando línea alternativa...
Alternativa ahora: ['Jubilación', 'Trabajo', 'Emprendimiento', 'Universidad', 'Escuela', 'Nacimiento']
Original sigue igual: ['Jubilación', 'Trabajo', 'Universidad', 'Escuela', 'Nacimiento']

✓ Las listas son independientes!
```

## 🧪 Casos de Prueba

Verifica:
- [ ] La lista se invierte correctamente
- [ ] La copia es independiente de la original
- [ ] Modificar la copia no afecta la original

## 💡 Pistas

1. `reverse()` modifica la lista original
2. `copy()` crea una copia superficial
3. También puedes usar `lista[:]` para copiar

## 🚀 Desafíos Extra

1. Crea una función que compare dos líneas temporales
2. Agrega fechas a cada evento
3. Crea múltiples universos paralelos (copias)

---

**Tiempo estimado**: 15 minutos  
**Archivo de solución**: `ejercicio_04.py`


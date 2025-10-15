# 🌮 Ejercicio 20: Menú del Día

## Dificultad: ⭐⭐ Intermedio

## 📝 Descripción

Crea un programa que pida el día de la semana y muestre el platillo especial de ese día en un restaurante.

## 🎯 Objetivo

Practicar comparación de strings con 7 opciones diferentes (días de la semana).

## 📋 Especificaciones

El programa debe:

1. Solicitar el día de la semana
2. Mostrar el platillo según:
   - **Lunes**: "Enchiladas verdes"
   - **Martes**: "Tacos al pastor"
   - **Miércoles**: "Pozole"
   - **Jueves**: "Mole con pollo"
   - **Viernes**: "Pescado a la veracruzana"
   - **Sábado**: "Barbacoa"
   - **Domingo**: "Menudo"
   - **Otro**: "Día no válido"

## 💻 Ejemplo de Ejecución

### Ejemplo 1:
```
=== RESTAURANTE "LA TRADICIÓN" ===
🍽️  Menú Especial del Día

Días disponibles: Lunes a Domingo

¿Qué día es hoy? martes

═══════════════════════════════
📅 MARTES
═══════════════════════════════

🌮 PLATILLO ESPECIAL:
Tacos al Pastor

Descripción:
Tortillas de maíz con carne de cerdo marinada en achiote,
servidos con piña, cilantro, cebolla y salsa verde.

Incluye:
• Orden de 5 tacos
• Frijoles refritos
• Agua de horchata

Precio: $85
═══════════════════════════════
¡Buen provecho!
```

### Ejemplo 2:
```
=== RESTAURANTE "LA TRADICIÓN" ===
🍽️  Menú Especial del Día

Días disponibles: Lunes a Domingo

¿Qué día es hoy? domingo

═══════════════════════════════
📅 DOMINGO
═══════════════════════════════

🥘 PLATILLO ESPECIAL:
Menudo

Descripción:
Caldo tradicional de pancita de res con maíz cacahuazintle,
chile guajillo y especias mexicanas.

Incluye:
• Tazón grande
• Tortillas de maíz
• Limón, cebolla y orégano
• Pan bolillo

Precio: $95
═══════════════════════════════
¡Buen provecho!
```

### Ejemplo 3:
```
=== RESTAURANTE "LA TRADICIÓN" ===
🍽️  Menú Especial del Día

Días disponibles: Lunes a Domingo

¿Qué día es hoy? juernes

❌ Día no válido
Por favor ingresa un día de la semana correcto:
Lunes, Martes, Miércoles, Jueves, Viernes, Sábado, Domingo
```

## 🧪 Casos de Prueba

Prueba tu programa con estos valores:

| Entrada | Platillo |
|---------|----------|
| lunes | Enchiladas verdes |
| Lunes | Enchiladas verdes |
| LUNES | Enchiladas verdes |
| martes | Tacos al pastor |
| miércoles | Pozole |
| miercoles | Pozole |
| jueves | Mole con pollo |
| viernes | Pescado a la veracruzana |
| sábado | Barbacoa |
| sabado | Barbacoa |
| domingo | Menudo |
| lun | Día no válido |
| monday | Día no válido |

## 💡 Pistas

1. Normaliza la entrada:
   ```python
   dia = input("Día: ").lower()
   ```

2. Considera variaciones de acentos:
   ```python
   if dia == "miercoles" or dia == "miércoles":
       # miércoles
   ```

3. Estructura con múltiples `elif` (7 días)

4. Otra opción usando diccionario (más avanzado):
   ```python
   menu = {
       "lunes": "Enchiladas verdes",
       "martes": "Tacos al pastor",
       # ...
   }
   ```

## 📅 Menú Semanal Completo

| Día | Platillo | Origen | Precio |
|-----|----------|--------|--------|
| 🌮 Lunes | Enchiladas verdes | Oaxaca | $75 |
| 🌮 Martes | Tacos al pastor | CDMX | $85 |
| 🥘 Miércoles | Pozole | Jalisco | $90 |
| 🍗 Jueves | Mole con pollo | Puebla | $95 |
| 🐟 Viernes | Pescado veracruzano | Veracruz | $120 |
| 🥩 Sábado | Barbacoa | Hidalgo | $100 |
| 🍲 Domingo | Menudo | Sonora | $95 |

## ⚠️ Errores Comunes

- ❌ No normalizar a minúsculas
- ❌ No considerar acentos (miércoles, sábado)
- ❌ No validar días incorrectos
- ❌ Ser sensible a mayúsculas
- ❌ Código muy repetitivo

## 🎓 Conceptos Practicados

- `if-elif-else` con 7+ opciones
- Comparación de strings
- Normalización de texto
- Manejo de acentos
- Validación de entrada

## 🍽️ Información Extra

**¿Por qué estos platillos?**
- Lunes: Ligero después del fin de semana
- Martes: Tacos (tradición mexicana)
- Miércoles: Pozole (mitad de semana)
- Jueves: Mole (platillo elaborado)
- Viernes: Pescado (tradición religiosa)
- Sábado: Barbacoa (desayuno tradicional)
- Domingo: Menudo (cura tradicional)

## 🚀 Desafíos Extra (Opcional)

1. **Menú completo**:
   - No solo platillo fuerte
   - Entrada, plato fuerte, postre, bebida

2. **Vegetariano/Vegano**:
   - Pregunta preferencias dietéticas
   - Ofrece alternativa vegetariana
   - Lunes vegetariano: Enchiladas de espinaca

3. **Opciones por tiempo de comida**:
   - Desayuno, comida, cena
   - Diferentes platillos según horario

4. **Sistema de reservación**:
   - Pregunta día y número de personas
   - Calcula precio total
   - Sugiere hora disponible

5. **Historial de menús**:
   - Guarda qué comió cada día
   - Sugiere no repetir
   - "Ya comiste tacos el martes pasado"

6. **Menús especiales**:
   - Primer viernes del mes: Buffet
   - Domingos familiares: Descuento grupos
   - Días festivos: Menú especial

7. **Combos**:
   ```
   Martes de Tacos:
   - 3 tacos: $45
   - 5 tacos: $70
   - 10 tacos: $120
   
   Incluye refresco o agua
   ```

8. **Calificaciones**:
   - Muestra calificación de cada platillo
   - Enchiladas: ⭐⭐⭐⭐⭐ (4.8/5)
   - Tacos: ⭐⭐⭐⭐⭐ (4.9/5)

9. **Disponibilidad**:
   - Algunos platillos se agotan
   - "Pozole: 5 órdenes restantes"
   - Opción de reservar

10. **Promociones**:
    - Lunes: 2x1 en enchiladas
    - Viernes: Postre gratis
    - Sábado-Domingo: 15% descuento familias

---

**Tiempo estimado**: 15-20 minutos  
**Archivo de solución**: `ejercicio_20.py`

---

## 🎉 ¡Felicidades!

Si llegaste hasta aquí, completaste los 20 ejercicios de Estructuras de Decisión. ¡Excelente trabajo!

### Próximos pasos:
1. Revisa tus soluciones
2. Optimiza tu código
3. Agrega los desafíos extra
4. Ayuda a tus compañeros
5. ¡Prepárate para el siguiente tema!

**¡Sigue programando!** 💻🚀


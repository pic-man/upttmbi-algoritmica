# ✅ 05 - Buenas Prácticas con Estructuras de Repetición

Escribir bucles correctos es fundamental, pero escribirlos de forma clara y segura es aún mejor. Estas recomendaciones te ayudarán a evitar errores comunes y a mantener tu código legible.

## 1. Define claramente la condición de salida

- Antes de programar, determina qué debe ocurrir para que el ciclo termine.
- Evita dependencias implícitas; sé explícito en la condición.

```python
while intentos < MAX_INTENTOS:
    # lógica
```

## 2. Inicializa variables antes del ciclo

Contadores, acumuladores o banderas deben tener un valor definido antes de entrar al bucle.

```python
total = 0
contador = 0
while contador < len(numeros):
    total += numeros[contador]
    contador += 1
```

## 3. Actualiza las variables de control dentro del ciclo

Un ciclo sin actualización puede bloquear el programa.

```python
while numero > 0:
    print(numero)
    numero -= 1  # ¡No olvides esto!
```

## 4. Evita ciclos innecesarios

- Usa comprensiones de listas o funciones como `sum`, `any`, `all` cuando sea posible.
- No recorras listas varias veces si puedes hacerlo en una sola pasada.

## 5. Mantén el cuerpo del bucle pequeño

Si el código dentro del ciclo se vuelve extenso, extrae partes en funciones auxiliares. Mejora la legibilidad y facilita las pruebas.

## 6. Cuida los ciclos anidados

- Reduce la profundidad siempre que puedas.
- Verifica la complejidad: un doble bucle sobre 10 000 elementos puede ser costoso.
- Considera estructuras alternativas (diccionarios, conjuntos, búsquedas directas).

## 7. Usa nombres descriptivos

`for numero in numeros` es más legible que `for x in lista`.

## 8. Valida datos de entrada

Los bucles suelen depender de los valores ingresados por el usuario. Valida antes de procesar para evitar comportamientos inesperados.

```python
while True:
    opcion = input("Selecciona 1-4: ")
    if opcion in {"1", "2", "3", "4"}:
        break
    print("Opción inválida.")
```

## 9. Controla los ciclos infinitos

- Si usas `while True`, asegúrate de tener un `break` claro.
- Agrega contadores de seguridad cuando sea necesario (por ejemplo, en simulaciones).

## 10. Aprovecha `enumerate` y `zip`

Evita manejar índices manuales si no hace falta.

```python
for indice, nombre in enumerate(estudiantes, start=1):
    print(indice, nombre)
```

## 11. Documenta comportamientos especiales

Si el bucle depende de un `break`, `continue` o valores sentinela, agrega comentarios que expliquen la lógica.

## 12. Prueba con casos límite

- Sin iteraciones (listas vacías, rango cero).
- Máxima cantidad de iteraciones esperadas.
- Entradas inválidas o valores extremos.

## 13. Sé consistente con el estilo

- Usa indentación de 4 espacios.
- Evita combinar `while` y `for` sin necesidad.
- Prefiere `for` para recorrer secuencias; `while` para condiciones.

---

Aplica estas prácticas en tus ejercicios y proyectos. Los bucles bien diseñados son clave para programas robustos y mantenibles. 🙌


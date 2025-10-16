# 🎪 Ejercicio 5: El Mago de las Listas

## Dificultad: ⭐ Básico

## 📝 Descripción

Tienes una lista de números del 1 al 10. "Haz desaparecer" el último número y guárdalo, luego haz lo mismo con el primero. Muestra cuántos números quedan y cuáles desaparecieron.

## 🎯 Objetivo

Practicar el método `pop()` con y sin índice.

## 📋 Especificaciones

1. Crear lista de números del 1 al 10
2. Usar `pop()` para eliminar y guardar el último número
3. Usar `pop(0)` para eliminar y guardar el primero
4. Mostrar los números que "desaparecieron"
5. Mostrar los números restantes

## 💻 Lista Inicial

```python
numeros_magicos = list(range(1, 11))
```

## 💻 Ejemplo de Ejecución

```
=== EL GRAN MAGO DE LAS LISTAS ===

🎩 Números mágicos iniciales:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Total: 10 números

✨ ¡ABRACADABRA! Haciendo desaparecer el último número...
💫 El número 10 ha desaparecido!

✨ ¡HOCUS POCUS! Haciendo desaparecer el primer número...
💫 El número 1 ha desaparecido!

📊 Resultado del truco:

Números que desaparecieron:
- Primero: 1
- Último: 10

🎭 Números restantes en el sombrero:
[2, 3, 4, 5, 6, 7, 8, 9]
Total restante: 8 números

🎪 ¡El truco fue un éxito!
```

## 🧪 Casos de Prueba

Verifica:
- [ ] Se eliminan correctamente el primero y el último
- [ ] Los números eliminados se guardan correctamente
- [ ] Quedan 8 números en la lista
- [ ] Los números son del 2 al 9

## 💡 Pistas

1. `pop()` sin argumentos elimina el último
2. `pop(0)` elimina el primero (índice 0)
3. `pop()` retorna el elemento eliminado
4. `range(1, 11)` genera números del 1 al 10

## 🚀 Desafíos Extra

1. Haz desaparecer números en posiciones aleatorias
2. Crea una función `hacer_desaparecer(lista, cantidad)`
3. Añade animación ASCII del truco de magia
4. Permite "reaparecer" los números (undo)

---

**Tiempo estimado**: 10-15 minutos  
**Archivo de solución**: `ejercicio_05.py`


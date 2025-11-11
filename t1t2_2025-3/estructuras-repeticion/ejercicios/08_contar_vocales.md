# 🔤 Ejercicio 8: Contar Vocales

## Dificultad: ⭐ Básico

## 📝 Descripción

Construye un programa que cuente cuántas vocales contiene una palabra o frase ingresada por el usuario.

## 🎯 Objetivo

Practicar el uso de ciclos `for` al recorrer cadenas de texto y aplicar condiciones dentro de ellos.

## 📋 Especificaciones

El programa debe:

1. Solicitar una cadena de texto.
2. Recorrer cada carácter con un ciclo `for`.
3. Contar cuántas vocales (a, e, i, o, u) aparecen, sin importar mayúsculas o minúsculas.
4. Mostrar el total encontrado.

## 💻 Ejemplo de Ejecución

### Ejemplo 1:
```
Ingresa una palabra o frase: Algoritmica
Cantidad de vocales: 5
```

### Ejemplo 2:
```
Ingresa una palabra o frase: PYTHON
Cantidad de vocales: 1
```

### Ejemplo 3:
```
Ingresa una palabra o frase: ssssss
Cantidad de vocales: 0
```

## 🧪 Casos de Prueba

| Entrada | Salida Esperada |
|---------|----------------|
| "Hola" | 2 |
| "Programación" | 5 |
| "xyz" | 0 |
| "" | 0 |
| "AEIOU" | 5 |

## 💡 Pistas

1. Convierte el texto a minúsculas usando `.lower()` para simplificar comparaciones.
2. Define un string con las vocales: `vocales = "aeiou"`.
3. Incrementa un contador cada vez que encuentres un carácter presente en `vocales`.

## ⚠️ Errores Comunes

- ❌ No considerar mayúsculas.
- ❌ Contar vocales con tilde como vocales distintas.
- ❌ Olvidar reiniciar el contador antes del ciclo.

## 🎓 Conceptos Practicados

- Ciclo `for`
- Recorrido de strings
- Condiciones simples

## 🚀 Desafíos Extra (Opcional)

1. Cuenta también las vocales con tilde (`á`, `é`, etc.).
2. Muestra cuántas veces aparece cada vocal por separado.
3. Ignora los espacios y caracteres especiales del conteo.

---

**Tiempo estimado**: 5-10 minutos  
**Archivo de solución**: `ejercicio_08.py`


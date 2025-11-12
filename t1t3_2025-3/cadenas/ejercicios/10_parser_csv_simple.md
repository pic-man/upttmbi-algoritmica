# 📄 Ejercicio 10: Parser CSV Simple

## Dificultad: ⭐⭐⭐ Avanzado

## 📝 Descripción

Simula la lectura de una fila CSV y convértela en un diccionario con claves predefinidas, manejando comillas y espacios.

## 🎯 Objetivo

Trabajar con `split()`, limpieza de campos y reconstrucción de estructuras.

## 📋 Especificaciones

1. Tener la fila `fila_csv` con campos separados por `,`.
2. Algunos campos pueden estar entre comillas y contener comas interiores.
3. Limpiar cada campo (quitar comillas y espacios laterales).
4. Emparejar con la lista de columnas `columnas`.
5. Mostrar el diccionario resultante.

## 💻 Datos Iniciales

```python
fila_csv = '  "Carlos Bravo", 27, "Guadalajara, MX", Desarrollador '
columnas = ["nombre", "edad", "ciudad", "ocupacion"]
```

## 💻 Ejemplo de Ejecución

```
=== PARSER CSV ===
Fila original:   "Carlos Bravo", 27, "Guadalajara, MX", Desarrollador 

Resultado:
{
  'nombre': 'Carlos Bravo',
  'edad': '27',
  'ciudad': 'Guadalajara, MX',
  'ocupacion': 'Desarrollador'
}
```

## 🧪 Casos de Prueba

- [ ] Maneja campos con comas dentro de comillas.
- [ ] Quita comillas dobles externas.
- [ ] Respeta el orden de `columnas`.
- [ ] Funciona aunque haya espacios extra.

## 💡 Pistas

1. Recorre la cadena manualmente detectando comillas para saber cuándo dividir.
2. Puedes usar un estado booleano (`en_comillas`).
3. `zip(columnas, valores)` facilita construir el diccionario.

## ⚠️ Errores Comunes

- ❌ Usar `split(",")` directo y romper campos con comas internas.
- ❌ Olvidar eliminar espacios y comillas tras separar.
- ❌ No validar que hay el mismo número de columnas y valores.

## 🎓 Conceptos Practicados

- Parsing manual de texto
- Estados en bucles
- Emparejamiento con `zip`

## 🚀 Desafíos Extra (Opcional)

1. Acepta filas con campos vacíos (`""`).
2. Genera una función que procese múltiples filas (lista de strings).
3. Permite cambiar el delimitador y el carácter de comilla.

---

**Tiempo estimado**: 25 minutos  
**Archivo de solución**: `ejercicio_10.py`  
**Métodos a usar**: `strip()`, `replace()`, iteración manual

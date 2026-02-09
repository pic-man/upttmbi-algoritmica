# 📖 06 - Ciclo Mientras (While)

## ¿Qué es el Ciclo While?

El ciclo **while** repite un bloque de instrucciones **mientras** una condición sea verdadera.

```
┌──────────────┐
│   Inicio     │
└──────┬───────┘
       │
       ▼
┌──────────────┐     Falso
│  ¿Condición? │────────────────┐
└──────┬───────┘                │
       │ Verdadero              │
       ▼                        │
┌──────────────┐                │
│ Instrucciones│                │
└──────┬───────┘                │
       │                        │
       └────────────────────────┤
                                │
                                ▼
                         ┌──────────────┐
                         │     Fin      │
                         └──────────────┘
```

## Sintaxis en Python

```python
while condicion:
    # instrucciones a repetir
    # actualizar condición para evitar ciclo infinito
```

## Ejemplos Básicos

### Contador ascendente

```python
contador = 1
while contador <= 5:
    print(f"Contador: {contador}")
    contador += 1  # IMPORTANTE: actualizar la variable

# Salida:
# Contador: 1
# Contador: 2
# Contador: 3
# Contador: 4
# Contador: 5
```

### Contador descendente

```python
contador = 5
while contador >= 1:
    print(f"Cuenta regresiva: {contador}")
    contador -= 1
print("¡Despegue!")
```

### Sumar números hasta cero

```python
suma = 0
numero = int(input("Ingrese un número (0 para terminar): "))

while numero != 0:
    suma += numero
    numero = int(input("Ingrese otro número (0 para terminar): "))

print(f"La suma total es: {suma}")
```

## Control del Ciclo

### break - Salir del ciclo

```python
while True:
    respuesta = input("¿Desea continuar? (s/n): ")
    if respuesta.lower() == 'n':
        break  # Sale del ciclo
    print("Continuando...")
```

### continue - Saltar a la siguiente iteración

```python
contador = 0
while contador < 10:
    contador += 1
    if contador % 2 == 0:
        continue  # Salta los pares
    print(contador)  # Solo imprime impares
```

## Ejemplo Completo: Menú interactivo

```python
while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Opción uno")
    print("2. Opción dos")
    print("3. Salir")
    
    opcion = input("Seleccione: ")
    
    if opcion == "1":
        print("Ejecutando opción uno...")
    elif opcion == "2":
        print("Ejecutando opción dos...")
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida")
```

## ⚠️ Evitar Ciclos Infinitos

```python
# ❌ MAL: Ciclo infinito (nunca termina)
contador = 1
while contador <= 5:
    print(contador)
    # Falta: contador += 1

# ✅ BIEN: Ciclo termina correctamente
contador = 1
while contador <= 5:
    print(contador)
    contador += 1  # Actualiza la variable
```

## 📝 Para Recordar

1. El ciclo **while** repite mientras la condición sea True
2. **Siempre** actualizar la variable de control
3. Usar **break** para salir del ciclo
4. Usar **continue** para saltar una iteración
5. Cuidado con los **ciclos infinitos**

## 🔜 Siguiente Paso

[Ir a: 08 - Ciclo Para →](./08_ciclo_para.md)

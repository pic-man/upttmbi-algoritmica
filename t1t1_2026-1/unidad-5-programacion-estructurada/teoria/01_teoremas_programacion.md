# 📖 01 - Teoremas de la Programación Estructurada

## ¿Qué es la Programación Estructurada?

La **programación estructurada** es un paradigma de programación que utiliza únicamente tres estructuras de control para crear cualquier programa.

## Teorema de Böhm-Jacopini

En 1966, los matemáticos Böhm y Jacopini demostraron que **cualquier programa** puede escribirse usando solo tres estructuras de control:

```
┌─────────────────────────────────────────────────────────────┐
│            ESTRUCTURAS DE CONTROL FUNDAMENTALES              │
├─────────────────┬─────────────────┬─────────────────────────┤
│   SECUENCIA     │    SELECCIÓN    │      ITERACIÓN          │
│                 │                 │                         │
│   Instrucción1  │   Si condición  │   Mientras condición    │
│   Instrucción2  │   Entonces A    │   Hacer                 │
│   Instrucción3  │   Sino B        │   Instrucciones         │
│                 │                 │   Fin Mientras          │
└─────────────────┴─────────────────┴─────────────────────────┘
```

## 1. Secuencia

Las instrucciones se ejecutan **una tras otra**, en orden.

```
┌─────────┐
│ Inicio  │
└────┬────┘
     │
     ▼
┌─────────┐
│ Paso 1  │
└────┬────┘
     │
     ▼
┌─────────┐
│ Paso 2  │
└────┬────┘
     │
     ▼
┌─────────┐
│ Paso 3  │
└────┬────┘
     │
     ▼
┌─────────┐
│   Fin   │
└─────────┘
```

```python
# Ejemplo de secuencia
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
print(f"Hola {nombre}, tienes {edad} años")
```

## 2. Selección (Decisión)

Permite elegir entre **dos o más caminos** según una condición.

```
        ┌─────────┐
        │Condición│
        └────┬────┘
             │
      ┌──────┴──────┐
     Sí             No
      │              │
      ▼              ▼
┌─────────┐    ┌─────────┐
│ Acción A│    │ Acción B│
└────┬────┘    └────┬────┘
     │              │
     └──────┬───────┘
            │
            ▼
```

```python
# Ejemplo de selección
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")
```

## 3. Iteración (Repetición)

Permite **repetir** un conjunto de instrucciones mientras se cumpla una condición.

```
        ┌─────────┐
        │Condición│◄───┐
        └────┬────┘    │
             │         │
      ┌──────┴──────┐  │
     Sí             No │
      │              │ │
      ▼              │ │
┌─────────┐          │ │
│ Acción  │──────────┘ │
└─────────┘            │
                       │
                       ▼
                 (Continúa)
```

```python
# Ejemplo de iteración
contador = 1
while contador <= 5:
    print(f"Iteración {contador}")
    contador += 1
```

## Ventajas de la Programación Estructurada

| Ventaja | Descripción |
|---------|-------------|
| **Claridad** | Código más fácil de leer y entender |
| **Mantenimiento** | Más fácil de modificar y corregir |
| **Depuración** | Errores más fáciles de encontrar |
| **Reutilización** | Código modular y reutilizable |
| **Verificación** | Se puede probar sistemáticamente |

## Características

1. **Un solo punto de entrada** por estructura
2. **Un solo punto de salida** por estructura
3. **Sin saltos incondicionales** (GOTO)
4. **Flujo de control claro** y predecible

## 📝 Para Recordar

1. Solo se necesitan **3 estructuras**: secuencia, selección, iteración
2. Cualquier programa puede escribirse con estas estructuras
3. El código es más **legible** y **mantenible**
4. Cada estructura tiene **una entrada** y **una salida**

## 🔜 Siguiente Paso

[Ir a: 02 - Estructuras de Decisión →](./02_estructuras_decision.md)

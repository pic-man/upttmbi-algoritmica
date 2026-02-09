# 📖 04 - Ámbito de Variables

## ¿Qué es el Ámbito?

El **ámbito** (scope) de una variable determina dónde puede ser accedida y utilizada en el programa.

```
┌─────────────────────────────────────────────────────────────┐
│ ÁMBITO GLOBAL                                                │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ variable_global = "Accesible en todo el programa"       │ │
│ └─────────────────────────────────────────────────────────┘ │
│                                                             │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ def mi_funcion():                                       │ │
│ │   ┌─────────────────────────────────────────────────┐   │ │
│ │   │ ÁMBITO LOCAL                                    │   │ │
│ │   │ variable_local = "Solo accesible aquí"          │   │ │
│ │   └─────────────────────────────────────────────────┘   │ │
│ └─────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

## Variables Locales

Existen **solo dentro** de la función donde se definen.

```python
def mi_funcion():
    # Variable local
    mensaje = "Hola desde la función"
    print(mensaje)

mi_funcion()        # "Hola desde la función"
# print(mensaje)    # ERROR: mensaje no existe fuera de la función
```

## Variables Globales

Existen en **todo el programa** y pueden ser leídas desde cualquier parte.

```python
# Variable global
contador_global = 0

def incrementar():
    global contador_global  # Indicar que usamos la global
    contador_global += 1

incrementar()
print(contador_global)  # 1
```

## Regla LEGB

Python busca variables en este orden:

```
L - Local       : Dentro de la función actual
E - Enclosing   : En funciones que contienen a la actual
G - Global      : A nivel de módulo
B - Built-in    : Funciones y nombres incorporados
```

```python
x = "global"

def externa():
    x = "enclosing"
    
    def interna():
        x = "local"
        print(x)  # "local"
    
    interna()
    print(x)  # "enclosing"

externa()
print(x)  # "global"
```

## Ejemplo Completo

```python
# Variable global
total_ventas = 0

def registrar_venta(monto):
    """Registra una venta y actualiza el total global."""
    global total_ventas
    
    # Variable local
    iva = monto * 0.16
    total_con_iva = monto + iva
    
    # Modificar global
    total_ventas += total_con_iva
    
    return total_con_iva

# Usar la función
venta1 = registrar_venta(100)
venta2 = registrar_venta(200)

print(f"Venta 1: ${venta1:.2f}")
print(f"Venta 2: ${venta2:.2f}")
print(f"Total acumulado: ${total_ventas:.2f}")
```

## ⚠️ Recomendaciones

```python
# ❌ EVITAR: Demasiadas variables globales
contador1 = 0
contador2 = 0
total = 0
# ... modificadas desde múltiples funciones

# ✅ MEJOR: Usar parámetros y retornos
def procesar(datos, opciones):
    resultado = calcular(datos, opciones)
    return resultado
```

## 📝 Para Recordar

1. **Local**: existe solo en la función
2. **Global**: existe en todo el programa
3. Usar `global` para **modificar** globales
4. **Minimizar** el uso de variables globales
5. Preferir **parámetros y retornos**

## 🔜 Siguiente Paso

[Ir a: 07 - Paso de Parámetros →](./07_paso_parametros.md)

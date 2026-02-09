# 📖 07 - Paso de Parámetros

## ¿Qué son los Parámetros?

Los **parámetros** son valores que se pasan a una función para que trabaje con ellos.

```python
def saludar(nombre):    # 'nombre' es el PARÁMETRO (en la definición)
    print(f"Hola, {nombre}")

saludar("Juan")         # "Juan" es el ARGUMENTO (en la llamada)
```

## Tipos de Parámetros

### 1. Parámetros Posicionales

El orden importa.

```python
def crear_perfil(nombre, edad, ciudad):
    print(f"{nombre}, {edad} años, de {ciudad}")

crear_perfil("Ana", 25, "Madrid")  # Orden correcto
```

### 2. Parámetros con Nombre (Keyword)

Se especifica el nombre del parámetro.

```python
crear_perfil(ciudad="Lima", nombre="Carlos", edad=30)
# El orden no importa si usamos nombres
```

### 3. Parámetros por Defecto

Tienen un valor predeterminado.

```python
def saludar(nombre, saludo="Hola"):
    print(f"{saludo}, {nombre}!")

saludar("María")              # "Hola, María!"
saludar("Pedro", "Buenos días")  # "Buenos días, Pedro!"
```

### 4. Parámetros Variables (*args)

Acepta cualquier número de argumentos.

```python
def sumar_todos(*numeros):
    return sum(numeros)

print(sumar_todos(1, 2, 3))        # 6
print(sumar_todos(1, 2, 3, 4, 5))  # 15
```

### 5. Parámetros de Palabra Clave (**kwargs)

Acepta argumentos con nombre.

```python
def mostrar_info(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Ana", edad=25, ciudad="Lima")
```

## Paso por Valor vs Referencia

### Tipos Inmutables (int, str, tuple)
Se pasa una **copia del valor**. El original no cambia.

```python
def duplicar(x):
    x = x * 2
    return x

numero = 5
resultado = duplicar(numero)
print(numero)     # 5 (no cambió)
print(resultado)  # 10
```

### Tipos Mutables (list, dict)
Se pasa una **referencia**. El original puede cambiar.

```python
def agregar_elemento(lista, elemento):
    lista.append(elemento)

mi_lista = [1, 2, 3]
agregar_elemento(mi_lista, 4)
print(mi_lista)  # [1, 2, 3, 4] (cambió)
```

## Ejemplo Completo

```python
def calcular_factura(productos, descuento=0, **opciones):
    """
    Calcula el total de una factura.
    
    Args:
        productos: Lista de tuplas (nombre, precio, cantidad)
        descuento: Porcentaje de descuento (0-100)
        **opciones: Opciones adicionales (iva, envio, etc.)
    
    Returns:
        dict: Desglose de la factura
    """
    subtotal = sum(precio * cant for _, precio, cant in productos)
    
    # Aplicar descuento
    monto_descuento = subtotal * (descuento / 100)
    subtotal_descuento = subtotal - monto_descuento
    
    # Aplicar IVA
    iva = opciones.get('iva', 0.16)
    monto_iva = subtotal_descuento * iva
    
    # Envío
    envio = opciones.get('envio', 0)
    
    total = subtotal_descuento + monto_iva + envio
    
    return {
        'subtotal': subtotal,
        'descuento': monto_descuento,
        'iva': monto_iva,
        'envio': envio,
        'total': total
    }

# Uso
productos = [
    ("Laptop", 1000, 1),
    ("Mouse", 25, 2)
]

factura = calcular_factura(
    productos,
    descuento=10,
    iva=0.16,
    envio=15
)

print(f"Total: ${factura['total']:.2f}")
```

## 📝 Para Recordar

1. **Parámetro**: variable en la definición
2. **Argumento**: valor en la llamada
3. Los valores por defecto van al **final**
4. `*args` para múltiples argumentos
5. `**kwargs` para argumentos con nombre
6. Tipos mutables pueden **modificarse**

---

¡Felicidades! Has completado la teoría de la Unidad 6.

[Ir a: Ejercicios →](../ejercicios/README.md)

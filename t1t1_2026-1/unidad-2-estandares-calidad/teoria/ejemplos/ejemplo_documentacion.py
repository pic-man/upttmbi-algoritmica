"""
Ejemplo de Código Bien Documentado
==================================

Autor: Profesor de Algorítmica
Fecha: 2025-01-25
Versión: 1.0

Descripción:
    Este módulo demuestra las mejores prácticas de documentación
    en Python, incluyendo docstrings, comentarios y estructura.

Uso:
    python ejemplo_documentacion.py
"""

# ============================================
# IMPORTS
# ============================================
from datetime import datetime

# ============================================
# CONSTANTES
# ============================================

# Porcentaje de IVA aplicable (16%)
IVA_PORCENTAJE = 0.16

# Descuento máximo permitido por política de la empresa
DESCUENTO_MAXIMO = 0.30

# Moneda utilizada en los cálculos
MONEDA = "USD"

# ============================================
# FUNCIONES AUXILIARES
# ============================================

def validar_monto(monto):
    """
    Valida que un monto sea un número positivo.
    
    Args:
        monto (float): El monto a validar
    
    Returns:
        bool: True si el monto es válido, False en caso contrario
    
    Example:
        >>> validar_monto(100.50)
        True
        >>> validar_monto(-50)
        False
    """
    return isinstance(monto, (int, float)) and monto >= 0


def validar_porcentaje(porcentaje):
    """
    Valida que un porcentaje esté entre 0 y 100.
    
    Args:
        porcentaje (float): El porcentaje a validar (0-100)
    
    Returns:
        bool: True si el porcentaje es válido
    
    Raises:
        ValueError: Si el porcentaje está fuera del rango permitido
    """
    if not 0 <= porcentaje <= 100:
        raise ValueError(f"El porcentaje debe estar entre 0 y 100, se recibió: {porcentaje}")
    return True


# ============================================
# FUNCIONES PRINCIPALES
# ============================================

def calcular_subtotal(productos):
    """
    Calcula el subtotal de una lista de productos.
    
    Suma el precio de cada producto multiplicado por su cantidad.
    
    Args:
        productos (list): Lista de diccionarios con estructura:
            - 'nombre' (str): Nombre del producto
            - 'precio' (float): Precio unitario
            - 'cantidad' (int): Cantidad de unidades
    
    Returns:
        float: El subtotal de todos los productos
    
    Raises:
        ValueError: Si la lista está vacía o tiene formato incorrecto
    
    Example:
        >>> productos = [
        ...     {'nombre': 'Laptop', 'precio': 1000, 'cantidad': 1},
        ...     {'nombre': 'Mouse', 'precio': 25, 'cantidad': 2}
        ... ]
        >>> calcular_subtotal(productos)
        1050.0
    """
    if not productos:
        raise ValueError("La lista de productos no puede estar vacía")
    
    subtotal = 0.0
    
    # Iterar sobre cada producto y acumular el total
    for producto in productos:
        precio = producto.get('precio', 0)
        cantidad = producto.get('cantidad', 1)
        subtotal += precio * cantidad
    
    return subtotal


def aplicar_descuento(monto, porcentaje_descuento):
    """
    Aplica un descuento a un monto dado.
    
    El descuento no puede exceder el máximo permitido (30%).
    
    Args:
        monto (float): El monto original
        porcentaje_descuento (float): El porcentaje de descuento (0-100)
    
    Returns:
        tuple: (monto_final, descuento_aplicado)
    
    Raises:
        ValueError: Si el monto es negativo o el descuento inválido
    """
    # Validar entrada
    if not validar_monto(monto):
        raise ValueError("El monto debe ser un número positivo")
    
    validar_porcentaje(porcentaje_descuento)
    
    # Convertir porcentaje a decimal
    descuento_decimal = porcentaje_descuento / 100
    
    # Limitar al descuento máximo permitido
    if descuento_decimal > DESCUENTO_MAXIMO:
        descuento_decimal = DESCUENTO_MAXIMO
        print(f"⚠️ Descuento limitado al máximo permitido: {DESCUENTO_MAXIMO * 100}%")
    
    # Calcular el descuento
    descuento_aplicado = monto * descuento_decimal
    monto_final = monto - descuento_aplicado
    
    return monto_final, descuento_aplicado


def calcular_iva(monto):
    """
    Calcula el IVA de un monto.
    
    Args:
        monto (float): El monto sobre el cual calcular el IVA
    
    Returns:
        float: El monto del IVA
    """
    return monto * IVA_PORCENTAJE


def generar_factura(productos, porcentaje_descuento=0):
    """
    Genera una factura completa con todos los cálculos.
    
    Args:
        productos (list): Lista de productos
        porcentaje_descuento (float, optional): Descuento a aplicar. Default: 0
    
    Returns:
        dict: Diccionario con todos los detalles de la factura
    """
    # Calcular subtotal
    subtotal = calcular_subtotal(productos)
    
    # Aplicar descuento si existe
    monto_con_descuento, descuento = aplicar_descuento(subtotal, porcentaje_descuento)
    
    # Calcular IVA
    iva = calcular_iva(monto_con_descuento)
    
    # Calcular total
    total = monto_con_descuento + iva
    
    # Construir factura
    factura = {
        'fecha': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'productos': productos,
        'subtotal': subtotal,
        'descuento': descuento,
        'iva': iva,
        'total': total,
        'moneda': MONEDA
    }
    
    return factura


# ============================================
# PROGRAMA PRINCIPAL
# ============================================

def main():
    """
    Función principal que demuestra el uso del sistema de facturación.
    """
    print("=" * 50)
    print("SISTEMA DE FACTURACIÓN - DEMO")
    print("=" * 50)
    
    # Datos de ejemplo
    productos_ejemplo = [
        {'nombre': 'Laptop HP', 'precio': 800.00, 'cantidad': 1},
        {'nombre': 'Mouse inalámbrico', 'precio': 25.00, 'cantidad': 2},
        {'nombre': 'Teclado mecánico', 'precio': 75.00, 'cantidad': 1},
    ]
    
    # Generar factura con 10% de descuento
    factura = generar_factura(productos_ejemplo, porcentaje_descuento=10)
    
    # Mostrar resultados
    print(f"\nFecha: {factura['fecha']}")
    print("\nProductos:")
    print("-" * 40)
    
    for producto in factura['productos']:
        total_item = producto['precio'] * producto['cantidad']
        print(f"  {producto['nombre']}: ${producto['precio']:.2f} x {producto['cantidad']} = ${total_item:.2f}")
    
    print("-" * 40)
    print(f"Subtotal:   ${factura['subtotal']:.2f}")
    print(f"Descuento:  -${factura['descuento']:.2f}")
    print(f"IVA (16%):  +${factura['iva']:.2f}")
    print("-" * 40)
    print(f"TOTAL:      ${factura['total']:.2f} {factura['moneda']}")
    print("=" * 50)


# Ejecutar solo si se llama directamente
if __name__ == "__main__":
    main()

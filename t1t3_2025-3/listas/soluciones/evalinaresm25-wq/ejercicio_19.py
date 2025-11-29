'''
Ejercicio 19: SUPERMERCADO INTELIGENTE
Estudiante: Eva Sofia Linares Medina
GitHub: @evalinaresm25-wq
Fecha: 2025-11-26

Descripción:
Agrega productos, calcula cantidades, elimina y calcula el total.

Métodos usados:
- append()
- remove()
- set()
- count()
'''
carrito = []
precios = {"manzana": 2, "pan": 1.5, "leche": 3, "huevos": 4}

def agregar(producto):
    carrito.append(producto)

def eliminar(producto):
    if producto in carrito:
        carrito.remove(producto)

def total():
    total = 0
    for prod in set(carrito):
        total += precios[prod] * carrito.count(prod)
    print("Total a pagar:", total)

agregar("pan")
agregar("pan")
agregar("leche")
total()

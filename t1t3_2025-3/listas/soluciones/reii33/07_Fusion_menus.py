"""Ejercicio 07: [Fusion de menus]
Estudiante: [Reibert David Andrade Oviedo]
GitHub: @[reii33]
Fecha: [19/11/2025]

Descripción:
[Fusiona dos menus de restaurante y elimina los duplicados]
Ejemplo de uso:
[Fusion de los menus A y B{duplicados}]
"""  
menu_a = ["hamburguesa", "pizza", "ensalada", "sopa"]
menu_b = ["pizza", "pasta", "ensalada", "tacos"]

print(f'Menu restaurante A  {menu_a}')

print(f'menu restaurante B {menu_b}')

fusion_menu = menu_a + menu_b

duplicados = set(fusion_menu)

print(f'Fusion de los menus A y B{duplicados}')






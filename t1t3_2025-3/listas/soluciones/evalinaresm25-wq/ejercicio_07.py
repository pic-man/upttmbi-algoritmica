'''
Ejercicio 7: FUSIÓN DE MENÚS
Estudiante: Eva Sofia Linares Medina
GitHub: @evalinaresm25-wq
Fecha: 2025-11-26

Descripción:
Combina los menús y elimina los duplicados.

Métodos usados:
- list()
- set()
'''
menu_a = ["hamburguesa", "pizza", "ensalada", "sopa"]
menu_b = ["pizza", "pasta", "ensalada", "tacos"]

menu_final = list(set(menu_a + menu_b))
print("Menú combinado:", menu_final)

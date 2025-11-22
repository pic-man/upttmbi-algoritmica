#Los restaurantes se fusionaron
#Combina sus menus en uno solo 
#Elimina los datos duplicados para que no aparezcan dos veces
import time

menu_a = ["hamburguesa","pizza","ensalada","sopa"]

print("menu restaurante a: ")
for comida in menu_a:
    print("-",comida)

menu_b = ["pizza","pasta","ensalada","tacos"]

print("menu restaurante b: ")
for comida in menu_b:
    print("-",comida)

menu_f1 = menu_a + menu_b
menu_f2 = []
eliminados = []

for comida in menu_f1:
    if comida not in menu_f2:
        menu_f2.append(comida)
    else:
        eliminados.append(comida)

print("fusionando...")

time.sleep(1)

print("menu fusionado: ")

for comida in menu_f2:
    print("-",comida)

print("platos unicos:",len(menu_f2))
print("duplicados eliminados: ",eliminados)
        



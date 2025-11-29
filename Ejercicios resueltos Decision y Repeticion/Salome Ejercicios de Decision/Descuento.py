#Ejercico 2: Precio Descuento
#Estudiante : Yoeleiny Mariasalome Barrios Zambrano
#GitHub:Yoeleiny205
#Fecha:2025,11,16

print("Descuento")
precio_original = float(input("Ingresa el precio del producto: $"))
if precio_original > 50: 
    descuento = precio_original * 0.10
    precio_final = precio_original - descuento
    print("Precio original:",precio_original)
    print("Descuento aplicado: 10%")
    print("Precio final: $",precio_final)
else:
    precio_final = precio_original
    print("Precio original: $",precio_original)
    print("Sin descuento aplicado")
    print("Precio final: $",precio_final)
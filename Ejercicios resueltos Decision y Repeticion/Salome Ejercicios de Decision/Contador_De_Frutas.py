#Ejercico 7: Contador de Frutas
#Estudiante : Yoeleiny Mariasalome Barrios Zambrano
#GitHub: Yoeleiny205
#Fecha:2025,11,16
print("¿Qué fruta deseas?")
print("Frutas disponibles: manzana, naranja, plátano")
print()

fruta = input("Ingresa el nombre de la fruta: ").lower()
if fruta == "manzana":
    print("Manzana: $15 por kg")
elif fruta == "naranja":
    print("Naranja: $12 por kg")
elif fruta == "plátano" or fruta == "platano": 
    print("Plátano: $10 por kg")
else:
    print("Lo sentimos,",fruta, "no está disponible")
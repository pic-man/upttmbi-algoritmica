#Ejercico 16: Paraguas
#Estudiante : Yoeleiny Mariasalome Barrios Zambrano
#GitHub: Yoeleiny205
#Fecha:2025,11,16
print("=== ASISTENTE DE CLIMA ===")
print()
probabilidad = int(input("¿Cuál es la probabilidad de lluvia? (%): "))
print()

if probabilidad < 30:
    print(" No necesitas paraguas")
    print("Probabilidad de lluvia: ",probabilidad,"%")
    print("Disfruta del buen clima!")
elif probabilidad <= 70: 
    print(" Lleva paraguas por si acaso")
    print("Probabilidad de lluvia: ",probabilidad,"%")
    print("Mejor prevenir que mojarse!")
else: 
    print(" Definitivamente lleva paraguas")
    print("Probabilidad de lluvia: ",probabilidad,"%")
    print("¡Muy probable que llueva! No olvides tu paraguas.")
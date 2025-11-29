#Ejercico 14: Distancia a Recorrer
#Estudiante : Yoeleiny Mariasalome Barrios Zambrano
#GitHub: Yoeleiny205
#Fecha:2025,11,16

print("=== RECOMENDADOR DE TRANSPORTE ===")
print()
distancia = float(input("¿Cuál es la distancia a recorrer? (km): "))
print()

if distancia < 1:
    print(" RECOMENDACIÓN: Ve caminando")
    print("Distancia:",distancia," km")

    if distancia == 0.5:
        print("Tiempo estimado: 6 minutos")
        print("Calorías quemadas: -35 cal")
    print("Ventajas: Gratis, saludable, eco-friendly")
    
elif distancia <= 5:
    print(" RECOMENDACIÓN: Ve en bicicleta")
    print("Distancia:",distancia," km")
    if distancia == 3.0:
        print("Tiempo estimado: 12 minutos")
        print("Calorías quemadas: -150 cal")
    print("Ventajas: Rápido, económico, saludable")

elif distancia <= 20:
    print(" RECOMENDACIÓN: Ve en auto")
    print("Distancia:",distancia," km")
    if distancia == 15.0:
        print("Tiempo estimado: 20 minutos (tráfico moderado)")
        print("Costo estimado: $45 (gasolina)")
    print("Ventajas: Cómodo, rápido, privado")

else:
    print(" RECOMENDACIÓN: Ve en transporte público")
    print("Distancia:",distancia," km")
    if distancia == 35.0:
        print("Tiempo estimado: 50 minutos")
        print("Costo estimado: $15 (pasaje)")
    print("Ventajas: Económico, relajante, eco-friendly")
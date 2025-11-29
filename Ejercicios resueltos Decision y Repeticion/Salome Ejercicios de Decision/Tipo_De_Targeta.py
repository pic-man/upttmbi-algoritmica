#Ejercico 15: Tipo Targeta
#Estudiante : Yoeleiny Mariasalome Barrios Zambrano
#GitHub: Yoeleiny205
#Fecha:2025,11,16
print("=== BENEFICIOS DE TARJETA DE CRÉDITO ===")
print()
print("Tipos disponibles: básica, oro, platino")
print()

tipo = input("Ingresa tu tipo de tarjeta: ").lower()
print()

if tipo == "basica" or tipo == "básica":
    print(" TARJETA BÁSICA")
    print("Beneficios:")
    print(" 1% de cashback en todas tus compras")
    print(" Protección de compras básica")
    print("Anualidad: $0") 

elif tipo == "oro":
    print(" TARJETA ORO")
    print("\nBeneficios:")
    print(" 2% de cashback en todas tus compras")
    print(" Seguro de viaje incluido")
    print(" Sin comisión en retiros internacionales")
    print(" Protección de compras")
    print("Anualidad: $500")

elif tipo == "platino":
    print(" TARJETA PLATINO")
    print("Beneficios:")
    print(" 3% de cashback en todas tus compras")
    print(" Seguro de viaje internacional premium")
    print(" Acceso a salas VIP en aeropuertos")
    print(" Protección de compras extendida")
    print(" Concierge 24/7")
    print(" Millas dobles en aerolíneas")
    print("Anualidad: $1,200")

else:
    print(" Tipo de tarjeta no válido")
    print("Por favor, elige entre: básica, oro o platino")
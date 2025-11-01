"""
Ejercicio 17: Streaming de Música
Muestra características y precio según el plan de suscripción.
"""

print("=== PLANES DE STREAMING DE MÚSICA ===\n")

# Solicitar el plan
plan = input("Ingresa el tipo de plan (gratuito/básico/premium): ").lower()

# Mostrar información según el plan
if plan == "gratuito":
    print("Música con anuncios")
elif plan == "básico" or plan == "basico":
    print("Música sin anuncios - $59/mes")
elif plan == "premium":
    print("Música sin anuncios + descargas - $99/mes")
else:
    print("Plan no válido")
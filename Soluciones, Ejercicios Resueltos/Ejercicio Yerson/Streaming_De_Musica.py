#Ejercico 17: Streming
#Estudiante:Yerson Josue Saavedra Barrios
#GitHub:Yerson17
#Fecha:2025-11-16
print("=== PLANES DE STREAMING ===")
print()
print("Planes disponibles: gratuito, básico, premium")
print()

plan = input("Elige tu plan: ").lower()
print()

if plan == "gratuito":
    print(" PLAN GRATUITO")
    print("Características:")
    print(" Catálogo completo de música")
    print(" Calidad estándar (128 kbps)")
    print(" Anuncios cada 3 canciones")
    print(" Sin descargas offline")
    print(" Saltos de canción limitados")
    print("Precio: GRATIS")

elif plan == "basico" or plan == "básico":
    print(" PLAN BÁSICO")
    print("Características:")
    print(" Catálogo completo de música")
    print(" Calidad (192 kbps)") 
    print(" Sin anuncios")
    print(" Sin descargas offline")
    print("Saltos de canción ilimitados")
    print("Precio: $59/mes")

elif plan == "premium":
    print(" PLAN PREMIUM")
    print("Características:")
    print(" Catálogo completo de música")
    print(" Calidad alta (320 kbps)")
    print(" Sin anuncios")
    print(" Descargas ilimitadas offline")
    print(" Saltos de canción ilimitados")
    print(" Podcasts exclusivos")
    print(" Modo offline")
    print("Precio: $99/mes")
    print("Ahorro anual: $198 (si pagas por año)")

else:
    print(" Plan no válido")
    print("Por favor, elige entre: gratuito, básico o premium")
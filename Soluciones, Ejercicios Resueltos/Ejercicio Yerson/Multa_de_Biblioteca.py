#Ejercico 12: Multa Biblioteca
#Estudiante:Yerson Josue Saavedra Barrios
#GitHub:Yerson17
#Fecha:2025-11-16
print("=== SISTEMA DE MULTAS - BIBLIOTECA ===")
print()
dias = int(input("¿Cuántos días de retraso tiene el libro? "))
print()

if dias == 0:
    print("¡Libro devuelto a tiempo!")
    print("Sin multa")
    print("Gracias por ser un usuario responsable")
else:
    if dias <= 5:
        tarifa = 5
    elif dias <= 10:
        tarifa = 10
    else:
        tarifa = 15
        
    multa_total = dias * tarifa
    
    print("--- RESUMEN ---")
    print("Días de retraso:",dias)
    print("Tarifa: $",tarifa," por día")
    print("Multa total: $",multa_total)
    print()
    
    if dias <= 5:
        print("Gracias por devolver el libro")
    elif dias <= 10:
        print("Por favor, paga la multa en recepción")
    else:
        print(" AVISO: Retraso excesivo")
        print("La multa es muy alta. Considera renovar tus préstamos a tiempo.")
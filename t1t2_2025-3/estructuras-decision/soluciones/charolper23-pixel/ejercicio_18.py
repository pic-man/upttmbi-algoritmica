"""
Ejercicio 18: Rutina de Ejercicio
Recomienda una rutina según el nivel de condición física.
"""

print("=== RECOMENDACIÓN DE RUTINA DE EJERCICIO ===\n")

# Solicitar el nivel de condición física
nivel = input("Ingresa tu nivel de condición física (principiante/intermedio/avanzado): ").lower()

# Recomendar rutina según el nivel
if nivel == "principiante":
    print("RUTINA RECOMENDADA: 20 minutos de cardio ligero")
elif nivel == "intermedio":
    print("RUTINA RECOMENDADA: 30 minutos de cardio + pesas")
elif nivel == "avanzado":
    print("RUTINA RECOMENDADA: 45 minutos de cardio intenso + pesas pesadas")
else:
    print("Nivel no válido")
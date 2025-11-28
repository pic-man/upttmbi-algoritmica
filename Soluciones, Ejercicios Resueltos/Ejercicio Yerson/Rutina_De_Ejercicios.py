#Ejercico 18: Rutina Ejercicios
#Estudiante:Yerson Josue Saavedra Barrios
#GitHub:Yerson17
#Fecha:2025-11-16
print("=== GENERADOR DE RUTINA DE EJERCICIO ===")
print()
print("Niveles disponibles: principiante, intermedio, avanzado")
print()

nivel = input("¿Cuál es tu nivel? ").lower()
print()

if nivel == "principiante":
    print(" RUTINA PARA PRINCIPIANTE")
    print("Duración: 20 minutos")
    print("Intensidad: Ligera")
    print("Tu rutina de hoy:")
    print("1. Calentamiento (5 min)")
    print("   - Caminata suave")
    print("   - Estiramientos básicos")
    print("2. Cardio (10 min)")
    print("   - Caminata rápida")
    print("   - O bicicleta suave")
    print("3. Enfriamiento (5 min)")
    print("   - Caminata lenta")
    print("   - Estiramientos")
    print(" Consejo: Mantén este ritmo por 2-3 semanas antes de aumentar intensidad")

elif nivel == "intermedio":
    print(" RUTINA PARA INTERMEDIO")
    print("Duración: 30-45 minutos") # De la tabla de pistas
    print("Intensidad: Media-Alta")
    print("Tu rutina de hoy:")
    print("1. Calentamiento (5 min)")
    print("   - Trote suave")
    print("   - Movilidad articular")
    print("2. Cardio (15 min)")
    print("   - Correr a ritmo constante")
    print("3. Entrenamiento de fuerza (20 min)")
    print("   - Circuito de cuerpo completo (Sentadillas, Lagartijas, Remos)")
    print("4. Enfriamiento (5 min)")
    print("   - Estiramientos")
    print(" Consejo: Enfócate en la técnica y aumenta el peso gradualmente")

elif nivel == "avanzado":
    print(" RUTINA PARA AVANZADO")
    print("Duración: 60 minutos")
    print("Intensidad: Alta")
    print("Tu rutina de hoy:")
    print("1. Calentamiento (10 min)")
    print("   - Trote ligero")
    print("   - Movilidad articular")
    print("   - Estiramientos dinámicos")
    print("2. Cardio HIIT (20 min)")
    print("   - 8 intervalos de 2 min")
    print("   - 1 min intenso + 1 min recuperación")
    print("3. Entrenamiento de fuerza (25 min)")
    print("   - Sentadillas: 4x12")
    print("   - Press de banca: 4x10")
    print("   - Peso muerto: 4x8")
    print("   - Dominadas: 4x8")
    print("4. Enfriamiento (5 min)")
    print("   - Trote suave")
    print("   - Estiramientos profundos")
    print(" Consejo: Mantén buena hidratación y descansa 48h entre sesiones intensas")

else:
    print(" Nivel no válido")
    print("Por favor, elige entre: principiante, intermedio o avanzado")
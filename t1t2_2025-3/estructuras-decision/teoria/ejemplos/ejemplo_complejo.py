"""
Ejemplo Complejo - Estructuras de Decisión
===========================================

Este ejemplo muestra el uso de múltiples condiciones combinadas
con operadores lógicos (and, or, not).

Objetivo: Sistema de aprobación de préstamo bancario.
"""

print("="*60)
print("SISTEMA DE EVALUACIÓN DE PRÉSTAMO BANCARIO")
print("="*60)

# Constantes del sistema
EDAD_MINIMA = 18
EDAD_MAXIMA = 65
INGRESO_MINIMO = 1000
INGRESO_MINIMO_SIN_AVAL = 2000
MONTO_MAXIMO_SIN_AVAL = 5000

# Recolectar información del solicitante
print("\nPor favor, completa los siguientes datos:\n")

nombre = input("Nombre completo: ")
edad = int(input("Edad: "))
ingreso_mensual = float(input("Ingreso mensual (USD): "))
tiene_deudas = input("¿Tienes deudas activas? (s/n): ").lower() == "s"
tiene_aval = input("¿Tienes un aval? (s/n): ").lower() == "s"
monto_solicitado = float(input("Monto del préstamo solicitado (USD): "))

# Variables para el resultado
aprobado = False
razon = []
recomendaciones = []

print("\n" + "="*60)
print("EVALUANDO SOLICITUD...")
print("="*60 + "\n")

# Validación 1: Edad
if edad < EDAD_MINIMA or edad > EDAD_MAXIMA:
    razon.append(f"❌ Edad fuera del rango ({EDAD_MINIMA}-{EDAD_MAXIMA} años)")
else:
    print(f"✅ Edad válida: {edad} años")

# Validación 2: Ingresos
if ingreso_mensual < INGRESO_MINIMO:
    razon.append(f"❌ Ingreso insuficiente (mínimo: ${INGRESO_MINIMO})")
else:
    print(f"✅ Ingreso válido: ${ingreso_mensual}")

# Validación 3: Deudas
if tiene_deudas:
    razon.append("❌ Tienes deudas activas")
    recomendaciones.append("Liquida tus deudas antes de solicitar un nuevo préstamo")
else:
    print("✅ Sin deudas activas")

# Validación 4: Monto y aval
if monto_solicitado > MONTO_MAXIMO_SIN_AVAL and not tiene_aval:
    razon.append(f"❌ Monto muy alto sin aval (máximo sin aval: ${MONTO_MAXIMO_SIN_AVAL})")
    recomendaciones.append("Consigue un aval o solicita un monto menor")
elif monto_solicitado > MONTO_MAXIMO_SIN_AVAL and tiene_aval:
    print(f"✅ Monto alto pero tienes aval: ${monto_solicitado}")
else:
    print(f"✅ Monto dentro del rango: ${monto_solicitado}")

# Validación 5: Ingreso suficiente para el monto sin aval
if not tiene_aval and ingreso_mensual < INGRESO_MINIMO_SIN_AVAL:
    razon.append(f"❌ Sin aval se requiere ingreso mínimo de ${INGRESO_MINIMO_SIN_AVAL}")
    recomendaciones.append("Consigue un aval o aumenta tus ingresos")

# Decisión final usando operadores lógicos complejos
if (
    EDAD_MINIMA <= edad <= EDAD_MAXIMA and
    ingreso_mensual >= INGRESO_MINIMO and
    not tiene_deudas and
    (
        monto_solicitado <= MONTO_MAXIMO_SIN_AVAL or
        (monto_solicitado > MONTO_MAXIMO_SIN_AVAL and tiene_aval)
    ) and
    (
        tiene_aval or
        (not tiene_aval and ingreso_mensual >= INGRESO_MINIMO_SIN_AVAL)
    )
):
    aprobado = True

# Mostrar resultado
print("\n" + "="*60)
print("RESULTADO DE LA EVALUACIÓN")
print("="*60 + "\n")

print(f"Solicitante: {nombre}")
print(f"Monto solicitado: ${monto_solicitado}")
print()

if aprobado:
    print("🎉 ¡PRÉSTAMO APROBADO! 🎉")
    print("\nDetalles:")
    print(f"  • Monto: ${monto_solicitado}")
    
    # Calcular tasa de interés según perfil
    if tiene_aval and ingreso_mensual >= INGRESO_MINIMO_SIN_AVAL:
        tasa_interes = 8.5
        print(f"  • Tasa de interés: {tasa_interes}% (Perfil Premium)")
    elif tiene_aval or ingreso_mensual >= INGRESO_MINIMO_SIN_AVAL:
        tasa_interes = 12.0
        print(f"  • Tasa de interés: {tasa_interes}% (Perfil Estándar)")
    else:
        tasa_interes = 15.0
        print(f"  • Tasa de interés: {tasa_interes}% (Perfil Básico)")
    
    # Calcular cuota mensual aproximada (12 meses)
    cuota_mensual = (monto_solicitado * (1 + tasa_interes / 100)) / 12
    print(f"  • Cuota mensual aproximada (12 meses): ${cuota_mensual:.2f}")
    
    print("\nPróximos pasos:")
    print("  1. Visita nuestra sucursal con tu identificación")
    print("  2. Firma los documentos del préstamo")
    print("  3. Recibe tu dinero en 24-48 horas")
    
else:
    print("❌ PRÉSTAMO NO APROBADO")
    print("\nRazones:")
    for r in razon:
        print(f"  {r}")
    
    if recomendaciones:
        print("\nRecomendaciones:")
        for rec in recomendaciones:
            print(f"  💡 {rec}")

print("\n" + "="*60)
print("Gracias por usar nuestro sistema")
print("="*60)

# ANÁLISIS DEL CÓDIGO:
# 
# Este ejemplo combina:
# 1. Múltiples condiciones con and/or
# 2. Anidación controlada (máximo 2 niveles)
# 3. Variables para almacenar resultados
# 4. Validaciones paso a paso con feedback
# 5. Cálculos condicionales
#
# Nota: En un sistema real, esto se dividiría en funciones
# para mejor legibilidad y mantenimiento.

# EJERCICIOS PARA PRACTICAR:
# 1. Agrega validación de historial crediticio (bueno/regular/malo)
# 2. Implementa diferentes plazos de pago (6, 12, 24 meses)
# 3. Crea un sistema de puntos para clasificar el perfil del cliente
# 4. Refactoriza el código usando funciones para cada validación


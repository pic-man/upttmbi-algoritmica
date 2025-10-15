"""
Ejemplo Anidado - Estructuras de Decisión
==========================================

Este ejemplo muestra cómo usar condicionales anidados
(condicionales dentro de otros condicionales).

Objetivo: Sistema de acceso a un club con múltiples validaciones.
"""

print("="*50)
print("SISTEMA DE ACCESO AL CLUB")
print("="*50)

# Datos del usuario
print("\nPor favor, proporciona tu información:")
edad = int(input("Edad: "))
tiene_invitacion = input("¿Tienes invitación? (s/n): ").lower() == "s"
es_socio = input("¿Eres socio del club? (s/n): ").lower() == "s"

print("\n" + "-"*50)
print("PROCESANDO INFORMACIÓN...")
print("-"*50 + "\n")

# Validación anidada
if edad >= 18:
    # La persona es mayor de edad
    if es_socio:
        # Es socio, puede entrar directamente
        print("✅ ACCESO CONCEDIDO")
        print("   Motivo: Eres socio del club")
        print("   Beneficio: Entrada gratuita + bebida de cortesía")
    else:
        # No es socio, verificar si tiene invitación
        if tiene_invitacion:
            print("✅ ACCESO CONCEDIDO")
            print("   Motivo: Tienes una invitación")
            print("   Costo: $50 (tarifa con invitación)")
        else:
            print("✅ ACCESO CONCEDIDO")
            print("   Motivo: Entrada general")
            print("   Costo: $100 (tarifa completa)")
else:
    # La persona es menor de edad
    print("❌ ACCESO DENEGADO")
    print("   Motivo: Debes ser mayor de 18 años")
    print("   Alternativa: Vuelve cuando seas mayor de edad")

print("\n" + "="*50)
print("Gracias por usar nuestro sistema")
print("="*50)

# NOTA SOBRE ANIDACIÓN:
# Este ejemplo usa hasta 3 niveles de anidación.
# En código profesional, se recomienda máximo 2-3 niveles.
# Si necesitas más, considera refactorizar usando funciones.

# EJERCICIOS PARA PRACTICAR:
# 1. Agrega una categoría para menores con adulto responsable
# 2. Implementa descuentos por día de la semana
# 3. Refactoriza el código para reducir la anidación


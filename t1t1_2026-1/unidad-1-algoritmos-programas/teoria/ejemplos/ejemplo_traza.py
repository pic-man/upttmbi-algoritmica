"""
Ejemplo: Traza de un Algoritmo (Corrida en Frío)
Unidad 1: Algoritmo y Programas

Este programa muestra paso a paso cómo se ejecuta un algoritmo,
simulando una traza o corrida en frío.

Algoritmo: Calcular la suma de los primeros N números
"""

print("=== Demostración de Traza de Algoritmo ===")
print("Algoritmo: Sumar los primeros N números\n")

# Entrada
n = int(input("Ingrese N (cantidad de números a sumar): "))

print("\n" + "="*60)
print("TABLA DE TRAZA")
print("="*60)
print(f"{'Paso':<6}{'Instrucción':<25}{'n':<6}{'i':<6}{'suma':<8}{'Condición':<15}")
print("-"*60)

# Inicialización
paso = 1
print(f"{paso:<6}{'n ← '+str(n):<25}{n:<6}{'-':<6}{'-':<8}{'-':<15}")

paso += 1
suma = 0
print(f"{paso:<6}{'suma ← 0':<25}{n:<6}{'-':<6}{suma:<8}{'-':<15}")

paso += 1
i = 1
print(f"{paso:<6}{'i ← 1':<25}{n:<6}{i:<6}{suma:<8}{'-':<15}")

# Ciclo
while True:
    paso += 1
    condicion = f"{i} <= {n} = {i <= n}"
    print(f"{paso:<6}{'MIENTRAS i <= n':<25}{n:<6}{i:<6}{suma:<8}{condicion:<15}")
    
    if not (i <= n):
        break
    
    paso += 1
    suma = suma + i
    print(f"{paso:<6}{'suma ← suma + i':<25}{n:<6}{i:<6}{suma:<8}{'-':<15}")
    
    paso += 1
    i = i + 1
    print(f"{paso:<6}{'i ← i + 1':<25}{n:<6}{i:<6}{suma:<8}{'-':<15}")

# Salida
paso += 1
print(f"{paso:<6}{'ESCRIBIR suma':<25}{n:<6}{i:<6}{suma:<8}{'Salida: '+str(suma):<15}")

print("="*60)
print(f"\nRESULTADO FINAL: La suma de 1 a {n} es {suma}")

# Verificación
verificacion = sum(range(1, n + 1))
print(f"VERIFICACIÓN: 1+2+...+{n} = {verificacion}")
print(f"¿Correcto? {'✅ Sí' if suma == verificacion else '❌ No'}")

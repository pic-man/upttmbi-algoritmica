"""
Ejemplo de Pruebas de Algoritmos
================================

Este archivo demuestra cómo diseñar y ejecutar pruebas
para verificar que los algoritmos funcionan correctamente.

Autor: Profesor de Algorítmica
Fecha: 2025-01-25
"""

# ============================================
# FUNCIONES A PROBAR
# ============================================

def es_par(numero):
    """Determina si un número es par."""
    return numero % 2 == 0


def calcular_factorial(n):
    """Calcula el factorial de n (n!)."""
    if n < 0:
        raise ValueError("No existe factorial de números negativos")
    if n == 0 or n == 1:
        return 1
    
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


def es_palindromo(texto):
    """Verifica si un texto es un palíndromo."""
    # Limpiar el texto: solo letras, en minúsculas
    texto_limpio = ''.join(c.lower() for c in texto if c.isalpha())
    return texto_limpio == texto_limpio[::-1]


def calcular_promedio(numeros):
    """Calcula el promedio de una lista de números."""
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)


# ============================================
# FUNCIONES DE PRUEBA
# ============================================

def ejecutar_prueba(nombre, esperado, obtenido):
    """Ejecuta una prueba y muestra el resultado."""
    if esperado == obtenido:
        print(f"  ✅ {nombre}: PASÓ")
        return True
    else:
        print(f"  ❌ {nombre}: FALLÓ (esperado: {esperado}, obtenido: {obtenido})")
        return False


def probar_es_par():
    """Pruebas para la función es_par()."""
    print("\n📋 Pruebas de es_par()")
    print("-" * 40)
    
    casos = [
        ("Número par positivo", es_par(4), True),
        ("Número impar positivo", es_par(7), False),
        ("Cero es par", es_par(0), True),
        ("Número par negativo", es_par(-6), True),
        ("Número impar negativo", es_par(-3), False),
        ("Número grande par", es_par(1000000), True),
    ]
    
    exitos = sum(ejecutar_prueba(nombre, esperado, obtenido) 
                 for nombre, obtenido, esperado in casos)
    
    print(f"\nResultado: {exitos}/{len(casos)} pruebas pasaron")
    return exitos == len(casos)


def probar_factorial():
    """Pruebas para la función calcular_factorial()."""
    print("\n📋 Pruebas de calcular_factorial()")
    print("-" * 40)
    
    casos = [
        ("Factorial de 0", calcular_factorial(0), 1),
        ("Factorial de 1", calcular_factorial(1), 1),
        ("Factorial de 5", calcular_factorial(5), 120),
        ("Factorial de 10", calcular_factorial(10), 3628800),
    ]
    
    exitos = sum(ejecutar_prueba(nombre, esperado, obtenido) 
                 for nombre, obtenido, esperado in casos)
    
    # Prueba de excepción
    try:
        calcular_factorial(-1)
        print("  ❌ Factorial negativo: FALLÓ (debió lanzar excepción)")
    except ValueError:
        print("  ✅ Factorial negativo: PASÓ (lanzó excepción correctamente)")
        exitos += 1
    
    print(f"\nResultado: {exitos}/{len(casos) + 1} pruebas pasaron")
    return exitos == len(casos) + 1


def probar_palindromo():
    """Pruebas para la función es_palindromo()."""
    print("\n📋 Pruebas de es_palindromo()")
    print("-" * 40)
    
    casos = [
        ("Palíndromo simple", es_palindromo("ana"), True),
        ("Palíndromo con mayúsculas", es_palindromo("Ana"), True),
        ("Palíndromo con espacios", es_palindromo("A man a plan a canal Panama"), True),
        ("No es palíndromo", es_palindromo("hola"), False),
        ("Palabra vacía", es_palindromo(""), True),
        ("Una letra", es_palindromo("a"), True),
        ("Palíndromo largo", es_palindromo("Anita lava la tina"), True),
    ]
    
    exitos = sum(ejecutar_prueba(nombre, esperado, obtenido) 
                 for nombre, obtenido, esperado in casos)
    
    print(f"\nResultado: {exitos}/{len(casos)} pruebas pasaron")
    return exitos == len(casos)


def probar_promedio():
    """Pruebas para la función calcular_promedio()."""
    print("\n📋 Pruebas de calcular_promedio()")
    print("-" * 40)
    
    casos = [
        ("Promedio normal", calcular_promedio([10, 20, 30]), 20.0),
        ("Promedio con decimales", calcular_promedio([1, 2, 3, 4]), 2.5),
        ("Lista vacía", calcular_promedio([]), 0),
        ("Un solo elemento", calcular_promedio([5]), 5.0),
        ("Números negativos", calcular_promedio([-10, 10]), 0.0),
    ]
    
    exitos = sum(ejecutar_prueba(nombre, esperado, obtenido) 
                 for nombre, obtenido, esperado in casos)
    
    print(f"\nResultado: {exitos}/{len(casos)} pruebas pasaron")
    return exitos == len(casos)


# ============================================
# PROGRAMA PRINCIPAL
# ============================================

def main():
    """Ejecuta todas las pruebas."""
    print("=" * 50)
    print("SUITE DE PRUEBAS - DEMOSTRACIÓN")
    print("=" * 50)
    
    resultados = [
        probar_es_par(),
        probar_factorial(),
        probar_palindromo(),
        probar_promedio(),
    ]
    
    print("\n" + "=" * 50)
    print("RESUMEN FINAL")
    print("=" * 50)
    
    total_funciones = len(resultados)
    funciones_ok = sum(resultados)
    
    print(f"Funciones probadas: {total_funciones}")
    print(f"Funciones correctas: {funciones_ok}")
    print(f"Funciones con errores: {total_funciones - funciones_ok}")
    
    if funciones_ok == total_funciones:
        print("\n✅ TODAS LAS PRUEBAS PASARON")
    else:
        print("\n⚠️ ALGUNAS PRUEBAS FALLARON")


if __name__ == "__main__":
    main()

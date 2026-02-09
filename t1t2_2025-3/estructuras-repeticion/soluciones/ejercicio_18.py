# Ejercicio 18: Registro de Ventas Diarias
total = 0.0
for dia in range(7):
    venta = float(input(f"Ventas del día {dia + 1}: $"))
    total = total + venta
print(f"Total semanal: ${total:.2f}")
print(f"Promedio diario: ${total / 7:.2f}")

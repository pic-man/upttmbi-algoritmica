#Ejercico 18: Registro de Ventas
#Estudiante : Jheferson Manuel Duran Marin
#GitHub: Jheferson1213
#Fecha:2025,11,30
print("Registro de Ventas Diarias")
dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
total_semanal = 0.0
total_dias = 0
error_encontrado = False

for dia in dias:
    if error_encontrado:
        break
    venta_str = input("Ventas del " + dia + ": ")
    venta = float(venta_str) 
    if venta < 0:
        print("Entrada inválida. Las ventas no pueden ser negativas.")
        error_encontrado = True
    else:
        total_semanal += venta
        total_dias += 1 
if not error_encontrado:
    if total_dias > 0:
        promedio_diario = total_semanal / total_dias
    else:
        promedio_diario = 0.0
    print("Total semanal:", round(total_semanal, 2))
    print("Promedio diario:", round(promedio_diario, 2))
# 🏧 Ejercicio 17: Simulación de Cajero

## Dificultad: ⭐⭐⭐ Avanzado

## 📝 Descripción

Implementa un cajero automático simplificado que permita realizar operaciones mientras el usuario no elija salir del menú.

## 🎯 Objetivo

Practicar ciclos `while` infinitos controlados con menús, validación de opciones y actualización de estados.

## 📋 Especificaciones

El programa debe:

1. Iniciar con un saldo definido (ej. `1000`).
2. Mostrar un menú con opciones como: `1) Consultar saldo`, `2) Depositar`, `3) Retirar`, `4) Salir`.
3. Permitir que el usuario seleccione opciones repetidamente hasta elegir salir.
4. Validar montos negativos y retiros superiores al saldo.
5. Mostrar mensajes claros después de cada operación.

## 💻 Ejemplo de Ejecución

### Ejemplo 1:
```
--- Cajero Automático ---
1) Consultar saldo
2) Depositar
3) Retirar
4) Salir
Selecciona una opción: 1
Saldo actual: $1000.00

Selecciona una opción: 2
Monto a depositar: 200
Depósito exitoso. Nuevo saldo: $1200.00

Selecciona una opción: 4
¡Gracias por usar el cajero!
```

### Ejemplo 2:
```
Selecciona una opción: 3
Monto a retirar: 1500
Fondos insuficientes. Tu saldo es de $1000.00
```

### Ejemplo 3:
```
Selecciona una opción: 5
Opción no válida. Inténtalo de nuevo.
```

## 🧪 Casos de Prueba

| Secuencia de acciones | Resultado esperado |
|-----------------------|--------------------|
| Consultar saldo -> Salir | Saldo inicial mostrado y mensaje de despedida |
| Depositar 500 -> Consultar | Saldo se incrementa a 1500 |
| Retirar 200 -> Consultar | Saldo disminuye correctamente |
| Retirar 2000 | Mensaje de fondos insuficientes |
| Opción inválida | Mensaje de error |

## 💡 Pistas

1. Usa un `while True` y `break` cuando el usuario elija salir.
2. Implementa funciones auxiliares para cada operación si quieres ordenar el código.
3. Maneja entradas no numéricas con `try/except` (opcional pero recomendable).
4. Muestra el menú en cada iteración para facilitar la interacción.

## ⚠️ Errores Comunes

- ❌ No validar montos negativos en depósitos o retiros.
- ❌ Permitir retiros superiores al saldo.
- ❌ No actualizar el saldo después de cada operación.

## 🎓 Conceptos Practicados

- Ciclo `while` infinito con menú
- Validación de datos
- Actualización de estado en variables

## 🚀 Desafíos Extra (Opcional)

1. Agrega una opción para transferir fondos entre dos cuentas.
2. Considera un límite diario de retiros y notifícalo.
3. Implementa un historial de operaciones que se muestre al salir.

---

**Tiempo estimado**: 20-30 minutos  
**Archivo de solución**: `ejercicio_17.py`


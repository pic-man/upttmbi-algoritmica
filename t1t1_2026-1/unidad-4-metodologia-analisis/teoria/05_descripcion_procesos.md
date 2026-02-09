# 📖 05 - Descripción de los Pasos para Llegar a la Solución

## El Proceso de Solución

El **proceso** es la secuencia ordenada de pasos que transforman los datos de entrada en los resultados de salida.

```
┌─────────────────────────────────────────────────────────────┐
│                    PROCESO DE SOLUCIÓN                       │
│                                                             │
│   ENTRADA ──▶ Paso 1 ──▶ Paso 2 ──▶ ... ──▶ Paso N ──▶ SALIDA │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Características de una Buena Descripción

1. **Secuencial**: Pasos en orden lógico
2. **Completa**: Incluye todos los pasos necesarios
3. **Clara**: Cada paso es entendible
4. **Precisa**: Sin ambigüedades
5. **Verificable**: Se puede seguir y probar

## Plantilla de Descripción de Proceso

```
═══════════════════════════════════════════════════════════
                    DESCRIPCIÓN DEL PROCESO
═══════════════════════════════════════════════════════════

PROBLEMA: [Descripción breve]

ENTRADA:
  - [dato1]: [tipo]
  - [dato2]: [tipo]

PROCESO:
  Paso 1: [Descripción del paso]
  Paso 2: [Descripción del paso]
  Paso 3: [Descripción del paso]
    3.1: [Sub-paso si es necesario]
    3.2: [Sub-paso si es necesario]
  Paso 4: [Descripción del paso]

SALIDA:
  - [resultado1]: [tipo]

VERIFICACIÓN:
  Entrada: [valores de prueba]
  Proceso: [seguimiento paso a paso]
  Salida esperada: [resultado]
═══════════════════════════════════════════════════════════
```

## Ejemplo Completo: Cajero Automático

### Problema
Simular un retiro de efectivo de un cajero automático.

### Descripción del Proceso

```
═══════════════════════════════════════════════════════════
PROCESO: RETIRO DE CAJERO AUTOMÁTICO
═══════════════════════════════════════════════════════════

ENTRADA:
  - numero_tarjeta: cadena (16 dígitos)
  - pin: cadena (4 dígitos)
  - monto_retiro: entero (múltiplo de 20)
  - saldo_cuenta: real

PROCESO:

Paso 1: VALIDAR TARJETA
  1.1 Verificar que el número tenga 16 dígitos
  1.2 SI no es válido: mostrar error y TERMINAR
  1.3 SI es válido: continuar al Paso 2

Paso 2: VALIDAR PIN
  2.1 Solicitar PIN al usuario
  2.2 Comparar con PIN almacenado
  2.3 SI es incorrecto:
      2.3.1 Incrementar contador de intentos
      2.3.2 SI intentos >= 3: bloquear tarjeta y TERMINAR
      2.3.3 SI NO: volver a 2.1
  2.4 SI es correcto: continuar al Paso 3

Paso 3: SOLICITAR MONTO
  3.1 Mostrar menú de montos predefinidos
  3.2 Permitir ingresar otro monto
  3.3 Validar que sea múltiplo de 20
  3.4 SI no es válido: mostrar error y volver a 3.1

Paso 4: VERIFICAR FONDOS
  4.1 Comparar monto_retiro con saldo_cuenta
  4.2 SI monto > saldo: mostrar "Fondos insuficientes" y TERMINAR
  4.3 SI monto <= saldo: continuar al Paso 5

Paso 5: PROCESAR RETIRO
  5.1 nuevo_saldo ← saldo_cuenta - monto_retiro
  5.2 Actualizar saldo en la cuenta
  5.3 Dispensar efectivo
  5.4 Generar recibo

Paso 6: FINALIZAR
  6.1 Preguntar si desea otra operación
  6.2 SI sí: volver al Paso 3
  6.3 SI no: expulsar tarjeta y mostrar despedida

SALIDA:
  - Efectivo dispensado
  - Recibo con nuevo saldo
  - Mensaje de confirmación

VERIFICACIÓN:
  Entrada: tarjeta válida, PIN correcto, retiro $100, saldo $500
  Resultado esperado: Efectivo $100, nuevo saldo $400
═══════════════════════════════════════════════════════════
```

## Pseudocódigo del Proceso

```
ALGORITMO RetiroCajero
    // Paso 1: Validar tarjeta
    SI NO validar_tarjeta(numero_tarjeta) ENTONCES
        ESCRIBIR "Tarjeta inválida"
        TERMINAR
    FIN SI
    
    // Paso 2: Validar PIN
    intentos ← 0
    REPETIR
        LEER pin_ingresado
        SI pin_ingresado == pin_correcto ENTONCES
            SALIR DEL CICLO
        SINO
            intentos ← intentos + 1
            SI intentos >= 3 ENTONCES
                ESCRIBIR "Tarjeta bloqueada"
                TERMINAR
            FIN SI
        FIN SI
    HASTA QUE intentos >= 3
    
    // Paso 3-5: Procesar retiro
    LEER monto_retiro
    SI monto_retiro > saldo ENTONCES
        ESCRIBIR "Fondos insuficientes"
    SINO
        saldo ← saldo - monto_retiro
        ESCRIBIR "Retire su efectivo"
        ESCRIBIR "Nuevo saldo:", saldo
    FIN SI
FIN ALGORITMO
```

## 📝 Para Recordar

1. Describir **cada paso** claramente
2. Incluir **condiciones** y decisiones
3. Considerar **casos de error**
4. Usar **sub-pasos** para detallar
5. **Verificar** con casos de prueba

---

¡Felicidades! Has completado la teoría de la Unidad 4.

[Ir a: Ejercicios →](../ejercicios/README.md)

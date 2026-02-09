# 🔐 Ejercicio 12: Intentos de Contraseña

## Dificultad: ⭐⭐ Intermedio

## 📝 Descripción

Construye un programa que simule un inicio de sesión sencillo, permitiendo hasta 3 intentos para ingresar la contraseña correcta.

## 🎯 Objetivo

Practicar ciclos `while` controlados por contador y condiciones de salida anticipada.

## 📋 Especificaciones

El programa debe:

1. Definir una contraseña preestablecida (ej. `"python123"`).
2. Solicitar al usuario que ingrese la contraseña.
3. Permitir un máximo de 3 intentos.
4. Mostrar un mensaje de acceso concedido si la contraseña es correcta.
5. Mostrar un mensaje de acceso bloqueado si se consumen los 3 intentos sin acierto.

## 💻 Ejemplo de Ejecución

### Ejemplo 1:
```
Ingresa la contraseña: hola
Contraseña incorrecta. Intentos restantes: 2
Ingresa la contraseña: python123
¡Acceso concedido!
```

### Ejemplo 2:
```
Ingresa la contraseña: 1234
Contraseña incorrecta. Intentos restantes: 2
Ingresa la contraseña: 1234
Contraseña incorrecta. Intentos restantes: 1
Ingresa la contraseña: 1234
Acceso bloqueado. Intenta más tarde.
```

### Ejemplo 3:
```
Ingresa la contraseña: python123
¡Acceso concedido!
```

## 🧪 Casos de Prueba

| Entradas | Salida Esperada |
|----------|-----------------|
| Correcta en el primer intento | Acceso concedido |
| Correcta en el segundo intento | Acceso concedido luego de 1 error |
| Correcta en el tercer intento | Acceso concedido sin mensaje de bloqueo |
| Todos los intentos incorrectos | Acceso bloqueado |
| Entrada vacía tres veces | Acceso bloqueado |

## 💡 Pistas

1. Usa una variable para contar los intentos realizados.
2. Disminuye los intentos restantes después de cada intento fallido.
3. Puedes terminar el ciclo anticipadamente con `break` al acertar.

## ⚠️ Errores Comunes

- ❌ Olvidar detener el ciclo cuando la contraseña es correcta.
- ❌ Mostrar intentos restantes negativos.
- ❌ No considerar mayúsculas/minúsculas si la contraseña debe ser exacta.

## 🎓 Conceptos Practicados

- Ciclo `while`
- Contadores y límites
- Condiciones de salida

## 🚀 Desafíos Extra (Opcional)

1. Permite al usuario definir la contraseña al inicio y luego ocultarla (no la imprimas).
2. Bloquea el acceso durante un tiempo simulado (mostrar mensaje con temporizador).
3. Diferencia entre mayúsculas y minúsculas según la configuración deseada.

---

**Tiempo estimado**: 10-15 minutos  
**Archivo de solución**: `ejercicio_12.py`


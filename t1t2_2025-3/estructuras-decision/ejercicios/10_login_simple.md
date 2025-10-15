# 🔐 Ejercicio 10: Inicio de Sesión Simple

## Dificultad: ⭐⭐ Intermedio

## 📝 Descripción

Crea un programa que simule un inicio de sesión simple. Define un usuario y contraseña correctos, luego pide al usuario que ingrese sus credenciales y verifica si son correctas.

## 🎯 Objetivo

Practicar el uso del operador `and` para combinar múltiples condiciones.

## 📋 Especificaciones

El programa debe:

1. Definir credenciales correctas:
   - Usuario: "admin"
   - Contraseña: "1234"
2. Solicitar usuario y contraseña al usuario
3. Determinar según:
   - **Ambos correctos**: "Acceso concedido ✅"
   - **Alguno incorrecto**: "Acceso denegado ❌"

## 💻 Ejemplo de Ejecución

### Ejemplo 1 (Acceso correcto):
```
=== SISTEMA DE LOGIN ===

Usuario: admin
Contraseña: 1234

✅ ¡Acceso concedido!
Bienvenido, admin
```

### Ejemplo 2 (Usuario incorrecto):
```
=== SISTEMA DE LOGIN ===

Usuario: carlos
Contraseña: 1234

❌ Acceso denegado
Usuario incorrecto
```

### Ejemplo 3 (Contraseña incorrecta):
```
=== SISTEMA DE LOGIN ===

Usuario: admin
Contraseña: 5678

❌ Acceso denegado
Contraseña incorrecta
```

### Ejemplo 4 (Ambos incorrectos):
```
=== SISTEMA DE LOGIN ===

Usuario: carlos
Contraseña: 5678

❌ Acceso denegado
Usuario y contraseña incorrectos
```

## 🧪 Casos de Prueba

Prueba tu programa con estos valores:

| Usuario | Contraseña | Resultado |
|---------|------------|-----------|
| admin | 1234 | Acceso concedido ✅ |
| admin | 0000 | Acceso denegado ❌ |
| user | 1234 | Acceso denegado ❌ |
| user | 0000 | Acceso denegado ❌ |
| ADMIN | 1234 | Acceso denegado ❌ |

## 💡 Pistas

1. Define las constantes al inicio:
   ```python
   USUARIO_CORRECTO = "admin"
   PASSWORD_CORRECTA = "1234"
   ```

2. Usa el operador `and`:
   ```python
   if usuario == USUARIO_CORRECTO and password == PASSWORD_CORRECTA:
       # acceso concedido
   else:
       # acceso denegado
   ```

3. Para mensajes específicos, usa estructura anidada:
   ```python
   if usuario == USUARIO_CORRECTO and password == PASSWORD_CORRECTA:
       print("Acceso concedido")
   elif usuario != USUARIO_CORRECTO and password != PASSWORD_CORRECTA:
       print("Usuario y contraseña incorrectos")
   elif usuario != USUARIO_CORRECTO:
       print("Usuario incorrecto")
   else:
       print("Contraseña incorrecta")
   ```

## ⚠️ Errores Comunes

- ❌ No usar `and` para verificar ambas condiciones
- ❌ No distinguir entre errores específicos (usuario vs contraseña)
- ❌ Ser sensible a mayúsculas sin advertir al usuario
- ❌ Mostrar la contraseña en pantalla (en sistemas reales se oculta)

## 🎓 Conceptos Practicados

- Operador `and` para combinar condiciones
- Validación de múltiples campos
- Lógica de autenticación básica
- Mensajes específicos de error

## 🔒 Seguridad (Solo información)

**Nota**: Este es un ejercicio educativo. En aplicaciones reales:
- Nunca guardes contraseñas en texto plano
- Usa encriptación (hashing)
- Implementa límite de intentos
- Usa sistemas de autenticación seguros (OAuth, JWT, etc.)

## 🚀 Desafíos Extra (Opcional)

1. **Límite de intentos**:
   - Permite máximo 3 intentos
   - Bloquea el acceso después de 3 fallos

2. **Múltiples usuarios**:
   ```python
   usuarios = {
       "admin": "1234",
       "usuario1": "pass1",
       "usuario2": "pass2"
   }
   ```

3. **Recuperación de contraseña**:
   - Agrega pregunta de seguridad
   - Permite resetear contraseña

4. **Niveles de acceso**:
   - Admin: acceso total
   - Usuario: acceso limitado
   - Invitado: solo lectura

5. **Registro de intentos**:
   - Guarda fecha y hora de cada intento
   - Muestra último acceso exitoso

---

**Tiempo estimado**: 15-20 minutos  
**Archivo de solución**: `ejercicio_10.py`


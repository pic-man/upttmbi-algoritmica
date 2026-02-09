# 🧪 Ejercicio 04: Diseñar Casos de Prueba

## Nivel: ⭐⭐ Intermedio

## 📝 Descripción

Diseña un plan de pruebas completo para el siguiente algoritmo de validación de contraseñas.

## 🎯 Objetivo

Practicar el diseño de casos de prueba considerando diferentes escenarios: normales, límite e inválidos.

## 📋 Algoritmo a Probar

```python
def validar_password(password):
    """
    Valida si una contraseña cumple con los requisitos de seguridad.
    
    Requisitos:
    - Mínimo 8 caracteres
    - Máximo 20 caracteres
    - Al menos una letra mayúscula
    - Al menos una letra minúscula
    - Al menos un número
    - Al menos un carácter especial (!@#$%^&*)
    
    Returns:
        tuple: (es_valida, lista_errores)
    """
    errores = []
    
    if len(password) < 8:
        errores.append("Debe tener al menos 8 caracteres")
    if len(password) > 20:
        errores.append("No debe exceder 20 caracteres")
    if not any(c.isupper() for c in password):
        errores.append("Debe contener al menos una mayúscula")
    if not any(c.islower() for c in password):
        errores.append("Debe contener al menos una minúscula")
    if not any(c.isdigit() for c in password):
        errores.append("Debe contener al menos un número")
    if not any(c in "!@#$%^&*" for c in password):
        errores.append("Debe contener al menos un carácter especial (!@#$%^&*)")
    
    es_valida = len(errores) == 0
    return es_valida, errores
```

## 📝 Requisitos

### 1. Diseña al menos 15 casos de prueba que incluyan:

- **Casos válidos** (contraseñas que cumplen todos los requisitos)
- **Casos de límite** (exactamente 8 caracteres, exactamente 20)
- **Casos inválidos** (falta cada requisito individualmente)
- **Casos especiales** (contraseña vacía, solo espacios, etc.)

### 2. Usa el siguiente formato para cada caso:

```
┌─────────────────────────────────────────────────────────────┐
│ CASO DE PRUEBA #[número]                                    │
├─────────────────────────────────────────────────────────────┤
│ Descripción: [Qué se está probando]                         │
│ Tipo: [Normal / Límite / Inválido / Especial]               │
│                                                             │
│ Entrada: "[contraseña de prueba]"                           │
│                                                             │
│ Salida esperada:                                            │
│   - es_valida: [True/False]                                 │
│   - errores: [lista de errores esperados]                   │
│                                                             │
│ Justificación: [Por qué este caso es importante]            │
└─────────────────────────────────────────────────────────────┘
```

### 3. Implementa las pruebas en Python

Crea un archivo que ejecute todos los casos de prueba y genere un reporte.

## 📤 Formato de Entrega

1. Documento con los 15+ casos de prueba diseñados
2. Archivo Python con las pruebas implementadas

## ✅ Criterios de Evaluación

| Criterio | Puntos |
|----------|--------|
| Cobertura de casos normales | 15 |
| Cobertura de casos límite | 25 |
| Cobertura de casos inválidos | 25 |
| Cobertura de casos especiales | 15 |
| Implementación en Python | 20 |

## 💡 Pistas

Considera probar:
- ¿Qué pasa con contraseña de exactamente 8 caracteres?
- ¿Y con 7? ¿Y con 21?
- ¿Qué pasa si falta SOLO la mayúscula?
- ¿Y si faltan TODOS los requisitos?
- ¿Contraseña vacía ""?
- ¿Solo espacios "        "?

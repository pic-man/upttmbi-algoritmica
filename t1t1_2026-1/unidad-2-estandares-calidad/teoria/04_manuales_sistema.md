# 📖 04 - Introducción a la Elaboración de Manuales

## Tipos de Manuales

En el desarrollo de software existen tres tipos principales de manuales:

```
┌─────────────────────────────────────────────────────────────┐
│                    TIPOS DE MANUALES                         │
├───────────────────┬───────────────────┬─────────────────────┤
│  MANUAL DEL       │  MANUAL DEL       │   MANUAL DE         │
│  SISTEMA          │  USUARIO          │   PROGRAMAS         │
│                   │                   │                     │
│  Para técnicos    │  Para usuarios    │   Para              │
│  y administradores│  finales          │   desarrolladores   │
└───────────────────┴───────────────────┴─────────────────────┘
```

## 1. Manual del Sistema

### ¿Qué es?

El **manual del sistema** es un documento técnico que describe la arquitectura, configuración y administración del software.

### Contenido Típico

```
MANUAL DEL SISTEMA
==================

1. INTRODUCCIÓN
   1.1 Propósito del documento
   1.2 Alcance del sistema
   1.3 Definiciones y abreviaturas

2. DESCRIPCIÓN GENERAL
   2.1 Perspectiva del sistema
   2.2 Funciones principales
   2.3 Características de los usuarios

3. REQUISITOS DEL SISTEMA
   3.1 Hardware mínimo
   3.2 Software requerido
   3.3 Dependencias

4. ARQUITECTURA
   4.1 Diagrama de componentes
   4.2 Flujo de datos
   4.3 Estructura de archivos

5. INSTALACIÓN
   5.1 Procedimiento de instalación
   5.2 Configuración inicial
   5.3 Verificación

6. ADMINISTRACIÓN
   6.1 Respaldos
   6.2 Mantenimiento
   6.3 Resolución de problemas

7. SEGURIDAD
   7.1 Accesos y permisos
   7.2 Políticas de seguridad
```

### Ejemplo de Sección

```markdown
## 3. REQUISITOS DEL SISTEMA

### 3.1 Hardware Mínimo
- Procesador: Intel Core i3 o equivalente
- Memoria RAM: 4 GB mínimo, 8 GB recomendado
- Espacio en disco: 500 MB disponibles
- Conexión a Internet: 10 Mbps

### 3.2 Software Requerido
- Sistema Operativo: Windows 10/11, macOS 10.15+, Ubuntu 20.04+
- Python: Versión 3.8 o superior
- Navegador: Chrome, Firefox o Edge (última versión)

### 3.3 Dependencias
Las siguientes librerías son necesarias:
- numpy >= 1.20.0
- pandas >= 1.3.0
- flask >= 2.0.0
```

## 2. Manual del Usuario

### ¿Qué es?

El **manual del usuario** es un documento orientado a los usuarios finales que explica cómo utilizar el software de manera clara y sencilla.

### Contenido Típico

```
MANUAL DEL USUARIO
==================

1. INTRODUCCIÓN
   1.1 Bienvenida
   1.2 ¿Qué puede hacer con este programa?
   1.3 Cómo usar este manual

2. PRIMEROS PASOS
   2.1 Iniciar el programa
   2.2 Pantalla principal
   2.3 Navegación básica

3. FUNCIONES PRINCIPALES
   3.1 [Función 1] - Paso a paso
   3.2 [Función 2] - Paso a paso
   3.3 [Función 3] - Paso a paso

4. EJEMPLOS PRÁCTICOS
   4.1 Ejemplo 1: [Caso de uso común]
   4.2 Ejemplo 2: [Otro caso de uso]

5. PREGUNTAS FRECUENTES
   - ¿Cómo hago X?
   - ¿Por qué aparece este mensaje?

6. SOLUCIÓN DE PROBLEMAS
   - Problema común 1 → Solución
   - Problema común 2 → Solución

7. GLOSARIO
   - Términos y definiciones
```

### Ejemplo de Sección

```markdown
## 3.1 Registrar una Venta

### Pasos:

1. **Abrir el módulo de ventas**
   - Haga clic en el menú "Ventas"
   - Seleccione "Nueva Venta"
   
   ![Captura del menú](imagenes/menu_ventas.png)

2. **Ingresar los datos del cliente**
   - Escriba el nombre del cliente
   - Si es cliente nuevo, haga clic en "Agregar Cliente"

3. **Agregar productos**
   - Busque el producto por nombre o código
   - Ingrese la cantidad
   - Haga clic en "Agregar"

4. **Finalizar la venta**
   - Verifique el total
   - Seleccione el método de pago
   - Haga clic en "Confirmar Venta"

### 💡 Consejo
Puede usar el escáner de código de barras para agregar productos más rápido.

### ⚠️ Importante
Verifique siempre el inventario antes de confirmar la venta.
```

## 3. Manual de Programas

### ¿Qué es?

El **manual de programas** (o manual técnico) documenta el código fuente, la lógica de programación y las estructuras de datos para otros desarrolladores.

### Contenido Típico

```
MANUAL DE PROGRAMAS
===================

1. INTRODUCCIÓN
   1.1 Objetivo del documento
   1.2 Convenciones de código
   1.3 Estructura del proyecto

2. ARQUITECTURA DEL CÓDIGO
   2.1 Diagrama de módulos
   2.2 Dependencias entre módulos
   2.3 Patrones de diseño utilizados

3. DESCRIPCIÓN DE MÓDULOS
   3.1 Módulo 1: [Nombre]
       - Propósito
       - Funciones
       - Dependencias
   3.2 Módulo 2: [Nombre]
       ...

4. ESTRUCTURAS DE DATOS
   4.1 Variables globales
   4.2 Estructuras principales
   4.3 Formatos de archivos

5. FUNCIONES Y PROCEDIMIENTOS
   5.1 Lista de funciones
   5.2 Documentación detallada
   5.3 Ejemplos de uso

6. ALGORITMOS PRINCIPALES
   6.1 [Algoritmo 1] - Explicación
   6.2 [Algoritmo 2] - Explicación

7. GUÍA DE MANTENIMIENTO
   7.1 Cómo agregar funcionalidades
   7.2 Cómo corregir errores
   7.3 Estándares de código
```

### Ejemplo de Sección

```markdown
## 5.2 Documentación de Funciones

### calcular_total(productos, descuento)

**Propósito:** Calcula el total de una lista de productos aplicando un descuento.

**Ubicación:** `modulos/ventas.py`, línea 45

**Parámetros:**
| Nombre | Tipo | Descripción |
|--------|------|-------------|
| productos | list | Lista de diccionarios con 'precio' y 'cantidad' |
| descuento | float | Porcentaje de descuento (0-100) |

**Retorno:**
| Tipo | Descripción |
|------|-------------|
| float | Total con descuento aplicado |

**Excepciones:**
- `ValueError`: Si el descuento no está entre 0 y 100

**Ejemplo:**
```python
productos = [
    {'nombre': 'Laptop', 'precio': 1000, 'cantidad': 1},
    {'nombre': 'Mouse', 'precio': 25, 'cantidad': 2}
]
total = calcular_total(productos, 10)  # Retorna 945.0
```

**Algoritmo:**
1. Calcular subtotal sumando precio × cantidad
2. Calcular monto de descuento
3. Restar descuento del subtotal
4. Retornar total
```

## Comparación de Manuales

| Aspecto | Manual Sistema | Manual Usuario | Manual Programas |
|---------|----------------|----------------|------------------|
| **Audiencia** | Administradores | Usuarios finales | Desarrolladores |
| **Lenguaje** | Técnico | Simple y claro | Muy técnico |
| **Contenido** | Configuración | Uso del software | Código fuente |
| **Imágenes** | Diagramas técnicos | Capturas de pantalla | Diagramas UML |
| **Actualización** | Por versión | Por cambios de interfaz | Por cambios de código |

## 📝 Para Recordar

1. Existen **tres tipos** de manuales: sistema, usuario y programas
2. Cada manual tiene una **audiencia específica**
3. El **lenguaje** debe adaptarse al lector
4. Los manuales deben **actualizarse** con el software
5. Incluir **ejemplos** facilita la comprensión

## 🔜 Siguiente Paso

Ahora aprenderás sobre las técnicas de escritura de código.

[Ir a: 05 - Técnicas de Escritura →](./05_tecnicas_escritura.md)

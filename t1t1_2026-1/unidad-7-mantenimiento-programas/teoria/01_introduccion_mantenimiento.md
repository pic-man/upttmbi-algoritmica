# 📖 01 - Introducción al Mantenimiento de Programas

## ¿Qué es el Mantenimiento de Software?

El **mantenimiento de software** es el proceso de modificar un programa después de su entrega para corregir errores, mejorar su rendimiento o adaptarlo a nuevos requisitos.

> "El mantenimiento consume entre el 60% y el 80% del costo total del ciclo de vida del software."

## Tipos de Mantenimiento

```
┌─────────────────────────────────────────────────────────────┐
│                 TIPOS DE MANTENIMIENTO                       │
├─────────────────┬─────────────────┬─────────────────────────┤
│   CORRECTIVO    │   ADAPTATIVO    │      PERFECTIVO         │
│                 │                 │                         │
│ Corregir errores│ Adaptar a       │ Mejorar rendimiento     │
│ y defectos      │ nuevos entornos │ o agregar funciones     │
└─────────────────┴─────────────────┴─────────────────────────┘
```

### 1. Mantenimiento Correctivo (20%)
- Corregir **errores** encontrados después de la entrega
- Solucionar **bugs** reportados por usuarios

### 2. Mantenimiento Adaptativo (25%)
- Adaptar el software a **nuevos sistemas operativos**
- Actualizar para **nuevas tecnologías**
- Modificar por **cambios legales**

### 3. Mantenimiento Perfectivo (50%)
- **Mejorar** el rendimiento
- **Agregar** nuevas funcionalidades
- **Optimizar** código existente

### 4. Mantenimiento Preventivo (5%)
- **Anticipar** problemas futuros
- **Refactorizar** código para facilitar cambios
- **Documentar** mejor el sistema

## Actividades de Mantenimiento

```
┌─────────────────────────────────────────────────────────────┐
│                CICLO DE MANTENIMIENTO                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   1. IDENTIFICAR el problema o mejora                       │
│         ↓                                                   │
│   2. ANALIZAR el impacto del cambio                         │
│         ↓                                                   │
│   3. DISEÑAR la solución                                    │
│         ↓                                                   │
│   4. IMPLEMENTAR los cambios                                │
│         ↓                                                   │
│   5. PROBAR exhaustivamente                                 │
│         ↓                                                   │
│   6. DOCUMENTAR los cambios                                 │
│         ↓                                                   │
│   7. LIBERAR la nueva versión                               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Factores que Afectan el Mantenimiento

| Factor | Impacto Positivo | Impacto Negativo |
|--------|------------------|------------------|
| **Documentación** | Bien documentado | Sin documentación |
| **Código** | Limpio y modular | Espagueti y confuso |
| **Pruebas** | Suite completa | Sin pruebas |
| **Estándares** | Consistentes | Variables |

## Buenas Prácticas

1. **Escribir código limpio** desde el inicio
2. **Documentar** todas las decisiones importantes
3. **Usar control de versiones** (Git)
4. **Crear pruebas automatizadas**
5. **Seguir estándares** de codificación
6. **Refactorizar** regularmente

## 📝 Para Recordar

1. El mantenimiento es la fase **más larga** del ciclo de vida
2. El código bien escrito es **más fácil** de mantener
3. Las **pruebas** son esenciales para el mantenimiento
4. La **documentación** reduce el tiempo de comprensión
5. **Planificar** para el mantenimiento desde el diseño

## 🔜 Siguiente Paso

[Ir a: 02 - Prueba de Caja Negra →](./02_prueba_caja_negra.md)

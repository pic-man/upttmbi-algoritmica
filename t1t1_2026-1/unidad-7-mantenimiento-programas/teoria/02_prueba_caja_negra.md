# 📖 02 - Técnica de Prueba de Caja Negra

## ¿Qué es la Prueba de Caja Negra?

La **prueba de caja negra** es una técnica de prueba que evalúa la funcionalidad de un programa **sin conocer su implementación interna**. Se enfoca en las entradas y salidas.

```
┌─────────────────────────────────────────────────────────────┐
│                    CAJA NEGRA                                │
│                                                             │
│    ENTRADA ──────▶ ┌───────────┐ ──────▶ SALIDA            │
│                    │   ????    │                            │
│   (Conocida)       │ (Oculto)  │        (Esperada)          │
│                    └───────────┘                            │
│                                                             │
│    Solo nos importa: ¿La salida es correcta?                │
└─────────────────────────────────────────────────────────────┘
```

## Características

| Aspecto | Descripción |
|---------|-------------|
| **Enfoque** | Comportamiento externo |
| **Conocimiento** | No se requiere ver el código |
| **Basado en** | Especificaciones y requisitos |
| **Objetivo** | Verificar funcionalidad |

## Técnicas de Caja Negra

### 1. Partición de Equivalencia

Dividir las entradas en **clases equivalentes** donde se espera el mismo comportamiento.

```
Ejemplo: Validar edad (18-65 años permitidos)

Clases de equivalencia:
┌────────────────────────────────────────────────┐
│ Clase 1: edad < 18     │ Inválido (muy joven)  │
│ Clase 2: 18 ≤ edad ≤ 65│ Válido                │
│ Clase 3: edad > 65     │ Inválido (muy mayor)  │
└────────────────────────────────────────────────┘

Casos de prueba (uno por clase):
- edad = 10  → Inválido
- edad = 30  → Válido
- edad = 70  → Inválido
```

### 2. Análisis de Valores Límite

Probar los **valores en los bordes** de cada clase.

```
Para el ejemplo anterior (18-65):

Límites a probar:
- 17 (justo antes del mínimo) → Inválido
- 18 (mínimo exacto)         → Válido
- 19 (justo después del mínimo) → Válido
- 64 (justo antes del máximo) → Válido
- 65 (máximo exacto)         → Válido
- 66 (justo después del máximo) → Inválido
```

### 3. Tabla de Decisión

Para funciones con **múltiples condiciones**.

```
Ejemplo: Descuento en tienda

Condiciones:
- Cliente VIP: Sí/No
- Compra > $100: Sí/No

┌─────────────┬────────┬────────┬────────┬────────┐
│             │ Caso 1 │ Caso 2 │ Caso 3 │ Caso 4 │
├─────────────┼────────┼────────┼────────┼────────┤
│ VIP         │   Sí   │   Sí   │   No   │   No   │
│ Compra >100 │   Sí   │   No   │   Sí   │   No   │
├─────────────┼────────┼────────┼────────┼────────┤
│ Descuento   │  20%   │  10%   │  10%   │   0%   │
└─────────────┴────────┴────────┴────────┴────────┘
```

## Ejemplo Completo

### Función a Probar

```python
def clasificar_triangulo(a, b, c):
    """
    Clasifica un triángulo según sus lados.
    Retorna: "Equilátero", "Isósceles", "Escaleno" o "No válido"
    """
```

### Plan de Pruebas de Caja Negra

```
┌─────────────────────────────────────────────────────────────┐
│                  CASOS DE PRUEBA                             │
├──────┬─────────────┬──────────────────┬─────────────────────┤
│ Caso │   Entrada   │ Salida Esperada  │      Técnica        │
├──────┼─────────────┼──────────────────┼─────────────────────┤
│  1   │ (5, 5, 5)   │ "Equilátero"     │ Clase válida        │
│  2   │ (5, 5, 3)   │ "Isósceles"      │ Clase válida        │
│  3   │ (3, 4, 5)   │ "Escaleno"       │ Clase válida        │
│  4   │ (1, 1, 3)   │ "No válido"      │ Suma lados ≤ tercero│
│  5   │ (0, 5, 5)   │ "No válido"      │ Valor límite (0)    │
│  6   │ (-1, 5, 5)  │ "No válido"      │ Valor negativo      │
└──────┴─────────────┴──────────────────┴─────────────────────┘
```

## Implementación de Pruebas

```python
def probar_clasificar_triangulo():
    casos = [
        ((5, 5, 5), "Equilátero"),
        ((5, 5, 3), "Isósceles"),
        ((3, 4, 5), "Escaleno"),
        ((1, 1, 3), "No válido"),
        ((0, 5, 5), "No válido"),
        ((-1, 5, 5), "No válido"),
    ]
    
    for (a, b, c), esperado in casos:
        resultado = clasificar_triangulo(a, b, c)
        estado = "✅" if resultado == esperado else "❌"
        print(f"{estado} ({a},{b},{c}) → {resultado} (esperado: {esperado})")

probar_clasificar_triangulo()
```

## 📝 Para Recordar

1. **Caja negra** = probar sin ver el código interno
2. Usar **partición de equivalencia** para reducir casos
3. **Valores límite** son propensos a errores
4. **Tablas de decisión** para condiciones múltiples
5. Documentar **todos los casos** de prueba

## 🔜 Siguiente Paso

[Ir a: 04 - Reingeniería →](./04_reingenieria.md)

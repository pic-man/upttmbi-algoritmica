# 📚 Sección T1T3 - Trimestre 2025-3

## Trayecto 1 (PNF) / Trayecto 3 (TSU)

Bienvenido a la sección T1T3. Aquí encontrarás todos los temas de la materia organizados con teoría, ejercicios y espacio para tus soluciones.

## 👥 Estudiantes Registrados

Ver archivo: [estudiantes.json](./estudiantes.json)

## 📖 Temas Disponibles

| # | Tema | Estado | Carpeta |
|---|------|--------|---------|
| 1 | Listas en Python | 🟢 Activo | [listas](./listas/) |
| 2 | Cadenas de caracteres | 🟢 Activo | [cadenas](./cadenas/) |

## 📚 Cómo usar este espacio

### Para cada tema encontrarás:

1. **📚 Teoría** (`teoria/`)
   - Material de estudio
   - Conceptos fundamentales
   - Ejemplos explicados

2. **📝 Ejercicios** (`ejercicios/`)
   - Problemas propuestos
   - Diferentes niveles de dificultad
   - Plantillas para tus soluciones

3. **💻 Soluciones** (`soluciones/`)
   - Tu carpeta personal
   - Entregas de ejercicios
   - Historial de progreso

## 🚀 Primeros Pasos

### 1️⃣ Estudia el tema

```bash
# Reemplaza <tema> por listas o cadenas
cd <tema>/teoria/
# Lee los archivos en orden numérico
```

### 2️⃣ Practica con ejemplos

```bash
# Reemplaza <tema> por listas o cadenas
cd <tema>/teoria/ejemplos/
python ejemplo_basico.py
```

### 3️⃣ Resuelve ejercicios

```bash
# Reemplaza <tema> por listas o cadenas
cd <tema>/ejercicios/
# Lee los enunciados
```

### 4️⃣ Sube tus soluciones

1. Haz **Fork** del repositorio
2. Clona tu fork
3. Crea tu carpeta en `soluciones/tu-usuario/`
4. Resuelve los ejercicios
5. Haz **commit** y **push**
6. Crea un **Pull Request**

## 📁 Estructura de tu trabajo

```
t1t3_2025-3/
├── listas/
│   ├── teoria/
│   │   ├── 01_introduccion_listas.md
│   │   ├── 02_metodos_listas.md
│   │   └── ejemplos/
│   ├── ejercicios/
│   │   ├── 01_pizzeria.md
│   │   └── plantilla_solucion.py
│   └── soluciones/
├── cadenas/
│   ├── teoria/
│   │   ├── 01_introduccion_cadenas.md
│   │   ├── 02_metodos_cadenas.md
│   │   └── ejemplos/
│   ├── ejercicios/
│   │   ├── 01_formato_identidad.md
│   │   └── plantilla_solucion.py
│   └── soluciones/
└── ...
```

## ⚠️ Reglas Importantes

### ✅ Debes:
- Estudiar la teoría antes de hacer ejercicios
- Crear tu carpeta en `soluciones/tu-usuario-github/`
- Usar la plantilla proporcionada
- Comentar tu código
- Probar antes de subir
- Seguir el formato de commits: `[T1T3][Listas] Descripción`

### ❌ NO debes:
- Modificar archivos de `teoria/`
- Modificar archivos de `ejercicios/`
- Tocar carpetas de otros estudiantes
- Modificar carpetas de otras secciones (t1t2_2025-3)
- Copiar código sin entender

## 📊 Tu Progreso

Lleva tu propio registro de ejercicios completados:

| Tema | Ejercicios Totales | Completados | Porcentaje |
|------|-------------------|-------------|------------|
| Listas | 21 | ? | ?% |
| Cadenas | 10 | ? | ?% |

## 🆘 ¿Necesitas Ayuda?

1. **Revisa la teoría** - A menudo la respuesta está ahí
2. **Ejecuta los ejemplos** - Modifícalos para entender
3. **Crea un Issue** - Formato: `[T1T3][Listas] Ayuda con ejercicio X`
4. **Pregunta al profesor** - En clase o por Issue

## 📝 Plantilla para Issues

```markdown
**Título:** [T1T3][Listas] Ayuda con ejercicio 5

**Descripción:**
## Ejercicio
Ejercicio 5: El Mago de las Listas

## Mi duda
No entiendo cómo usar pop() para guardar el elemento eliminado

## Lo que he intentado
```python
# Mi código aquí
```

## Error que obtengo
[Pega el error o describe el problema]
```

## 📈 Estadísticas de la Sección

Para ver el progreso general:
```bash
# Número de estudiantes
cat estudiantes.json | grep -c "github"

# Estudiantes que entregaron en un tema
ls -1 listas/soluciones/ | wc -l
```

## 📧 Contacto

- **Issues en GitHub**: Para dudas técnicas
- **Clase presencial**: Para explicaciones detalladas
- **Correo institucional**: Para asuntos administrativos

---
¡Mucho éxito en tu aprendizaje! 💪📚

**Recuerda:** La práctica constante es la clave del éxito en programación.

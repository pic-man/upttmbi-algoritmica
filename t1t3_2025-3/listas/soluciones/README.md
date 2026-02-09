# 💻 Soluciones de Estudiantes - Listas en Python

## 📁 Carpeta de Entregas

Esta carpeta contiene las soluciones de todos los estudiantes para el tema de Listas.

## 📂 Estructura

Cada estudiante tiene su propia carpeta con su usuario de GitHub:

```
soluciones/
├── README.md (este archivo)
├── usuario-estudiante-1/
│   ├── info.json
│   ├── ejercicio_01.py
│   ├── ejercicio_02.py
│   └── ...
├── usuario-estudiante-2/
│   ├── info.json
│   ├── ejercicio_01.py
│   └── ...
└── ...
```

## 🚀 Cómo Subir tus Soluciones

### 1. Crea tu carpeta personal

```bash
cd t1t3_2025-3/listas/soluciones/
mkdir tu-usuario-github
cd tu-usuario-github
```

### 2. Crea tu archivo de información

```bash
cat > info.json << 'EOF'
{
  "nombre": "Tu Nombre Completo",
  "cedula": "V-12345678",
  "seccion": "T1T3",
  "tema": "listas",
  "correo": "tu.correo@example.com",
  "github": "tu-usuario-github",
  "fecha_inicio": "2025-10-15"
}
EOF
```

### 3. Copia la plantilla y resuelve

```bash
# Copia la plantilla
cp ../../ejercicios/plantilla_solucion.py ejercicio_01.py

# Edita y resuelve
nano ejercicio_01.py
```

### 4. Guarda y sube

```bash
# Desde la raíz del repositorio
git add t1t3_2025-3/listas/soluciones/tu-usuario-github/
git commit -m "[T1T3][Listas] Agregar ejercicio 1 - Pizzería"
git push origin main
```

## ⚠️ Reglas Importantes

### ✅ SÍ puedes:
- Crear/modificar archivos en **TU** carpeta solamente
- Subir archivos `.py` con tus soluciones
- Actualizar tu `info.json`
- Agregar comentarios extensos
- Crear archivos de prueba personales

### ❌ NO puedes:
- Modificar carpetas de otros estudiantes
- Modificar archivos fuera de tu carpeta
- Subir archivos que no sean código Python
- Copiar código sin entender
- Hacer commits directos (solo Pull Requests)

## 📋 Formato de Archivos

### Nombre de archivos:
```
ejercicio_01.py
ejercicio_02.py
...
ejercicio_21.py
```

### Contenido del archivo:
```python
"""
Ejercicio X: Nombre del Ejercicio
Estudiante: Tu Nombre Completo
GitHub: @tu-usuario-github
Fecha: YYYY-MM-DD

Descripción:
[Descripción de tu solución]

Métodos usados:
- append(), remove(), etc.
"""

# Tu código aquí
```

## 📊 Tu Progreso

Verifica tu progreso:

```bash
ls -1 ejercicio_*.py | wc -l
```

O crea un script `mi_progreso.py`:

```python
import os

total = 21
completados = len([f for f in os.listdir('.') if f.startswith('ejercicio_') and f.endswith('.py')])
porcentaje = (completados / total) * 100

print(f"📊 Progreso: {completados}/{total} ({porcentaje:.1f}%)")

if porcentaje == 100:
    print("🎉 ¡Felicidades! Completaste todos los ejercicios")
elif porcentaje >= 75:
    print("💪 ¡Excelente progreso! Ya casi terminas")
elif porcentaje >= 50:
    print("👍 Buen avance, sigue así")
else:
    print("🚀 ¡Vamos! Aún tienes mucho por aprender")
```

## 🎯 Checklist de Entrega

Antes de crear tu Pull Request:

- [ ] Mi carpeta está en la ruta correcta
- [ ] Tengo el archivo `info.json`
- [ ] Mis archivos se llaman `ejercicio_XX.py`
- [ ] Cada archivo tiene el encabezado completo
- [ ] Mi código tiene comentarios
- [ ] Probé todos mis programas
- [ ] Solo modifiqué archivos en MI carpeta
- [ ] Mi commit tiene mensaje descriptivo

## 💡 Consejos

1. **Resuelve en orden** - Los ejercicios están ordenados por dificultad
2. **Prueba tu código** - Usa diferentes casos de prueba
3. **Comenta bien** - Explica tu lógica
4. **Consulta la teoría** - Revisa los archivos .md
5. **Experimenta** - Prueba diferentes métodos

## 📈 Estadísticas

Para ver cuántos estudiantes han entregado:

```bash
# Número de estudiantes
ls -1 | grep -v README.md | wc -l

# Estudiante con más ejercicios
for dir in */; do 
  echo "$dir: $(ls -1 $dir/ejercicio_*.py 2>/dev/null | wc -l)"
done | sort -t: -k2 -rn | head -1
```

## 🆘 ¿Problemas?

1. **No sé por dónde empezar**: Lee la teoría primero
2. **Error de sintaxis**: Verifica indentación y paréntesis
3. **No funciona**: Prueba en el REPL de Python paso a paso
4. **Atascado**: Crea un Issue con tu pregunta específica

## 📧 Contacto

- Crea un Issue: `[T1T3][Listas] Pregunta sobre ejercicio X`
- Pregunta en clase
- Revisa CONTRIBUTING.md

---

¡Mucho éxito con tus ejercicios! 💪🐍

**Recuerda**: Las listas son fundamentales en Python. Domínalas y tendrás una base sólida.


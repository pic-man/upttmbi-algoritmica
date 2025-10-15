# 💻 Soluciones de Estudiantes - Estructuras de Decisión

## 📁 Carpeta de Entregas

Esta carpeta contiene las soluciones de todos los estudiantes para el tema de Estructuras de Decisión.

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
cd t1t3_2025-3/estructuras-decision/soluciones/
mkdir tu-usuario-github
cd tu-usuario-github
```

### 2. Crea tu archivo de información

```bash
cat > info.json << 'EOF'
{
  "nombre": "Tu Nombre Completo",
  "cedula": "V-12345678",
  "seccion": "T1T2",
  "tema": "estructuras-decision",
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
git add t1t3_2025-3/estructuras-decision/soluciones/tu-usuario-github/
git commit -m "[T1T2][Estructuras-Decision] Agregar ejercicio 1"
git push origin main
```

## ⚠️ Reglas Importantes

### ✅ SÍ puedes:
- Crear/modificar archivos en **TU** carpeta solamente
- Subir archivos `.py` con tus soluciones
- Actualizar tu `info.json`
- Agregar comentarios extensos en tu código
- Crear archivos de notas personales (`notas.txt`, etc.)

### ❌ NO puedes:
- Modificar carpetas de otros estudiantes
- Modificar archivos fuera de tu carpeta
- Subir archivos que no sean `.py`, `.json` o `.txt`
- Copiar código de otros sin entender
- Hacer commits directos (solo Pull Requests)

## 📋 Formato de Archivos

### Nombre de archivos:
```
ejercicio_01.py
ejercicio_02.py
...
ejercicio_20.py
```

### Contenido del archivo:
Cada archivo `.py` debe tener:

```python
"""
Ejercicio X: Nombre del Ejercicio
Estudiante: Tu Nombre Completo
GitHub: @tu-usuario-github
Fecha: YYYY-MM-DD

Descripción:
[Descripción de qué hace el programa]

Ejemplo de uso:
Entrada: [ejemplo]
Salida: [ejemplo]
"""

# Tu código aquí
```

## 📊 Tu Progreso

Puedes revisar tu progreso contando los archivos en tu carpeta:

```bash
ls -1 ejercicio_*.py | wc -l
```

O crear un script `progreso.py`:

```python
import os

total_ejercicios = 20
completados = len([f for f in os.listdir('.') if f.startswith('ejercicio_') and f.endswith('.py')])
porcentaje = (completados / total_ejercicios) * 100

print(f"Progreso: {completados}/{total_ejercicios} ({porcentaje:.1f}%)")
```

## 🎯 Checklist de Entrega

Antes de crear tu Pull Request, verifica:

- [ ] Mi carpeta está en la ruta correcta
- [ ] Tengo el archivo `info.json` con mis datos
- [ ] Mis archivos se llaman `ejercicio_XX.py` (con ceros)
- [ ] Cada archivo tiene el encabezado completo
- [ ] Mi código tiene comentarios explicativos
- [ ] Probé todos mis programas y funcionan
- [ ] No modifiqué archivos de otros estudiantes
- [ ] Mi commit tiene mensaje descriptivo

## 💡 Consejos

1. **Organización**: Resuelve los ejercicios en orden
2. **Respaldo**: Haz commit frecuente de tu progreso
3. **Pruebas**: Prueba cada ejercicio antes de subirlo
4. **Comentarios**: Comenta tu código para que entiendas después
5. **Ayuda**: Si te atascas, crea un Issue

## 📈 Estadísticas

Para ver estadísticas de toda la clase:

```bash
# Número de estudiantes que han entregado
ls -1 | grep -v README.md | wc -l

# Estudiante con más ejercicios
for dir in */; do 
  echo "$dir: $(ls -1 $dir/ejercicio_*.py 2>/dev/null | wc -l)"
done | sort -t: -k2 -rn | head -1
```

## 🆘 ¿Problemas?

Si tienes problemas:

1. **Estructura incorrecta**: Revisa que tu carpeta esté en el lugar correcto
2. **Nombre incorrecto**: Tu carpeta debe ser tu usuario de GitHub (minúsculas)
3. **Archivos no aparecen**: Verifica que hiciste `git add` correctamente
4. **Pull Request rechazado**: Lee los comentarios del profesor

## 📧 Contacto

Para dudas sobre entregas:
- Crea un Issue: `[T1T2][Estructuras-Decision] Pregunta sobre entrega`
- Pregunta en clase
- Revisa el archivo CONTRIBUTING.md

---

¡Mucho éxito con tus ejercicios! 💪

**Recuerda**: La práctica constante es la clave del éxito en programación.


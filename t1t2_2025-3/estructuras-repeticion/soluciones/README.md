# 💻 Soluciones de Estudiantes - Estructuras de Repetición

## 📁 Carpeta de Entregas

Esta carpeta agrupa las soluciones de todos los estudiantes para el tema de **Estructuras de Repetición**.

## 📂 Estructura

Cada estudiante debe contar con una carpeta nombrada con su usuario de GitHub:

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
cd t1t2_2025-3/estructuras-repeticion/soluciones/
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
  "tema": "estructuras-repeticion",
  "correo": "tu.correo@example.com",
  "github": "tu-usuario-github",
  "fecha_inicio": "2025-11-11"
}
EOF
```

### 3. Copia la plantilla y resuelve

```bash
# Copia la plantilla del directorio de ejercicios
cp ../../ejercicios/plantilla_solucion.py ejercicio_01.py

# Edita y resuelve
nano ejercicio_01.py
```

### 4. Guarda y sube tus cambios

```bash
# Desde la raíz del repositorio
git add t1t2_2025-3/estructuras-repeticion/soluciones/tu-usuario-github/
git commit -m "[T1T2][Estructuras-Repeticion] Agregar ejercicio 1"
git push origin main
```

## ⚠️ Reglas Importantes

### ✅ SÍ puedes:
- Modificar archivos **solo dentro de tu carpeta**.
- Subir tus soluciones en archivos `.py`, `.json` o `.txt`.
- Actualizar tus datos en `info.json`.
- Agregar notas propias dentro de tu carpeta.

### ❌ NO puedes:
- Editar carpetas o archivos de otros estudiantes.
- Modificar material oficial (ejercicios, teoría, plantillas).
- Subir archivos binarios o ejecutables.
- Copiar código sin entenderlo.

## 📋 Formato de Archivos

### Nombres de archivos:
```
ejercicio_01.py
ejercicio_02.py
...
ejercicio_20.py
```

### Encabezado obligatorio:

```python
"""
Ejercicio X: Nombre del Ejercicio
Estudiante: Tu Nombre Completo
GitHub: @tu-usuario
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

Cuenta tus archivos resueltos:

```bash
ls -1 ejercicio_*.py | wc -l
```

O crea un script de seguimiento:

```python
import os

total_ejercicios = 20
completados = len([f for f in os.listdir('.') if f.startswith('ejercicio_') and f.endswith('.py')])
porcentaje = (completados / total_ejercicios) * 100

print(f"Progreso: {completados}/{total_ejercicios} ({porcentaje:.1f}%)")
```

## 🎯 Checklist de Entrega

Antes de crear tu Pull Request, verifica que:

- [ ] Tu carpeta está en la ruta correcta.
- [ ] Tienes `info.json` con tus datos.
- [ ] Los archivos se llaman `ejercicio_XX.py`.
- [ ] Cada archivo incluye el encabezado completo.
- [ ] Probaste los programas con varios casos (incluye entradas extremas para bucles).
- [ ] No tocaste archivos ajenos.
- [ ] Tus commits tienen mensajes descriptivos.

## 💡 Consejos

1. Resuelve los ejercicios en orden creciente de dificultad.
2. Haz commits frecuentes para no perder avances.
3. Prueba tus bucles con entradas pequeñas y grandes.
4. Agrega comentarios que expliquen la lógica de control de iteraciones.
5. Si te atascas, pide ayuda a tiempo.

## 📈 Estadísticas útiles

```bash
# Número de estudiantes que han entregado
ls -1 | grep -v README.md | wc -l

# Estudiante con más ejercicios resueltos
for dir in */; do
  echo "$dir: $(ls -1 ${dir}ejercicio_*.py 2>/dev/null | wc -l)"
done | sort -t: -k2 -rn | head -1
```

## 🆘 ¿Problemas?

1. **Estructura incorrecta**: verifica que tu carpeta esté dentro de `soluciones/`.
2. **Nombre incorrecto**: la carpeta debe coincidir con tu usuario de GitHub.
3. **Archivos faltantes**: confirma que realizaste `git add` correctamente.
4. **Pull Request rechazado**: revisa los comentarios del profesor y ajusta.

## 📧 Contacto

- Crea un Issue: `[T1T2][Estructuras-Repeticion] Pregunta sobre entrega`
- Consulta en clase
- Revisa el archivo `CONTRIBUTING.md`

---

¡Mucho éxito resolviendo los ejercicios iterativos! 💪 Recuerda practicar constantemente para dominar los bucles.


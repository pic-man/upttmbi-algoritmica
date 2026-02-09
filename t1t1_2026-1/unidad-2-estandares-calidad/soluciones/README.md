# 💻 Soluciones de Estudiantes - Unidad 2

## 📁 Carpeta de Entregas

Esta carpeta contiene las soluciones de todos los estudiantes para la Unidad 2: Estándares de Calidad.

## 📂 Estructura

Cada estudiante tiene su propia carpeta con su usuario de GitHub:

```
soluciones/
├── README.md (este archivo)
├── usuario-estudiante-1/
│   ├── info.json
│   ├── ejercicio_01.py
│   └── ...
└── ...
```

## 🚀 Cómo Subir tus Soluciones

### 1. Crea tu carpeta personal

```bash
cd unidad-2-estandares-calidad/soluciones/
mkdir tu-usuario-github
cd tu-usuario-github
```

### 2. Crea tu archivo de información

```bash
cat > info.json << 'EOF'
{
  "nombre": "Tu Nombre Completo",
  "cedula": "V-12345678",
  "seccion": "TU-SECCION",
  "unidad": "unidad-2-estandares-calidad",
  "correo": "tu.correo@example.com",
  "github": "tu-usuario-github",
  "fecha_inicio": "2025-01-25"
}
EOF
```

### 3. Copia la plantilla y resuelve

```bash
cp ../../ejercicios/plantilla_solucion.py ejercicio_01.py
# Edita y resuelve
```

### 4. Guarda y sube

```bash
git add .
git commit -m "[Unidad-2] Agregar ejercicio 1"
git push origin main
```

## ⚠️ Reglas Importantes

### ✅ SÍ puedes:
- Crear/modificar archivos en **TU** carpeta solamente
- Subir archivos `.py` con tus soluciones
- Actualizar tu `info.json`

### ❌ NO puedes:
- Modificar carpetas de otros estudiantes
- Copiar código de otros sin entender

## 📋 Formato de Archivos

```
ejercicio_01.py
ejercicio_02.py
...
```

---
¡Mucho éxito con tus ejercicios! 💪

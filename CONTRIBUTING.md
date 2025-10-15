# 📘 Guía General de Contribución

## 🎯 Estructura de Aprendizaje

Cada tema sigue este flujo:

```
1. 📚 TEORÍA → 2. 💡 EJEMPLOS → 3. 📝 EJERCICIOS → 4. 📤 ENTREGA
```

## 🚀 Proceso Completo

### 1️⃣ Identifica tu sección

- **T1T3**: [t1t3_2025-3](./t1t3_2025-3/)
- **T1T2**: [t1t2_2025-3](./t1t2_2025-3/)

### 2️⃣ Estudia la teoría del tema

```bash
# Ejemplo para estructuras-decision
cd t1t3_2025-3/estructuras-decision/teoria/

# Lee en orden:
# 01_introduccion.md
# 02_if_else_elif.md
# 03_operadores_comparacion.md
# etc...
```

### 3️⃣ Practica con ejemplos

```bash
cd teoria/ejemplos/

# Ejecuta y modifica los ejemplos
python ejemplo_basico.py
python ejemplo_anidado.py
python ejemplo_complejo.py
```

### 4️⃣ Haz Fork y Clona

```bash
# 1. Ve a GitHub y haz clic en el botón "Fork" (esquina superior derecha)
# 2. Espera a que GitHub cree tu copia personal
# 3. Clona TU fork (no el original):

git clone https://github.com/TU-USUARIO/upttmbi-algoritmica.git
cd upttmbi-algoritmica
```

### 5️⃣ Crea tu carpeta de soluciones

```bash
# Reemplaza "tu-usuario-github" con tu usuario real (todo en minúsculas)
# Ejemplo: si tu usuario es "JuanPerez123", usa "juanperez123"

mkdir -p t1t3_2025-3/estructuras-decision/soluciones/tu-usuario-github

# Crea tu archivo de información
cat > t1t3_2025-3/estructuras-decision/soluciones/tu-usuario-github/info.json << 'INFOJSON'
{
  "nombre": "Tu Nombre Completo",
  "cedula": "V-12345678",
  "seccion": "T1T3",
  "tema": "estructuras-decision",
  "correo": "tu.correo@example.com",
  "github": "tu-usuario-github",
  "fecha_inicio": "2025-10-15"
}
INFOJSON
```

**Ejemplo real:**
```bash
mkdir -p t1t3_2025-3/estructuras-decision/soluciones/juanperez

cat > t1t3_2025-3/estructuras-decision/soluciones/juanperez/info.json << 'INFOJSON'
{
  "nombre": "Juan Pérez García",
  "cedula": "V-20123456",
  "seccion": "T1T3",
  "tema": "estructuras-decision",
  "correo": "juan.perez@gmail.com",
  "github": "juanperez",
  "fecha_inicio": "2025-10-15"
}
INFOJSON
```

### 6️⃣ Resuelve ejercicios

```bash
# Copia la plantilla para cada ejercicio
cp t1t3_2025-3/estructuras-decision/ejercicios/plantilla_solucion.py \
   t1t3_2025-3/estructuras-decision/soluciones/tu-usuario-github/ejercicio_01.py

# Edita con tu editor favorito
# Opciones: nano, vim, code, o cualquier editor
nano t1t3_2025-3/estructuras-decision/soluciones/tu-usuario-github/ejercicio_01.py
```

**Ejemplo de solución:**
```python
"""
Ejercicio 1: Edad Válida
Estudiante: Juan Pérez García
GitHub: @juanperez
Fecha: 2025-10-15

Descripción:
Programa que valida si la edad ingresada es válida y determina
si la persona es menor o mayor de edad.
"""

# Solicitar la edad al usuario
edad = int(input("Ingresa tu edad: "))

# Validar la edad
if edad < 0:
    print("Edad no válida")
elif edad <= 17:
    print("Eres menor de edad")
elif edad <= 120:
    print("Eres mayor de edad")
else:
    print("Edad no válida")
```

### 7️⃣ Guarda tus cambios (Commit)

```bash
# Agrega tus archivos al staging
git add t1t3_2025-3/estructuras-decision/soluciones/tu-usuario-github/

# Verifica qué vas a subir
git status

# Crea un commit con mensaje descriptivo
git commit -m "[T1T3][Estructuras-Decision] Agregar ejercicios 1-5 - Juan Pérez"

# Sube a tu fork en GitHub
git push origin main
```

### 8️⃣ Crea un Pull Request

1. Ve a **tu fork** en GitHub
2. Verás un mensaje: "This branch is X commits ahead..." 
3. Click en **"Contribute"** → **"Open Pull Request"**
4. Verifica que la comparación sea:
   - **base repository**: `profesor-usuario/upttmbi-algoritmica` 
   - **base**: `main`
   - **head repository**: `tu-usuario/upttmbi-algoritmica`
   - **compare**: `main`
5. Escribe un título descriptivo:
   ```
   [T1T3][Estructuras-Decision] - Juan Pérez - Ejercicios 1-5
   ```
6. Completa la descripción:
   ```markdown
   ## 📝 Ejercicios entregados
   - [x] Ejercicio 1: Edad Válida
   - [x] Ejercicio 2: Precio con Descuento
   - [x] Ejercicio 3: Aprobado/Reprobado
   - [x] Ejercicio 4: Número Positivo/Negativo
   - [x] Ejercicio 5: Elegir Deporte
   
   ## 💬 Comentarios
   - Estudié la teoría antes de hacer los ejercicios
   - Probé todos los casos de prueba
   - Tuve dificultad con el ejercicio 4 en la validación de cero
   
   ## ✅ Checklist
   - [x] Mi código está en mi carpeta personal
   - [x] Probé todos los ejercicios
   - [x] Mi código tiene comentarios
   - [x] Solo modifiqué archivos de mi carpeta
   - [x] Leí la teoría del tema
   ```
7. Click en **"Create Pull Request"**

### 9️⃣ Espera la revisión

El profesor revisará tu código y:
- ✅ **Aprobará** y hará merge si está correcto
- 💬 **Dejará comentarios** con sugerencias
- 🔄 **Solicitará cambios** si hay errores

Si se solicitan cambios:
1. Realiza las correcciones en tu computadora
2. Haz commit: `git commit -am "Corregir validaciones según comentarios"`
3. Haz push: `git push origin main`
4. El PR se actualizará automáticamente

## 📁 Estructura de tu carpeta

```
tu-seccion/tema/soluciones/tu-usuario-github/
├── info.json                    # Tu información personal
├── ejercicio_01.py             # Edad Válida
├── ejercicio_02.py             # Precio con Descuento
├── ejercicio_03.py             # Aprobado/Reprobado
└── ...                         # Más ejercicios
```

## 🚫 Reglas Importantes

### ❌ NO MODIFICAR

- Archivos en `teoria/` (son del profesor)
- Archivos en `ejercicios/` (son las instrucciones)
- Carpetas de otros estudiantes
- Carpetas de otras secciones
- Archivo `estudiantes.json`

### ✅ SÍ PUEDES

- Leer toda la teoría y ejemplos
- Ejecutar los ejemplos localmente
- Copiar ejemplos a tu carpeta personal para experimentar
- Modificar SOLO archivos en tu carpeta de soluciones
- Comentar y mejorar tu propio código
- Hacer preguntas mediante Issues

## 📝 Formato de Commits

```bash
# Estructura:
[SECCIÓN][TEMA] Descripción breve

# ✅ Buenos commits:
git commit -m "[T1T3][Estructuras-Decision] Agregar ejercicios 1-5"
git commit -m "[T1T2][Estructuras-Decision] Corregir ejercicio 3"
git commit -m "[T1T3][Estructuras-Decision] Optimizar código ejercicio 10"

# ❌ Malos commits:
git commit -m "update"
git commit -m "fix"
git commit -m "cambios"
git commit -m "ejercicios"
```

## ⚠️ Errores Comunes y Soluciones

### Error: "Permission denied (publickey)"
```bash
# Verifica tu configuración de SSH o usa HTTPS
git clone https://github.com/tu-usuario/upttmbi-algoritmica.git
```

### Error: "Your branch is behind"
```bash
# Actualiza tu fork con el repositorio original
git remote add upstream https://github.com/profesor-usuario/upttmbi-algoritmica.git
git fetch upstream
git merge upstream/main
git push origin main
```

### Error: "Merge conflict"
```bash
# Si hay conflictos, resuélvelos manualmente
git status                    # Ver archivos en conflicto
# Edita los archivos, busca <<<<<<, ====== y >>>>>>
git add .
git commit -m "Resolver conflictos"
git push origin main
```

### Error: "Mi PR incluye archivos de otros"
- Verifica que solo modificaste archivos en TU carpeta
- Si modificaste archivos por error, deshaz los cambios:
```bash
git checkout HEAD -- ruta/del/archivo/equivocado
```

## 🆘 ¿Necesitas ayuda?

### Crea un Issue

1. Ve a la pestaña **Issues**
2. Click en **New Issue**
3. Título descriptivo:
   ```
   [T1T3][Estructuras-Decision] Ayuda con ejercicio 5 - Juan Pérez
   ```
4. Describe tu problema:
   ```markdown
   ## 🤔 Problema
   No entiendo cómo validar múltiples condiciones en el ejercicio 5
   
   ## 💻 Mi código
   ```python
   # Pega tu código aquí
   ```
   
   ## ❓ Pregunta específica
   ¿Cómo puedo usar elif para más de 3 opciones?
   ```

### Tipos de ayuda disponibles

- 🐛 **Bug/Error**: Algo no funciona
- ❓ **Pregunta**: Necesitas aclaración
- 💡 **Idea**: Sugerencia de mejora
- 📚 **Teoría**: Dudas sobre conceptos

## ✅ Checklist Final

Antes de crear tu Pull Request, verifica:

- [ ] Leí toda la teoría del tema
- [ ] Practiqué con los ejemplos
- [ ] Mi carpeta está en la ruta correcta
- [ ] Creé el archivo `info.json` con mis datos
- [ ] Mis archivos tienen nombres descriptivos (ejercicio_XX.py)
- [ ] Mi código tiene comentarios explicativos
- [ ] Probé mi código con diferentes valores
- [ ] Mi código funciona sin errores
- [ ] Solo modifiqué archivos en MI carpeta
- [ ] Mi commit tiene un mensaje descriptivo
- [ ] Revisé que no incluya archivos de otros

---
¡Éxito en tu aprendizaje! 🚀💻

**Recuerda**: La programación se aprende practicando. No te desanimes si algo no funciona a la primera. ¡Sigue intentando!


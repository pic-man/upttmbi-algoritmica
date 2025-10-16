# 📚 Guía para Estudiantes - Cómo Entregar Ejercicios

## 🎯 Flujo de Trabajo

```
1. Hacer FORK del repositorio
2. CLONAR tu fork a tu computadora
3. Crear TU CARPETA en soluciones/
4. Resolver ejercicios
5. COMMIT + PUSH a tu fork
6. Crear PULL REQUEST
7. Esperar revisión del profesor
```

---

## 📖 PASO A PASO DETALLADO

### **PASO 1: Hacer Fork del Repositorio** (Solo UNA vez)

1. Ve a: https://github.com/pic-man/upttmbi-algoritmica
2. Click en el botón **"Fork"** (arriba a la derecha)
3. Selecciona tu cuenta personal
4. Espera a que GitHub cree tu copia

✅ Ahora tienes una copia del repositorio en tu cuenta

---

### **PASO 2: Clonar TU Fork** (Solo UNA vez)

Abre tu terminal y ejecuta:

```bash
# Reemplaza TU-USUARIO con tu usuario de GitHub
git clone https://github.com/TU-USUARIO/upttmbi-algoritmica.git

# Entra a la carpeta
cd upttmbi-algoritmica
```

✅ Ahora tienes el código en tu computadora

---

### **PASO 3: Identificar Tu Sección**

**¿Estás en T1T2 o T1T3?**

- **T1T2** → Carpeta: `t1t2_2025-3/estructuras-decision/`
- **T1T3** → Carpeta: `t1t3_2025-3/listas/`

---

### **PASO 4: Crear Tu Carpeta Personal** (Solo UNA vez)

```bash
# Para T1T3 (ejemplo con listas)
cd t1t3_2025-3/listas/soluciones
mkdir tu-usuario-github
cd tu-usuario-github

# Crear archivo de información
cat > info.json << 'EOF'
{
  "nombre": "Tu Nombre Completo",
  "cedula": "V-12345678",
  "seccion": "T1T3",
  "tema": "listas",
  "correo": "tu.correo@gmail.com",
  "github": "tu-usuario-github",
  "fecha_inicio": "2025-10-16"
}
EOF
```

**Para T1T2:**
```bash
cd t1t2_2025-3/estructuras-decision/soluciones
mkdir tu-usuario-github
cd tu-usuario-github
# Crear info.json (cambiar seccion a "T1T2" y tema a "estructuras-decision")
```

✅ Ya tienes tu espacio de trabajo

---

### **PASO 5: Estudiar la Teoría**

Antes de resolver ejercicios, lee la teoría:

**T1T3 (Listas):**
```bash
cd ../../../teoria/
ls -la
# Lee: 01_introduccion_listas.md, 02_metodos_listas.md, etc.
```

**T1T2 (Estructuras de Decisión):**
```bash
cd ../../../teoria/
ls -la
# Lee: 01_introduccion.md, 02_if_else_elif.md, etc.
```

---

### **PASO 6: Resolver Ejercicios**

```bash
# Volver a tu carpeta
cd ../soluciones/tu-usuario-github/

# Copiar la plantilla
cp ../../ejercicios/plantilla_solucion.py ejercicio_01.py

# Editar con tu editor favorito
nano ejercicio_01.py
# o
code ejercicio_01.py
# o
vim ejercicio_01.py
```

**Estructura de tu solución:**

```python
"""
Ejercicio 1: Pizzería
Estudiante: Juan Pérez
GitHub: @juanperez
Fecha: 2025-10-16

Descripción:
Programa que gestiona ingredientes de pizza
"""

# Tu código aquí
ingredientes = ["queso", "tomate", "anchoas", "jamón"]
ingredientes.append("pepperoni")
ingredientes.remove("anchoas")
print(ingredientes)
```

---

### **PASO 7: Probar Tu Código**

```bash
python ejercicio_01.py
```

✅ Si funciona correctamente, continúa

---

### **PASO 8: Guardar Cambios (Commit)**

```bash
# Volver a la raíz del repositorio
cd ../../../../

# Ver qué cambios hiciste
git status

# Agregar tus archivos
git add t1t3_2025-3/listas/soluciones/tu-usuario-github/

# Guardar cambios con mensaje descriptivo
git commit -m "[T1T3][Listas] Agregar ejercicio 1 - Pizzería"
```

**Formato del mensaje:**
- `[T1T3][Listas]` o `[T1T2][Estructuras-Decision]`
- Descripción clara de qué hiciste

---

### **PASO 9: Subir a Tu Fork (Push)**

```bash
git push origin main
```

✅ Tus cambios ahora están en tu fork de GitHub

---

### **PASO 10: Crear Pull Request**

1. Ve a tu fork en GitHub: `https://github.com/TU-USUARIO/upttmbi-algoritmica`
2. Verás un mensaje: **"This branch is X commits ahead..."**
3. Click en **"Contribute"** → **"Open Pull Request"**
4. **Título del PR:**
   ```
   [T1T3] Juan Pérez - Ejercicios 1-5
   ```
5. **Descripción:**
   ```markdown
   ## Ejercicios entregados
   - [x] Ejercicio 1: Pizzería
   - [x] Ejercicio 2: Lista de Reproducción
   - [x] Ejercicio 3: Contador de Puntos
   
   ## Comentarios
   - Estudié la teoría antes de resolver
   - Probé todos los casos de prueba
   
   ## Checklist
   - [x] Mi código está en mi carpeta personal
   - [x] Probé todos los ejercicios
   - [x] Mi código tiene comentarios
   ```
6. Click en **"Create Pull Request"**

✅ El profesor recibirá tu entrega

---

### **PASO 11: Esperar Revisión**

El profesor:
- ✅ Aprobará tu código → Se integrará al repositorio principal
- 💬 Dejará comentarios → Lee y aprende de ellos
- 🔄 Solicitará cambios → Haz las correcciones y vuelve a hacer push

---

## 🔄 ENTREGAS POSTERIORES

Para entregar más ejercicios:

```bash
# 1. Asegúrate de estar actualizado
cd upttmbi-algoritmica
git pull origin main

# 2. Resuelve el siguiente ejercicio
cd t1t3_2025-3/listas/soluciones/tu-usuario-github/
cp ../../ejercicios/plantilla_solucion.py ejercicio_02.py
# Edita ejercicio_02.py

# 3. Commit y push
cd ../../../../
git add .
git commit -m "[T1T3][Listas] Agregar ejercicio 2"
git push origin main

# 4. El Pull Request existente se actualizará automáticamente
```

---

## ❓ PROBLEMAS COMUNES

### Error: "Permission denied"
```bash
# Verifica que clonaste TU fork, no el original
git remote -v
# Debe decir: https://github.com/TU-USUARIO/...
```

### Error: "Conflicts"
```bash
# Actualiza tu fork con el original
git pull https://github.com/pic-man/upttmbi-algoritmica.git main
git push origin main
```

### "No sé en qué carpeta poner mis ejercicios"
- T1T3 → `t1t3_2025-3/listas/soluciones/tu-usuario/`
- T1T2 → `t1t2_2025-3/estructuras-decision/soluciones/tu-usuario/`

---

## 📋 CHECKLIST FINAL

Antes de crear tu Pull Request:

- [ ] Leí toda la teoría del tema
- [ ] Mi carpeta está en `soluciones/mi-usuario/`
- [ ] Creé el archivo `info.json`
- [ ] Mis archivos se llaman `ejercicio_01.py`, `ejercicio_02.py`, etc.
- [ ] Cada archivo tiene el encabezado con mi información
- [ ] Mi código tiene comentarios explicativos
- [ ] Probé todos mis programas y funcionan
- [ ] Solo modifiqué archivos en MI carpeta
- [ ] Mi mensaje de commit es descriptivo
- [ ] Hice push a mi fork

---

## 🆘 ¿NECESITAS AYUDA?

1. **Revisa CONTRIBUTING.md**
2. **Crea un Issue:**
   - Título: `[T1T3][Listas] Ayuda con ejercicio 5`
   - Describe tu problema
   - Muestra tu código
   - Explica qué error recibes

3. **Pregunta en clase**

---

## 🎯 RESUMEN RÁPIDO

```bash
# 1. Fork en GitHub (una vez)
# 2. Clonar
git clone https://github.com/TU-USUARIO/upttmbi-algoritmica.git
cd upttmbi-algoritmica

# 3. Crear tu carpeta (una vez)
mkdir t1t3_2025-3/listas/soluciones/tu-usuario

# 4. Resolver ejercicios
# 5. Commit
git add .
git commit -m "[T1T3][Listas] Ejercicio X"

# 6. Push
git push origin main

# 7. Pull Request en GitHub
```

---

**¡Mucho éxito en tus ejercicios!** 🚀

**Repositorio:** https://github.com/pic-man/upttmbi-algoritmica


# 🎓 UPTTMBI - Algorítmica
## Repositorio de Ejercicios de Programación

Bienvenido al repositorio oficial de ejercicios de la materia de Algorítmica.

## 📚 Secciones Activas

| Sección | Trayecto | Trimestre | Tema Principal | Carpeta | Estudiantes |
|---------|----------|-----------|----------------|---------|-------------|
| T1T3 | 1 (PNF) / 3 (TSU) | 2025-3 | Listas (21 ejercicios) | [t1t3_2025-3](./t1t3_2025-3/) | Ver carpeta |
| T1T2 | 1 (PNF) / 2 (TSU) | 2025-3 | Estructuras de Decisión (20 ejercicios) | [t1t2_2025-3](./t1t2_2025-3/) | Ver carpeta |

## 📖 Temas Disponibles

Cada sección contiene los siguientes temas organizados en:
- 📚 **Teoría**: Material de estudio, conceptos y explicaciones
- 📝 **Ejercicios**: Problemas para practicar
- 💻 **Soluciones**: Entregas de estudiantes

### Temas Actuales:

**T1T2 - Estructuras de Decisión:**
- 📚 5 archivos de teoría completa
- 💻 3 ejemplos ejecutables
- 📝 20 ejercicios (básico a avanzado)

**T1T3 - Listas en Python:**
- 📚 2 archivos de teoría (introducción, métodos)
- 💻 1 ejemplo ejecutable
- 📝 21 ejercicios (básico a avanzado)

## 👥 Para Estudiantes

### 📝 Paso 1: Identifica tu sección

Entra a la carpeta de tu sección:
- **T1T3**: [Ver instrucciones](./t1t3_2025-3/README.md)
- **T1T2**: [Ver instrucciones](./t1t2_2025-3/README.md)

### 📚 Paso 2: Estudia la teoría

Antes de resolver ejercicios, lee el material teórico:
```
tu-seccion/nombre-tema/teoria/
```

### 📝 Paso 3: Practica con ejercicios

Resuelve los ejercicios propuestos:
```
tu-seccion/nombre-tema/ejercicios/
```

### 📤 Paso 4: Sube tus soluciones

Entrega tus soluciones en:
```
tu-seccion/nombre-tema/soluciones/tu-usuario-github/
```

### 📋 Reglas Generales

- ✅ Lee la teoría antes de hacer ejercicios
- ✅ Solo trabaja en la carpeta de TU sección
- ✅ Usa nombres descriptivos para tus archivos
- ✅ Comenta tu código
- ✅ Practica con los ejemplos antes de ejercicios
- ❌ NO modifiques archivos de otras secciones
- ❌ NO modifiques archivos de otros estudiantes
- ❌ NO modifiques los archivos de teoría o ejercicios

## 👨‍🏫 Para el Profesor

### Gestión por sección y tema

Cada sección es independiente y cada tema dentro tiene:
- `teoria/` - Material educativo que subes tú
- `ejercicios/` - Problemas propuestos
- `soluciones/` - Entregas de estudiantes

### Agregar nuevo tema

```bash
# Ejemplo: agregar tema "ciclos"
mkdir -p t1t3_2025-3/ciclos/{teoria/ejemplos,ejercicios,soluciones}
mkdir -p t1t2_2025-3/ciclos/{teoria/ejemplos,ejercicios,soluciones}
```

### Comandos útiles

```bash
# Ver estudiantes de una sección
cat t1t3_2025-3/estudiantes.json

# Ver entregas de un tema específico
ls -la t1t3_2025-3/estructuras-decision/soluciones/

# Contar cuántos estudiantes entregaron
ls -1 t1t3_2025-3/estructuras-decision/soluciones/ | wc -l

# Ver últimos commits de un estudiante
git log --author="nombre-estudiante" --oneline

# Ver cambios de un Pull Request
gh pr view NUMERO --web
```

### Estadísticas rápidas

```bash
# Estudiantes por sección
echo "T1T3: $(cat t1t3_2025-3/estudiantes.json | grep -c 'github')"
echo "T1T2: $(cat t1t2_2025-3/estudiantes.json | grep -c 'github')"

# Entregas por tema
for seccion in t1t3_2025-3 t1t2_2025-3; do
  echo "$seccion - Estructuras Decision: $(ls -1 $seccion/estructuras-decision/soluciones/ | wc -l)"
done
```

## 📖 Recursos Generales

- [Guía de contribución](CONTRIBUTING.md)
- [Documentación de Python](https://docs.python.org/es/)
- [Tutorial de Git](https://git-scm.com/book/es/v2)
- [Guía de GitHub](https://guides.github.com/)
- [PEP 8 - Guía de estilo Python](https://pep8.org/es/)

## 📧 Contacto

Para dudas o problemas, crea un Issue en este repositorio especificando tu sección.

## 📄 Licencia

Este material es de uso exclusivo para estudiantes de la UPTTMBI.

---
**Universidad Politécnica Territorial del Medio Bravo Iragorry**  
Materia: Algorítmica | Trimestre: 2025-3


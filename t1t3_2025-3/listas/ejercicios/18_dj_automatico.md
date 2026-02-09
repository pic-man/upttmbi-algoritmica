# 🎵 Ejercicio 18: DJ Automático

## Dificultad: ⭐⭐⭐ Avanzado

## 📝 Descripción

Crea una función que gestione una cola de reproducción musical: agregar álbumes, reproducir siguiente, agregar urgentes, mostrar próximas 3.

## 🎯 Objetivo

Implementar sistema de cola (queue) con listas.

## 💻 Lista Inicial

```python
cola_reproduccion = []
```

## 📋 Funciones a Implementar

```python
def agregar_album(cola, canciones):
    """Agrega múltiples canciones al final"""
    pass

def reproducir_siguiente(cola):
    """Reproduce (elimina) la primera canción"""
    pass

def agregar_urgente(cola, cancion):
    """Agrega canción al inicio (suena inmediatamente)"""
    pass

def ver_proximas(cola, cantidad=3):
    """Muestra las próximas N canciones"""
    pass
```

## 💻 Ejemplo de Ejecución

```
=== DJ AUTOMÁTICO ===

Agregando álbum "Greatest Hits"...
✓ Agregadas 5 canciones

Cola actual: 5 canciones

🎵 Próximas 3:
1. Song A
2. Song B
3. Song C

▶️ Reproduciendo: Song A

Cola actual: 4 canciones

🚨 ¡Canción urgente!
✓ "Emergency Song" agregada al inicio

🎵 Ahora suena: Emergency Song

Cola restante: 4 canciones
```

## 💡 Pistas

1. `extend()` para agregar álbum completo
2. `pop(0)` para reproducir siguiente
3. `insert(0, cancion)` para urgentes
4. `lista[:3]` para ver próximas 3

---

**Tiempo estimado**: 40-50 minutos  
**Archivo de solución**: `ejercicio_18.py`


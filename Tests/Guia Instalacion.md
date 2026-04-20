---
draft: true
---


# 🎓 Guía CSS para Bóveda de Matemática y Física en Obsidian

## 📁 Estructura de Archivos

Coloca todos los archivos CSS en:

```
Tu-Bóveda/
└── .obsidian/
    └── snippets/
        ├── base.css
        ├── headers.css
        ├── latex-formulas.css
        ├── tables.css
        ├── code-blocks.css
        └── yaml-styles.css
```

> **Importante:** La carpeta `.obsidian/` puede estar oculta en tu explorador de archivos. En Windows, activa "Mostrar archivos ocultos". En macOS, presiona `Cmd + Shift + .`.

---

## ⚡ Activación en Obsidian

1. Abre Obsidian
2. Ve a **Configuración** → **Apariencia** → **Fragmentos CSS** (sección al final)
3. Haz clic en el ícono 🔄 para actualizar la lista
4. Activa cada fragmento con su interruptor:
    - ✅ `base`
    - ✅ `headers`
    - ✅ `latex-formulas`
    - ✅ `tables`
    - ✅ `code-blocks`
    - ✅ `yaml-styles`

---

## 📝 Ejemplos de YAML Frontmatter

### Nota de Teorema

```yaml
---
titulo: "Teorema de Stokes"
tipo: teorema
materia: calculo
dificultad: avanzado
cssclasses:
  - tipo-teorema
  - materia-calculo
  - dificultad-avanzada
tags: [calculo-vectorial, integrales-de-linea, superficies]
fecha: 2025-03-09
fuente: "Stewart, Cálculo 8va ed."
---
```

### Nota de Demostración

```yaml
---
titulo: "Demostración: Teorema de Bolzano"
tipo: demostracion
materia: calculo
dificultad: intermedio
cssclasses:
  - tipo-demostracion
  - materia-calculo
  - dificultad-intermedia
tags: [analisis, continuidad, teorema-bolzano]
fecha: 2025-03-09
teorema-base: "[[Teorema de Bolzano]]"
---
```

### Nota de Concepto / Definición

```yaml
---
titulo: "Espacio Vectorial"
tipo: concepto
materia: algebra
dificultad: basico
cssclasses:
  - tipo-concepto
  - materia-algebra
  - dificultad-basica
tags: [algebra-lineal, espacios-vectoriales, definicion]
fecha: 2025-03-09
prerequisitos: ["[[Grupos]]", "[[Campos]]"]
---
```

### Nota General (Sin tipo específico)

```yaml
---
titulo: "Apuntes Clase — Física Cuántica"
materia: fisica
fecha: 2025-03-09
clase: "Física Moderna III"
tags: [cuantica, apuntes, pendiente-revisar]
---
```

---

## 🎨 Cómo Personalizar Colores

Todos los colores del sistema se centralizan en `base.css`. Modifica las variables en las secciones `.theme-light` y `.theme-dark`:

```css
/* Ejemplo: cambiar el acento principal de azul a verde */
.theme-light {
  --accent-primary:  #2a9c4a;   /* era #2a7fc1 (azul) */
  --accent-teal:     #1a9e8f;   /* mantener el teal */
}
```

### Variables clave para cambiar:

|Variable|Efecto|
|---|---|
|`--accent-primary`|Color de H1, bordes LaTeX, cabeceras de tabla|
|`--accent-teal`|Color de H3, hover de links, detalles decorativos|
|`--bg-primary`|Fondo principal de la nota|
|`--font-text`|Fuente del texto de párrafo|
|`--font-mono`|Fuente de bloques de código|
|`--latex-bg-start/end`|Colores del degradado en fórmulas LaTeX|

---

## 📦 Plugins Recomendados

### Esenciales para este sistema CSS:

|Plugin|Propósito|
|---|---|
|**Dataview**|Consultas dinámicas usando campos YAML; crea índices automáticos de teoremas, conceptos, etc.|
|**Metadata Menu**|Gestiona campos YAML con formularios visuales; asigna `cssclasses` fácilmente|
|**Templater**|Crea plantillas automáticas con el YAML correcto para cada tipo de nota|
|**Style Settings**|Si quieres controlar variables CSS desde la interfaz gráfica sin tocar código|

### Complementos matemáticos:

|Plugin|Propósito|
|---|---|
|**Extended MathJax**|Añade paquetes LaTeX extras (physics, amsmath, etc.)|
|**Obsidian LaTeX Suite**|Atajos de teclado para escribir LaTeX más rápido|
|**Number Theorems**|Numeración automática de ecuaciones y teoremas|

### Organización:

|Plugin|Propósito|
|---|---|
|**Obsidian Tasks**|Gestión de tareas de estudio pendientes|
|**Periodic Notes**|Notas de sesión de estudio con fecha|
|**Graph Analysis**|Visualiza relaciones entre conceptos y teoremas|

---

## 💡 Campos YAML Adicionales Recomendados

Además de `tipo`, `materia` y `dificultad`, considera estos campos:

```yaml
# Control de estudio
estado: "borrador" | "completo" | "revisar" | "memorizar"
ultima-revision: 2025-03-09
repeticiones: 3           # Para espaciado de repetición (spaced repetition)

# Relaciones académicas
prerequisitos: ["[[Nota 1]]", "[[Nota 2]]"]
implica: ["[[Nota 3]]"]   # Qué conceptos se derivan de este
contraejemplo: "[[Nota X]]"

# Contexto académico
fuente: "Rudin, Análisis Real Cap. 4"
clase: "Análisis Matemático II"
profesor: "Dr. García"
semestre: "2025-1"

# Metadatos de contenido
tiene-ejercicios: true
tiene-demostracion: "[[Dem: Nombre del Teorema]]"
corolarios: ["[[Corolario 1]]"]
```

---

## 🔧 Callouts Personalizados

Los siguientes callouts están integrados en `yaml-styles.css`:

```markdown
> [!theorem] Nombre del Teorema
> Enunciado formal del teorema aquí.

> [!proof] Demostración
> Pasos de la demostración.

> [!definition] Espacio Métrico
> Un espacio métrico es un par $(X, d)$ donde...

> [!example] Ejemplo
> Consideremos la función $f(x) = x^2$...

> [!warning] Cuidado
> No confundir con el concepto de límite puntual.
```

---

## ❓ Solución de Problemas

**Los estilos no aparecen:** → Verifica que los snippets estén activados en Configuración → Apariencia

**Las fórmulas LaTeX no tienen fondo:** → Asegúrate de tener instalado el plugin "MathJax" o que el renderizado matemático esté activo

**La clase CSS no se aplica:** → Verifica que el YAML use `cssclasses` (con s al final) y que el valor sea exactamente igual al nombre de la clase

**Los colores no cambian al modificar `base.css`:** → Desactiva y reactiva el snippet en Configuración para forzar la recarga

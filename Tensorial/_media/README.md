---
title: _media
draft: true
---

# _media — figuras y código del curso Tensorial

Carpeta de recursos visuales. Convención (igual que en Control Clásico):

- **`img_gen/`** — figuras **generadas** en formato `.svg` (diagramas TikZ B/N estilo libro: sistemas de coordenadas, vectores, flujo, circulación; y gráficas matplotlib de campos, equipotenciales, líneas de campo). Se embeben en las notas con `![[nombre.svg|ancho]]`.
- **`code_gen/`** — el **código** que produce esas figuras (`.py` matplotlib / `.tex` TikZ), para poder regenerarlas y revisarlas.
- **Raíz `_media/`** — imágenes hechas a mano o externas que no se generan por código.

Obsidian resuelve los embeds por nombre de archivo desde cualquier subcarpeta. Para generarlas se usa la skill `graficar-figuras`. Las figuras planeadas están anotadas con `# fig:` en [[Tree Tensorial]].

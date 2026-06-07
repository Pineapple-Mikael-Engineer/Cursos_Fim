---
title: Operaciones Vectoriales
tags:
  - analisis-tensorial
  - teoria
  - notacion-indices
  - index
draft: false
aliases:
  - operaciones vectoriales
  - rotacion punto cruz en indices
  - Vector operations
---

# Operaciones Vectoriales

> [!definicion]
> Las operaciones vectoriales del capítulo —**rotación**, **producto punto** y **producto cruz**— escritas en las tres notaciones (vectorial, matricial y de Einstein) para exhibir sus diferencias. En índices, sobre cartesianas ortonormales:
> $$a_i'=R_{ij}a_j,\qquad \vec{A}\cdot\vec{B}=A_iB_i,\qquad (\vec{A}\times\vec{B})_k=\varepsilon_{ijk}A_iB_j.$$

> [!info]
> Es la sección 1.2 del [[index | capítulo 1]] (libro, cap. 1.2). Apoya sobre la [[Notacion Indices Sumatorias | notación de índices]] y el [[Algebra Lineal para Tensores | álgebra de matrices]]. Se desglosa en:
> - [[Rotacion de Vectores]] — rotación 2D, matriz $[R(\phi)]$ y forma $a_i'=R_{ij}a_j$ (cap. 1.2.1).
> - [[Productos Vectoriales]] — punto $A_iB_i$ y cruz $\varepsilon_{ijk}A_iB_j\hat{e}_k$ (cap. 1.2.2).
> - [[Calculos con Notacion Einstein]] — dos derivaciones guía: invariancia de la magnitud e identidad BAC-CAB (cap. 1.2.3).
>
> Las herramientas $\delta_{ij}$ y $\varepsilon_{ijk}$ que aparecen al multiplicar bases viven en [[Simbolos Especiales/index | Símbolos Especiales]].

---

## Ejemplo

> [!ejemplo]
> **La misma operación en tres notaciones.** El producto punto $\vec{A}\cdot\vec{B}$ en $\mathbb{R}^3$:
>
> | Notación | Escritura | Comentario |
> |---|---|---|
> | Vectorial | $\vec{A}\cdot\vec{B}=\lvert\vec{A}\rvert\lvert\vec{B}\rvert\cos\theta$ | independiente de coordenadas |
> | Matricial | $\vec{A}\cdot\vec{B}\rightarrow[A]^\dagger[B]$ | fila por columna |
> | Einstein | $\vec{A}\cdot\vec{B}=A_iB_i$ | suma sobre $i$ |
>
> La notación de Einstein arranca de $A_iB_j(\hat{e}_i\cdot\hat{e}_j)$ y, usando $\hat{e}_i\cdot\hat{e}_j=\delta_{ij}$, colapsa a $A_iB_i$. Las tres dicen lo mismo; la de Einstein es la que mejor escala a manipulaciones complejas.

---

## En qué consiste

> [!teoria]
> La estrategia del libro es presentar cada operación primero en notación vectorial y matricial, y reescribirla en Einstein. La notación vectorial es **independiente del sistema de coordenadas** pero opaca para calcular; la de Einstein es transparente para calcular pero **atada a cartesianas**. El patrón de trabajo es: convertir a índices, manipular (contraer con $\delta_{ij}$, $\varepsilon_{ijk}$), y **volver a notación vectorial** al final para recuperar un resultado válido en cualquier sistema. Las dos derivaciones guía de [[Calculos con Notacion Einstein]] ilustran ese ciclo completo.

> [!info] Apariciones físicas
> Estos productos están en toda la física: el **trabajo** de una fuerza es $W=\int d\vec{r}\cdot\vec{F}$ (producto punto), y la **fuerza de Lorentz** sobre una carga es $\vec{F}=\frac{q}{c}\,\vec{v}\times\vec{B}$ (producto cruz). Por eso dominar su forma en índices es prerrequisito del cálculo vectorial posterior.

## Resumen

> [!resumen]
> | Subnota | Operación | Forma en Einstein |
> |---|---|---|
> | [[Rotacion de Vectores]] | rotación 2D | $a_i'=R_{ij}a_j$ |
> | [[Productos Vectoriales]] | punto / cruz | $A_iB_i$ / $\varepsilon_{ijk}A_iB_j\hat{e}_k$ |
> | [[Calculos con Notacion Einstein]] | derivaciones guía | invariancia de magnitud, BAC-CAB |

> [!corolario]
> Las tres operaciones comparten una misma lección: escritas en índices, su manipulación es mecánica, y el resultado se reexpresa en forma vectorial para recobrar la independencia de coordenadas. Es el primer banco de pruebas serio del convenio de Einstein y de los símbolos $\delta_{ij}$, $\varepsilon_{ijk}$.

> [!referencia]
> - Notación base: [[Notacion Indices Sumatorias]] · [[Algebra Lineal para Tensores]].
> - Símbolos que intervienen: [[Simbolos Especiales/Delta Kronecker]] · [[Simbolos Especiales/Simbolo Levi-Civita]] · [[Simbolos Especiales/Identidad Epsilon-Delta]].

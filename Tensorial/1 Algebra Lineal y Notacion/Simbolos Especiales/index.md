---
title: Símbolos Especiales
order: 4
tags:
  - analisis-tensorial
  - teoria
  - notacion-indices
  - index
draft: false
aliases:
  - simbolos especiales
  - delta y levi-civita
  - Special symbols
---

# Símbolos Especiales

> [!definicion]
> Dos arreglos de índices mecanizan toda el álgebra vectorial en notación de Einstein: la **delta de Kronecker** $\delta_{ij}$, que codifica el producto punto y la base ortonormal ($\hat{e}_i\cdot\hat{e}_j=\delta_{ij}$), y el **símbolo de Levi-Civita** $\varepsilon_{ijk}$, que codifica el producto cruz ($(\vec{A}\times\vec{B})_i=\varepsilon_{ijk}A_jB_k$). La **identidad $\varepsilon$-$\delta$** los enlaza y reduce las identidades vectoriales a manipulación de índices.

> [!info]
> Sección del [[index | capítulo 1]] (libro, cap. 1.2-1.3). Trabajamos en cartesianas con base $\hat{e}_i$ ortonormal y fija, sobre la [[Notacion Indices Sumatorias | notación de Einstein]]. Se desglosa en:
> - [[Delta Kronecker]] — $\delta_{ij}$, propiedad de sustitución, producto punto (cap. 1.2.2).
> - [[Simbolo Levi-Civita]] — $\varepsilon_{ijk}$, permutaciones, producto cruz (cap. 1.2.2).
> - [[Identidad Epsilon-Delta]] — $\varepsilon_{ijk}\varepsilon_{mnk}=\delta_{im}\delta_{jn}-\delta_{in}\delta_{jm}$ e identidades vectoriales (cap. 1.2.3).

---

## Ejemplo

> [!ejemplo]
> **Cada símbolo es un producto.** Las dos operaciones básicas del álgebra vectorial se escriben con un símbolo cada una:
>
> | Operación | Notación vectorial | Notación de índices | Símbolo |
> |---|---|---|---|
> | Producto punto | $\vec{A}\cdot\vec{B}$ | $A_iB_i=\delta_{ij}A_iB_j$ | $\delta_{ij}$ |
> | Producto cruz | $(\vec{A}\times\vec{B})_i$ | $\varepsilon_{ijk}A_jB_k$ | $\varepsilon_{ijk}$ |
> | Doble cruz (BAC-CAB) | $\vec{A}\times(\vec{B}\times\vec{C})$ | $\varepsilon_{ijk}\varepsilon_{klm}A_jB_lC_m$ | $\varepsilon\varepsilon\to\delta\delta$ |
>
> La última fila es el motivo de toda la sección: un producto de **dos** $\varepsilon$ se convierte, por la identidad $\varepsilon$-$\delta$, en una combinación de $\delta$, y cada $\delta$ se reabsorbe por sustitución. Las identidades vectoriales dejan de memorizarse: se derivan.

---

## En qué consiste

> [!teoria]
> En cartesianas ortonormales la base satisface $\hat{e}_i\cdot\hat{e}_j=\delta_{ij}$ y $\hat{e}_i\times\hat{e}_j=\varepsilon_{ijk}\hat{e}_k$. Sustituir estas dos relaciones en $\vec{A}\cdot\vec{B}=A_iB_j(\hat{e}_i\cdot\hat{e}_j)$ y $\vec{A}\times\vec{B}=A_iB_j(\hat{e}_i\times\hat{e}_j)$ produce directamente las fórmulas por componentes. Por eso $\delta_{ij}$ y $\varepsilon_{ijk}$ no son definiciones ad hoc: son las **tablas de multiplicar de la base** escritas como arreglos de índices.

## Resumen

> [!resumen]
> | Subnota | Aporta | Fórmula clave |
> |---|---|---|
> | [[Delta Kronecker]] | producto punto, sustitución | $\delta_{ij}A_j=A_i$ |
> | [[Simbolo Levi-Civita]] | producto cruz, antisimetría | $(\vec{A}\times\vec{B})_i=\varepsilon_{ijk}A_jB_k$ |
> | [[Identidad Epsilon-Delta]] | identidades vectoriales | $\varepsilon_{ijk}\varepsilon_{mnk}=\delta_{im}\delta_{jn}-\delta_{in}\delta_{jm}$ |

> [!corolario]
> Con $\delta$, $\varepsilon$ y su identidad, demostrar una identidad vectorial (BAC-CAB, $\vec\nabla\times(\vec\nabla\times\vec{F})$, etc.) se vuelve un cálculo mecánico de índices, sin geometría ni casos. Es la primera ganancia tangible de la notación de Einstein.

> [!referencia]
> - Notación que las soporta: [[Notacion Indices Sumatorias]].
> - Primer uso intensivo: [[Operaciones Vectoriales/Calculos con Notacion Einstein]].
> - Operaciones que mecanizan: [[Operaciones Vectoriales/Productos Vectoriales]].

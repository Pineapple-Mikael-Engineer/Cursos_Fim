---
title: Productos Vectoriales
tags:
  - analisis-tensorial
  - teoria
  - notacion-indices
  - producto-punto
  - producto-cruz
draft: false
aliases:
  - productos vectoriales
  - producto punto y cruz
  - dot and cross product
  - vector products
---

# Productos Vectoriales

> [!definicion]
> El álgebra vectorial define **dos** productos entre vectores. El **producto punto** $\vec{A}\cdot\vec{B}$ devuelve un **escalar**; el **producto cruz** $\vec{A}\times\vec{B}$ devuelve un **vector**. En cartesianas ortonormales,
> $$\vec{A}\cdot\vec{B}=\lvert\vec{A}\rvert\lvert\vec{B}\rvert\cos\theta=A_iB_i,\qquad \vec{A}\times\vec{B}=\varepsilon_{ijk}A_iB_j\hat{e}_k,\quad \lvert\vec{A}\times\vec{B}\rvert=\lvert\vec{A}\rvert\lvert\vec{B}\rvert\operatorname{sen}\theta.$$

> [!info]
> Es la operación 1.2.2 del libro, dentro de [[index | Operaciones Vectoriales]] del [[../index | capítulo 1]]. Esta nota **compara** los dos productos; el desarrollo completo de cada uno —definición, demostración en índices, propiedades y ejemplos— vive en su propia hoja: [[Producto Punto]] y [[Producto Cruz]]. El punto introduce la [[Simbolos Especiales/Delta Kronecker | delta de Kronecker]] $\delta_{ij}$ (vía $\hat{e}_i\cdot\hat{e}_j=\delta_{ij}$) y la cruz el [[Simbolos Especiales/Simbolo Levi-Civita | símbolo de Levi-Civita]] $\varepsilon_{ijk}$. Su uso combinado para derivar identidades se ve en [[Calculos con Notacion Einstein]].

---

## Comparativa

> [!info] Punto vs cruz
> | Aspecto | Producto punto $\vec{A}\cdot\vec{B}$ | Producto cruz $\vec{A}\times\vec{B}$ |
> |---|---|---|
> | Resultado | **escalar** | **(pseudo)vector** $\perp$ al plano |
> | Geometría | $\lvert\vec{A}\rvert\lvert\vec{B}\rvert\cos\theta$ | $\lvert\vec{A}\rvert\lvert\vec{B}\rvert\operatorname{sen}\theta$ (área) |
> | Forma en índices | $A_iB_j\delta_{ij}=A_iB_i$ | $\varepsilon_{ijk}A_iB_j\hat{e}_k$ |
> | Símbolo que usa | $\delta_{ij}$ | $\varepsilon_{ijk}$ |
> | Simetría | conmutativo $\vec{A}\cdot\vec{B}=\vec{B}\cdot\vec{A}$ | anticonmutativo $\vec{A}\times\vec{B}=-\vec{B}\times\vec{A}$ |
> | Se anula cuando | $\vec{A}\perp\vec{B}$ | $\vec{A}\parallel\vec{B}$ |
> | Consigo mismo | $\vec{A}\cdot\vec{A}=\lvert\vec{A}\rvert^2$ | $\vec{A}\times\vec{A}=0$ |
> | Caso físico | trabajo $W=\int d\vec{r}\cdot\vec{F}$ | torque $\vec{\tau}=\vec{r}\times\vec{F}$, Lorentz $\vec{v}\times\vec{B}$ |
>
> Los dos son **complementarios**: el punto extrae la parte paralela de un vector respecto de otro ($\cos$), el cruz la perpendicular ($\operatorname{sen}$). Por eso $(\vec{A}\cdot\vec{B})^2+\lvert\vec{A}\times\vec{B}\rvert^2=\lvert\vec{A}\rvert^2\lvert\vec{B}\rvert^2$.

> [!corolario]
> Toda la diferencia entre ambos productos cabe en qué símbolo aparece al multiplicar las bases: $\hat{e}_i\cdot\hat{e}_j=\delta_{ij}$ (simétrico → escalar conmutativo) frente al $\varepsilon_{ijk}$ del determinante (antisimétrico → vector anticonmutativo). Con $\delta$ y $\varepsilon$ como únicas herramientas nuevas, cualquier identidad vectorial se deriva mecánicamente en índices.

> [!referencia]
> - Producto escalar (def., demostración, propiedades): [[Producto Punto]].
> - Producto vectorial (def., demostración, propiedades): [[Producto Cruz]].
> - Derivaciones que combinan ambos (invariancia de magnitud, BAC-CAB): [[Calculos con Notacion Einstein]].
> - Símbolos involucrados: [[Simbolos Especiales/Delta Kronecker]] · [[Simbolos Especiales/Simbolo Levi-Civita]] · [[Simbolos Especiales/Identidad Epsilon-Delta]].

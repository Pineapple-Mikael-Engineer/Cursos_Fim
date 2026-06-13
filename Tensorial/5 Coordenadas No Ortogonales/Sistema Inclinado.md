---
title: Un Sistema de Coordenadas Inclinado
tags:
  - analisis-tensorial
  - teoria
  - coordenadas-no-ortogonales
draft: false
aliases:
  - sistema inclinado
  - base oblicua
  - inclined coordinate system
---

# Un Sistema de Coordenadas Inclinado

> [!definicion]
> Un sistema **inclinado** tiene una base $\hat g'_1,\hat g'_2$ de vectores unitarios **no ortogonales** ($\hat g'_i\cdot\hat g'_j\neq\delta_{ij}$). En él, la proyección habitual **falla**: la componente $v'_1$ de un vector **no** es $\vec v\cdot\hat g'_1$, porque los ejes no son perpendiculares.

> [!info]
> Inicia el desarrollo del [[index | capítulo 5]] (libro, cap. 5.2.1). Es el problema que motiva introducir las componentes [[Metrica/Covarianza Contravarianza | covariantes y contravariantes]] y el [[Metrica/Tensor Metrico | tensor métrico]]. Comparado con el sistema cartesiano ortonormal ($\hat e_i\cdot\hat e_j=\delta_{ij}$), donde todo es simple.

---

## Ejemplo

> [!ejemplo]
> **La proyección que funciona y la que no.** En un sistema **ortonormal** ($\hat e_i\cdot\hat e_j=\delta_{ij}$), proyectar recupera la componente:
> $$\vec v\cdot\hat e_1=(v_1\hat e_1+v_2\hat e_2)\cdot\hat e_1=v_1(\hat e_1\cdot\hat e_1)+v_2(\hat e_2\cdot\hat e_1)=v_1\delta_{11}+v_2\delta_{21}=v_1.\ ✓$$
>
> ![[sistema_inclinado.svg|460]]
>
> En el sistema **inclinado** $\vec v=v'_1\hat g'_1+v'_2\hat g'_2$, el mismo intento da un término de más:
> $$\vec v\cdot\hat g'_1=v'_1(\hat g'_1\cdot\hat g'_1)+v'_2(\hat g'_2\cdot\hat g'_1)=v'_1+v'_2(\hat g'_2\cdot\hat g'_1)\neq v'_1.$$
> El término $v'_2(\hat g'_2\cdot\hat g'_1)$ **no se anula** porque $\hat g'_2\cdot\hat g'_1\neq0$ (ejes no perpendiculares). La proyección simple ya no aísla la componente.

---

## En qué consiste

> [!teoria]
> La belleza del sistema ortonormal venía de $\hat e_i\cdot\hat e_j=\delta_{ij}$: al proyectar, todos los términos cruzados ($i\neq j$) se anulaban. En un sistema inclinado los términos cruzados $\hat g'_i\cdot\hat g'_j$ ($i\neq j$) **sobreviven**, y aparecen en cualquier producto punto. Por ejemplo,
> $$\vec A\cdot\vec B=A'_1B'_1+A'_2B'_2+(A'_1B'_2+A'_2B'_1)(\hat g'_1\cdot\hat g'_2),$$
> con un término extra respecto al caso ortonormal $A_1B_1+A_2B_2$.
>
> Hay dos caminos para volver a una forma simple, ambos desarrollados en el capítulo:
> 1. Definir **componentes covariantes** que absorben los términos cruzados, de modo que $\vec A\cdot\vec B=A'_iB̃'_i$ (ver [[Metrica/Covarianza Contravarianza | covarianza/contravarianza]]).
> 2. Usar el **tensor métrico** $M_{ij}=\hat g_i\cdot\hat g_j$: $\vec A\cdot\vec B=A^iB^jM_{ij}$ (ver [[Metrica/Tensor Metrico | tensor métrico]]).

> [!warning] Restricción de este capítulo
> Para empezar simple, se asume que la base inclinada es **invariante en la posición** (no cambia de un punto a otro) y unitaria ($\hat g'_i\cdot\hat g'_i=1$). El caso general (bases que varían con la posición y curvatura) es el de la geometría diferencial / Relatividad General.

## Resumen

> [!resumen]
> | Aspecto | Ortonormal | Inclinado |
> |---|---|---|
> | Base | $\hat e_i\cdot\hat e_j=\delta_{ij}$ | $\hat g'_i\cdot\hat g'_j\neq\delta_{ij}$ |
> | Componente por proyección | $v_1=\vec v\cdot\hat e_1$ ✓ | $\vec v\cdot\hat g'_1\neq v'_1$ ✗ |
> | Producto punto | $A_1B_1+A_2B_2$ | con términos cruzados extra |
> | Solución | — | covariante/contravariante + métrica |

> [!corolario]
> El sistema inclinado expone el problema central del capítulo: sin ortogonalidad, la proyección ya no da la componente y el producto punto se llena de términos cruzados $\hat g'_i\cdot\hat g'_j$. La salida es duplicar la noción de componente (covariante y contravariante) y empaquetar los productos cruzados en el [[Metrica/Tensor Metrico | tensor métrico]] $M_{ij}$.

> [!referencia]
> - Las dos clases de componentes: [[Metrica/Covarianza Contravarianza]].
> - El tensor que arregla el producto punto: [[Metrica/Tensor Metrico]].
> - La base dual que cierra la construcción: [[Metrica/Base Dual Reciproca]].

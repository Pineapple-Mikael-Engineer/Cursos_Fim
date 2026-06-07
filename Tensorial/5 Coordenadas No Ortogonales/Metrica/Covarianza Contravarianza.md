---
title: Covarianza y Contravarianza
tags:
  - analisis-tensorial
  - teoria
  - coordenadas-no-ortogonales
  - covarianza
draft: false
aliases:
  - covarianza contravarianza
  - componentes covariantes y contravariantes
  - componentes covariantes
  - componentes contravariantes
  - covariance and contravariance
---

# Covarianza y Contravarianza

> [!definicion]
> En un sistema inclinado, las componentes **originales** $A^i$ de $\vec A=A^i\hat g_i$ (proyección **paralela** a los ejes) son **contravariantes** (superíndice). A partir de ellas se definen las componentes **covariantes** $\tilde A_i$ (subíndice), que **absorben los términos cruzados** $\hat g_i\cdot\hat g_j$:
> $$\tilde A_i=A_j\,(\hat g_i\cdot\hat g_j)\qquad(\text{suma sobre }j).$$
> Con esta mezcla, el producto punto recupera su forma simple del caso ortonormal:
> $$\vec A\cdot\vec B=A^i\tilde B_i=\tilde A_iB^i.$$

> [!info]
> Sección 5.2.2 del libro, dentro de [[index | Métrica]]. Resuelve el problema planteado en [[../Sistema Inclinado | el sistema inclinado]]: el producto punto cargado de términos cruzados. La otra vía equivalente es el [[Tensor Metrico | tensor métrico]] $M_{ij}$ —de hecho $\tilde A_i=A_j(\hat g_i\cdot\hat g_j)=M_{ij}A^j$—. La interpretación geométrica de $A_i$ como proyección sobre una base se completa en [[Base Dual Reciproca | la base dual]].
>
> ![[co_contravariante_proyecciones.svg|460]]
>
> Componentes contravariantes $v^i$ (proyección paralela a los ejes) y covariantes $v_i$ (proyección perpendicular) de un mismo vector en un sistema inclinado.

> [!warning] Ojo: las covariantes NO son componentes sobre la misma base
> Las componentes covariantes **no** reconstruyen el vector con la base original: $\vec B\neq\tilde B_1\hat g_1+\tilde B_2\hat g_2$. Son una herramienta de cálculo para el producto punto; para que $v_i$ sea una componente legítima hace falta la [[Base Dual Reciproca | base dual]] $\hat g^i$, de modo que $\vec v=v_i\hat g^i$.

---

## Ejemplo

> [!ejemplo]
> **Base inclinada a $60^\circ$.** Sea una base unitaria con $\hat g'_1\cdot\hat g'_2=\cos 60^\circ=\tfrac12$. Tomemos $\vec A$ de componentes contravariantes $(A'^1,A'^2)=(3,2)$ y $\vec B$ de $(B'^1,B'^2)=(1,4)$.
>
> **Paso 1 — covariantes de $\vec B$** (ec. 5.25), con $\hat g'_1\cdot\hat g'_2=\tfrac12$:
> $$\tilde B'_1=B'^1+B'^2(\hat g'_1\cdot\hat g'_2)=1+4\cdot\tfrac12=3,$$
> $$\tilde B'_2=B'^1(\hat g'_1\cdot\hat g'_2)+B'^2=1\cdot\tfrac12+4=\tfrac92.$$
>
> **Paso 2 — producto punto mezclando** (ec. 5.27):
> $$\vec A\cdot\vec B=A'^i\tilde B'_i=A'^1\tilde B'_1+A'^2\tilde B'_2=3\cdot3+2\cdot\tfrac92=9+9=18.$$
>
> **Paso 3 — verificación directa** con los términos cruzados (ec. 5.23):
> $$\vec A\cdot\vec B=A'^1B'^1+A'^2B'^2+(A'^1B'^2+A'^2B'^1)(\hat g'_1\cdot\hat g'_2)=3+8+(12+2)\cdot\tfrac12=11+7=18.\ ✓$$
>
> Las dos cuentas coinciden: usar una componente covariante y una contravariante evita arrastrar el término cruzado a mano.

---

## En qué consiste

> [!teoria]
> El problema (ver [[../Sistema Inclinado]]) es que en la base inclinada el producto punto trae un término de más respecto al ortonormal:
> $$\vec A\cdot\vec B=A'^iB'^j(\hat g'_i\cdot\hat g'_j)=A'^1B'^1+A'^2B'^2+(A'^1B'^2+A'^2B'^1)(\hat g'_1\cdot\hat g'_2).$$
> La idea es **reagrupar** ese término dentro de las componentes de uno de los vectores y dejar la suma con la forma limpia $\sum_i A'^i(\cdots)_i$.

> [!teorema] El producto punto se reduce a $\vec A\cdot\vec B=A^i\tilde B_i$
> Definiendo las componentes covariantes de $\vec B$, el producto punto de un sistema inclinado adopta la misma forma que en el ortonormal, con una sola suma.

> [!demostracion]
> **Paso 1 — partir de la forma con términos cruzados** (en 2D, ec. 5.23):
> $$\vec A\cdot\vec B=A'^1B'^1+A'^2B'^2+(A'^1B'^2+A'^2B'^1)(\hat g'_1\cdot\hat g'_2).$$
>
> **Paso 2 — factorizar por las contravariantes de $\vec A$** (ec. 5.24):
> $$\vec A\cdot\vec B=A'^1\big(B'^1+B'^2(\hat g'_1\cdot\hat g'_2)\big)+A'^2\big(B'^1(\hat g'_1\cdot\hat g'_2)+B'^2\big).$$
>
> **Paso 3 — bautizar los paréntesis como covariantes de $\vec B$** (ec. 5.25):
> $$\tilde B'_1=B'^1+B'^2(\hat g'_1\cdot\hat g'_2),\qquad \tilde B'_2=B'^1(\hat g'_1\cdot\hat g'_2)+B'^2.$$
>
> **Paso 4 — leer el resultado** (ec. 5.27):
> $$\vec A\cdot\vec B=A'^1\tilde B'_1+A'^2\tilde B'_2=A'^i\tilde B'_i.$$
> Por simetría del producto punto, también puede absorberse el término cruzado en $\vec A$ (ec. 5.28–5.29), dando $\vec A\cdot\vec B=\tilde A'_iB'^i$. El producto interno **necesita** una mezcla de un índice covariante y uno contravariante, pero da igual cuál de los dos vectores se escriba en covariantes. $\blacksquare$

> [!proposicion] Forma general en $n$ dimensiones
> Levantando la restricción a 2D, las componentes covariantes se generan de las contravariantes con la expresión general (ec. 5.30):
> $$\tilde A'_i=A'^j\,(\hat g'_i\cdot\hat g'_j),$$
> con convención de Einstein (suma sobre $j$; en $n$ dimensiones, $n$ términos). En un sistema **ortonormal** $\hat g'_i\cdot\hat g'_j=\delta_{ij}$, así que $\tilde A'_i=A'^i$: las componentes covariante y contravariante **coinciden**, y se recupera el producto punto estándar $A_iB_i$. Por eso esta notación es lo bastante general para abarcar también los sistemas cartesianos y curvilíneos previos.

## Resumen

> [!resumen]
> | Aspecto | Contravariante | Covariante |
> |---|---|---|
> | Notación | $A^i$ (superíndice) | $\tilde A_i$ (subíndice) |
> | Qué es | componente original (proyección paralela a los ejes) | combinación que absorbe los términos cruzados |
> | Definición | dada por $\vec A=A^i\hat g_i$ | $\tilde A_i=A^j(\hat g_i\cdot\hat g_j)$ |
> | Producto punto | \| $\vec A\cdot\vec B=A^i\tilde B_i=\tilde A_iB^i$ \| | (mezcla un índice arriba y uno abajo) |
> | Ortonormal | $\tilde A_i=A^i$ (coinciden) | se recupera $A_iB_i$ |

> [!corolario]
> Las componentes contravariantes son las "naturales" (proyección paralela a los ejes); las covariantes son una recombinación que esconde los productos cruzados $\hat g_i\cdot\hat g_j$ de la base. El producto interno es invariante porque empareja un índice arriba con uno abajo. Esa recombinación es exactamente la acción del [[Tensor Metrico | tensor métrico]], $\tilde A_i=M_{ij}A^j$.

> [!referencia]
> - El problema que motiva todo: [[../Sistema Inclinado]].
> - La métrica que ejecuta la conversión: [[Tensor Metrico]].
> - La base dual que da sentido geométrico a $v_i$: [[Base Dual Reciproca]].

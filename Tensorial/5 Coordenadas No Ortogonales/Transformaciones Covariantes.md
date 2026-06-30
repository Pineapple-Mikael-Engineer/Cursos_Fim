---
title: Transformaciones de Componentes Covariantes
order: 4
tags:
  - analisis-tensorial
  - teoria
  - coordenadas-no-ortogonales
  - covarianza
draft: false
aliases:
  - transformaciones covariantes
  - componentes covariantes
  - covariant transformation
---

# Transformaciones de Componentes Covariantes $B'_i=g^j{}_i B_j$

> [!definicion]
> Las componentes **covariantes** de un vector transforman al revés que las contravariantes: contraen el **primer** índice de la matriz.
> $$B'_i=g^j{}_i\,B_j,\qquad\qquad B_i=t^j{}_i\,B'_j,$$
> con $t^i{}_j=\partial x'^i/\partial x^j$ y $g^i{}_j=\partial x^i/\partial x'^j$, las mismas matrices de las [[Transformaciones Contravariantes | transformaciones contravariantes]]. La **base contravariante** $\hat g^i$ transforma como las componentes contravariantes: $\hat g'^i=t^i{}_j\,\hat g^j$.

> [!info]
> Es el cap. 5.2.5 del libro, dentro del [[index | capítulo 5]]. Es el reverso de las [[Transformaciones Contravariantes]] (cap. 5.2.3) y cierra el cuadro simétrico de reglas; usa el convenio de [[Notacion Subindices Superindices]] (cap. 5.2.4). Las componentes covariantes $B_i$ y la base dual $\hat g^i$ se definen en [[Metrica/index | la métrica]] (cap. 5.2.2), donde $B_i=M_{ij}B^j$.
>
> **Notación:** $t^i{}_j$ no primado→primado, $g^i{}_j$ primado→no primado, con $t^i{}_j g^j{}_k=\delta^i{}_k$. Las posiciones horizontales de los índices importan: en $g^j{}_i$ el sumado $j$ es **superíndice** y el libre $i$ **subíndice**.

---

## Ejemplo

> [!ejemplo]
> **Mismo sistema inclinado, componentes covariantes.** Retomamos la transformación de [[Transformaciones Contravariantes | la nota contravariante]]:
> $$[t]=\begin{pmatrix} 1 & -\tfrac{1}{\sqrt3}\\[2pt] 0 & \tfrac{2}{\sqrt3}\end{pmatrix},\qquad [g]=[t]^{-1}=\begin{pmatrix} 1 & \tfrac12\\[2pt] 0 & \tfrac{\sqrt3}{2}\end{pmatrix}.$$
> Sea un vector con componentes **covariantes** $B_1=2,\ B_2=\sqrt3$ en el sistema no primado. Transforman contrayendo el **primer** índice, $B'_i=g^j{}_i B_j$:
> $$B'_1=g^1{}_1 B_1+g^2{}_1 B_2=1\cdot2+0\cdot\sqrt3=2,$$
> $$B'_2=g^1{}_2 B_1+g^2{}_2 B_2=\tfrac12\cdot2+\tfrac{\sqrt3}{2}\cdot\sqrt3=1+\tfrac32=\tfrac52.$$
> **Contraste con las contravariantes:** allí se usaba $[t]$ y se contraía el **segundo** índice ($v'^i=t^i{}_j v^j$); aquí se usa $[g]$ y se contrae el **primero** ($B'_i=g^j{}_i B_j$). Las dos clases de componentes viajan con matrices distintas y por índices distintos.
>
> La inversa $B_i=t^j{}_i B'_j$ recupera el original: $B_1=1\cdot2+0\cdot\tfrac52=2$, $B_2=-\tfrac{1}{\sqrt3}\cdot2+\tfrac{2}{\sqrt3}\cdot\tfrac52=\tfrac{-2+5}{\sqrt3}=\sqrt3$. ✓

---

## En qué consiste

> [!teorema] Las componentes covariantes contraen el primer índice
> A partir de la invariancia del producto interno, $B_i=t^j{}_i\,B'_j$ (e inversa $B'_i=g^j{}_i\,B_j$).

> [!demostracion]
> **Paso 1 — el producto interno es invariante.** El producto punto es un escalar; escrito con una mezcla de componentes contravariantes y covariantes (regla de oro: un índice arriba, uno abajo),
> $$\vec A\cdot\vec B=A^i B_i=A'^j B'_j.$$
>
> **Paso 2 — usar la regla contravariante para $A$.** Las componentes contravariantes de $\vec A$ ya transforman según $A'^j=t^j{}_i\,A^i$. Sustituyendo en el lado primado,
> $$A^i B_i=A'^j B'_j=\big(t^j{}_i\,A^i\big)B'_j=A^i\,\big(t^j{}_i\,B'_j\big).$$
>
> **Paso 3 — válido para todo $\vec A$.** Como la igualdad $A^i B_i=A^i\,(t^j{}_i B'_j)$ vale para cualquier $A^i$, los coeficientes de cada $A^i$ coinciden:
> $$\boxed{\,B_i=t^j{}_i\,B'_j\,}.$$
>
> **Paso 4 — invertir.** Multiplicando por la inversa (o repitiendo con $A_i=g^j{}_i A'^j$) se obtiene la directa
> $$B'_i=g^j{}_i\,B_j.\qquad\blacksquare$$
> El índice sumado es el **primero** (superíndice) de la matriz, opuesto al de las componentes contravariantes, que contraen el **segundo**.

> [!proposicion] Contravariante vs covariante: qué índice se contrae
> | | Contrae el índice... | Directa | Inversa |
> |---|---|---|---|
> | Componente contravariante $v^i$ | **segundo** de $[t]$/$[g]$ | $v'^i=t^i{}_j\,v^j$ | $v^i=g^i{}_j\,v'^j$ |
> | Componente covariante $v_i$ | **primero** de $[t]$/$[g]$ | $v'_i=g^j{}_i\,v_j$ | $v_i=t^j{}_i\,v'_j$ |
>
> Es la asimetría clave del capítulo: superíndices y subíndices transforman con matrices recíprocas y por índices opuestos. Por eso $A^iB_i$ es invariante (los factores $t$ y $g$ se cancelan vía $t^i{}_j g^j{}_k=\delta^i{}_k$).

> [!proposicion] La base contravariante transforma como las componentes contravariantes
> La base dual $\hat g^i$ (definida por $\hat g_i\cdot\hat g^j=\delta_i{}^j$ en [[Metrica/Base Dual Reciproca | la base dual]]) transforma contrayendo el **segundo** índice, igual que $v^i$:
> $$\hat g'^i=t^i{}_j\,\hat g^j,\qquad\qquad \hat g^i=g^i{}_j\,\hat g'^j.$$
> Esto confirma la clasificación de $\hat g^i$ como **contravariante** (superíndice): su ley de transformación es idéntica a la de las componentes contravariantes, en contraste con la base $\hat g_i$, que es covariante.

> [!info] Las 8 relaciones (componentes y bases, co y contra)
> Cuadro simétrico completo del cap. 5. Cada columna es un sentido de la transformación.
>
> | Objeto | Carácter | No primado → primado | Primado → no primado |
> |---|---|---|---|
> | Componente $v^i$ | contravariante | $v'^i=t^i{}_j\,v^j$ | $v^i=g^i{}_j\,v'^j$ |
> | Componente $v_i$ | covariante | $v'_i=g^j{}_i\,v_j$ | $v_i=t^j{}_i\,v'_j$ |
> | Base $\hat g_i$ | covariante | $\hat g'_i=g^j{}_i\,\hat g_j$ | $\hat g_i=t^j{}_i\,\hat g'_j$ |
> | Base $\hat g^i$ | contravariante | $\hat g'^i=t^i{}_j\,\hat g^j$ | $\hat g^i=g^i{}_j\,\hat g'^j$ |
>
> **Patrón:** lo **contravariante** (superíndice: $v^i$, $\hat g^i$) usa $[t]$ de ida y contrae el segundo índice; lo **covariante** (subíndice: $v_i$, $\hat g_i$) usa $[g]$ de ida y contrae el primero. Componentes y base del mismo carácter transforman igual.

## Resumen

> [!resumen]
> | Aspecto | Componente covariante $v_i$ | Base contravariante $\hat g^i$ |
> |---|---|---|
> | Transforma | $v'_i=g^j{}_i\,v_j$ | $\hat g'^i=t^i{}_j\,\hat g^j$ |
> | Índice contraído | el **primero** de $[g]$ | el **segundo** de $[t]$ |
> | Inversa | $v_i=t^j{}_i\,v'_j$ | $\hat g^i=g^i{}_j\,\hat g'^j$ |
> | Carácter | covariante (subíndice) | contravariante (superíndice) |

> [!corolario]
> Las componentes covariantes transforman al revés de las contravariantes: contraen el **primer** índice de la matriz ($v'_i=g^j{}_i v_j$), mientras las contravariantes contraen el **segundo** ($v'^i=t^i{}_j v^j$). La base contravariante $\hat g^i$ acompaña a las componentes contravariantes. Esta dualidad exacta es lo que vuelve invariante al producto interno $A^iB_i$ y sostiene el convenio de [[Notacion Subindices Superindices | índices arriba/abajo]].

> [!referencia]
> - El reverso simétrico: [[Transformaciones Contravariantes]].
> - El convenio arriba/abajo: [[Notacion Subindices Superindices]].
> - Componentes covariantes y base dual: [[Metrica/index]].
> - Subir/bajar índices con la métrica: [[Metrica/Tensor Metrico]].

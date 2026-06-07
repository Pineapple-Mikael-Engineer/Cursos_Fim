---
title: Producto Cruz
tags:
  - analisis-tensorial
  - teoria
  - notacion-indices
  - producto-cruz
draft: false
aliases:
  - producto cruz
  - producto vectorial
  - cross product
  - vector product
---

# Producto Cruz $\vec{A}\times\vec{B}=\varepsilon_{ijk}A_iB_j\hat{e}_k$

> [!definicion]
> El **producto cruz** (o vectorial) de dos vectores es el **vector** $\vec{C}=\vec{A}\times\vec{B}$ con magnitud
> $$\lvert\vec{C}\rvert=\lvert\vec{A}\rvert\,\lvert\vec{B}\rvert\operatorname{sen}\theta,$$
> perpendicular al plano de $\vec{A}$ y $\vec{B}$, y sentido dado por la **regla de la mano derecha**. En forma determinante e índices,
> $$\vec{A}\times\vec{B}=\begin{vmatrix}\hat{e}_1&\hat{e}_2&\hat{e}_3\\A_1&A_2&A_3\\B_1&B_2&B_3\end{vmatrix}=\varepsilon_{ijk}A_iB_j\hat{e}_k.$$

> [!info]
> Es la mitad "cruz" de la operación 1.2.2 del libro, dentro de [[index | Operaciones Vectoriales]] del [[../index | capítulo 1]]. Introduce el [[Simbolos Especiales/Simbolo Levi-Civita | símbolo de Levi-Civita]] $\varepsilon_{ijk}$, que codifica la antisimetría del determinante. Su hermano escalar es el [[Producto Punto | producto punto]]; ambos se comparan en [[Productos Vectoriales]]. El doble producto cruz se delega a [[Simbolos Especiales/Identidad Epsilon-Delta]].

---

## Ejemplo

> [!ejemplo]
> **Producto cruz numérico.** Sean $\vec{A}=(1,0,0)=\hat{e}_1$ y $\vec{B}=(0,1,0)=\hat{e}_2$. Por la forma determinante,
> $$\vec{A}\times\vec{B}=\begin{vmatrix}\hat{e}_1&\hat{e}_2&\hat{e}_3\\1&0&0\\0&1&0\end{vmatrix}=(0\cdot0-0\cdot1)\hat{e}_1+(0\cdot0-1\cdot0)\hat{e}_2+(1\cdot1-0\cdot0)\hat{e}_3=\hat{e}_3.$$
> En índices, $\vec{A}\times\vec{B}=\varepsilon_{ijk}A_iB_j\hat{e}_k$; el único par con $A_iB_j\neq0$ es $i=1,j=2$, que aporta $\varepsilon_{12k}\hat{e}_k=\varepsilon_{123}\hat{e}_3=\hat{e}_3$. Recuperamos la regla básica de la base derecha:
> $$\hat{e}_1\times\hat{e}_2=\hat{e}_3,\qquad \hat{e}_2\times\hat{e}_3=\hat{e}_1,\qquad \hat{e}_3\times\hat{e}_1=\hat{e}_2.$$

> [!ejemplo]
> **Cruz general y perpendicularidad.** Para $\vec{A}=(2,1,0)$ y $\vec{B}=(0,3,1)$:
> $$\vec{A}\times\vec{B}=\begin{vmatrix}\hat{e}_1&\hat{e}_2&\hat{e}_3\\2&1&0\\0&3&1\end{vmatrix}=(1\cdot1-0\cdot3)\hat{e}_1+(0\cdot0-2\cdot1)\hat{e}_2+(2\cdot3-1\cdot0)\hat{e}_3=\hat{e}_1-2\hat{e}_2+6\hat{e}_3.$$
> Comprobación de perpendicularidad: $\vec{C}\cdot\vec{A}=1\cdot2+(-2)\cdot1+6\cdot0=0$ y $\vec{C}\cdot\vec{B}=1\cdot0+(-2)\cdot3+6\cdot1=0$. Luego $\vec{C}\perp\vec{A}$ y $\vec{C}\perp\vec{B}$, como debe.

> [!ejemplo]
> **Área de un paralelogramo.** El paralelogramo de lados $\vec{A}=(3,0,0)$ y $\vec{B}=(1,2,0)$ tiene área $\lvert\vec{A}\times\vec{B}\rvert$:
> $$\vec{A}\times\vec{B}=\begin{vmatrix}\hat{e}_1&\hat{e}_2&\hat{e}_3\\3&0&0\\1&2&0\end{vmatrix}=(0-0)\hat{e}_1+(0-0)\hat{e}_2+(6-0)\hat{e}_3=6\,\hat{e}_3,$$
> de área $\lvert\vec{A}\times\vec{B}\rvert=6$. Coincide con base $\times$ altura: base $\lvert\vec{A}\rvert=3$ por altura $2$ (la componente de $\vec{B}$ perpendicular a $\vec{A}$).
>
> ![[regla_mano_derecha.svg]]

---

## En qué consiste

> [!teoria]
> El producto cruz $\vec{C}=\vec{A}\times\vec{B}$ es un vector de magnitud $\lvert\vec{C}\rvert=\lvert\vec{A}\rvert\lvert\vec{B}\rvert\operatorname{sen}\theta$ (el **área del paralelogramo** de lados $\vec{A}$ y $\vec{B}$), perpendicular al plano que ambos generan, con sentido dado por la **regla de la mano derecha**: dedos de $\vec{A}$ girando hacia $\vec{B}$, el pulgar marca $\vec{C}$. Por depender de la mano del sistema (cambia de signo al pasar a coordenadas izquierdas), $\vec{C}$ es en rigor un **pseudovector**; aquí, restringidos a sistemas derechos, se trata como vector ordinario.

> [!teorema] Producto cruz: determinante e índices
> $$\vec{A}\times\vec{B}=\begin{vmatrix}\hat{e}_1&\hat{e}_2&\hat{e}_3\\A_1&A_2&A_3\\B_1&B_2&B_3\end{vmatrix}=\varepsilon_{ijk}A_iB_j\hat{e}_k,\qquad (\vec{A}\times\vec{B})_k=\varepsilon_{ijk}A_iB_j.$$

> [!demostracion]
> **Paso 1 — Expandir el determinante** por la primera fila (cofactores):
> $$\vec{A}\times\vec{B}=\hat{e}_1\begin{vmatrix}A_2&A_3\\B_2&B_3\end{vmatrix}-\hat{e}_2\begin{vmatrix}A_1&A_3\\B_1&B_3\end{vmatrix}+\hat{e}_3\begin{vmatrix}A_1&A_2\\B_1&B_2\end{vmatrix},$$
> es decir
> $$\vec{A}\times\vec{B}=(A_2B_3-A_3B_2)\hat{e}_1+(A_3B_1-A_1B_3)\hat{e}_2+(A_1B_2-A_2B_1)\hat{e}_3.$$
>
> **Paso 2 — Leer cada componente como suma antisimétrica.** Cada paréntesis es una resta de productos $A_iB_j$ con índices intercambiados; ese patrón es exactamente el del símbolo de Levi-Civita $\varepsilon_{ijk}$ ($+1$ permutación par de $(1,2,3)$, $-1$ impar, $0$ con índice repetido). Por ejemplo, la componente $\hat{e}_3$:
> $$(\vec{A}\times\vec{B})_3=A_1B_2-A_2B_1=\varepsilon_{123}A_1B_2+\varepsilon_{213}A_2B_1=\varepsilon_{ij3}A_iB_j.$$
>
> **Paso 3 — Reunir las tres componentes.** Lo mismo vale para $k=1$ y $k=2$, de modo que $(\vec{A}\times\vec{B})_k=\varepsilon_{ijk}A_iB_j$. Multiplicando por $\hat{e}_k$ y sumando sobre $k$:
> $$\vec{A}\times\vec{B}=\varepsilon_{ijk}A_iB_j\hat{e}_k,$$
> con suma sobre $i,j,k$. El determinante y la forma índice son la misma expresión; $\varepsilon_{ijk}$ es la "máquina de cofactores". $\blacksquare$

> [!proposicion] Propiedades
> | Propiedad | Expresión |
> |---|---|
> | Anticonmutativa | $\vec{A}\times\vec{B}=-\,\vec{B}\times\vec{A}$ |
> | Vector consigo mismo | $\vec{A}\times\vec{A}=0$ |
> | Distributiva | $\vec{A}\times(\vec{B}+\vec{C})=\vec{A}\times\vec{B}+\vec{A}\times\vec{C}$ |
> | Magnitud | $\lvert\vec{A}\times\vec{B}\rvert=\lvert\vec{A}\rvert\lvert\vec{B}\rvert\operatorname{sen}\theta=$ área del paralelogramo |
> | Paralelos $\Leftrightarrow$ | $\vec{A}\times\vec{B}=0$ (con $\vec{A},\vec{B}\neq0$) |
>
> La anticonmutatividad sale directa de la antisimetría de $\varepsilon_{ijk}$: $(\vec{A}\times\vec{B})_k=\varepsilon_{ijk}A_iB_j=-\varepsilon_{jik}A_iB_j=-(\vec{B}\times\vec{A})_k$ (renombrando los mudos $i\leftrightarrow j$). Como corolario, $\vec{A}\times\vec{A}=-\vec{A}\times\vec{A}\Rightarrow\vec{A}\times\vec{A}=0$.

> [!info] Apariciones físicas
> El producto cruz aparece allí donde hay un eje perpendicular a un plano de acción. El **torque** de una fuerza $\vec{F}$ aplicada en $\vec{r}$ es
> $$\vec{\tau}=\vec{r}\times\vec{F},$$
> y la **fuerza de Lorentz** sobre una carga $q$ con velocidad $\vec{v}$ en un campo $\vec{B}$ es
> $$\vec{F}=\frac{q}{c}\,\vec{v}\times\vec{B}.$$
> En ambos el resultado es perpendicular a las causas, y su carácter de pseudovector refleja que dependen de la orientación del sistema.

> [!info] Doble producto cruz
> El producto cruz no es asociativo; el **doble producto cruz** $\vec{A}\times(\vec{B}\times\vec{C})$ se reduce a productos punto mediante la identidad $\varepsilon$-$\delta$, dando la regla BAC-CAB
> $$\vec{A}\times(\vec{B}\times\vec{C})=(\vec{A}\cdot\vec{C})\,\vec{B}-(\vec{A}\cdot\vec{B})\,\vec{C}.$$
> La derivación completa se delega a [[Simbolos Especiales/Identidad Epsilon-Delta]].

## Resumen

> [!resumen]
> | Aspecto | Expresión |
> |---|---|
> | Definición geométrica | $\lvert\vec{A}\times\vec{B}\rvert=\lvert\vec{A}\rvert\lvert\vec{B}\rvert\operatorname{sen}\theta$, mano derecha |
> | Forma determinante | $\begin{vmatrix}\hat{e}_1&\hat{e}_2&\hat{e}_3\\A_1&A_2&A_3\\B_1&B_2&B_3\end{vmatrix}$ |
> | Forma en índices | $(\vec{A}\times\vec{B})_k=\varepsilon_{ijk}A_iB_j$ |
> | Tipo de resultado | (pseudo)vector $\perp$ al plano |
> | Anticonmutativa | $\vec{A}\times\vec{B}=-\vec{B}\times\vec{A}$ |
> | Nulo $\Leftrightarrow$ | $\vec{A}\parallel\vec{B}$ |
> | Casos físicos | torque $\vec{\tau}=\vec{r}\times\vec{F}$, Lorentz $\vec{v}\times\vec{B}$ |

> [!corolario]
> El producto cruz codifica la antisimetría del determinante en el símbolo $\varepsilon_{ijk}$: su componente $k$ es $\varepsilon_{ijk}A_iB_j$. De ahí salen anticonmutatividad, $\vec{A}\times\vec{A}=0$ y el área del paralelogramo, sin trigonometría. Junto a la delta del producto punto, $\varepsilon_{ijk}$ es la única herramienta nueva que el cálculo vectorial necesita.

> [!referencia]
> - Símbolo de Levi-Civita y permutaciones: [[Simbolos Especiales/Simbolo Levi-Civita]].
> - Operación hermana (escalar): [[Producto Punto]].
> - Comparativa punto vs cruz: [[Productos Vectoriales]].
> - Doble producto cruz (BAC-CAB) e identidad $\varepsilon$-$\delta$: [[Simbolos Especiales/Identidad Epsilon-Delta]].

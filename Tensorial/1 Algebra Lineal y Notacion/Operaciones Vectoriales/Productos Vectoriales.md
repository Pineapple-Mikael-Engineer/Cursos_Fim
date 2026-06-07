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
  - producto punto
  - producto cruz
  - dot product
  - cross product
---

# Productos Vectoriales

> [!definicion]
> El **producto punto** de dos vectores es un escalar; en cartesianas, usando $\hat{e}_i\cdot\hat{e}_j=\delta_{ij}$,
> $$\vec{A}\cdot\vec{B}=\lvert\vec{A}\rvert\lvert\vec{B}\rvert\cos\theta=A_iB_j\,\delta_{ij}=A_iB_i,\qquad \vec{A}\cdot\vec{A}=\lvert\vec{A}\rvert^2.$$
> El **producto cruz** es un vector $\vec{C}=\vec{A}\times\vec{B}$ con $\lvert\vec{C}\rvert=\lvert\vec{A}\rvert\lvert\vec{B}\rvert\operatorname{sen}\theta$ y dirección por la regla de la mano derecha; en índices,
> $$\vec{A}\times\vec{B}=\varepsilon_{ijk}A_iB_j\hat{e}_k.$$

> [!info]
> Es la operación 1.2.2 del libro, dentro de [[index | Operaciones Vectoriales]] del [[../index | capítulo 1]]. El punto introduce la [[Simbolos Especiales/Delta Kronecker | delta de Kronecker]] $\delta_{ij}$ y la cruz el [[Simbolos Especiales/Simbolo Levi-Civita | símbolo de Levi-Civita]] $\varepsilon_{ijk}$; los detalles de ambos símbolos se delegan a [[Simbolos Especiales/index | Símbolos Especiales]]. Su uso combinado para derivar identidades se ve en [[Calculos con Notacion Einstein]].

---

## Ejemplo

> [!ejemplo]
> **Producto punto numérico.** Sean $\vec{A}=(1,2,3)$ y $\vec{B}=(4,5,6)$. Usando $\vec{A}\cdot\vec{B}=A_iB_i$ (suma sobre $i=1,2,3$):
> $$\vec{A}\cdot\vec{B}=A_1B_1+A_2B_2+A_3B_3=1\cdot4+2\cdot5+3\cdot6=4+10+18=32.$$
> Como caso particular, $\vec{A}\cdot\vec{A}=1+4+9=14=\lvert\vec{A}\rvert^2$, de modo que $\lvert\vec{A}\rvert=\sqrt{14}$.

> [!ejemplo]
> **Producto cruz numérico.** Sean $\vec{A}=(1,0,0)=\hat{e}_1$ y $\vec{B}=(0,1,0)=\hat{e}_2$. Por la forma determinante,
> $$\vec{A}\times\vec{B}=\begin{vmatrix}\hat{e}_1&\hat{e}_2&\hat{e}_3\\1&0&0\\0&1&0\end{vmatrix}=(0\cdot0-0\cdot1)\hat{e}_1+(0\cdot0-1\cdot0)\hat{e}_2+(1\cdot1-0\cdot0)\hat{e}_3=\hat{e}_3.$$
> En índices, $\vec{A}\times\vec{B}=\varepsilon_{ijk}A_iB_j\hat{e}_k$; el único par con $A_iB_j\neq0$ es $i=1,j=2$, que aporta $\varepsilon_{12k}\hat{e}_k=\varepsilon_{123}\hat{e}_3=\hat{e}_3$. Resultado: $\vec{C}=\hat{e}_3$, perpendicular a $\vec{A}$ y $\vec{B}$, consistente con la regla de la mano derecha ($\hat{e}_1\times\hat{e}_2=\hat{e}_3$).

> [!ejemplo]
> **Cruz general.** Para $\vec{A}=(2,1,0)$ y $\vec{B}=(0,3,1)$:
> $$\vec{A}\times\vec{B}=\begin{vmatrix}\hat{e}_1&\hat{e}_2&\hat{e}_3\\2&1&0\\0&3&1\end{vmatrix}=(1\cdot1-0\cdot3)\hat{e}_1+(0\cdot0-2\cdot1)\hat{e}_2+(2\cdot3-1\cdot0)\hat{e}_3=\hat{e}_1-2\hat{e}_2+6\hat{e}_3.$$
> Comprobación de perpendicularidad: $\vec{C}\cdot\vec{A}=1\cdot2+(-2)\cdot1+6\cdot0=0$ y $\vec{C}\cdot\vec{B}=1\cdot0+(-2)\cdot3+6\cdot1=0$. $\vec{C}\perp\vec{A},\vec{B}$.

---

## En qué consiste

> [!teoria] Producto punto
> El producto punto entre $\vec{A}$ y $\vec{B}$ es el escalar $\vec{A}\cdot\vec{B}=\lvert\vec{A}\rvert\lvert\vec{B}\rvert\cos\theta$, con $\theta$ el ángulo entre ambos. Con $\vec{A}\cdot\vec{A}$ se recupera la magnitud al cuadrado, $\vec{A}\cdot\vec{A}=\lvert\vec{A}\rvert^2$.

> [!teorema] Producto punto en índices
> $$\vec{A}\cdot\vec{B}=A_iB_i.$$

> [!demostracion]
> **Paso 1 — Expandir en componentes.** Escribiendo $\vec{A}=A_i\hat{e}_i$ y $\vec{B}=B_j\hat{e}_j$ (índices **distintos** para mantener las sumas independientes):
> $$\vec{A}\cdot\vec{B}=A_i\hat{e}_i\cdot B_j\hat{e}_j=A_iB_j\,(\hat{e}_i\cdot\hat{e}_j).$$
>
> **Paso 2 — Ortonormalidad de la base.** En cartesianas los vectores base son ortonormales, lo que se codifica con la delta de Kronecker:
> $$\hat{e}_i\cdot\hat{e}_j=\delta_{ij}=\begin{cases}1&i=j\\0&i\neq j\end{cases}\;\Longrightarrow\;\vec{A}\cdot\vec{B}=A_iB_j\,\delta_{ij}.$$
>
> **Paso 3 — Contraer la delta.** $\delta_{ij}$ anula todo término con $i\neq j$ y sustituye un índice por el otro ($A_iB_j\delta_{ij}=A_iB_i$):
> $$\vec{A}\cdot\vec{B}=A_iB_j\delta_{ij}=A_1B_1+A_2B_2+A_3B_3=A_iB_i.\qquad\blacksquare$$

> [!teoria] Producto cruz
> El producto cruz $\vec{C}=\vec{A}\times\vec{B}$ es un vector de magnitud $\lvert\vec{C}\rvert=\lvert\vec{A}\rvert\lvert\vec{B}\rvert\operatorname{sen}\theta$ (el área del paralelogramo), perpendicular al plano de $\vec{A}$ y $\vec{B}$, con sentido dado por la **regla de la mano derecha**: dedos de $\vec{A}$ hacia $\vec{B}$, el pulgar marca $\vec{C}$. Por depender de la mano del sistema, $\vec{C}$ es en rigor un **pseudovector**; aquí, restringidos a sistemas derechos, se trata como vector ordinario.

> [!teorema] Producto cruz: determinante e índices
> $$\vec{A}\times\vec{B}=\begin{vmatrix}\hat{e}_1&\hat{e}_2&\hat{e}_3\\A_1&A_2&A_3\\B_1&B_2&B_3\end{vmatrix}=\varepsilon_{ijk}A_iB_j\hat{e}_k.$$

> [!demostracion]
> **Paso 1 — Expandir el determinante** por la primera fila:
> $$\vec{A}\times\vec{B}=(A_2B_3-A_3B_2)\hat{e}_1+(A_3B_1-A_1B_3)\hat{e}_2+(A_1B_2-A_2B_1)\hat{e}_3.$$
>
> **Paso 2 — Reconocer el patrón antisimétrico.** Cada componente $k$ es $\sum_{i,j}\varepsilon_{ijk}A_iB_j$ con $\varepsilon_{ijk}$ el símbolo de Levi-Civita ($+1$ permutación par de $(1,2,3)$, $-1$ impar, $0$ si se repite un índice). Por ejemplo, la componente $\hat{e}_3$ recoge $\varepsilon_{123}A_1B_2+\varepsilon_{213}A_2B_1=A_1B_2-A_2B_1$. Reuniendo las tres:
> $$\vec{A}\times\vec{B}=\varepsilon_{ijk}A_iB_j\hat{e}_k,$$
> con suma sobre $i,j,k$. La componente $k$-ésima es $(\vec{A}\times\vec{B})_k=\varepsilon_{ijk}A_iB_j$. $\blacksquare$

> [!info] Apariciones físicas
> Ambos productos son omnipresentes en física. El **trabajo** de una fuerza $\vec{F}$ sobre un desplazamiento es la integral de línea del producto punto,
> $$W=\int d\vec{r}\cdot\vec{F},$$
> y la **fuerza de Lorentz** sobre una carga $q$ con velocidad $\vec{v}$ en un campo $\vec{B}$ es un producto cruz,
> $$\vec{F}=\frac{q}{c}\,\vec{v}\times\vec{B}.$$

## Resumen

> [!resumen]
> | Producto | Definición geométrica | Forma en índices | Tipo |
> |---|---|---|---|
> | Punto | $\lvert\vec{A}\rvert\lvert\vec{B}\rvert\cos\theta$ | $A_iB_j\delta_{ij}=A_iB_i$ | escalar |
> | $\vec{A}\cdot\vec{A}$ | $\lvert\vec{A}\rvert^2$ | $A_iA_i$ | escalar |
> | Cruz | $\lvert\vec{A}\rvert\lvert\vec{B}\rvert\operatorname{sen}\theta$, mano derecha | $\varepsilon_{ijk}A_iB_j\hat{e}_k$ | (pseudo)vector |

> [!corolario]
> El producto punto colapsa por $\hat{e}_i\cdot\hat{e}_j=\delta_{ij}$ a una suma simple $A_iB_i$; el cruz codifica la antisimetría del determinante en $\varepsilon_{ijk}$. Estos dos símbolos —$\delta$ y $\varepsilon$— son las únicas herramientas nuevas que el capítulo necesita: con ellas, cualquier identidad vectorial se deriva mecánicamente, como se ve en [[Calculos con Notacion Einstein]].

> [!referencia]
> - Delta de Kronecker y su contracción: [[Simbolos Especiales/Delta Kronecker]].
> - Símbolo de Levi-Civita y permutaciones: [[Simbolos Especiales/Simbolo Levi-Civita]].
> - Identidad $\varepsilon$-$\delta$ para combinar dos cruces: [[Simbolos Especiales/Identidad Epsilon-Delta]].
> - Derivaciones que usan ambos productos: [[Calculos con Notacion Einstein]].

---
title: Símbolo de Levi-Civita
order: 2
tags:
  - analisis-tensorial
  - teoria
  - notacion-indices
  - levi-civita
draft: false
aliases:
  - simbolo de levi-civita
  - epsilon de permutacion
  - simbolo de permutacion
  - Levi-Civita symbol
  - permutation symbol
---

# Símbolo de Levi-Civita $\varepsilon_{ijk}$

> [!definicion]
> El **símbolo de Levi-Civita** $\varepsilon_{ijk}$ vale, según la permutación de sus índices respecto de $(1,2,3)$:
> $$\varepsilon_{ijk}=\begin{cases}+1 & (i,j,k)\ \text{permutación \textbf{par} de }(1,2,3)\\[2pt] -1 & (i,j,k)\ \text{permutación \textbf{impar}}\\[2pt] 0 & \text{algún índice repetido}\end{cases}$$
> Es **totalmente antisimétrico**: intercambiar dos índices cambia el signo. Codifica el producto cruz: $(\vec{A}\times\vec{B})_i=\varepsilon_{ijk}A_jB_k$.

> [!info]
> Vive en [[index | Símbolos Especiales]] del [[../index | capítulo 1]] (libro, cap. 1.2.2). Usa la [[Notacion Indices Sumatorias | notación de Einstein]]. Su pareja en el producto punto es [[Delta Kronecker]]; el producto $\varepsilon_{ijk}\varepsilon_{mnk}$ se reduce a deltas en [[Identidad Epsilon-Delta]].

> [!info] Arreglo $3\times3\times3$
> ![[levi_civita_3d.svg|330]]
>
> $\varepsilon_{ijk}$ visto como un arreglo $3\times3\times3$; cada celda es $+1$, $-1$ o $0$ según la permutación de $(i,j,k)$.

---

## Ejemplo

> [!ejemplo]
> **Una componente de un producto cruz.** Calcular la componente $1$ de $\vec{A}\times\vec{B}$ con $\vec{A}=(2,0,1)$ y $\vec{B}=(0,3,1)$, usando $(\vec{A}\times\vec{B})_i=\varepsilon_{ijk}A_jB_k$ con $i=1$:
> $$(\vec{A}\times\vec{B})_1=\varepsilon_{1jk}A_jB_k.$$
> Solo dos términos de $\varepsilon_{1jk}$ son no nulos: $\varepsilon_{123}=+1$ (par) y $\varepsilon_{132}=-1$ (impar). Entonces
> $$(\vec{A}\times\vec{B})_1=\varepsilon_{123}A_2B_3+\varepsilon_{132}A_3B_2=A_2B_3-A_3B_2=(0)(1)-(1)(3)=-3.$$
> Coincide con la fórmula clásica $A_2B_3-A_3B_2$: el símbolo $\varepsilon_{ijk}$ **es** la regla del determinante, índice a índice.

> [!ejemplo]
> **Lectura de signos por permutación.** Evaluar cada caso clasificando la permutación de $(1,2,3)$:
> $$\varepsilon_{231}=+1\ (\text{par, cíclica}),\quad \varepsilon_{321}=-1\ (\text{impar}),\quad \varepsilon_{223}=0\ (\text{índice repetido}).$$
> Las permutaciones **pares** (positivas) son $(1,2,3),(2,3,1),(3,1,2)$ —las cíclicas— y las **impares** (negativas) $(2,1,3),(1,3,2),(3,2,1)$. De los $3^3=27$ valores, solo $6$ son no nulos.

---

## En qué consiste

> [!teoria]
> El producto cruz de la base cartesiana es $\hat{e}_i\times\hat{e}_j=\varepsilon_{ijk}\hat{e}_k$ (con suma sobre $k$). Sustituyendo en $\vec{A}\times\vec{B}=A_iB_j(\hat{e}_i\times\hat{e}_j)$:
> $$\vec{A}\times\vec{B}=\varepsilon_{ijk}A_iB_j\,\hat{e}_k,\qquad (\vec{A}\times\vec{B})_k=\varepsilon_{kij}A_iB_j.$$
> Visto como arreglo, $\varepsilon_{ijk}$ es un cubo $3\times3\times3$ con solo $6$ entradas no nulas ($\pm1$) sobre las permutaciones de $(1,2,3)$; el resto es cero. Es la versión por índices de la regla del determinante para el producto cruz.

> [!info] Forma determinante
> El producto cruz como determinante simbólico equivale al símbolo:
> $$\vec{A}\times\vec{B}=\begin{vmatrix}\hat{e}_1 & \hat{e}_2 & \hat{e}_3\\ A_1 & A_2 & A_3\\ B_1 & B_2 & B_3\end{vmatrix}=\varepsilon_{ijk}A_jB_k\,\hat{e}_i.$$
> La expansión del determinante reproduce exactamente los $6$ términos con signo de $\varepsilon_{ijk}$.

> [!teorema] Antisimetría
> El símbolo cambia de signo al intercambiar dos índices y se conserva bajo permutación **cíclica**:
> $$\varepsilon_{ijk}=-\varepsilon_{ikj}=-\varepsilon_{jik}=-\varepsilon_{kji},\qquad \varepsilon_{ijk}=\varepsilon_{jki}=\varepsilon_{kij}.$$

> [!demostracion]
> **Antisimetría y anulación.** *Paso 1 (intercambio).* Un intercambio de dos índices transforma una permutación par en impar y viceversa; por definición eso invierte el signo: $\varepsilon_{ijk}=-\varepsilon_{ikj}$. *Paso 2 (ciclo = dos intercambios).* Una permutación cíclica $ijk\to jki$ son dos intercambios sucesivos, $(-1)^2=+1$, así que conserva el signo: $\varepsilon_{ijk}=\varepsilon_{jki}$. *Paso 3 (índice repetido).* Si dos índices son iguales, p. ej. $i=j$, intercambiarlos no cambia el arreglo pero debe invertir el signo: $\varepsilon_{iik}=-\varepsilon_{iik}$, luego $\varepsilon_{iik}=0$. Por eso solo las permutaciones sin repetición son no nulas.

## Resumen

> [!resumen]
> | Aspecto | Valor / fórmula |
> |---|---|
> | Permutación par | $\varepsilon_{123}=\varepsilon_{231}=\varepsilon_{312}=+1$ |
> | Permutación impar | $\varepsilon_{213}=\varepsilon_{132}=\varepsilon_{321}=-1$ |
> | Índice repetido | $\varepsilon_{iik}=0$ |
> | Antisimetría | $\varepsilon_{ijk}=-\varepsilon_{ikj}$ |
> | Ciclo | $\varepsilon_{ijk}=\varepsilon_{jki}=\varepsilon_{kij}$ |
> | Producto cruz | $(\vec{A}\times\vec{B})_i=\varepsilon_{ijk}A_jB_k$ |

> [!corolario]
> $\varepsilon_{ijk}$ es la forma indexada del producto cruz y del determinante: $6$ entradas $\pm1$ que llevan toda la combinatoria de signos. Su antisimetría es lo que distingue al cruz del punto, y al combinarlo consigo mismo aparece la [[Identidad Epsilon-Delta | identidad $\varepsilon$-$\delta$]], puente hacia las identidades vectoriales.

> [!referencia]
> - Símbolo dual (producto punto): [[Delta Kronecker]].
> - Reducción $\varepsilon\varepsilon\to\delta\delta$: [[Identidad Epsilon-Delta]].
> - Aplicación a productos: [[Operaciones Vectoriales/Productos Vectoriales]].

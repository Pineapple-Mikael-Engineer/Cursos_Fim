---
title: Tensor Metrico
order: 2
tags:
  - analisis-tensorial
  - teoria
  - coordenadas-no-ortogonales
  - covarianza
draft: false
aliases:
  - tensor metrico
  - metrica
  - matriz metrica
  - metric tensor
---

# Tensor Metrico $M_{ij}=\hat g_i\cdot\hat g_j$

> [!definicion]
> El **tensor métrico** de un sistema con base $\hat g_i$ es la matriz de productos punto de la base:
> $$M_{ij}=\hat g_i\cdot\hat g_j,$$
> **simétrico** ($M_{ij}=M_{ji}$). **Baja índices** —convierte contravariantes en covariantes dentro del mismo sistema— $v_i=M_{ij}v^j$, y reescribe el producto punto con componentes contravariantes:
> $$\vec A\cdot\vec B=A^iB^jM_{ij}=\tilde A_jB^j=A^i\tilde B_i.$$

> [!info]
> Sección 5.2.2 del libro, dentro de [[index | Métrica]]. Es la vía equivalente a la de [[Covarianza Contravarianza | covarianza/contravarianza]]: la métrica es justo la operación que define las componentes covariantes, $\tilde A_i=M_{ij}A^j$. La métrica está determinada **solo por la base** del sistema. Su inverso $M^{ij}$ y la base contravariante aparecen en [[Base Dual Reciproca | la base dual]].
>
> **Notación:** aquí $M_{ij}$ (libro); en otros textos y en Relatividad General es $g_{ij}$ — reservamos $g$ para la matriz de transformación $[g]$.

---

## Ejemplo

> [!ejemplo]
> **Métrica de una base inclinada a $60^\circ$.** Base unitaria con $\hat g'_1\cdot\hat g'_2=\cos 60^\circ=\tfrac12$.
>
> **Paso 1 — construir $M_{ij}$** (ec. 5.31), usando $\hat g'_i\cdot\hat g'_i=1$ y $\hat g'_1\cdot\hat g'_2=\tfrac12$:
> $$[M]=\begin{pmatrix}\hat g'_1\cdot\hat g'_1 & \hat g'_1\cdot\hat g'_2\\[2pt]\hat g'_2\cdot\hat g'_1 & \hat g'_2\cdot\hat g'_2\end{pmatrix}=\begin{pmatrix}1 & \tfrac12\\[2pt]\tfrac12 & 1\end{pmatrix}.$$
> Es simétrica, como debe ser.
>
> **Paso 2 — producto punto con la métrica** (ec. 5.34), para $\vec A=(A'^1,A'^2)=(3,2)$ y $\vec B=(B'^1,B'^2)=(1,4)$:
> $$\vec A\cdot\vec B=A'^iB'^jM_{ij}=A'^1B'^1\cdot1+A'^2B'^2\cdot1+(A'^1B'^2+A'^2B'^1)\cdot\tfrac12.$$
> $$=3\cdot1+8\cdot1+(12+2)\cdot\tfrac12=3+8+7=18.$$
>
> **Paso 3 — comprobar bajando un índice** (ec. 5.33): $\tilde A'_j=A'^iM_{ij}$ da $\tilde A'_1=3+2\cdot\tfrac12=4$, $\tilde A'_2=3\cdot\tfrac12+2=\tfrac72$; entonces $\vec A\cdot\vec B=\tilde A'_jB'^j=4\cdot1+\tfrac72\cdot4=4+14=18.\ ✓$ Coincide con el resultado obtenido en [[Covarianza Contravarianza | covarianza/contravarianza]].

---

## En qué consiste

> [!teoria]
> La métrica empaqueta de una vez todos los productos de la base, $\hat g_i\cdot\hat g_j$, que son justo los responsables de los términos cruzados del producto punto. Aplicada a las componentes contravariantes de un vector, las convierte en covariantes (**baja el índice**, ec. 5.33):
> $$\tilde A_i=M_{ij}A^j.$$
> Esta es la misma definición de componente covariante de [[Covarianza Contravarianza]], ahora en forma matricial.

> [!teorema] El producto punto es $\vec A\cdot\vec B=A^iB^jM_{ij}$ y se reduce al caso ortonormal
> Con componentes contravariantes para **ambos** vectores y la métrica, el producto interno tiene una sola expresión válida en cualquier sistema (ortonormal o inclinado).

> [!demostracion]
> **Paso 1 — escribir los vectores en la base** $\hat g_i$:
> $$\vec A=A^i\hat g_i,\qquad \vec B=B^j\hat g_j.$$
>
> **Paso 2 — multiplicar y usar bilinealidad del producto punto:**
> $$\vec A\cdot\vec B=(A^i\hat g_i)\cdot(B^j\hat g_j)=A^iB^j\,(\hat g_i\cdot\hat g_j).$$
>
> **Paso 3 — reconocer la métrica** (ec. 5.31), obteniendo la ec. 5.34:
> $$\vec A\cdot\vec B=A^iB^jM_{ij}.$$
> Sumando primero sobre $i$ aparece $\tilde A_jB^j$ (ec. 5.35); sumando primero sobre $j$, $A^i\tilde B_i$ (ec. 5.36): se reencuentran las formas de [[Covarianza Contravarianza]].
>
> **Paso 4 — caso ortonormal.** Si la base es ortonormal, $M_{ij}=\hat g_i\cdot\hat g_j=\delta_{ij}$, y
> $$\vec A\cdot\vec B=A^iB^j\delta_{ij}=A^iB^i=A_1B_1+A_2B_2,$$
> el producto interno estándar. La nueva fórmula **contiene** al caso ortonormal como un caso particular. $\blacksquare$

> [!proposicion] Simetría
> De la definición $M_{ij}=\hat g_i\cdot\hat g_j$ y la conmutatividad del producto punto se sigue de inmediato (ec. 5.32):
> $$M_{ij}=\hat g_i\cdot\hat g_j=\hat g_j\cdot\hat g_i=M_{ji}.$$
> La matriz $[M]$ es simétrica.

> [!info] La métrica es un tensor de rango 2
> $M_{ij}$ está determinada **solo por la base** del sistema. Este hecho —que sus componentes transforman como las de un tensor de rango dos— se prueba en [[../Covarianza Contravarianza en Tensores]]; por eso se le llama propiamente *tensor* métrico y no solo *matriz* métrica.

## Resumen

> [!resumen]
> | Aspecto | Expresión |
> |---|---|
> | Definición | $M_{ij}=\hat g_i\cdot\hat g_j$ |
> | Simetría | $M_{ij}=M_{ji}$ |
> | Baja índice | \| $v_i=M_{ij}v^j$ (contravariante $\to$ covariante) \| |
> | Producto punto | $\vec A\cdot\vec B=A^iB^jM_{ij}=\tilde A_jB^j=A^i\tilde B_i$ |
> | Ortonormal | $M_{ij}=\delta_{ij}\Rightarrow \vec A\cdot\vec B=A^iB^i$ |

> [!corolario]
> El tensor métrico es el resumen completo de la geometría de la base: con él, el producto punto de un sistema inclinado se escribe igual que el de uno ortonormal, $\vec A\cdot\vec B=A^iB^jM_{ij}$, y se obtienen las componentes covariantes bajando índices, $v_i=M_{ij}v^j$. Para **subir** índices se necesita su inverso $M^{ij}$, que vive en [[Base Dual Reciproca | la base dual]].

> [!referencia]
> - La vía equivalente vía componentes: [[Covarianza Contravarianza]].
> - El inverso $M^{ij}$ y la base contravariante: [[Base Dual Reciproca]].
> - Por qué es un tensor de rango 2: [[../Covarianza Contravarianza en Tensores]].

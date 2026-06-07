---
title: Base Dual o Reciproca
tags:
  - analisis-tensorial
  - teoria
  - coordenadas-no-ortogonales
  - covarianza
draft: false
aliases:
  - base dual
  - base reciproca
  - base contravariante
  - dual basis
  - reciprocal basis
---

# Base Dual o Reciproca $\hat g^i$

> [!definicion]
> La **base contravariante** o **dual** $\hat g^i$ (superíndice) se define por la condición de reciprocidad con la base covariante $\hat g_i$:
> $$\hat g_i\cdot\hat g^j=\delta_i{}^j.$$
> Permite escribir el mismo vector con las dos clases de componentes:
> $$\vec v=v^i\,\hat g_i=v_i\,\hat g^i.$$
> Con ella, la métrica de superíndices $M^{ij}=\hat g^i\cdot\hat g^j$ **sube índices**: $v^i=M^{ij}v_j$.

> [!info]
> Sección 5.2.5 del libro (parte de base dual), dentro de [[index | Métrica]]. Es la pieza que da sentido geométrico a las componentes [[Covarianza Contravarianza | covariantes]] $v_i$: son las componentes de $\vec v$ **sobre la base dual**. La $M^{ij}$ es la inversa de la $M_{ij}$ del [[Tensor Metrico | tensor métrico]] ($M^{ik}M_{kj}=\delta^i{}_j$).

---

## Ejemplo

> [!ejemplo]
> **Base dual de una base inclinada a $60^\circ$.** En coordenadas cartesianas auxiliares, sea $\hat g_1=(1,0)$ y $\hat g_2=(\cos 60^\circ,\operatorname{sen}60^\circ)=(\tfrac12,\tfrac{\sqrt3}{2})$; son unitarios y $\hat g_1\cdot\hat g_2=\tfrac12$.
>
> **Paso 1 — imponer reciprocidad para $\hat g^1$** (ec. 5.74): debe cumplir $\hat g_1\cdot\hat g^1=1$ y $\hat g_2\cdot\hat g^1=0$. Lo segundo dice que $\hat g^1\perp\hat g_2$; lo primero fija su escala. Resolviendo,
> $$\hat g^1=\big(1,\,-\tfrac{1}{\sqrt3}\big).$$
> Comprobación: $\hat g_1\cdot\hat g^1=1$ y $\hat g_2\cdot\hat g^1=\tfrac12\cdot1+\tfrac{\sqrt3}{2}\cdot(-\tfrac{1}{\sqrt3})=\tfrac12-\tfrac12=0.\ ✓$
>
> **Paso 2 — imponer reciprocidad para $\hat g^2$**: $\hat g_2\cdot\hat g^2=1$ y $\hat g_1\cdot\hat g^2=0$. Lo segundo da $\hat g^2\perp\hat g_1$ (eje vertical); lo primero la escala:
> $$\hat g^2=\big(0,\,\tfrac{2}{\sqrt3}\big).$$
> Comprobación: $\hat g_1\cdot\hat g^2=0$ y $\hat g_2\cdot\hat g^2=\tfrac{\sqrt3}{2}\cdot\tfrac{2}{\sqrt3}=1.\ ✓$
>
> **Paso 3 — métrica de superíndices** $M^{ij}=\hat g^i\cdot\hat g^j$ (sube índices):
> $$[M^{ij}]=\begin{pmatrix}\tfrac43 & -\tfrac23\\[2pt] -\tfrac23 & \tfrac43\end{pmatrix}=[M_{ij}]^{-1},$$
> inversa de $[M_{ij}]=\begin{pmatrix}1&\tfrac12\\\tfrac12&1\end{pmatrix}$ (det $=\tfrac34$). Nótese que la base dual **no** es unitaria: $\hat g^i\cdot\hat g^i\neq1$ en general.

---

## En qué consiste

> [!teoria]
> Las componentes covariantes $v_i$ ya simplificaban el producto punto, pero no eran componentes "sobre" ninguna base: $\vec v\neq v_i\hat g_i$. La base dual repara esto. Definida por $\hat g_i\cdot\hat g^j=\delta_i{}^j$, hace que las **covariantes sean componentes legítimas** sobre $\hat g^i$ (ec. 5.71–5.72):
> $$\vec v=v^i\hat g_i\quad(\text{contravariantes sobre }\hat g_i),\qquad \vec v=v_i\hat g^i\quad(\text{covariantes sobre }\hat g^i).$$

> [!teorema] La reciprocidad $\hat g_i\cdot\hat g^j=\delta_i{}^j$
> Exigir que el producto punto $\vec A\cdot\vec B$ se reduzca a $A^iB_i$ cuando $\vec A$ se escribe en la base covariante con componentes contravariantes y $\vec B$ en la base dual con componentes covariantes, **fuerza** $\hat g_i\cdot\hat g^j=\delta_i{}^j$.

> [!demostracion]
> **Paso 1 — escribir cada vector en su pareja base/componente** (ec. 5.73): $\vec A=A^i\hat g_i$ (contravariantes sobre la base covariante), $\vec B=B_j\hat g^j$ (covariantes sobre la base dual). Entonces
> $$\vec A\cdot\vec B=(A^i\hat g_i)\cdot(B_j\hat g^j)=A^iB_j\,(\hat g_i\cdot\hat g^j).$$
>
> **Paso 2 — igualar con la forma conocida.** De [[Covarianza Contravarianza]] el producto punto vale $\vec A\cdot\vec B=A^iB_i$. Comparando,
> $$A^iB_j\,(\hat g_i\cdot\hat g^j)=A^iB_i.$$
>
> **Paso 3 — arbitrariedad de $\vec A,\vec B$.** Como la igualdad vale para componentes $A^i,B_j$ arbitrarias, los coeficientes deben coincidir término a término. El lado derecho es $A^iB_i=A^iB_j\delta_i{}^j$, luego (ec. 5.74–5.75)
> $$\hat g_i\cdot\hat g^j=\delta_i{}^j.\qquad\blacksquare$$

> [!proposicion] Geometría en 2D
> La condición $\hat g_i\cdot\hat g^j=\delta_i{}^j$ determina la dirección y la magnitud de la dual a partir de la base covariante. En 2D: $\hat g^1\cdot\hat g_2=0$ y $\hat g^1\cdot\hat g_1=1$, es decir **$\hat g^1$ es perpendicular a $\hat g_2$** y su proyección sobre el eje 1 (paralelo a $\hat g_1$) vale exactamente $1$; análogamente $\hat g^2\perp\hat g_1$ con proyección unidad sobre el eje 2. Esto fija $\hat g^1,\hat g^2$ por completo.

> [!info] Subir índices con $M^{ij}$
> Definida la métrica de superíndices $M^{ij}=\hat g^i\cdot\hat g^j$, la operación inversa a bajar índices es **subir**:
> $$v^i=M^{ij}v_j,$$
> y $M^{ij}$ es la inversa matricial de la $M_{ij}$ del [[Tensor Metrico | tensor métrico]]: $M^{ik}M_{kj}=\delta^i{}_j$. Así $v^i=M^{ij}v_j=M^{ij}M_{jk}v^k=\delta^i{}_kv^k=v^i$, consistente.

## Resumen

> [!resumen]
> | Aspecto | Expresión |
> |---|---|
> | Definición | $\hat g_i\cdot\hat g^j=\delta_i{}^j$ |
> | Doble expansión | $\vec v=v^i\hat g_i=v_i\hat g^i$ |
> | Geometría (2D) | $\hat g^1\perp\hat g_2$, proyección unidad sobre el eje 1 |
> | Métrica superíndices | \| $M^{ij}=\hat g^i\cdot\hat g^j=[M_{ij}]^{-1}$ \| |
> | Sube índice | $v^i=M^{ij}v_j$ (covariante $\to$ contravariante) |

> [!corolario]
> La base dual cierra la construcción del capítulo: con $\hat g^i$ definida por $\hat g_i\cdot\hat g^j=\delta_i{}^j$, las componentes covariantes pasan de ser un truco de cálculo a componentes geométricas reales ($\vec v=v_i\hat g^i$), y su métrica $M^{ij}$ sube índices, completando el par bajar/subir con el [[Tensor Metrico | tensor métrico]].

> [!referencia]
> - Las componentes que esta base hace geométricas: [[Covarianza Contravarianza]].
> - La métrica $M_{ij}$ que $M^{ij}$ invierte: [[Tensor Metrico]].
> - Marco del capítulo: [[index | Métrica]].

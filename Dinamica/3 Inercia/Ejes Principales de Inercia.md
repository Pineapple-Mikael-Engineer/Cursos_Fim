---
title: Ejes Principales de Inercia
tags:
  - dinamica
  - teoria
  - inercia
draft: false
aliases:
  - ejes principales
  - momentos principales
  - momentos principales de inercia
  - diagonalización del tensor de inercia
  - principal axes
  - principal moments of inertia
---

# Ejes Principales de Inercia $\;\mathbf I\vec v=\lambda\vec v$

> [!definicion]
> Los **ejes principales de inercia** son las direcciones en que el [[Tensor de Inercia]] es
> **diagonal**, es decir, en que todos los **productos de inercia se anulan**. Se hallan resolviendo el
> **problema de autovalores**
> $$\mathbf I\,\vec v=\lambda\,\vec v:$$
> los autovalores $\lambda_i$ son los **momentos principales** $I_1,I_2,I_3$ y los autovectores
> asociados $\vec v_i$ son los **ejes principales** (forman una base **ortonormal**). En esos ejes
> $$\mathbf I=\mathrm{diag}(I_1,I_2,I_3),\qquad \vec H=(I_1\omega_1,\,I_2\omega_2,\,I_3\omega_3),$$
> y las [[Ecuaciones de Euler 3D]] se **separan** (cada componente con un único momento principal).

> [!info]
> Diagonalizar el [[Tensor de Inercia]] de la [[3 Inercia/index | inercia]] es el paso que simplifica
> toda la rotación del cuerpo rígido: anula el acoplamiento entre ejes y desenreda las
> [[Ecuaciones de Euler 3D]]. Referencia: Goldstein §5.4.

---

## Ejemplo

> [!ejemplo]
> **Diagonalizar el tensor de dos masas.**
>
> Del [[Tensor de Inercia]] de dos masas puntuales sale, respecto al origen,
> $$\mathbf I=ma^2\begin{pmatrix} 2 & -2 & 0\\ -2 & 2 & 0\\ 0 & 0 & 4\end{pmatrix}.$$
> Hallar sus momentos principales y ejes principales.
>
> El eje $z$ ya está desacoplado ($\lambda=4ma^2$). El bloque $2\times2$
> $\begin{pmatrix} 2 & -2\\ -2 & 2\end{pmatrix}$ tiene autovalores
> $$\lambda=2\pm2\quad\Rightarrow\quad \lambda=0\ \text{ y }\ \lambda=4,$$
> medidos en unidades de $ma^2$. Luego los **momentos principales** son
> $$I_1=0,\qquad I_2=4ma^2,\qquad I_3=4ma^2.$$
> Los **autovectores** del bloque son $(1,1,0)/\sqrt2$ para $\lambda=0$ (a lo largo de la recta que une
> las masas) y $(1,-1,0)/\sqrt2$ para $\lambda=4ma^2$ (perpendicular a ella).
>
> > [!solucion]
> > Los ejes principales son las **diagonales del cuadrado** (no los ejes $x,y$, donde el producto
> > $I_{xy}\neq0$). El momento principal **nulo**, $I_1=0$, corresponde al eje que **contiene** a las
> > masas: no hay masa fuera de él, así que nada se opone a rotar en torno a esa recta.

---

## En qué consiste

> [!teoria] Por qué siempre existen
> Hallar los ejes principales es **diagonalizar** una matriz simétrica. Como veremos, el teorema
> espectral garantiza que esto **siempre es posible** con una rotación: cualquier cuerpo, por irregular
> que sea, tiene en cada punto tres ejes principales ortogonales. La idea física: los productos de
> inercia miden el **acoplamiento** entre ejes; girando los ejes a la orientación adecuada ese
> acoplamiento se anula y el tensor queda diagonal.

> [!teorema] Teorema espectral aplicado a $\mathbf I$
> Como el tensor de inercia es **simétrico y real** ($I_{ij}=I_{ji}\in\mathbb R$):
> 1. sus autovalores $\lambda_i$ (los momentos principales) son **reales**, y
> 2. los autovectores correspondientes a autovalores distintos son **ortogonales**.
>
> En consecuencia $\mathbf I$ es **ortogonalmente diagonalizable**:
> $$\mathbf I=\mathbf R\,\mathbf I_{\text{diag}}\,\mathbf R^{T},\qquad \mathbf R^{T}\mathbf R=\mathbb 1,$$
> donde $\mathbf I_{\text{diag}}=\mathrm{diag}(I_1,I_2,I_3)$ y las **columnas de $\mathbf R$ son los ejes
> principales** $\vec v_i$.

> [!demostracion]
> **Paso 1 — Autovalores reales.** Sea $\mathbf I\vec v=\lambda\vec v$ con $\vec v\neq\vec0$, admitiendo
> en principio $\lambda\in\mathbb C$ y $\vec v\in\mathbb C^3$. Multiplicando por $\vec v^{*}$ (conjugado
> traspuesto) por la izquierda:
> $$\vec v^{*}\!\cdot\mathbf I\vec v=\lambda\,\vec v^{*}\!\cdot\vec v=\lambda\,\lVert\vec v\rVert^2 .$$
> El escalar $s=\vec v^{*}\!\cdot\mathbf I\vec v$ es **real**, porque como $\mathbf I$ es real y simétrica
> ($\mathbf I^{T}=\mathbf I$, $\mathbf I^{*}=\mathbf I$) coincide con su conjugado:
> $$s^{*}=(\vec v^{*}\mathbf I\vec v)^{*}=\vec v^{T}\mathbf I^{*}\vec v^{*}
> =\vec v^{T}\mathbf I\vec v^{*}=(\vec v^{*}\mathbf I^{T}\vec v)^{*\,*}=\vec v^{*}\mathbf I\vec v=s.$$
> Como $\lVert\vec v\rVert^2>0$ es real, $\lambda=s/\lVert\vec v\rVert^2$ es **real**. $\;\square$
>
> **Paso 2 — Autovectores ortogonales.** Sean $\mathbf I\vec v_1=\lambda_1\vec v_1$ y
> $\mathbf I\vec v_2=\lambda_2\vec v_2$ con $\lambda_1\neq\lambda_2$ (ya reales). Calculamos
> $\vec v_2\cdot\mathbf I\vec v_1$ de dos formas. Por un lado,
> $$\vec v_2\cdot\mathbf I\vec v_1=\vec v_2\cdot(\lambda_1\vec v_1)=\lambda_1\,\vec v_1\cdot\vec v_2 .$$
> Por otro, usando la **simetría** $\mathbf I^{T}=\mathbf I$ para pasar el operador al otro factor,
> $$\vec v_2\cdot\mathbf I\vec v_1=(\mathbf I\vec v_2)\cdot\vec v_1=(\lambda_2\vec v_2)\cdot\vec v_1
> =\lambda_2\,\vec v_1\cdot\vec v_2 .$$
> Restando ambas expresiones,
> $$(\lambda_1-\lambda_2)\,\vec v_1\cdot\vec v_2=0 .$$
> Como $\lambda_1\neq\lambda_2$, necesariamente $\vec v_1\cdot\vec v_2=0$, es decir
> $\vec v_1\perp\vec v_2$. (Si hay autovalores repetidos, su autoespacio tiene una base ortonormal por
> Gram–Schmidt.) Normalizando los $\vec v_i$ y colocándolos como columnas de $\mathbf R$ se obtiene
> $\mathbf R$ ortogonal con $\mathbf I=\mathbf R\,\mathbf I_{\text{diag}}\,\mathbf R^{T}$. $\;\blacksquare$

> [!proposicion] Atajo por simetría (sin resolver autovalores)
> No siempre hace falta diagonalizar:
> - Todo **eje de simetría** del cuerpo es un eje principal.
> - Todo eje **perpendicular a un plano de simetría** es un eje principal.
>
> Por eso en cuerpos con simetría (cilindros, esferas, placas, prismas) los ejes principales se leen
> **a simple vista** y los productos de inercia se anulan por paridad de la distribución de masa.

> [!warning]
> - Los ejes principales dependen del **punto** de referencia: los ejes principales en el centro de masa
>   **no coinciden** en general con los de otro punto (se relacionan vía el
>   [[Teorema del Eje Paralelo]]).
> - Un momento principal es **nulo** solo si **toda** la masa yace sobre ese eje (caso ideal, como en el
>   ejemplo); en un sólido real los tres $I_i>0$.
> - Que $\mathbf I$ sea diagonal en unos ejes **no** implica $I_1=I_2=I_3$: diagonal y degenerado son
>   cosas distintas (un cuerpo asimétrico tiene tres momentos principales diferentes).

## Resumen

> [!resumen]
> | Concepto | Expresión | Idea |
> |:---|:---|:---|
> | Problema de autovalores | $\mathbf I\vec v=\lambda\vec v$ | hallar ejes que diagonalizan |
> | Momentos principales | $\lambda_i=I_1,I_2,I_3$ | autovalores (reales, $\geq0$) |
> | Ejes principales | $\vec v_i$ ortonormales | autovectores |
> | Tensor diagonalizado | $\mathbf I=\mathbf R\,\mathbf I_{\text{diag}}\,\mathbf R^{T}$ | $\mathbf R$ ortogonal, columnas $=\vec v_i$ |
> | Atajo | eje de simetría $\Rightarrow$ principal | sin resolver autovalores |

> [!corolario]
> En ejes principales $\vec H=(I_1\omega_1,I_2\omega_2,I_3\omega_3)$ y
> $T_{rot}=\tfrac12(I_1\omega_1^2+I_2\omega_2^2+I_3\omega_3^2)$: el momento angular y la energía se
> escriben sin términos cruzados, y las [[Ecuaciones de Euler 3D]] quedan desacopladas. Es la base
> natural de la dinámica del cuerpo rígido.

> [!referencia]
> Goldstein §5.4. Objeto que se diagonaliza: [[Tensor de Inercia]]. Cambio de punto:
> [[Teorema del Eje Paralelo]]. Aplicación directa: [[Ecuaciones de Euler 3D]]. Contexto:
> [[3 Inercia/index]].

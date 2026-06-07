---
title: Integral de Superficie
tags:
  - analisis-tensorial
  - teoria
  - calculo-vectorial
  - operadores-integrales
  - integral-de-superficie
draft: false
aliases:
  - integral de superficie
  - flujo
  - vector de area
  - surface integral
---

# Integral de Superficie $\int_S d\vec\sigma$

> [!definicion]
> La **integral de superficie** suma una cantidad sobre una superficie $S$ mediante el **vector de área** $d\vec\sigma=\hat{n}\,d\sigma=d\sigma_i\hat{e}_i$: su magnitud es el área diferencial $d\sigma$ y su dirección es la normal $\hat{n}$. Su caso central es el **flujo** de un campo $\vec v$,
> $$\Phi_S=\int_S d\vec\sigma\cdot\vec v=\int_S d\sigma_i\,v_i,$$
> un **escalar** (el índice $i$ está sumado).

> [!info]
> Sección **2.2.3** del libro; segunda hija de [[index | Operadores Integrales]] (cap. 2.2). El integrando es un [[Campos Escalares y Vectoriales | campo]]. El flujo es la cantidad que el [[Teoremas Integrales/Teorema de Gauss | teorema de Gauss]] iguala a la integral de volumen de la [[Operadores Diferenciales/Divergencia | divergencia]]; la convención de $\hat{n}$ con el borde $C$ es la que usa el [[Teoremas Integrales/Teorema de Stokes | teorema de Stokes]].

---

## Ejemplo

> [!ejemplo]
> **Flujo del campo radial $\vec v=(x,\,y,\,z)$ a través de la cara superior de un cubo.** Tomamos la cara $z=1$ del cubo unidad, con $0\le x\le1$, $0\le y\le1$. Por convención (superficie con normal hacia afuera, hacia $+z$) el vector de área es
> $$d\vec\sigma=\hat{e}_z\,dx\,dy\quad\Rightarrow\quad d\sigma_z=dx\,dy,\ \ d\sigma_x=d\sigma_y=0.$$
> El producto punto retiene solo la componente $z$ del campo, que sobre la cara vale $v_z=z=1$:
> $$d\vec\sigma\cdot\vec v=d\sigma_i\,v_i=d\sigma_z\,v_z=(1)\,dx\,dy.$$
> Integrando sobre la cara:
> $$\int_S d\vec\sigma\cdot\vec v=\int_0^1\!\!\int_0^1 (1)\,dx\,dy=\int_0^1 dy\int_0^1 dx=(1)(1)=1.$$
> El flujo a través de esa cara es $1$. Si sumamos las seis caras del cubo unidad $[0,1]^3$, las tres caras en $x{=}1$, $y{=}1$, $z{=}1$ aportan $1$ cada una, y las tres caras en $x{=}0$, $y{=}0$, $z{=}0$ aportan $0$ (allí la componente normal $v_i=0$). El flujo total es $3$, en acuerdo con el [[Teoremas Integrales/Teorema de Gauss | teorema de Gauss]]: $\int_V\vec\nabla\cdot\vec v\,d\tau=\int_V 3\,d\tau=3$, pues $\vec\nabla\cdot\vec v=3$ y el volumen es $1$.

---

## En qué consiste

> [!teoria]
> La integral de superficie se representa por su operador $\int_S d\vec\sigma$, con $d\vec\sigma$ un vector de magnitud igual a un área diferencial de $S$ y dirección perpendicular a la superficie. Escribiendo $d\vec\sigma=\hat n\,d\sigma$ y, en cartesianas, $d\vec\sigma=d\sigma_i\hat{e}_i$, el flujo se desarrolla con $\hat{e}_i\cdot\hat{e}_j=\delta_{ij}$:
> $$\int_S d\vec\sigma\cdot\vec v=\int_S d\sigma_i\hat{e}_i\cdot v_j\hat{e}_j=\int_S d\sigma_i\,v_j\,\delta_{ij}=\int_S d\sigma_i\,v_i,$$
> donde $d\sigma_i$ es **positivo o negativo** según el signo de $\hat n\cdot\hat{e}_i$. El resultado es un escalar.

> [!regla] Convención de la normal $\hat{n}$
> Como toda superficie tiene dos lados, hay que fijar el sentido de $\hat n$:
> 1. **Superficie cerrada** (encierra un volumen): $\hat n$ apunta siempre **hacia afuera**.
> 2. **Superficie abierta** (con borde): $\hat n$ se fija por la **regla de la mano derecha** respecto del camino cerrado $C$ que recorre el borde — los dedos siguen $C$, el pulgar da $\hat n$.

> [!proposicion] Operaciones menos comunes
> $$\int_S d\vec\sigma\,\Phi=\hat{e}_i\int_S d\sigma_i\,\Phi\quad(\text{produce un vector}),$$
> $$\int_S d\vec\sigma\times\vec v=\hat{e}_k\int_S d\sigma_i\,\varepsilon_{ijk}\,v_j\quad(\text{produce un vector}).$$
> Los versores salen de la integral por ser la base cartesiana independiente de la posición.

## Resumen

> [!resumen]
> | Operación | Fórmula en índices | Resultado |
> |---|---|---|
> | Flujo | $\int_S d\vec\sigma\cdot\vec v=\int_S d\sigma_i\,v_i$ | escalar |
> | Sobre escalar | $\int_S d\vec\sigma\,\Phi=\hat{e}_i\int_S d\sigma_i\,\Phi$ | vector |
> | Producto cruz | $\int_S d\vec\sigma\times\vec v=\hat{e}_k\int_S d\sigma_i\,\varepsilon_{ijk}v_j$ | vector |
> | Vector de área | $d\vec\sigma=\hat{n}\,d\sigma=d\sigma_i\hat{e}_i$ | $\hat n$ afuera / mano derecha |

> [!corolario]
> El vector de área $d\vec\sigma$ carga la información de dirección normal; el producto punto con $\vec v$ extrae la componente que **atraviesa** la superficie, dando el flujo. Fijar $\hat n$ (afuera en superficie cerrada, mano derecha en abierta) es lo que hace coherentes el [[Teoremas Integrales/Teorema de Gauss | teorema de Gauss]] y el [[Teoremas Integrales/Teorema de Stokes | de Stokes]].

> [!referencia]
> - Forma de operador y reglas: [[index | Operadores Integrales]].
> - Hermanas: [[Integral de Linea]], [[Integral de Volumen]].
> - Flujo y divergencia: [[Operadores Diferenciales/Divergencia]], [[Teoremas Integrales/Teorema de Gauss]].

---
title: Integral de Superficie
order: 2
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

> [!info] Vector de área
> ![[integral_superficie.svg|330]]
>
> $d\vec\sigma=\hat n\,d\sigma$: magnitud igual al área diferencial, dirección normal a la superficie.

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

## Ejemplo

> [!ejemplo]
> **Flujo de $\vec v=(0,0,z)$ a través de un hemisferio, con parametrización completa.** Calculamos $\int_S d\vec\sigma\cdot\vec v$ sobre el hemisferio superior $S$ de radio $R$, $x^2+y^2+z^2=R^2$ con $z\ge0$, normal hacia afuera.
>
> **Paso 1 — parametrizar la superficie.** En esféricas sobre la esfera de radio $R$,
> $$\vec r(\theta,\phi)=R\,(\operatorname{sen}\theta\cos\phi,\ \operatorname{sen}\theta\operatorname{sen}\phi,\ \cos\theta),\qquad \theta:0\to\tfrac\pi2,\ \ \phi:0\to2\pi.$$
>
> **Paso 2 — vector de área $d\vec\sigma$.** La normal exterior a la esfera es radial, $\hat n=\hat r$, y el elemento de área esférico es $d\sigma=R^2\operatorname{sen}\theta\,d\theta\,d\phi$. Entonces
> $$d\vec\sigma=\hat r\,R^2\operatorname{sen}\theta\,d\theta\,d\phi,\qquad \hat r=(\operatorname{sen}\theta\cos\phi,\ \operatorname{sen}\theta\operatorname{sen}\phi,\ \cos\theta).$$
>
> **Paso 3 — evaluar el campo y el producto punto.** Sobre $S$, $\vec v=(0,0,z)=(0,0,R\cos\theta)$, luego
> $$d\vec\sigma\cdot\vec v=d\sigma_i\,v_i=\big(R^2\operatorname{sen}\theta\,d\theta\,d\phi\big)\,(\hat r)_z\,(R\cos\theta)=R^3\cos^2\theta\operatorname{sen}\theta\,d\theta\,d\phi,$$
> usando $(\hat r)_z=\cos\theta$.
>
> **Paso 4 — integrar.**
> $$\int_S d\vec\sigma\cdot\vec v=R^3\int_0^{2\pi}\!\!d\phi\int_0^{\pi/2}\cos^2\theta\operatorname{sen}\theta\,d\theta=R^3\,(2\pi)\Big[-\tfrac{\cos^3\theta}{3}\Big]_0^{\pi/2}=2\pi R^3\cdot\frac13=\frac{2\pi R^3}{3}.$$
>
> **Comprobación con el [[Teoremas Integrales/Teorema de Gauss | teorema de Gauss]].** Cerramos $S$ con el disco basal $D$ ($z=0$, normal $-\hat{e}_z$); allí $\vec v=(0,0,0)$ y su flujo es nulo. Como $\vec\nabla\cdot\vec v=\partial z/\partial z=1$, el teorema da
> $$\oint_{S\cup D}d\vec\sigma\cdot\vec v=\int_V 1\,d\tau=\frac12\cdot\frac{4}{3}\pi R^3=\frac{2\pi R^3}{3},$$
> es decir el flujo por el volumen de media bola coincide con el flujo por el hemisferio, ya que el disco no aporta. Mismo resultado: $2\pi R^3/3$.

---

## En qué consiste

> [!teoria]
> La integral de superficie se representa por su operador $\int_S d\vec\sigma$, con $d\vec\sigma$ un vector de magnitud igual a un área diferencial de $S$ y dirección perpendicular a la superficie. Escribiendo $d\vec\sigma=\hat n\,d\sigma$ y, en cartesianas, $d\vec\sigma=d\sigma_i\hat{e}_i$, el flujo se desarrolla con $\hat{e}_i\cdot\hat{e}_j=\delta_{ij}$:
> $$\int_S d\vec\sigma\cdot\vec v=\int_S d\sigma_i\hat{e}_i\cdot v_j\hat{e}_j=\int_S d\sigma_i\,v_j\,\delta_{ij}=\int_S d\sigma_i\,v_i,$$
> donde $d\sigma_i$ es **positivo o negativo** según el signo de $\hat n\cdot\hat{e}_i$. El resultado es un escalar.

> [!teorema] Paso a índices
> $$\int_S d\vec\sigma\cdot\vec v=\int_S d\sigma_i\,v_i.$$

> [!demostracion]
> **Paso 1 — descomponer el vector de área.** El vector de área lleva la normal y la magnitud del área diferencial; en la base cartesiana,
> $$d\vec\sigma=\hat n\,d\sigma=d\sigma_i\,\hat{e}_i,\qquad d\sigma_i=(\hat n\cdot\hat{e}_i)\,d\sigma,$$
> de modo que cada componente $d\sigma_i$ es la proyección del área sobre el plano normal a $\hat{e}_i$ (con signo).
>
> **Paso 2 — escribir el campo y formar el producto punto.** Con $\vec v=v_j\,\hat{e}_j$ y por linealidad,
> $$d\vec\sigma\cdot\vec v=(d\sigma_i\,\hat{e}_i)\cdot(v_j\,\hat{e}_j)=d\sigma_i\,v_j\,(\hat{e}_i\cdot\hat{e}_j).$$
>
> **Paso 3 — ortonormalidad $\hat{e}_i\cdot\hat{e}_j=\delta_{ij}$.** La delta colapsa $j\to i$:
> $$d\vec\sigma\cdot\vec v=d\sigma_i\,v_j\,\delta_{ij}=d\sigma_i\,v_i.$$
>
> **Paso 4 — integrar.** Por linealidad del operador de superficie,
> $$\int_S d\vec\sigma\cdot\vec v=\int_S d\sigma_i\,v_i=\int_S\big(v_1\,d\sigma_1+v_2\,d\sigma_2+v_3\,d\sigma_3\big),$$
> con $i$ repetido y sumado: un escalar (el flujo). $\blacksquare$

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
